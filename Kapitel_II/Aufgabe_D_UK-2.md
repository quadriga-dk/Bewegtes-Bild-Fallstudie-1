# Annotationsergebnisse: Datenabgleich und -erläuterung

Sobald die Annotationsarbeit für das Video abgeschlossen ist, kann das Paket mit unserer Musterlösung verglichen werden. Die Lösungsdatei steht hier zum Download bereit. 
+++
```{important} 
Trotz der Verwendung der Ontologie können sich Annotationsentscheidungen von Person zu Person unterscheiden. Wichtig ist, dass die Ergebnisse miteinander verglichen werden können. Punktuelle Erläuterungen unserer Entscheidungen werden in diesem Kapitel ausgeführt. 
```
## Importfunktion

In Advene gibt es die Möglichkeit ein bestehendes Packages in ein anderes zu importieren.
+++
*Wofür kann in diesem Schritt die Importfunktion nützlich sein?*
:::{dropdown} Antwort
Diese Funktion ist hilfreich, um beispielsweise verschiedene Annotationen, die zum gleichen Video erstellt wurden, miteinander zu vergleichen. 
+++
Hierzu folgende Schritte durchführen: 
+++
1.	Unter "File" die Option "Import package" anklicken
2.	Das zu importierende Packet auswählen
3.	Im "Package importer view" zur Unterscheidung der Annotationstypen einen Titelzusatz, wie z.B. IMPORTED, angeben. Dieser Zusatz wird hinter die importierten Annotationstypen gehängt
4.	Anschließen die gewünschten Annotationstypen, die importiert werden sollen, anklicken 
5.	Die importierten Annotationstypen stehen nun zur Verfügung und können in der Timeline View angezeigt werden
:::

Ein ausführlicherer Guide für das Importieren findet sich sowohl unter Punkt 3.3 (S. 45ff) im Manual als auch im zweiten Videotutorial (Video: XX)

## Error-Package: Fehlersuche & Korrektur

Im Folgenden steht hier ein Package bereit, in dem einige Fehler eingebaut sind.
```{admonition} Übung
*Welche Fehler konnten gefunden werden?*
:::{dropdown} Antwort
ANTWORT NOCH AUSFÜHREN
:::
*Wie können die Fehler korrigiert werden?*
:::{dropdown} Antwort
ANTWORT NOCH AUSFÜHREN
:::
```
## Diskussion der Ergebnisse

Mit der AdA-Filmontologie kann ermöglicht werden auf der Grundlage eines Klassifikationsschemas filmanalytische Beobachtungen zu systematisieren. Die Systematisierung ist also ein notwendiger Schritt, um Metadaten einerseits unter ganz spezifischen Kriterien herzustellen als auch anschließend vergleichen zu können. 
+++
Ziel dieser Fallstudie ist es in einem nächsten Schritt durch die Visualisierung dieser Metadaten audiovisuelle Inszenierungsmuster zu analysieren und als Affekrhetorik zu qualifizieren. Doch bevor wir uns der eigentlichen Analyse widmen, wollen wir die Ergebnisse der Annotationsarbeit diskutieren. Denn Annotationsentscheidungen sind nicht immer selbsterklärend. Und auch eine Ontologie kann ihre Grenzen aufweisen. 
+++
Für die Diskussion gehen wir nachfolgend punktuell auf konkrete Probleme und Fragen ein, die während des Annotierens aufgekommen sind. Da eine ganzheitliche Diskussion aller Annotationsentscheidungen und Schritte den Rahmen dieser Übungen sprengt, adressieren wir hier die wichtigsten.

### Annotationstyp: Field Size (Einstellungsgröße)

Die Frage nach dem Referenzobjekt zur Bestimmung der Einstellungsgröße ist nicht immer eindeutig. Dies gilt insbesondere für die Einstellungen, die 2D animiert sind oder in denen eine Frame-in-Frame Anordnung zu sehen ist.
+++
Bei Einstellungen also, in denen die Bestimmung des Referenzobjekts zur Messung der Einstellungsgröße unklar blieb, haben wir den Wert 'neither' eingetragen, wie beispielsweise hier:
+++
```{image} ../_images/A4-S04.png
:align: center
:height: 300px
:name: A4-S04
```
````{margin}
```{hint}
Um UUIDs (universally unique identifier) zu suchen, muss die Suchfunktion angepasst werden. Dazu einen Rechtsklick auf das Lupen-Symbol neben dem Suchfeld und die Option 'Searched
elements' auswählen. Im sich öffnenden Fenster die Option 'Ids' (am Ende der Liste, Liste ggf. aufziehen) auswählen.
```
````
Die UUID dieser Annotation ist folgende: `0aac70ea-219b-11ef-9bca-90b11c948b9a`
+++
*Warum ist die Festlegung auf einen Wert in dieser Einstellung schwierig?*
:::{dropdown} Antwort
Auf eine 2D simulierte Ansicht eines Papierblocks blendet sich von links nach rechts der in blau gefärbte Schriftzug "The Numbers" ein. Diese Ansicht erinnert an eine Präsentationsfolie. Obwohl die Einstellung im Verhältnis zu unserem Standpunkt nah wirken mag, lässt sich eine Distanz nicht eindeutig festlegen, da die Einbettung in eine räumliche Umgebung fehlt, die eine Skalierung zulassen würde. 
:::

#### 2D-Animationen

Bei multiplen und/oder simultan auftretenden Animationselementen sieht es ähnlich aus. Es gibt keine klaren Relationen oder Anhaltspunkte im Raum, durch die eine Skalierung zur Bestimmung einer Einstellungsgröße nach bekannten Systemen möglich wäre, wie es bei dieser Annotation mit der UUID `3fbfc132-00a8-11ef-a9a8-001c42d38318` der Fall ist:
```{image} ../_images/A4-S05.png
:align: center
:height: 300px
:name: A4-S05
```
In diesem Beispiel wäre die Möglichkeit für ein kontrastierendes Syntaxelement wie [VS] ebenfalls sinnvoll, da durch die Trennung der verschiedenen Bildgrenzen multiple Elemente zu sehen sind. Wir haben uns für die Werte 'neither' sowie 'extreme long shot' entschieden. Der Wert 'extreme long shot' ist anwendbar auf das rechte Bild im animierten Splitscreen. Die Referenzobjekte zur Bemessung der Entfernung sind hier die Kräne. <br>
Dort, wo Fragen nach Skalierungen und Referenzbestimmungen komplexer werden, zeigen sich jedoch gleichzeitig auch die Grenzen einer Ontologie.
