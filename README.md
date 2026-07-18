# GGV-Keys
Verteilungsschlüssel für die Gemeinschaftliche Gebäudeversorgung §42b EnWG[^1]

Der **"Schwäbische Schlüssel"** (auch "Konservativer Schlüssel" oder "fairshare" genannt), der hier definiert und implementiert wird, hat ähnliche Fairness-Eigenschaft wie der in der [FAQ des Bundeswirtschaftsministeriums](https://www.bundeswirtschaftsministerium.de/Redaktion/DE/FAQ/Solarpaket/faq-solarpaket.html) definierte *statische Schlüssel*, verteilt aber wie der ebendort genannte *dynamische Schlüssel* falls möglich stets die gesamte Energiemenge.

## Eigenschaften
Der Schwäbische Schlüssel verteilt einen möglichst großen Teil der Energiemenge, die im Zeitinterval erzeugt wurde.
Kein Teilnehmer erhält mehr Energie zugeteilt, als er verbraucht hat.
Ansonsten aber nicht weniger als irgendein anderer Teilnehmer.

![Schwäbischer Aufteilungsschlüssel: Hellblau = Bedarf, Dunkelblau = Zuteilung](https://github.com/tophensen/GGV-Keys/blob/main/plot_konservativ_6kwh.png)

Der statische Aufteilungsschlüssel kann in solchen Fällen einen Teil der Energie
nicht zuteilen (rot):

![Statischer Aufteilungsschlüssel: Hellblau = Bedarf, Dunkelblau = Zuteilung, Rot = Nicht zugeteilt](https://github.com/tophensen/GGV-Keys/blob/main/plot_statisch_6kwh.png)

Der dynamische Aufteilungsschlüssel verteilt zwar die gesamte Strommenge, übervorteilt aber große Verbraucher auf Kosten der kleinen:

![Dynamischer Aufteilungsschlüssel: Hellblau = Bedarf, Dunkelblau = Zuteilung](https://github.com/tophensen/GGV-Keys/blob/main/plot_dynamisch_6kwh.png)

## Implementierungen
Es gibt unterschiedliche Methoden, den Schäbischen Aufteilungsschlüssel zu implementieren: 
- als iterative Version des statischen Schlüssels, bei dem die jeweils in einer Runde nicht zugeteilte Energiemenge in der nächsten Runde aufgeteilt wird
- mithilfe einer sortierten Liste der Verbräuche: Beginnend beim kleinsten wird der Verbrauch jeweils vollständig erfüllt solange die restlichen Verbraucher mindestens dasselbe bekommen könnten. Sobald dies nicht mehr der Fall ist, wird der Rest gleichmäßig aufgeteilt. 
  
Implementierungen existieren hier in 
[Python](https://github.com/tophensen/GGV-Keys/blob/main/fairshare.py), 
[Excel](https://github.com/tophensen/GGV-Keys/blob/main/fairshare.xlsx) und 
[OpenOffice](https://github.com/tophensen/GGV-Keys/blob/main/fairshare.ods). 

Mit [GGV-plot.py](https://github.com/tophensen/GGV-Keys/blob/main/GGV-plot.py) und [GGV-plot.ipynb](https://github.com/tophensen/GGV-Keys/blob/main/GGV-plot.ipynb) lässt sich der Aufteilungsschlüssel darstellen und mit dem statischen und dynamischen Schlüssel vergleichen.

## Messstellenbetreiber und Messdienstleister, die den Schwäbischen Schlüssel anbieten:
Bisher leider keine bekannt. 

[^1]: EnWG §42b (5) Die durch die Gebäudestromanlage erzeugte elektrische Energie wird rechnerisch auf alle teilnehmenden Letztverbraucher aufgeteilt, wobei die rechnerisch aufteilbare Strommenge begrenzt ist auf die Strommenge, die innerhalb eines 15-Minuten-Zeitintervalls in der Solaranlage erzeugt oder von allen teilnehmenden Letztverbrauchern verbraucht wird, je nachdem welche dieser Strommengen geringer ist. Die rechnerische Aufteilung dieser Strommenge zwischen den teilnehmenden Letztverbrauchern erfolgt anhand des zwischen dem teilnehmenden Letztverbraucher und dem Betreiber nach Absatz 2 Nummer 1 vereinbarten Aufteilungsschlüssels. Im Zweifel ist die durch die Gebäudestromanlage erzeugte elektrische Energie zu gleichen Teilen auf die teilnehmenden Letztverbraucher zu verteilen. Die einem einzelnen teilnehmenden Letztverbraucher im Wege der rechnerischen Aufteilung innerhalb eines 15-Minuten-Zeitintervalls zuteilbare Strommenge ist begrenzt auf die durch ihn in diesem Zeitintervall verbrauchte Strommenge. Der Betreiber der Gebäudestromanlage teilt der im Rahmen der elektronischen Marktkommunikation zuständigen Stelle den Aufteilungsschlüssel mit.
