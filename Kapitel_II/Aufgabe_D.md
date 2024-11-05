---
lang: de-DE
---
# Einführung

## Kapitelübersicht
[Einführung](Aufgabe_D) <br>
[Annotation mit dem AdA-Template: Schritte und Arbeitsprozess](Aufgabe_D_UK-1) <br>
[Annotationsergebnisse: Datenabgleich und -erläuterung](Aufgabe_D_UK-2) <br>
[Methodenreflexion und Resümee](Aufgabe_D_UK-3)
+++
In diesem Kapitel erstellen wir Annotationen mit einer Filmontologie.
+++
*Wir befinden uns hier:*
![Aufgabe 3](../assets/Aufgabenstruktur-04.png)

Im vorigen Kapitel haben wir gezeigt, wie anhand von Semantic Web Prinzipien eine filmanalytische Ontologie entstehen kann. Mehr Infos dazu, was eine filmanalytische Datenontolgie ist und leistet, gibt es [hier](Aufgabe_C) <br>
In diesem Schritt soll es nun darum gehen mit der AdA-Filmontologie in der Videoannotationssoftware [Advene](https://www.advene.org/) zu arbeiten. 

```{admonition} Kurz erklärt: Was ist die AdA-Filmontologie?
:class: dropdown
Die AdA-Filmontologie ist ein von der BMBF-geförderten Nachwuchsgruppe "[Affektrhetoriken des Audiovisuellen](https://www.ada.cinepoetics.fu-berlin.de/index.html)" (kurz: AdA) nach Semantic Web Standards entwickelts systematisches Beschreibungsvokabular filmanalytischer Konzepte und Termini. Sie ist zur Anwendung für komplexe und feingleiderige Videoannotationen ausgelegt. Die Ontologie ermöglicht die Herstellung und Visualisierung filmanalytischer Annotationsdaten. Mehr Infos und weiterführende Links gibt es in diesem [Book](Aufgabe_C_UK-2) sowie [hier](https://www.ada.cinepoetics.fu-berlin.de/Methoden/index.html) und [hier](https://www.cinepoetics.fu-berlin.de/methods/3_Tools/1_Vokabular_der_AdA-Filmontologie/index.html).
```
Hierzu werden im ersten Teil die jeweiligen [Schritte und der Workflow für die Annotationsarbeit](Aufgabe_D_UK-1) mit der AdA-Ontologie sowie dem AdA Core-Template skizziert. Zwei ausführliche Videotutorials, ein umfangreiches Manual und verschiedene Fragen sollen dabei helfen, die Funktionsweisen und Prozesse nachzuvollziehen. Im Kapitel [Annotationsergebnisse: Datenabgleich und -erläuterung](Aufgabe_D_UK-2) gibt es zunächst eine Übungsaufgabe, in der die zuvor erlenten Kompetenzen geprüft werden können. Anschließend werden die Entscheidungen, sowie Probleme und Grenzen der Ontologie diskutiert.

```{admonition} GROB- UND FEINLERNZIELE
:class: dropdown
**Groblernziel**
+++
Mithilfe von Annotationsdaten, die auf Basis einer filmanalytischen Ontologie erstellt und visualisiert werden, können audiovisuelle Inszenierungsmuster erkannt und differenzieren werden.
+++
**Feinlernziele**
1. Die AdA Filmontolgie kann eingerichtet und implementierte automatische Erkenneralgorithmen durchgeführt werden.
2. Die Funktionen der Segmentierungsbereinigung können angewendet werden.
3. Ein Set an Annotationsdaten kann mit der Ada Filmontologie erstellt werden.
```

## Untersuchungsgegenstand und Voraussetzungen

Untersuchungsgegenstand unserer Fallstudie sind Online-Videos zur Klimakrise. Entlang eines Videobeispiels soll diese Übung sowohl die Annotationsschritte als auch etwaige offene Fragen und Probleme, die sich während des Annotationsprozesses ergeben, skizzieren. Das Video ist als Download in diesem [Book](../Kapitel_I/Untersuchungsgegenstand.md) verfügbar. 
+++
Voraussetzung für die Annotationsarbeit in der Videoannotationssoftware Advene ist das [AdA-Template](../assets/AdA_template_07_2021.azp). Das AdA-Template ist ein Annotationspaket, welches das Vokabular der AdA-Ontologie bereits als vordefinierte Vorlage enthält.
```{hint}
Wer erst bei diesem Schritt einsteigt, kann sich notwendiges Vorwissen jeweils hier aneignen:
+++
[Einführung in die datengestütze Filmanalyse, Forschungsfragen und Lernziele](../Kapitel_I/Einführung_in_die_datengestützte_Filmanalyse) <br>
[Untersuchungsgegenstand](../Kapitel_I/Untersuchungsgegenstand) <br>
[Einarbeiten in die Filmontologie](/Kapitel_II/Aufgabe_C)
```
## Videotutorials

````{margin}
```{note}
Die Videotutorials sind auf Englisch. Ein ausführliches Manual in deutscher Sprache (s.u.) steht ebenfalls zur Verfügung.
```
````
Für die Annotationsarbeit mit der Ontologie wurden zwei Videotutorials erstellt (Stratil, Huthmann, Demir 2024). Eine kurze Inhaltsübersicht soll zur Orientierung dienen. Wer ab einem bestimmten Inhaltsabschnitt starten möchte, kann auf den jeweiligen Titel-Link klicken. Unten sind die Videos in voller Länge abrufbar.

### Video: Advene Basics

* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=139" target="_blank">The Interface: Menus Videoplayer, Timeline</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=304" target="_blank">Setup: Package and Video File</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=451" target="_blank">Annotation Types: Creating, Editing, Displaying, Deleting</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=551" target="_blank">Automatic Video Analysis</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=687" target="_blank">Creating Annotations: Creating, Merging, Deleting, Copying or Moving, Editing</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=803" target="_blank">Edit View</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=826" target="_blank">Search and Replace</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=890" target="_blank">Quick Edit & Quick Fill</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=1070" target="_blank">Table View<a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&start=1172" target="_blank">Export & Visualization</a>

<iframe src="https://videoup.uni-potsdam.de/Panopto/Pages/Embed.aspx?id=cf912751-5223-4132-80bb-b20300a60e55&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

### Video: AdA-Template

* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=126" target="_blank">Ada-Template: Package</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=169" target="_blank">AdA Corpus Analysis View</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=226" target="_blank">Process Video, Shot Validation & Subtitles</a> 
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=476" target="_blank">Scene Segmentation</a> 
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=499" target="_blank">Packages: Splitting, Merging, Importing</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=623" target="_blank">Annotate with Short Cuts</a>
* <a href="https://videoup.uni-potsdam.de/Panopto/Pages/Viewer.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&start=698" target="_blank">Checker Function</a>

<iframe src="https://videoup.uni-potsdam.de/Panopto/Pages/Embed.aspx?id=71ca2ea8-b7ee-492f-a9ef-b20300a665d3&autoplay=false&offerviewer=true&showtitle=false&showbrand=false&captions=false&interactivity=all" height="405" width="720" style="border: 1px solid #464646;" allowfullscreen allow="autoplay"></iframe>

## Weiterführende Infos und Material

Beide Videotutorials bieten gute Einstiegshilfen und Erklärungen der wichtigsten Funktionen und Anwendungen für die Arbeit mit der AdA-Filmontologie. Als Quick Guides sollen sie somit einen schnellen Start in die Annotationsarbeit ermöglichen. 
+++
Im Rahmen des AdA-Projekts wurde als Teil des AdA-Toolkits ein Manual entwickelt, welches darüber hinaus noch ausführlichere Anweisungen bereitstellt (Pfeilschifter et. al.). Detaillierte und spezifische Hilfen zu den je einzelnen Funktionen können dem Manual entnommen werden. Hier steht das Manual in deutscher Fassung zum Dowload bereit: [AdA-Manual](../assets/Manual_Advene_AdA_D_Vers1_0.pdf). Eine englische Version kann vom [AdA-Toolkit](https://www.ada.cinepoetics.fu-berlin.de/ada-toolkit/index.html) bezogen werden.

## Die nächsten Schritte...
```{image} ../assets/Laptop-Manual.png
:align: right
:height: 200px
:name: laptop-manual
```
1.	Videos anschauen und Manual (bei Bedarf) hinzuziehen <br>
2.	Advene starten und loslegen! 🎬
+++
```{seealso}
Unseren Workflow mit einigen Übungsfragen haben wir auf der nächsten Seite notiert. 
```

