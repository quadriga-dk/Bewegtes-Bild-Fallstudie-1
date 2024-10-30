---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
```{code-cell} ipython3
:tags: [remove-cell]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors
```

# Annotation mit dem AdA-Template: Schritte und Arbeitsprozess

Für die Arbeit mit dem AdA-Template muss Advene installiert sein und ausgeführt werden. Installationsanweisungen und Hinweise gibt unter [Technische Voraussetzungen](../Kapitel_I/Technische_Voraussetzungen).

## Workflow und Annotationsprozess

1.	Download des [AdA-Templates](../assets/AdA_template_07_2021.azp), der [AdA-Filmontologie](../assets/Ada_Filmontologie_Deu_23_07_2021.pdf) und des [Manuals](../assets/Manual_Advene_AdA_D_Vers1_0.pdf).
+++
2.	Öffnung der Anwendung Advene. Wird die Developement-Version von Advene über eine virtuelle Maschine für Linux genutzt, muss einer dieser beiden Befehle im Ubuntu-Terminal eingegeben werden: <br>
`cd src/advene` oder `GDK_BACKEND=x11 advene`. <br>
Advene öffnet automatisch bei jedem Start ein neues Paket als advenespezifische **.azp-Datei**
+++
3.	Template-.azp in das Paket laden und das Video verknüpfen (Video: XX, Manual: S. 4)
+++
````{margin}
```{note}
Die AdA Corpus Analysis View bietet eine Basisauswahl an Annotationstypen, mit der wir für unseren Gegenstand arbeiten werden.
```
````
4.	Eine neue Timeline öffnen und die AdA Corpus Analysis View als Annotationsgrundlage für die Spuren, die annotiert werden sollen, integrieren. Unter folgendem Reiter können weitere vordefinierte Annotationstypen der Ontologie eingeblendet und andere ausgeblendet werden (Video: XX, Manual: S. 6ff)
```{image} ../_images/A4-S01.png
:align: center
:height: 250px
:name: a4-s01
```

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz_1.json", colors = colors.jupyterquiz)
```

5.	Durchführung automatischer Erkenneralgorithmen und Überprüfung der Einstellungen mit der Validation View. Anschließend Bereinigung und Renummerierung der Einstellungen (Video: XX, Manual: S. 116)

`````{admonition} Welche Schritte müssen vollzogen werden, damit die automatischen Erkenneralgorithmen durchgeführt werden?
:class: tip
````{admonition} Antwort
:class: dropdown
Um die automatische Videoanalyse durchzuführen auf ‘File’ und ‘Process Video’ gehen. Anschließend öffnet sich der ‘Importer’. Unter 'Filter' werden Auswahloptionen angezeigt.
`````

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz_2.json", colors = colors.jupyterquiz)
```

`````{admonition} Warum müssen die Einstellungen renummeriert werden?
:class: tip
````{admonition} Antwort
:class: dropdown
Nicht jede Einstellungsgrenze wird korrekt gesetzt. Daher ist es notwendig mit der Shot Validation die Einstellungsgrenzen zu korrigieren. Dieser Schritt ist unerlässlich und bildet die Grundlage für alle weiteren Annotationsspuren, die nach dem Einstellungsprinzip annotiert werden. Nach der Bereinigung mit der Shot Validation sind die Einstellungsnummern i.d.R. nicht mehr korrekt. Diese müssen dann überprüft und angepasst werden.
`````

6.	Download der Untertitel von YouTube und Import der Untertitel (Video: XX, Manual: S. 126ff)

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz_3.json", colors = colors.jupyterquiz)
```

7.	Annotationen als Zeiteinheiten auf der Timeline für jeden Annotationstypen erstellen. Den Annotationen via Short Cuts und Quick Fill (s. Ontologie) oder durch Freitext-Eingabe Werte zuordnen (Video: XX, Manual: S. 69ff & 131ff)
```{image} ../_images/A4-S03.png
:height: 350px
:name: a4-s03
```
```{image} ../_images/A4-S02.png
:height: 250px
:name: a4-s02
```

```{tip}
Für die Erstellung korrekter bzw. präsizer Start- und Endzeit der Annotationen kann die Wiedergabegeschwindigkeit angepasst und mit den Frame-Tasten gearbeitet werden.
```

Für einige Annotationstypen haben wir die Annotationen als Verläufe angelegt, für andere haben wir nach dem Einstellungsprinzip segmentiert. Folgende Tabelle soll als Annotationshilfe dienen:

```{attention}
Diese Annotationssegmentierung kann von Gegenstand zu Gegenstand, je nach den Formen der Inszenierung, variieren. Für diese Übung soll die Tabelle lediglich als Orientierungshilfe dienen.
```

````{margin}
```{tip}
Mit der Funktion 'Search/replace content' können die erstellten und bereinigten Annotationen, die beispielsweise für den Typ 'Montg | Shot' als Einstellungen segmentiert wurden, in jede weitere Spur kopiert werden, die ebenfalls nach dem Einstellungsprinzip segmentiert wird. Um alle darin enthaltenen Werte zu löschen, das 'Replace by' Feld leer lassen.
```
````

````{margin}
Die Annotation des Typs 'Volume' wird über automatischer Erkenner als Verlauf generiert.
````

+++
| Segmentierung nach Einstellung      | Segmentierung nach Verlauf            |
|-------------------------------------|---------------------------------------|
| Shot (semi-automatische Generierung) | Setting                              |
| Shot Duration                        | Found Footage                        |
| Montage Figure Macro                 | Animation                            |
| Field Size                           | Dialogue Text                        |
| Image Intrinsic Movement             | Image Brightness                     |
| Image Content                        | Colour Range                         |
| Camera Angle                         | Dominant Movement Direction          |
| Camera Movement Direction            | Recording/Playback Speed             |
| Body Language Emotion                | Dialogue Emotion                     |
|                                      | Sound Gesture Dynamics               |
|                                      | Music Mood                           |
|                                      | Montage Figure Macro                 |


`````{admonition} Für einige Annotationstypen können Syntaxelemente verwendet werden. Was beschreiben die Werte **[TO]** sowie **[VS]** jeweils?
:class: tip
````{admonition} Antwort
:class: dropdown
**[TO]**: Beschreibt die Möglichkeit, ein Syntaxelement zu verwenden, das
eine kontinuierliche Entwicklung zwischen zwei Werten anzeigt. <br>
**[VS]**: Beschreibt die Möglichkeit, ein Syntaxelement zu verwenden, das
zwei kontrastierende Werte verbindet.
`````

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz-4.json", colors = colors.jupyterquiz)
```

```{admonition} Antwort
:class: dropdown
Die Verwendung von Syntaxelementen ermöglicht es kontinuierliche Entwicklungen wie auch synchrone Kontraste, die beispielsweise innerhalb einer Einstellung auftauchen, miteinander zu verbinden. Ein gutes Beispiel für für die Verwendung des Syntaxelement [TO] ist der Wechsel von Einstellungsgrößen innerhalb einer Einstellung. Ein gutes Beispiel für die Verwendung des Syntaxelement [VS] sind synchron inszenierte Dialog Emotionen bei mehreren Figuren innerhalb einer Einstellung.
```

8.	Überprüfung und Bereinigung mit der Checker-Funktion (Video: XX, Manual: S. 91ff)
+++
9.	Das finale Package kann [visualisiert](Aufgabe_D) und auch in andere Dateiformate exportiert werden (Video: XX, Manual: S. 106ff & 133ff)







