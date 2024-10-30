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

# Übung zur Konfiguration der Timeline und Qualifizierung der Daten

## Aufgabe 1 

Im Folgenden ist eine konfigurierte Visualisierung der Timeline zu sehen. 

````{margin}
➡️ Zum Vergrößern draufklicken oder ranzoomen
````

```{image} ../_images/A5-S10.png
:align: center
:height: 330px
:name: A5-S10
```

```{code-cell} ipython3
:tags: [remove-input]
display_quiz("../quizzes/E_UK-2_Quiz-1.json", colors = colors.jupyterquiz)
```

```{admonition} Lösungsweg
:class: dropdown
Hier nochmal die richtige Lösung:
+++
DominantMovementDirection(colorfield:content labels:true representation:rect legend:true colorscheme:paired), <br>
ImageIntrinsicMovement(height:100 representation:line labels:false)
+++
Gehen wir die **Syntaxelemente** einzeln durch:
+++
Für **DominantMovementDirection** gilt:
+++
`colorfield`: der Wert `content` ist korrekt, an der rechten Seite ist eine Legende aller annotierten Werte mit dem Syntaxelement `content` (also ihrem Inhalt) zu sehen.
+++
`labels`: der Wert `true` ist korrekt, da wir die Timecode-Leiste für den Annotationstypen konfiguriert haben.
+++
`representation`: der Wert `rect` ist korrekt, die Darstellungsform entspricht einem Balkendiagramm.
+++
`legend`: der Wert `true` ist korrekt, wir haben eine Legende an der rechten Seite konfiguriert.
+++
`colorscheme`: der Wert `paired` ist korrekt, wir haben uns nach dem Vega-Farbschema für ein Kategorie-Schema entschieden, um die einzelnen Inhaltswerte der Annotationen besser abbilden zu können.
+++
Für **ImageIntrinsicMovement** gilt:
+++
`height`: der Wert `100` ist korrekt. Wenn man ein wenig mit der Pixelgröße herumspielt, sieht man direkt die Unterschiede!
+++
`representation`: der Wert `line` ist korrekt, auch hier sehen die anderen Werte der Darstellungsoption `representation` ganz anders aus (durch ein wenig Ausprobieren kommt man schnell zur Lösung…).
+++
`labels`: der Wert `false` ist korrekt, wir haben die Timecode-Leiste für den Annotationstypen ausgeblendet.
```
## Aufgabe 2

Eine Visualisierung mit folgenden Eigenschaften soll erstellt werden:
+++
In der genannten Reihenfolge sollen die Annotationstypen **Found Footage**, **Image Intrinsic Movement** und **Recording/Playback Speed** angezeigt werden. Eine Timecode-Leiste soll für alle drei Typen konfiguriert werden.
+++
Der Annotationstyp **Found Footage** soll einzeilig mit einer Pixelhöhe von 30 dargestellt werden. Eine Legende mit dem Inhalt der Annotationen soll angezeigt werden. Als Farbschema soll `plasma` gewählt werden. 
+++
Der Annotationstyp **Image Intrinsic Movement** soll als Histogramm mit einer Pixelhöhe von 100 angezeigt werden. Eine Legende mit dem Verlauf als `parsed` soll eingeblendet werden. Als Farbschema soll `pinkyellowgreen` gewählt werden.
+++
Der Annotationstyp **Recording/Playback Speed** soll als Balkendiagramm mit einer Legende und den Annotationsinhalten im Farbschema `dark2` angezeigt werden.

```{admonition} Lösung
:class: dropdown
Folgende Konfigurationen in der Syntax haben wir eingegeben, um die oben beschriebene Ansicht zu erhalten: 

![screenshot-A5-11](../_images/A5-S11.png)

Auf was besonders zu achten ist:
+++
* Um die Syntaxelemente zu konfigurieren, müssen die Werte durch Klammern (ohne Leerzeichen) angegeben werden
* Die Syntaxreihe für jeden Annotationstypen muss mit einem Komma abgeschlossen werden
* Darstellungsoption und Wert werden mit einem Doppelpunkt ohne Leerzeichen voneinander getrennt
* Mehrere Optionen für einen Annotationstypen werden durch Leerzeichen voneinander getrennt
* Um eine einzeilige Darstellung zu konfigurieren, muss das Syntaxelement `single_line` angegeben werden (und nicht die Option `representation`)
* Wird eine Timeline neu geöffnet, finden sich unter 'Expand' alle vordefinierten Syntaxeinstellungen. Die Timeline-Leiste ist bereits standardmäßig auf `labels:true` eingestellt und muss nicht nochmal definiert werden. Zum Ausblenden der Leiste muss die Option jedoch auf `labels:false` geändert werden
* Nicht alle Annotationstypen können mit allen Repräsentationswerten angezeigt werden (hier am besten einfach ausprobieren!)

So sieht die oben beschriebene Darstellung als Datenvisualisierung aus: <br>
(...bitte ranzoomen für eine größere Ansicht)

![screenshot-A5-12](../_images/A5-S12.png)

```


