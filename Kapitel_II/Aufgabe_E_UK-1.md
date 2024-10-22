# AdA-Timeline: Funktionsweisen, Bedienung, Anpassung

In unserem Video-Quickguide zur AdA-Timeline werden Aufbau und Funktion, verschiedene Anpassungsoptionen in der Darstellung sowie Exportmöglichkeiten erläutert. Für detaillierte Beschreibungen zu allen Optionen empfehlen wir das [Manual](../assets/Manual_Advene_AdA_D_Vers1_0.pdf).
+++
VIDEO EINBINDEN
# Die wichtigsten Schritte im Überblick

## Timeline aufrufen

````{margin}
```{note}
Die Timeline wird mit dem Standard Browser geöffnet. Die URL kann jedoch auch in einem anderen installierten Browser geöffnet werden.
```
````
In Advene muss zunächst das mit dem AdA-Template erstellte Annotationspaket geöffnet werden. Anschließend kann über das W3-Symbol in der Icon-Leiste eine Visualisierungsform ausgewählt werden. Hier entweder die online oder offline Version der Timeline auswählen. Wir arbeiten in dieser Übung mit der online Variante. 
```{image} ../_images/A5-S02.png
:align: center
:height: 250px
:name: a2-s02
```
```{hint}
In der Online-Variante werden aktuelle Visualisierungsdatenbanken von der Homepage des Entwicklers abgerufen, in der Offline-Variante werden lokale Ressourcen der jeweiligen aktuellen Advene-Version genutzt.
```
Am oberen Rand umfasst die Timeline zwei fixierte Spuren: 1. Die zoom control, mit der man frei skalieren kann und 2. die Referenzspur, welche den jeweils ausgewählten Bereich anhand eines festgelegten Annotationstypen anzeigt.

````{margin}
```{note}
Beim Öffnen ist die Referenzspur automatisch auf den Annotationstypen "shot" festgelegt. Dies kann über das Edit-Fenster geändert werden. Mehr Infos zur Anpassung s.u.
```
````
![screenshot-A5-03](../_images/A5-S03.png)

Die Zoom-Funktion erlaubt sowohl die Übersicht über einen gesamten Film als auch das beliebige Hineinzoomen in Detailansichten. Um den zoom control zu bedienen, die linke Maustaste gedrückt halten und den Bereich skalieren, der angezeigt werden soll. Den Browser danach aktualisieren.
+++
Alle weiteren im Hauptbereich der Timeline angezeigten Spuren zeigen die einzelnen Annotationstypen untereinander. Sie sind auf den denselben Zeitabschnitt wie die Referenzspur bezogen, sodass alle untereinander angezeigten, spurenübergreifenden Werte zeitgleiche Phänomene adressieren.
+++
Die einzelnen Werte der Annotationstypen werden links als Legende angezeigt. 
![screenshot-A5-04](../_images/A5-S04.png)

# Anpassungsoptionen

Die AdA-Timeline verwendet eine textbasierte Syntax für die Darstellungskonfiguration. Diese ist als für Menschen lesbare URL enkodiert. Mit der Textcharakteristik der Syntax können – auch ohne Programmierkenntnisse – selbstständig Visualisierungen mit unterschiedlichen Einstellungen erstellt und verändert werden. 
+++
````{margin}
```{attention}
Wer die Timeline über die URL-Syntax konfigurieren will, findet auf S. 141 des Manuals die Anweisungen.
```
````
Anpassungen der AdA-Timeline können sowohl direkt über die URL als auch über das Edit-Fenster vorgenommen werden. Aufgrund der besseren Übersichtlichkeit empfiehlt sich die Anpassung der Timeline im Edit-Fenster. Diese Option beschreiben wir auch kurz hier.

## Anpassungen mit dem Edit-Fenster

Um das Edit-Fenster zu öffnen, oben rechts im Browser auf 'Edit' klicken. Nun öffnet sich das Fenster.

```{image} ../_images/A5-S05.png
:align: center
:height: 200px
:name: a5-s05
```
+++
Veränderungen an der Darstellung der Timeline werden über Syntaxelemente vorgenommen. Eine Übersicht aller Syntaxelemente ist [hier](../assets/Übersicht-Syntaxelemente-AdA-Timeline.pdf) einsehbar. <br>
Beim Öffnen des Edit-Fensters erscheint das Textfeld der Syntax. Syntaxelemente werden mit einem `&` voneinander getrennt. 
+++
Wird ein spezifischer Zeitabschnitt über die zoom control für die Anzeige gewählt, so wird dieser Abschnitt als Timecode in der Syntax wie folgt dargestellt: `&t=00:00:32.658,00:01:19.094`
+++
Der Timecode kann über das Edit-Fenster angepasst werden. Hierzu einfach die genauen Zeiteingaben eintragen. 
![screenshot-A5-06](../_images/A5-S06.png)


