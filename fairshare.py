# FairShare: Der Schwäbische Schlüssel in drei
#            unterschiedlichen Implementierungen
#
# Es wird ein möglichst großer Teil der Energiemenge verteilt,
# die im Zeitinterval erzeugt wurde (have, "Haben").
#
# Kein Teilnehmer erhält mehr Energie zugeteilt (give[]), als er verbraucht hat (need[]).
# Ansonsten aber nicht weniger als irgendein anderer Teilnehmer.
#
# Etwaige nicht zuteilbare Energie bleibt übrig und wird ins Netz eingespeist.

sigDigits=4
rndErr = 10**(-sigDigits)

# Conceptually simple, reasonably fast implementation.
# Needs a sorted list, but no argsort:
# Fill glasses in order of their size (need[]).
# As soon as the remaining amount divided by the number of 
# remaining glasses is not enough to fill the next 
# glass, we fill all remaining glasses with that amount 
def fairShareSorted(need,have):
    havehad = have  # Für's Protokoll
    nleft=len(need) # Anzahl (noch nicht verarbeiteter) Teilnehmer
    give = need.copy() # Zuteilung (wird unten korrigiert, falls Bedarf > Produktion)

    # Bedarf der Teilnehmer wird in aufsteigender Reihenfolge abgearbeitet:
    for sn in sorted(need):
        # Noch nicht zugeteilte Energie aufgeteilt auf
        # noch nicht verarbeitete Teilnehmer:
        havePP = have/nleft #round(have/nleft,sigDigits)
        if sn > havePP: # Teilnehmer will mehr Energie als havePP,
            break       # mehr gibt's aber nicht! (Korrektur unten)
        else:
            # Zuteilung:
            # Da give = need is hier nur noch
            have -= sn # Haben und
            nleft -= 1 # Zähler zu korrigieren

    # Wenn nleft = 0, war Bedarf durch Haben gedeckt,
    # ansonsten...
    if nleft > 0:
        maxgive = have/nleft #round(have/nleft,sigDigits) # = havePP
        for i,n in enumerate(need):
            if n > maxgive: # wird bei havePP gekappt:
                give[i] = maxgive
                have -= maxgive

    # wurde mehr verteilt als da war? (sans Rundungsfehler)
    assert(have >= -rndErr)
    assert(sum(give) <= havehad + rndErr)

    return give

# Implementation without sorting, basically an iterative 
# version of the Statische Schlüssel: Distribute 1/n, 
# collect remainders (spill over) and distribute among  
# not yet full glasses in next iteration. 
# Repeat until sum of remainders is small (typ. 2-3 iters)
def fairShareIter(need,have):
    havehad = have  # Für's Protokoll
    nleft=len(need) # Anzahl (noch nicht verarbeiteter) Teilnehmer

    stillneed = need.copy()
    give = [0.0]*nleft
    while have > rndErr and nleft > 0:
        #print("still left: %.3f"%have)
        # Wir verteilen was wir haben zu gleichen Teilen
        # auf diejenigen, die noch nicht voll sind:
        givePP = have/nleft #round(have/nleft,sigDigits)
        nleft = 0
        for i,n in enumerate(stillneed):
            if givePP < n:
                # falls das noch nicht reicht:
                give[i] += givePP
                stillneed[i] -= givePP
                have -= givePP
                nleft += 1
            else:
                # falls das reicht:
                give[i] += stillneed[i]
                have -= stillneed[i]
                stillneed[i] = 0.

    # wurde mehr verteilt als da war? (sans Rundungsfehler)
    assert(have >= -rndErr)
    assert(sum(give) <= havehad + rndErr)

    return give

# Fastest implementation, up to 2x as fast 
# as fairShareSorted, but same concept - 
# this time using argsort to fill/process 
# give[] in ascending order of needs[].
def fairShareArgSort(need,have):
    nleft=len(need)
    haveleft = have
    havePP = haveleft/nleft
    give = need.copy()
    # argsort(need): 
    for i in sorted(range(len(need)),key=lambda j:need[j]):        
        if need[i] > havePP:
            give[i] = havePP
        else:
            # give[i] = need[i] # already set via .copy() above
            haveleft -= need[i]
            nleft -= 1
            if nleft > 0:
                havePP = haveleft/nleft
    return give

