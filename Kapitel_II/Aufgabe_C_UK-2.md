# AdA-Filmontologie: Filmanalyse und Semantic Web

In der vorigen Übung haben wir gezeigt, wie ein Set an filmanalytischen Beschreibungen in eine Ontologie nach Semantic Web Standards überführt werden kann. Schrittweise soll so nachvollzogen werden können, wie mit einem semantischen Modell formalästhetische Relationen als maschinenlesbare Triple hergestellt werden können.
Ausgehend von dieser Systematisierung hat die BMBF-geförderte Nachwuchsgruppe "[Affektrhetoriken des Audiovisuellen](https://www.ada.cinepoetics.fu-berlin.de/index.html)" (kurz: AdA) eine Filmontologie entwickelt, die in enger Zusammenarbeit mit Informatiker und Entwickler von [Advene](https://www.advene.org/), [Dr. Olivier Aubert](https://www.olivieraubert.net/) entstanden ist.

## Methode

````{margin}
```{hint} 
Ausführliche Informationen zur eMAEX-Methode gibt es unter [Empirische Methoden](../Kapitel_I/Empirische_Methoden) in diesem Book oder auf der Website: [Empirische Medienästhetik](https://www.empirische-medienaesthetik.fu-berlin.de/emaex-system/emaex_kurzversion/index.html) sowie [hier](https://www.cinepoetics.fu-berlin.de/methods/1_Methode/2_Ansatz_eMAEX/index.html).
```
````
Die methodische Umsetzung des AdA-Projekts greift zurück auf die [eMAEX-Methode](https://www.empirische-medienaesthetik.fu-berlin.de/emaex-system/emaex_kurzversion/index.html). eMAEX steht für electronically based media analysis of expressive-movement-images und beschreibt eine systematisierte Methode, in der das Zuschauendenempfinden über Rhythmus- und Bewegungsprofile als multimodale Ausdrucksbewegungsbilder des Films untersucht wird. 
Im Fokus steht hierbei die empirische Rekonstruktion einer Zuschauendenaffizierung als ästhetische Muster der Gestaltung audiovisueller Bewegungen. 
```{figure} ../assets/eMAEX-A3.png
:align: center
:height: 300px
:name: eMAEX-S-A3

Zeitliche Entfaltung der Ausdrucksbewegungen in einer Szene
```
## Ontolgie

Ausgehend von diesen Überlegungen wurde auf Grundlage des oben skizzierten Frameworks eine maschinenlesbare Analysesystematik (Ontologie) entwickelt. Die Notwendigkeit einer maschinenlesbaren Systematik ergibt sich zwangsläufig, denn durch die Analyse großer Datenmengen häufen sich Beschreibungsdaten an. Ohne maschinelle Unterstützung bei der Auswertung aufgrund ihres Umfangs, wären solche Analysen großer Datenkorpora nicht zu bewältigen.
+++
Um eben diese großen Datensätze an multidimensionalen Beschreibungen für einen größeren Korpus überhaupt erst zu ermöglichen, wurde eine auf Semantic Web Prinzipien basierende Systematik entwickelt – die AdA-Filmontologie, eine OWL-basierte-Ontologie. <br>
Durch die Integration (semi-)automatisch erzeugter Annotationen als auch die Möglichkeit der Maschinenlesbarkeit sowie weitere Verknüpfungsmöglichkeiten für semantische Metadaten, können filmanalytische Beschreibungsmuster als semantische Triple formuliert und diese in Form von **Linked Open Data** zugänglich, durchsuchbar sowie für den Austausch und Vergleich von Analysedaten öffentlich gemacht werden. 
```{admonition} Was sind Linked Open Data?
Linked Open Data (LOD) ist ein Konzept nach Semantic Web Prinzipien, welches die Veröffentlichung und Verknüpfung offen zugänglicher Daten im Internet beschreibt. Es ermöglicht, dass Daten aus verschiedenen Quellen miteinander in Relation treten, um diese leichter durchsuchbar wie auch nutzbarer zu machen.
+++
**Linked Data**: Stellt sicher, dass die Daten miteinander verknüpft sind. <br>
**Open Data**: Stellt sicher, dass die verknüpften Daten, z.B. Datenbanken von öffentlichen Einrichtungen oder Museen etc., frei und offen zugänglich sind.
+++
Mehr Infos: ...
```
### Struktur der AdA-Ontologie

Die AdA-Ontologie umfasst 502 einzelne Annotationswerte, die 78  Annotationstypenzugeordnet sind, welche wiederum auf 8 Beschreibungsebenen, wie z.B. Akustik, Montage, Bildkomposition oder Kamera, organisiert sind:
```{figure} ../assets/AdA-Struktur-LodLive.png
:align: center
:height: 450px
:name: ada-lodlive

Struktur: Ebenen, Typen, Werte – visualisiert mit LodLive
```
Definiert sind die filmanalytischen Konzepte, Begriffe und Beschreibungen auf der Grundlage von OWL (Web Ontology Language) und RDF (Ressource Description Framework) in einer Klassenstruktur mit dazugehörigen Eigenschaften:

1. **Annotationslevel** sind allgemeine Beschreibungskategorien, die aus einem Set ähnlicher Annotationstypen bestehen (z.B. Akustik oder Kamera).

2. **Annotationstypen** sind Konzepte der Filmanalyse, unter denen ein Film analysiert wird (z.B. Musik: Stimmung oder Kamerabewegung: Tempo).

3. **Annotationswerte** beschreiben die je konkreten Eigenschaften, die ein Annotationstyp haben kann (z.B. Kamerabewegung: Tempo: langsam, mittel, schnell, wechselnd).
+++
````{margin}
**Für eine Interaktion auf den Link klicken!**
````
Die mit OntoViz erstellte [interaktiven Visualisierung](https://ada.cinepoetics.org/ontoviz/), zeigt ebenfalls exemplarisch die dreigliedrige Dimension der Ontologie (hier als Ausschnitt):
```{figure} ../assets/AdA-Struktur-Ontoviz.png
:align: center
:height: 450px
:name: ada-ontoviz

Visualisierung mit OntoViz
```
