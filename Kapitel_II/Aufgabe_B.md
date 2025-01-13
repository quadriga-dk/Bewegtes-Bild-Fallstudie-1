---
lang: de-DE
---
# Einführung
## Kapitelübersicht

[Einführung](Aufgabe_B) <br>
[Annotieren mit Advene](Aufgabe_B_UK-1) <br>
[Annotieren mit Elan](Aufgabe_B_UK-2) <br>
[Methodenreflexion und Resümee](Aufgabe_B_UK-3)
+++
In diesem Kapitel soll das Annotieren mit Tools durch Freitexteingaben erprobt werden.
+++
*Wir befinden uns hier:*
![Aufgabe 2](../assets/Aufgabenstruktur-02.png)

Hierzu wird zunächst eine Parameterbestimmung und -erweiterung vorgenommen. Mit der Bestimmung unserer Parameter können wir uns anschließend der Annotationsarbeit widmen. Im Kapitel [Annotieren mit Advene](Aufgabe_B_UK-1) machen wir uns mit den Funktionsweisen von Advene vertraut und erstellen Annotationstypen sowie Annotationen. Im Kapitel [Annotieren mit ELAN](Aufgabe_B_UK-2) wiederholen wir diesen Schritt mit dem Tool ELAN. Im Anschluss besprechen wir die angewandte [Methode](Aufgabe_B_UK-3).

```{admonition} Lernziele
:class: lernziele
**Groblernziel**
+++
Mithilfe digitaler Annotationsverfahren können Metadaten zu audiovisuellem Material hergestellt werden.
+++
**Feinlernziele**
1. Die Basisfunktionen der Tools können verstanden und angeeignet werden.
2. Mit den Tools können Annotationstypen zusammengestellt werden.
3. Nach spezifischer Segmentierung können Annotationen erstellt und Werte für die Annotationen bestimmt werden.
```

````{margin}
```{admonition} Siehe auch
:class: seealso
Erläuterungen zum Begriff "Annotation" gibt es [hier](Aufgabe_A).
```
````

## Freitextannotationen

Die Programme Advene und ELAN ermöglichen die Herstellung von Annotationsdaten auf einer Timeline sowie die Einbettung von Videos. <br>
Die Annotationen in dieser Übung basieren auf Freitexteingaben. Das bedeutet, dass keine Klassifierzierungschemata filmanalytischer Parameter oder Werte der Annotationsarbeit zugrunde liegen. 
Die konkrete Arbeit mit einem solchen Schema, einer sogenannten Ontologie, wird Teil der nächsten drei Aufgaben sein. Zunächst soll es hier darum gehen, grundlegende Funktionen von Tools zu erlernen und anzuwenden. **Toolagnostische Perspektiven** sollen damit ebenfalls adressiert werden. 
```{admonition} Was ist mit "toolagnostischen Perspektiven" gemeint?
Insbesondere oft im Kontext der Softwareentwicklung oder in der IT-Infrastuktur verwendeter Begriff, meint toolagnostisch, dass bestimmte Methoden, Konzepte oder Frameworks unabhängig von einem spezifischen Werkzeug angewendet werden können. Wichtig ist, dass das Prinzip oder die Methode mit verschiedenen Tools umgesetzt werden kann. Das Framework für unsere Fallstudie ist somit die Entwicklung einer maschinenlesbaren, filmanalytischen Ontologie (mehr Infos zum Begriff der "Datenontologie" gibt es unter [Weiterführende Informationen](/Kapitel_I/weiterführende_Informationen) sowie im [dritten Kapitel](Aufgabe_C)).
```
```{attention}
**KLEINER HINWEIS** ⬇️ ⬇️ ⬇️ <br>
Im Kapitel [Annotieren mit einer Filmontologie](Aufgabe_D) gibt es ein auf die Arbeit mit einer spezifisch entwickelten Ontologie angepassten Video Quick Guide zu den Basisfunktionen von Advene. Da dieser Quick Guide ebenso komplexere Prozesse adressiert, die wir hier noch nicht anwenden, haben wir uns in diesem Arbeitsschritt dazu entschieden, lediglich die notwendigen Funktionen für eine reine Freitextannotation zu dokumentieren. Wer sich hier bereits die komplexeren Funktionen aneignen möchte, kann sich das Video selbstverständlich anschauen. 
```
## Parameterbestimmung und -erweiterung

````{margin}
```{admonition} Hinnweis
:class: hinweis
Aus der ersten Übung hat sich gezeigt, dass Parameter, wie z.B. Sound oder Kamera, mehrere Inhaltsebenen haben können. Damit wir diese Elemente ebenfalls abdecken, splitten wir für diese beiden Beispiele (also Sound & Kamera) die Parameter in je einzelne Bestandteile. 
```
````
 Bevor wir mit der eigentlichen Annotationsarbeit beginnen, ist es notwendig, ähnlich wie bei der [Tabellarischen Annotation](Aufgabe_A), die Parameter festzulegen, die als Spuren auf der Timeline annotiert werden sollen. Für eine erste Vergleichsbasis nutzen wir dieselben Parameter, die wir bereits in der tabellarischen Annotation verwendet haben ([s. Fig. 3](../assets/Kurzdefinition-Parameter.png)). Dieses Mal gehen wir aber minimal kleinteiliger vor:

******************
* Einstellungsnummer
* Dauer in Sekunden
* Einstellungsgröße
* Bildinhalt
* Montage
* **Kamerabewegung**
* **Kameraperspektive**
* **Musik**
* **Dialog**
* Farbe
* Licht 
******************

Das sind die Parameter (also Spuren) die wir in dieser Übung annotieren möchten. Wie geht es weiter? <br>
Als nächstes installieren wir die Programme Advene und ELAN. Unter dem Punkt [Technische Voraussetzungen](../Kapitel_I/Technische_Voraussetzungen) finden sich die Links und Anweisungen zur Installation. Sind die Anwendungen installiert, kann mit der Annotationsarbeit begonnen werden. Hierzu machen wir uns im nächsten Schritt mit den Funktionsweisen vertraut.
+++
Los geht es! 💥