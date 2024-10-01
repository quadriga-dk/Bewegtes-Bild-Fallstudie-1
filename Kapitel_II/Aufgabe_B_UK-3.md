# Annotieren mit *ELAN*
In diesem Unterkapitel soll das Annotationstool ELAN vorgestellt sowie die wesentlichen Funktionen und Bedienungsweisen kurz und übersichtlich umrissen werden. Umfassende Anleitungen aller Grundfunktionen im Detail können auf der [Seite des Entwicklers](https://archive.mpi.nl/tla/elan) eingesehen werden. Ein ausführliches Manual steht ebenfalls hier zum Download bereit. MANUAL ZUM DOWNLOAD BEREITSTELLEN
+++
ELAN (Eudico Linguistik Annotator) ist eine Open Source Transkriptions- und Annotationssoftware für Mediendateien mit Schwerpunkt Video. ELAN kennzeichnet sich insbesondere durch die Möglichkeit der Herstellung multimodaler Annotationen aus, wie zum Beispiel durch simultane Annotationsarbeiten an Bild und Ton. 
+++
Ähnlich wie in Advene, können in ELAN ebenfalls Annotationen auf einer Timeline angefertigt werden. Durch verschiedene Exportmöglichkeiten in andere Formate (wie z.B. als **CSV-File**) können die Annotationsergebnisse für Präsentationen und andere Projekte genutzt werden.

## Interface, Bedienung und Einrichtung

````{margin}
```{important} 
Die Videodatei ist erstmal undefiniert. Um Sicherheitskopien erstellen zu können, muss die Datei (im elanspezifischen **.eaf** Format) gespeichert werden. Hierzu unter 'Datei > Speichern unter…' die Datei benennen und speichern. Anschließend ebenfalls unter 'Datei' die automatische Sicherheitskopie aktivieren.
```
````
Wird die Anwendung gestartet öffnet sich zunächst ein blankes Interface. In der Menüleiste am oberen Rand kann die Videodatei, die annotiert werden soll, über den Reiter 'Datei' und 'Neu' hinzugefügt werden.
```{image} ../_images/A2-S09.png
:align: center
:height: 400px
:name: a2-s09
```
Sobald die Datei verknüpft ist, erscheint die Annotationsoberfläche. Unter der Videoanzeige ist eine **Wiedergabesteuerung** zu sehen. Die Steuerung kann über die Scroll,- Pixel,- Frame-, oder Sekundentasten vorgenommen werden. 
+++
Der **Auswahlsteuerung** neben der Wiedergabesteuerung kann angepasst werden. Folgende Optionen (der Reihenfolge nach) sind möglich: <br>
1. Ausgewählter Bereich wird abgespielt
2. Auswahl wird aufgehoben
3. Fadenkreuz bewegt sich an den Anfang oder an das Ende des markierten Bereichs
4. Der Cursor springt zur vorigen/nächsten oder drüber/drunterliegenden Annotation
5. 'Auswahl-Modus aktivieren': Bereich wird bei Wiedergabe oder vorwärt/rückwärts-Bewegung markiert
+++
Der **Schleifenmodus** spielt den ausgewählten Bereich im Loop ab.
+++
Die **Navigation der Timeline** erfolgt durch den grauen Balken unter der Wiedergabe- und Auswahlsteuerung. Die Leiste stellt den gesamten Filmverlauf dar. Durch Klicken in die Zeile springt der Zeiger an die entsprechende Stelle. 
+++
Die **Größenskalierung** der Timeline erfolgt über den Regler am unteren rechten Rand.
+++
Im Fenster rechts neben dem Videoplayer kann unter 'Steuerung' die Wiedergabegeschwindigkeit des Videos angepasst werden. 
![screenshot-A2-10](../_images/A2-S10.png)
+++
*In welchen Fällen ist die Regulierung der Wiedergabegeschwindigkeit sinnvoll?*
:::{dropdown} Antwort
Manchmal kann es sehr nützlich sein, die Wiedergabegeschwindigkeit an den eigenen **Annotationsrhythmus** anzupassen. Einige Einstellungen können als sehr schnell wahrgenommen werden. Die Reduzierung der Geschwindigkeit kann helfen, dass jene Bildinhalte, die man als Werte in den Annotationen anlegen möchte, auch tatsächlich präzise erfasst werden. 
:::
Solbald das Video mit dem ELAN-Projekt verknüpft ist, können Annotationszeilen – *tiers* gennant – sowie Annotationen angelegt werden. Wie das genau funktioniert, wird auf der nächsten Seite erklärt. 