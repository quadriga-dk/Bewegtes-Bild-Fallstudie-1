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

# Übung zu Semantic Web Prinzipien
## Aufgabe 1

Im Folgenden ist eine alphabetisch sortierte Liste mit basisschematischen Begriffen der Filmanalyse zu sehen:
______________________
* Amerikanische Einstellung
* Aufsicht
* Ausblenden / fade-out
* Einblenden / fade-in
* Einstellungsgröße
* Fischauge
* Großaufnahme
* Harmonisch
* Horizontaler Schwenk
* Jump Cut
* Kamerabewegung
* Kameraperspektive
* Match on Action
* Montage Macro
* Montage Micro
* Montagesequenz
* Musik Tonalität
* Neutral
* Normalsicht
* Parallelmontage
* Plansequenz
* Point-of-view
* spannungsgeladen
* Steady-Cam
* Teleobjektiv
* Totale
* Überblenden / Cross-fade
* Untersicht
* Weitwinkelobjektiv
* Zoom
______________________
Diese Begriffe sollen in diese vorgebene [Matrix](../assets/Einarbeiten_in_die_Filmontologie_Aufgabe_1_Quadriga.docx) an Ebenen, Typen und Werten eingeordnet werden: 
```{figure} ../assets/Matrix-A3.png
---
align: center
height: 600px
name: matrix-aufgabe-3
---

Matrix: Ebenen, Typen, Werte
```
## Aufgabe 2

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/C_UK-1_Quiz_1.json", colors = colors.jupyterquiz)
```