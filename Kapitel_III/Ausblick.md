# Diskussion und Ausblick

Ein besonderer Fokus der AdA-Ontologie liegt auf der Interoperabilität. Dies ermöglicht eine Integrierung der Dateninfrastruktur in potentiell andere Systeme. Genau in dieser Interoperabilität sehen wir mögliche Anknüpfungspunkte für zukünftige Erweiterungen und Anpassungen. Auf welche weiteren Aspekte und Eigenschaften kann das Framework ausgeweitet werden? Wie kann die Datenerhebung mit Blick auf die Organisation großer Filmkorpora effizienter gestaltet werden? 

Die Anwendbarkeit bereits bestehender Erkenneralgorithmen, wie die shot detection, sehen wir als einen großen Vorteil bei der Analyse größerer Datenmengen. Ein potentieller Ausblick ist die Erweiterung um weitere automatische und semi-automatische Erkenner. Dies könnte beispielsweise eine automatische Farb-und Gestenerkennung beinhalten. 

Die Weiterentwicklung der Ontologie ist für Anpassungen und kollaborativen Austausch offen. Insofern stehen hier Prinzip und Methodik einer qualitativen Empirie stets im Vordergrund. Wichtig dabei ist, dass die quantitative Produktion von Daten und Metadaten für uns immer als Hilfsmittel begriffen werden, sie dienen nicht dem reinen Selbstzweck und bedürfen einer Einordnung und Interpretation. 

Ein Auszug aus der Publikation "Audiovisuelle Rhetorik als politische Intervention" von Jasper Stratil (Mitentwickler der AdA-Ontologie) zeigt exemplarisch, wie die Nutzung quantitativer Annotationsdaten innerhalb eines konkreten Forschungsvorhabens mit Fokus auf qualitativer Empirie aussehen kann:

```{figure} ../assets/Dissauszug-JS.png
---
align: center
name: dissauszug-jasper-stratil
---

Annotationsbasierte Ausdrucksbewegungsanalyse zu <span style="font-variant: small-caps;" >Occupy Wall Strett </span> © Jasper Stratil
```
Die Relation zwischen einer subjektiven Seherfahrung und ihrer Greifbarmachung durch Daten stellt insofern das Hauptinteresse unseres Verständnisses digitaler Filmanalyse dar. Ein wichtiger Bestandteil hierbei ist die Datenvisualisierung in Form einer dynamischen Timeline. Konkret können komplexe Metadaten "lesbar" gemacht werden. Entscheidend sind dabei nicht einzelne Annotationswerte, sondern die zeitliche Dynamik multipler, synchroner und asynchroner Werte verschiedener Annotationsebenen im Verhältnis zueinander {cite}`stratil2024`. 

## Datenmanagement 

Die Fallstudie konzentriert sich in ihren Lerneinheiten auf die Entwicklung grundlegender Datenkompetenzen mithilfe der Erhebung digitaler Annotationsdaten. Für eine größtmögliche Nachvollziehbarkeit sowie Transparenz haben wir den Untersuchungsgegenstand auf eine Mediendatei beschränkt. 
Wie das Datenmanagement bei umfangreichen Film- und Videokorpora aussehen kann, steht als potentieller Ausblick noch offen, denn die Frage nach der Organisation großer Datenmengen ist nicht unerheblich. 

Die Adressierung dieser Thematik in all ihrer Komplexität ist ein eigener Gegenstand und kann hier nicht in Gänze besprochen werden. Um dennoch einen Einblick zu verschaffen, wie das Datenmanagement bei größeren Korpora aussehen kann, möchten wir auf das Repositorium des AdA-Projektes verweisen. Alle Annotationsdaten, Korpus-Metadaten und Softwarekomponenten des Projektes sind als Repositorien auf <a href="https://zenodo.org/records/8328663" class="external-link" target="_blank">Zenodo</a>" sowie auf "<a href="https://github.com/ProjectAdA/ada-ae/tree/main/filmontology" class="external-link" target="_blank">Github</a>" publiziert und somit öffentlich zugänglich und zur Nachnutzung bereitgestellt. 
Der Datensatz umfasst mehr als 92.000 manuelle sowie semi-automatisch strukturierte Annotationen für 391 audiovisuelle Medieneinheiten, die in Advene erstellt wurden, sowie mehr als 400.000 automatisch generierte Annotationen zur erweiterten Korpusanalyse. Die Annotationen sind unter der CC BY-SA 3.0-Lizenz veröffentlicht und liegen als Linked Open Data in Form von RDF-Tripeln, gespeichert als Turtle-Dateien, vor {cite}`bakels2023`. 

Mit Repositorien können also Infrastrukturen aufgestellt werden, die zur Organisierung, Kuratierung sowie Publikation umfangreicher Datensätze im Kontext digitaler Forschungsarbeit dienen. Sie gewährleisten die nachhaltige Verfügbarkeit, Nachvollziehbarkeit sowie Wiederverwendbarkeit bzw. Nachnutzung der Daten. Das Beispiel aus dem AdA-Projekt veranschaulicht nicht nur Methoden der Datenerhebung, sondern zeigt auch, wie diese Daten für weiterführende Analysen zugänglich und nutzbar gemacht werden können.

## Literatur

```{bibliography}
:filter: docname in docnames
```