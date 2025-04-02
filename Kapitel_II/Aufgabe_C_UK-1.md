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
(Überführung-Prinzipien)=
# Übung zu Semantic Web Prinzipien

## Aufgabe 1

```{admonition} Übungsaufgabe
:class: exercise
<span style="color:purple">**Ziel**</span>:
Im Folgenden ist eine alphabetisch sortierte Liste mit basisschematischen Begriffen der Filmanalyse zu sehen. Diese sollen korrekt in die vorgegebene [Matrix](../assets/Einarbeiten_in_die_Filmontologie_Aufgabe_1_Quadriga.docx) an Ebenen, Typen und Werten eingeordnet werden.

<span style="color:purple">**Aufgabe**</span>:
1. Betrachten Sie die alphabetisch sortierte Liste mit 30 filmanalytischen Begriffen.
2. Ordnen Sie jeden Begriff als Typ oder Wert ein und bestimmen Sie die hierarchischen Beziehungen.
3. Begründen Sie Ihre Entscheidungen anhand der semantischen Eigenschaften der Begriffe.
4. Vegleichen Sie Ihre Ergebnisse mit der [Lösung](../assets/Lösung_Aufgabe_1_Semantic_Web.pdf).

<span style="color:purple">**Bearbeitungzeit**</span>: Ca. 20 Min.
```

---

````{margin}
```{admonition} Hinweis
:class: hinweis
Achten Sie besonders auf die hierarchischen Beziehungen zwischen den Begriffen.
Berücksichtigen Sie, dass einige Begriffe Oberkategorien bilden (Ebenen), andere Unterkategorien (Typen) und wieder andere konkrete Ausprägungen (Werte).
```
````

<div style="column-count: 3; column-gap: 2em;">
<ul>
<li>Amerikanische Einstellung</li>
<li>Aufsicht</li>
<li>Ausblenden / fade-out</li>
<li>Einblenden / fade-in</li>
<li>Einstellungsgröße</li>
<li>Fischauge</li>
<li>Großaufnahme</li>
<li>Harmonisch</li>
<li>Horizontaler Schwenk</li>
<li>Jump Cut</li>
<li>Kamerabewegung</li>
<li>Kameraperspektive</li>
<li>Match on Action</li>
<li>Montage Macro</li>
<li>Montage Micro</li>
<li>Montagesequenz</li>
<li>Musik Tonalität</li>
<li>Neutral</li>
<li>Normalsicht</li>
<li>Parallelmontage</li>
<li>Plansequenz</li>
<li>Point-of-view</li>
<li>Spannungsgeladen</li>
<li>Steady-Cam</li>
<li>Teleobjektiv</li>
<li>Totale</li>
<li>Überblenden / cross-fade</li>
<li>Untersicht</li>
<li>Weitwinkelobjektiv</li>
<li>Zoom</li>
</ul>
</div>

---


Die [Matrix](../assets/Einarbeiten_in_die_Filmontologie_Aufgabe_1_Quadriga.docx) ist hier nochmals als Abbildung visualisiert.

```{figure} ../assets/Matrix-A3.png
---
align: center
height: 600px
name: matrix-aufgabe-3
---

Matrix: Ebenen, Typen, Werte
```

## Aufgabe 2

```{admonition} Übungsaufgabe
:class: exercise
<span style="color:purple">**Ziel**</span>: Identifizieren Sie die korrekte semantische Triple-Struktur für eine gegebene filmanalytische Beschreibung.


<span style="color:purple">**Aufgabe**</span>:
Unten sind drei Antwortmöglichkeiten für die Freitext-Beschreibung: “Hier gibt es eine langsame Kamerafahrt nach links” aufgelistet.
1. Analysieren Sie die drei unterschiedlichen Triple-Darstellungen (A, B und C).
und bestimmen Sie, welche Triple-Struktur die Beschreibung semantisch korrekt und gemäß Semantic Web Prinzipien repräsentiert.
2. Begründen Sie Ihre Entscheidung anhand der folgenden Kriterien:
* Konsistenz der Subjekt-Prädikat-Objekt-Struktur
* Präzision der semantischen Beziehungen
* Konformität mit ontologischen Grundprinzipien

<span style="color:purple">**Bearbeitungzeit**</span>: Ca. 10 Min.
```


**A**
```bash
'Segment X' 'hat auf dem Level Kamera' 'den Wert langsam' + 
'Segment X' 'hat auf dem Level Kamera' 'den Wert links' + 
'Segment X' 'hat auf dem Level Kamera' 'den Wert Kamerafahrt'
```

**B**
```bash
'Segment X' 'hat im Type Kamerabewegung Typ den Wert' 'Kamerafahrt' +
'Segment X' 'hat im Type Kamerabewegung Richtung den Wert' 'links' + 
'Segment X' 'hat im Type Kamerabewegung Geschwindigkeit den Wert' 'langsam'
```
**C**
```bash
'Im Type Kamerabewegung Typ hat' 'Segment X' 'den Wert Kamerafahrt' + 
'Im Type Kamerabewegung Richtung hat' 'Segment X' 'den Wert links' + 
'Im Type Kamerabewegung Geschwindigkeit hat' 'Subjekt X' 'den Wert langsam'
```

````{margin}
```{admonition} Hinweis
:class: hinweis
Beachten Sie, dass ein semantisches Triple immer aus Subjekt, Prädikat und Objekt besteht.
Achten Sie auf Inkonsistenzen in der Benennung von Entitäten zwischen den verschiedenen Triples.
```
````

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/C_UK-1_Quiz_1.json", colors = colors.jupyterquiz)
```