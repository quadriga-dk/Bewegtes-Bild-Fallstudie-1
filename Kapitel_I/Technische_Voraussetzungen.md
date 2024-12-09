---
lang: de-DE
---
# Technische Voraussetzungen

Zur Durchführung von Annotationen nutzen wir die frei zugänglichen Programme **Advene** und **ELAN**. Instruktionen sowie Hinweise zum Download für MacOS, Windows sowie Linux gibt es <a href="https://www.advene.org/download.html#download" class="external-link" target="_blank">hier</a> (für Advene) sowie <a href="https://archive.mpi.nl/tla/elan/download" class="external-link" target="_blank">hier</a> (für Elan).
+++
Über die <a href="https://github.com/oaubert/advene/" class="external-link" target="_blank">Projektseite</a> auf Github kann ebenfalls die Advene Development-Version für Linux gedownloaded werden. 

## Installationsanleitung Advene für Linux mit einer virtuellen Maschine

````{margin}
```{attention} 
*Parallels Desktop* ist beispielsweise eine kostenpflichtige virtuelle Maschine eines anderen Herstellers.
```
````

Wer die Development-Version für Linux über einen Mac nutzen möchte, kann sich eine virtuelle Maschine einrichten und Linux installieren.

### Schritt-für-Schritt Anleitung

Für das Installationspaket und -anleitung siehe: http://advene.org/download.html#download
+++
#### Einrichtung Repository
+++
Um *Ubuntu* zu erlauben aus einem unbekannten Repository sich Daten herunterladen zu dürfen, wird hier das Git-Repository des Entwicklers Olivier Aubert als vertrauenswürdige Quelle im System hinterlegt:
+++
<pre>

sudo wget --quiet -O /etc/apt/sources.list.d/advene.list 
https://olivieraubert.net/advene/debian/binary/advene.list

wget --quiet -O - https://olivieraubert.net/olivieraubert.asc | sudo apt-key add -

</pre>

#### Installation Advene

Nach der Einrichtung des Repositorys erfolgt nun die tatsächliche Installation des Programms selbst.

<pre>

sudo apt update && sudo apt install advene advene-full

</pre>

#### Development Version

Aktuellste Entwicklungen der Software können in der Development-Version benutzt werden. Um alle notwendigen Hilfsprogramme auf dem Rechner zu haben, muss zunächst die aktuell veröffentlichte Advene Version installiert werden (siehe oben).

Danach kann durch die folgenden Eingaben die Development-Version aus dem Git-Repository des Entwicklers bezogen werden:

<pre>

mkdir src

cd src

git clone https://github.com/oaubert/advene.git

</pre>


````{margin}
```{attention} 
Start via Programm-Icon öffnet den regulären Release!
```
````
Bei jedem Start kann nun mit `cd src/advene` sowie `GDK_BACKEND=x11 advene` die Development-Version von Advene geöffnet werden.
