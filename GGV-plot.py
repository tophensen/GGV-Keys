#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button,RadioButtons
from random import random
import sys

def statisch(need,have):
    """
    Die verfügbare Energiemenge (have) wird zu gleichen Teilen auf die
    Teilnehmer aufgeteilt. Anteile, die den jeweiligen Bedarf (need[])
    übertreffen, werden nicht vollständig zugeteilt.
    """
    havePP = have/len(need)
    give = [havePP if havePP < n else n for n in need]
    return give

def dynamisch2(need,have):
    """
    Die verfügbare Energiemenge (have) wird entsprechend dem Anteil des
    jeweiligen Nutzers am Gesamtenergieverbrauch (need[i]/sum(need)) zugeteilt.
    """
    allneed=sum(need)
    give = [n/allneed * have for n in need]
    give = [n if n < g else g for n,g in zip(need,give)]
    return give

def dynamisch(need,have):
    """
    Die verfügbare Energiemenge (have) wird entsprechend dem Anteil des
    jeweiligen Nutzers am Gesamtenergieverbrauch (need[i]/sum(need)) zugeteilt.
    Equivalent: Alle Teilnehmer erhalten einen festen relativen Anteil ihres
    Verbrauchs entsprechend dem Verhältnis zwischen verfügbarer Energiemenge
    und Gesamtverbrauch
    """
    factor = min(1.0,have/sum(need))
    give = [n*factor for n in need]
    return give

def konservativ(need,have):
    """
    Die Energiemenge (have) wird bis zur Größe der Summe der Verbräuche aller
    Teilnehmer (need[]) vollständig so verteilt, dass kein Teilnehmer
    weniger erhält als irgendein anderer Teilnehmer, es sei denn, sein
    Verbrauch (der des ersteren) kann bereits vollständig gedeckt werden.
    """
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

# Demo:
if __name__ == "__main__":
    
    xtext = 0.5
    ytext = 0.9
    plt.ion()
    verbrauch=[0.5,0.7,1.2,1.3,1.8,3.9]
    verbrauch.sort()

    fig=plt.figure("GGV Verteilungsschlüssel",figsize=(8,5))
    axbut = plt.axes([0.8,0.7,0.15,0.05])
    axslide = plt.axes([0.8,0.1,0.15,0.5])
    axschl = plt.axes([0.8,0.8,0.15,0.15])
    axplt = plt.axes([0.1,0.1,0.65,0.85])
    plt.ylabel("Verbrauch in kWh")
    plt.xlabel("TN")
    Emake = 6.0
    schl = "s"
    prevschl = schl
    semaphor=False

    def update_schl(s):
        global schl,semaphor
        schl = s
        semaphor=True
    rad=RadioButtons(axschl,["statisch","dynamisch","konservativ"])
    rad.on_clicked(update_schl)

    def update_input(i):
        global Emake,semaphor
        Emake = i
        semaphor=True
    slide=Slider(axslide,"Erzeugung [kWh]",valmin=0,valmax=20,valinit=Emake,orientation="vertical",initcolor="#FFFFFF00")
    slide.on_changed(update_input)

    def update_verbrauch(state):
        global verbrauch,semaphor,slide
        verbrauch = [4.0*random() for _ in range(len(verbrauch))]
        verbrauch.sort()
        semaphor=True
    but=Button(axbut,"Verbräuche Neu")
    but.on_clicked(update_verbrauch)

    while True:
        semaphor=False
        Eneed=sum(verbrauch)
        #print("Verbrauch: %.2f kWh"%Eneed)
        needPP = Eneed/len(verbrauch)

        bneed=plt.bar(range(1,1+len(verbrauch)),verbrauch,edgecolor="#4000E0FF",facecolor="#e4d9ffff",zorder=2)
        ftxt=plt.figtext(xtext,ytext,"Verbraucht: %.2f kWh (⌀ %.2f kWh pro TN)"%(Eneed,needPP),va="top",ha="right")

        makePP = Emake / len(verbrauch)
        ftxt._text+="\nErzeugt: %.2f kWh (⌀ %.2f kWh pro TN)"%(Emake,makePP)
        hl=plt.hlines([Emake/len(verbrauch)],0.6,6.4,color="k",linestyle="--",lw=0.5,zorder=1)

        prevschl = schl
        if schl.startswith("s"):
            vertfunc = statisch
            verttxt = "Statischer Schlüssel"
        if schl.startswith("d"):
            vertfunc = dynamisch
            verttxt = "Dynamischer Schlüssel"
        if schl.startswith("k"):
            vertfunc = konservativ
            verttxt = "Konservativer Schlüssel"
        ftxt._text += "\n"+verttxt

        solaranteil=vertfunc(verbrauch,Emake)
        Everteilt=sum(solaranteil)
        bgive=plt.bar(range(1,1+len(solaranteil)),solaranteil,edgecolor="#0808E0FF",facecolor="#0808E060",zorder=3)

        Eeinsp=Emake-Everteilt
        ftxt._text += ", zugeteilt: %.2f kWh"%Everteilt
        ftxt._text += "\nnicht zugeteilt: %.2f kWh"%max(0,Eeinsp)
        Everteilbar = min(Eneed,Emake)
        if Eeinsp >= 0.01:
            ftxt._text += "\ndavon theoretisch noch zuteilbar: %.2f kWh"%max(0,Everteilbar-Everteilt)

        annos = []
        if Eeinsp >= 0.01 and Emake <= Eneed:
            for i,g in enumerate(solaranteil):
                if g < makePP:
                    a=plt.annotate("",xytext=(i+1,g),xy=(i+1,makePP),arrowprops=dict(arrowstyle="|-|",color="#C02020FF",linewidth=3.0))
                    annos.append(a)

        while semaphor == False and plt.fignum_exists(fig.number):
            plt.pause(0.1)
        if not plt.fignum_exists(fig.number):
            break

        if hl != None:
            hl.remove()
        for a in annos:
            a.remove()
        bneed.remove()
        bgive.remove()
        ftxt.remove()


