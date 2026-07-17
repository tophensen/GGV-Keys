# GGV-Keys
Verteilungsschlüssel für die Gemeinschaftliche Gebäudeversorgung §42b EnWG[^1]

Der **"Schwäbische Schlüssel"** (auch "Konservativer Schlüssel" oder "fairshare" genannt), der in hier definiert und implementiert wird, hat ähnliche Fairness-Eigenschaft wie der in der [FAQ des Bundeswirtschaftsministeriums](https://www.bundeswirtschaftsministerium.de/Redaktion/DE/FAQ/Solarpaket/faq-solarpaket.html) sog. *statische Schlüssel*, verteilt aber wie der sog. *dynamische Schlüssel* falls möglich stets die gesamte Energiemenge.

Der Schwäbische Schlüssel verteilt einen möglichst großen Teil der Energiemenge, die im Zeitinterval erzeugt wurde.
Kein Teilnehmer erhält mehr Energie zugeteilt, als er verbraucht hat.
Ansonsten aber nicht weniger als irgendein anderer Teilnehmer.

Es gibt unterschiedliche Methoden, diesen zu implementieren: Siehe [FairShare.py](https://github.com/tophensen/GGV-Keys/blob/main/fairshare.py)/[FairShare.ods](https://github.com/tophensen/GGV-Keys/blob/main/fairshare.ods).

Mit [GGV-plot.py](https://github.com/tophensen/GGV-Keys/blob/main/GGV-plot.py) und [GGV-plot.ipynb](https://github.com/tophensen/GGV-Keys/blob/main/GGV-plot.ipynb) lässt sich der Aufteilungsschlüssel darstellen und mit dem statischen und dynamischen Schlüssel vergleichen.


[^1]: (5) Die durch die Gebäudestromanlage erzeugte elektrische Energie wird rechnerisch auf alle teilnehmenden Letztverbraucher aufgeteilt, wobei die rechnerisch aufteilbare Strommenge begrenzt ist auf die Strommenge, die innerhalb eines 15-Minuten-Zeitintervalls in der Solaranlage erzeugt oder von allen teilnehmenden Letztverbrauchern verbraucht wird, je nachdem welche dieser Strommengen geringer ist. Die rechnerische Aufteilung dieser Strommenge zwischen den teilnehmenden Letztverbrauchern erfolgt anhand des zwischen dem teilnehmenden Letztverbraucher und dem Betreiber nach Absatz 2 Nummer 1 vereinbarten Aufteilungsschlüssels. Im Zweifel ist die durch die Gebäudestromanlage erzeugte elektrische Energie zu gleichen Teilen auf die teilnehmenden Letztverbraucher zu verteilen. Die einem einzelnen teilnehmenden Letztverbraucher im Wege der rechnerischen Aufteilung innerhalb eines 15-Minuten-Zeitintervalls zuteilbare Strommenge ist begrenzt auf die durch ihn in diesem Zeitintervall verbrauchte Strommenge. Der Betreiber der Gebäudestromanlage teilt der im Rahmen der elektronischen Marktkommunikation zuständigen Stelle den Aufteilungsschlüssel mit.
