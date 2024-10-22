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
```{admonition} Übung
*Für unseren Beispielgegenstand haben wir die Auswahl der Annotationstypen an das Video angepasst. Welcher Typ wurde zur Corpus View hinzugefügt? Und welcher wurde weggelassen?* <br>
MULTIPLE CHOICE EINFÜGEN
```
5.	Durchführung automatischer Erkenneralgorithmen und Überprüfung der Einstellungen mit der Validation View. Anschließend Bereinigung und Renummerierung der Einstellungen (Video: XX, Manual: S. 116)
```{admonition} Übung
1. *Welche Schritte müssen vollzogen werden, damit die automatischen Erkenneralgorithmen durchgeführt werden?*
:::{dropdown} Lösung
Um die automatische Videoanalyse durchzuführen auf 'File' und 'Process Video' gehen. Anschließend öffnet sich der 'Importer'. 
Was muss unter 'Filter' ausgewählt werden, damit die Einstellungsgrenzen automatisch generiert werden? >> MULTIPLE CHOICE <br>
A: ShotdetectApp importer <br>
B: Scene change detection 
:::
2. *Warum müssen die Einstellungen renummeriert werden?*
:::{dropdown} Lösung
Nicht jede Einstellungsgrenze wird korrekt gesetzt. Daher ist es notwendig mit der Shot Validation die Einstellungsgrenzen zu korrigieren. Dieser Schritt ist unerlässlich und bildet die Grundlage für alle weiteren Annotationsspuren, die nach dem Einstellungsprinzip annotiert werden 
:::
```
6.	Download der Untertitel von YouTube und Import der Untertitel (Video: XX, Manual: S. 126ff)
```{admonition} Übung
*Welchem Annotationstypen können die Untertitel zugeordnet werden?* <br>
MULTIPLE CHOICE EINFÜGEN
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
Für einige Annotationstypen haben wir die Annotationen als Verläufe angelegt, für andere haben wir nach dem Einstellungsprinzip segmentiert. Folgende Übersicht soll als Annotationshilfe dienen:
````{margin}
```{tip}
Mit der Funktion 'Search/replace content' können die erstellten und bereinigten Annotationen, die beispielsweise für den Typ 'Montg | Shot' als Einstellungen segmentiert wurden, in jede weitere Spur kopiert werden, die ebenfalls nach dem Einstellungsprinzip segmentiert wird. Um alle darin enthaltenen Werte zu löschen, das 'Replace by' Feld leer lassen.
```
````
+++
| Segmentierung nach Einstellung    | Segmentierung nach Verlauf            |
|-----------------------------------|---------------------------------------|
| Shot                              | Setting                               |
| Shot Duration                     | Found Footage                         |
| Montage Figure Macro                      | Animation                             |
| Field Size                        | Dialogue Text                         |
| Image Intrinsic Movement          | Image Brightness                      |
|  Camera Angle               | Colour Range                          |
|  Image Content                 | Dominant Movement Direction           |
|                     | Recording/Playback Speed              |
|                     | Camera Movement Direction             |
|                                   | Dialogue Emotion                      |
|                                   | Sound Gesture Dynamics                |
|                                   | Music Mood                            |
|                                   | Body Language Emotion        |

```{admonition} Übung
*Für einige Annotationstypen können Syntaxelemente verwendet werden. Was beschreiben die Werte **[TO]** sowie **[VS]** jeweils?*
:::{dropdown} Lösung
**[TO]**: Beschreibt die Möglichkeit, ein Syntaxelement zu verwenden, das
eine kontinuierliche Entwicklung zwischen zwei Werten anzeigt. <br>
**[VS]**: Beschreibt die Möglichkeit, ein Syntaxelement zu verwenden, das
zwei kontrastierende Werte verbindet.
:::
*Für wie viele Annotationstypen des Core-Templates können Syntaxelemente verwendet werden?* <br>
QUIZ EINFÜGEN (entweder MC oder Numerischer Wert)
```
8.	Überprüfung und Bereinigung mit der Checker-Funktion (Video: XX, Manual: S. 91ff)
+++
9.	Das finale Package kann [visualisiert](Aufgabe_D) und auch in andere Dateiformate exportiert werden (Video: XX, Manual: S. 106ff & 133ff)







