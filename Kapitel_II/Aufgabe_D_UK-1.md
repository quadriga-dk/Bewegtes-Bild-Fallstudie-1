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
(Schritte-und-Arbeitsprozess)=
# Annotation mit dem AdA-Template: Schritte und Arbeitsprozess

Für die Arbeit mit dem AdA-Template muss Advene installiert sein und ausgeführt werden. Installationsanweisungen und Hinweise gibt unter [Technische Voraussetzungen](../Präambel/Technische%20Voraussetzungen.md).

```{admonition} Übungsaufgabe
:class: exercise
<span style="color:purple">**Ziel**</span>: Erstellen eines Annotationspaketes auf Basis der AdA-Ontologie mit dem AdA-Core-Template.

<span style="color:purple">**Aufgabe**</span>:
Erstellen Sie ein Annotationspaket in Advene basierend auf der AdA-Ontologie. Nutzen Sie dafür das AdA-Core-Template, das bereits ein vordefiniertes Set an Annotationstypen enthält. Diese decken die wichtigsten Analysekategorien ab und erleichtern Ihnen den Einstieg.
In den folgenden Abschnitten finden Sie eine detaillierte Beschreibung des gesamten Workflows mit präzisen Schritt-für-Schritt-Anweisungen.

<span style="color:purple">**Bearbeitungzeit**</span>: Ca. 180 Min.
```

## Übungsanleitung: Grundlagen der ontologiebasierten Annotation mit Advene
### Einrichtung und Vorbereitung der Annotationsumgebung

1.	Installieren Sie Advene und laden sie das [AdA-Template](../assets/AdA_template_07_2021.azp), die [AdA-Filmontologie](../assets/Ada_Filmontologie_Deu_23_07_2021.pdf) und das [Manual](../assets/Manual_Advene_AdA_D_Vers1_0.pdf) herunter.
2.	Starten Sie Advene. Wird die Developement-Version von Advene über eine virtuelle Maschine für Linux genutzt, muss einer dieser beiden Befehle im Ubuntu-Terminal eingegeben werden: 
`cd src/advene` oder `GDK_BACKEND=x11 advene`.
Advene öffnet automatisch bei jedem Start ein neues Paket als advenespezifische **.azp-Datei**
3.	Importieren sie das AdA-Template (.azp-Datei) in das Paket und verknüpfen Sie das Video (<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=126" target="_blank" class="external-link" >Video: Ada-Template: Package</a>, Manual: S. 4)
````{margin}
```{admonition} Hinweis
:class: hinweis
Die AdA Corpus Analysis View bietet eine Basisauswahl an Annotationstypen, mit der wir für unseren Gegenstand arbeiten werden.
```
````
4.	Öffnen Sie eine neue Timeline und integrieren Sie anschließend die AdA Corpus Analysis View als Annotationsgrundlage für die Spuren, die annotiert werden sollen. Unter folgendem Reiter können weitere vordefinierte Annotationstypen der Ontologie eingeblendet und andere ausgeblendet werden (<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=169" target="_blank"  class="external-link" >Video: AdA Corpus Analysis View</a>, Manual: S. 6ff)
```{image} ../_images/A4-S01.png
:align: center
:height: 250px
:name: a4-s01
```
````{margin}
```{admonition} Hinweis
:class: hinweis
Hierfür können die Annotationstypen auch mit der [Musterlösung](../assets/QUADRIGA-Fallstudie-Annotationspackage.azp) abgeglichen werden.
```
````

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz_1.json", colors = colors.jupyterquiz)
```

5.	Führen Sie die automatische Einstellungserkennung durch und validieren bzw. bereinigen Sie die Ergebnisse mit der Validation View. Anschließend müssen die Einstellungen renummeriert werden (<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=226" target="_blank" class="external-link" >Video: Process Video, Shot Validation & Subtitles</a>, Manual: S. 116)

`````{admonition} Welche Schritte müssen vollzogen werden, damit die automatischen Erkenneralgorithmen durchgeführt werden?
:class: exercise
````{admonition} Antwort
:class: solution, dropdown
Um die automatische Videoanalyse durchzuführen auf ‘File’ und ‘Process Video’ gehen. Anschließend öffnet sich der ‘Importer’. Unter 'Filter' werden Auswahloptionen angezeigt.
`````

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz_2.json", colors = colors.jupyterquiz)
```

`````{admonition} Warum müssen die Einstellungen renummeriert werden?
:class: exercise
````{admonition} Antwort
:class: solution, dropdown
Nicht jede Einstellungsgrenze wird korrekt gesetzt. Daher ist es notwendig mit der Shot Validation die Einstellungsgrenzen zu korrigieren. Dieser Schritt ist unerlässlich und bildet die Grundlage für alle weiteren Annotationsspuren, die nach dem Einstellungsprinzip annotiert werden. Nach der Bereinigung mit der Shot Validation sind die Einstellungsnummern i.d.R. nicht mehr korrekt. Diese müssen dann überprüft und angepasst werden.
`````

6.	Importieren Sie, sofern verfügbar, die Untertitel und ordnen Sie diese dem korrekten Annotationstyp zu. (<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=665" target="_blank" class="external-link" >Video: Importing Subtitles</a>, Manual: S. 126ff)

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/D_UK-1_Quiz_3.json", colors = colors.jupyterquiz)
```

### Erstellung der Annotationen

7. Erstellen Sie Annotationen als Zeiteinheiten entlang der Timeline und wenden Sie dabei, wie unten beschrieben, das korrekte Segmentierungsprinzip an. Ordnen Sie den Annotationen Werte zu - nutzen Sie dafür:
* Short Cuts und Quick Fill für ontologiebasierte Einträge
* Freitext-Eingaben für Werte ohne Ontologiebezug
(<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=623" target="_blank" class="external-link" >Video: Annotate with Short Cuts</a>, Manual: S. 69ff & 131ff)
```{image} ../_images/A4-S03.png
:height: 350px
:name: a4-s03
```
```{image} ../_images/A4-S02.png
:height: 250px
:name: a4-s02
```

```{admonition} Tipp
:class: hinweis
Für die Erstellung korrekter bzw. präsizer Start- und Endzeit der Annotationen kann die Wiedergabegeschwindigkeit angepasst und mit den Frame-Tasten gearbeitet werden.
```

Für einige Annotationstypen haben wir die Annotationen als Verläufe angelegt, für andere haben wir nach dem Einstellungsprinzip segmentiert. Folgende Tabelle soll als Annotationshilfe dienen:

```{admonition} Achtung
:class: caution
Diese Annotationssegmentierung kann von Gegenstand zu Gegenstand, je nach den Formen der Inszenierung, variieren. Für diese Übung soll die Tabelle lediglich als Orientierungshilfe dienen.
```

````{margin}
```{admonition} Tipp
:class: hinweis
Mit der Funktion 'Search/replace content' können die erstellten und bereinigten Annotationen, die beispielsweise für den Typ 'Montg | Shot' als Einstellungen segmentiert wurden, in jede weitere Spur kopiert werden, die ebenfalls nach dem Einstellungsprinzip segmentiert wird. Um alle darin enthaltenen Werte zu löschen, das 'Replace by' Feld leer lassen.
```
````

````{margin}
➡️ Die Annotation des Typs 'Volume' wird über automatischer Erkenner als Verlauf generiert.
````

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
:class: exercise
````{admonition} Antwort
:class: solution, dropdown
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
:class: solution, dropdown
Die Verwendung von Syntaxelementen ermöglicht es kontinuierliche Entwicklungen wie auch synchrone Kontraste, die beispielsweise innerhalb einer Einstellung auftauchen, miteinander zu verbinden. Ein gutes Beispiel für für die Verwendung des Syntaxelement [TO] ist der Wechsel von Einstellungsgrößen innerhalb einer Einstellung. Ein gutes Beispiel für die Verwendung des Syntaxelement [VS] sind synchron inszenierte Dialog Emotionen bei mehreren Figuren innerhalb einer Einstellung.
```

8. Nutzen Sie die 'Search/replace'-Funktion zur effizienten Übertragung von Segmentierungen
9. Überprüfen und bereinigen Sie Ihre Annotationen mit der Checker-Funktion (<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=698" target="_blank" class="external-link" >Video: Checker Function</a>, Manual: S. 91ff)
10.	Exportieren Sie Ihre Ergebnisse in ein geeignetes Dateiformat zur [Visualisierung](Aufgabe_D) und weiteren Analyse (<a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=1172" target="_blank" class="external-link ">Video: Export & Visualization</a>, Manual: S. 106ff & 133ff)







