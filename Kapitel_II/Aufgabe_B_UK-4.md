# *ELAN*: Annotationszeilen (Tiers) und Annotationen
## Zeilen
Eine 'default'-Zeile wird automatisch bei jedem neuen Annotationsdokument angelegt. Diese kann im Vorfeld entweder umbenannt oder gelöscht werden. 
+++
````{margin}
```{attention} 
Beim Schließen des Bearbeitungsfensters ohne die Einfügung der Zeile wird die Zeile nicht gespeichert.
```
````
Um eine neue Zeile bzw. "tier" anzulegen, im Menüpunkt auf 'Zeile > Neue Zeile einfügen…' klicken. Das sich öffnende Bearbeitungsfenster ermöglicht die Benennung der Zeile. Weitere Attribute (wie z.B. "Teilnehmer" oder "Annotator") können ebenfalls ergänzt werden. Um die Zeile zu speichern, auf 'Einfügen' klicken. 
```{image} ../_images/A2-S11.png
:align: center
:height: 500px
:name: a2-s11
```
````{hint} 
Die Farben des Zeilentitels sowie der Zeilenleiste selbst können nach eigenen Belieben angepasst werden. Hierzu im Fenster der Zeileneigenschaften 'Weitere Optionen' wählen. 
```{image} ../_images/A2-S12.png
:align: center
:height: 250px
:name: a2-s12
```
````
## Erstellen von Templates

Mit Elan ist es möglich Annotationsprojekte als Templates zu sichern. Die Erstellung eines Templates empfiehlt sich insbesondere, wenn für mehrere Filme oder Filmausschnitte Annotationen mit dem gleichen Set an Parametern erstellt werden sollen. Hierzu können Basisspuren, also Annotationszeilen, vordefiniert und anschließend die Datei als Vorlage gesichert werden. 
+++
Um ein Template zu erstellen, einfach vorgehen wie beim Start eines regulären Annotationsprojektes. Anschließend die Zeilen erstellen und die Datei unter 'Speichern als Vorlage' im **.etf-Format** sichern.
+++
Zur Nutzung der Vorlage Elan starten und unter 'Datei > Neu…' die Vorlagedatei wählen und öffnen.

## Annotationen

Annotationen werden als Zeitsegmente entlang der Timeline angelegt. Es gibt die Möglichkeit Annotationen A) **"frei Hand"** zu erstellen oder B) **präzisere Zeitabschnitte** durch beispielswseise die Frame- und Pixeltaste anzulegen.
+++
### Variante A
Der schnellste Weg eine Annotation zu erstellen ist mit dem Zeiger in das Feld der Annotationen an die Zeitstelle zu klicken, an der es losgehen soll, gedrückt halten und den Zeiger bis zum gewünschten Ende ziehen (geht vorwärts wie rückwärts). Der markierte Bereich erscheint violett. Mit einem Doppelklick in die gewünschte Zeile kann der Annotation ein Inhalt bzw. Wert beigeordnet werden. Zum Speichern 'Enter' drücken.
+++
![screenshot-A2-13](../_images/A2-S13.png)
+++
Jetzt kann man entweder…:
* …diese Auswahl aufheben (durchgestrichenes S im Auswahl-Modus) bzw. an anderer Stelle eine neue Auswahl erstellen
* …im gleichen Auswahlbereich in eine andere Zeile mit Doppelklick eine weitere Annotation hinzufügen,
* …in dieselbe Annotation durch Doppelklick wieder neuen Text hinzuschreiben, den Text verändern (dies geht natürlich jederzeit)

### Variante B

Wer präzise Annotationen erstellen möchte kann mit der Bedienung der Wiedergabesteuerung arbeiten. Hierfür ist es wichtig, dass unter dem Medienfenster die Zeitanzeige auf Frames eingestellt ist. Mit einem Rechtsklick auf die Zeitanzeige kann das Ausgabeformat geändert werden. Abhängig von der **Frame Rate** des Videos "PAL" oder "NTSC" wählen. 
Zur Erstellung der Annotation dann an den ungefähren Bereich des Anfangs navigieren und mit der Frametaste bzw. Pixeltaste den genauen Anfang bestimmen. Dann den 'Auswahl-Modus' aktivieren und erneut mit der Frametaste/Pixeltaste zur Endzeit der Annotation steuern. Den 'Auswahl-Modus' deaktivieren und mit einem Doppelklick die Annotation erstellen bzw. einen Wert einfügen. 
```{admonition} Was ist "PAL" oder "NTSC"?
Die Zeitformate **PAL** oder **NTSC** beziehen sich auf die Bildfrequenz – also Frame Rate. PAL-Videos werden üblicherweise mit einer Frame Rate von 25 Bildern pro Sekunde (FPS = frames per second) aufgenommen während NTSC mit einer Frame Rate von 30 Bildern pro Sekunde arbeitet. <br>
Die Frame Rate eines Videos kann über gängige Videoabspielprogramme herausgefunden werden. Hierzu die Metadateninformationen abrufen: 
Beispielsweise unter VLC im Abspielmodus mit cmd + I (Mac)  bzw. Strg + J (Windows) und dann unter 'Codecdetails > Bildwiederholrate'.
```
*Welche Framerate hat unser Beispielvideo und welches Zeitformat muss gewählt werden?* QUIZ EINBINDEN

### Annotationen bearbeiten 

Bereits angelegte Annotationen können ganz einfach geändert werden. Der Annotationsinhalt kann am schnellsten über einen Doppelklick auf die Annotation bearbeitet werden. Weitere Optionen können anschließend mit einem Rechtsklick aufgerufen werden. Hier die wichtigsten kurz erklärt:

* 'Annotationswert ändern' = der Inhalt der Annotation kann bearbeitet werden
* Annotation aufteilen' = die Annotation wird am Punkt des Mausanzeigers aufgeteilt
* Zusammenfügen mit der vorigen oder nächsten Annotation' = Annotationen können "gemerged", also zu einer Annotation verbunden werden
* 'Annotationswert löschen' = der Inhalt der Annotation wird gelöscht
* 'Annotation löschen' = die gesamte Annotation wird gelöscht 
+++
Fertige Annotationen können auch a) bewegt oder b) in ihrer Länge verändert werden, indem man die 'ALT' (Windows) bzw. Option-Taste (Mac) gedrückt haltend auf den Strich klickt (wechselt zu grün). Anschließend zum a) Verschieben die Annotation entlang der Zeitleiste bewegen, um die Position zu verändern oder b) am Ende der Annotation an der Zeitmarke vorwärts oder rückwärts bewegen.