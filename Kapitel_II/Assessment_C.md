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

# 🏆Selbsttest: Wissen und Praxis

````{admonition} Hinweis
:class: hinweis

Diese Übungsaufgaben dienen Ihrer Selbsteinschätzung und helfen Ihnen, das im Kapitel Gelernte zu reflektieren.

Sie können die Fragen in beliebiger Reihenfolge beantworten und auch mehrfach versuchen. 

**So funktioniert es:**
- Wählen Sie bei jeder Frage die Antwort(en), die Sie für richtig halten
- Lesen Sie das Feedback zu den einzelnen Antwortoptionen sorgfältig durch
- Die Erklärungen helfen Ihnen, Ihr Verständnis zu vertiefen – auch bei korrekten Antworten 

Es erfolgt keine Bewertung oder Speicherung Ihrer Ergebnisse. Nutzen Sie dieses Assessment, um Wissenslücken zu identifizieren und gegebenenfalls die entsprechenden Abschnitte des Kapitels noch einmal zu bearbeiten.

**Geschätzte Zeit**: xxx (Platzhalter)

Viel Erfolg!
````
## Sektion I: Verständnis der Prinzipien des Semantic Web auf die Filmanalyse
### Frage 1

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice1 = [{
    "question": """Was ist der Hauptzweck einer Ontologie mit Schwerpunkt Filmanalyse im Kontext des Semantic Web?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Standardisierung von Bildformaten für filmische Analysen",
            "correct": False,
            "feedback": """× Eine Ontologie beschäftigt sich nicht primär mit Bildformaten oder der Katalogisierung von Filmen. Sie ersetzt auch nicht menschliche Prozesse, sondern macht das von Menschen generierte Wissen für Maschinen verarbeitbar."""
        },
        {
            "answer": "Die Katalogisierung aller bekannten Filme in einer Datenbank",
            "correct": False,
            "feedback": """× Eine Ontologie beschäftigt sich nicht primär mit Bildformaten oder der Katalogisierung von Filmen. Sie ersetzt auch nicht menschliche Prozesse, sondern macht das von Menschen generierte Wissen für Maschinen verarbeitbar."""
        },
        {
            "answer": "Die strukturierte Darstellung von Wissen, um es maschinenlesbar zu machen",
            "correct": True,
            "feedback": """✓ Korrekt! Eine Ontologie im Semantic Web dient dazu, Wissen zu strukturieren und Begriffe sowie deren Beziehungen so zu ordnen, dass sie maschinenlesbar werden."""
        },
        {
            "answer": "Das Ersetzen menschlicher Annotations- und Analyseprozesse",
            "correct": False,
            "feedback": """× Eine Ontologie beschäftigt sich nicht primär mit Bildformaten oder der Katalogisierung von Filmen. Sie ersetzt auch nicht menschliche Prozesse, sondern macht das von Menschen generierte Wissen für Maschinen verarbeitbar."""
        }
    ]
}]

display_quiz(multiple_choice1, colors=colors.jupyterquiz)
```

### Frage 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice2 = [{
    "question": """Aus welchen Komponenten besteht ein semantisches Triple? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Subjekt",
            "correct": True,
            "feedback": """✓ Genau! Ein semantisches Triple besteht aus Subjekt, Prädikat und Objekt - den drei grundlegenden Elementen, die zusammen eine Aussage bilden."""
        },
        {
            "answer": "Prädikat",
            "correct": True,
            "feedback": """✓ Genau! Ein semantisches Triple besteht aus Subjekt, Prädikat und Objekt - den drei grundlegenden Elementen, die zusammen eine Aussage bilden."""
        },
        {
            "answer": "Objekt",
            "correct": True,
            "feedback": """✓ Genau! Ein semantisches Triple besteht aus Subjekt, Prädikat und Objekt - den drei grundlegenden Elementen, die zusammen eine Aussage bilden."""
        },
        {
            "answer": "Schema",
            "correct": False,
            "feedback": """× Die Grundstruktur eines semantischen Triples umfasst ausschließlich Subjekt, Prädikat und Objekt. Schema und Level sind zwar relevante Konzepte in anderen Kontexten des Semantic Web, gehören aber nicht zu den Komponenten eines einzelnen Triples."""
        },
        {
            "answer": "Level",
            "correct": False,
            "feedback": """× Die Grundstruktur eines semantischen Triples umfasst ausschließlich Subjekt, Prädikat und Objekt. Schema und Level sind zwar relevante Konzepte in anderen Kontexten des Semantic Web, gehören aber nicht zu den Komponenten eines einzelnen Triples."""
        }
    ]
}]

display_quiz(multiple_choice2, colors=colors.jupyterquiz)
```

### Frage 3
A. Die Entität, über die eine Aussage getroffen wird  
B. Der Wert oder die Entität, die dem Subjekt durch das Prädikat zugeordnet wird  
C. Die Relation oder Eigenschaft, die das Subjekt mit dem Objekt verbindet  
D. Eine eindeutige Kennung für die Komponenten eines Triples  



```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice3 = [{
    "question": """Ordnen Sie die Komponenten des semantischen Triples ihren korrekten Beschreibungen zu""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Subjekt , B. Prädikat , C. Objekt , D. URI",
            "correct": False,
            "feedback": """× Nicht korrekt """
        },
        {
            "answer": "A. Subjekt, B. Prädikat, C. URI, D. Objekt",
            "correct": False,
            "feedback": """× Nicht korrekt """
        },
        {
            "answer": "A. Subjekt, B. Objekt, C. URI , D. Prädikat ",
            "correct": False,
            "feedback": """× Nicht korrekt """
        },
        {
            "answer": "A. Subjekt, B. Objekt, C. Prädikat, D. URI",
            "correct": True,
            "feedback": """Hervorragend! Sie verstehen die Grundbausteine von semantischen Triples und ihre Funktionen innerhalb des Semantic Web."""
        }
    ]
}]

display_quiz(multiple_choice3, colors=colors.jupyterquiz)
```

### Frage 4

Erläutern Sie, warum bei der filmanalytischen Anwendung von semantischen Triplen das "Segment X" als Subjekt verwendet wird und nicht direkt der Film als Ganzes?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_C-4')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiel für korrekte Antwort:**

Die Verwendung von "Segment X" als Subjekt ermöglicht eine präzise zeitliche Lokalisierung der analytischen Beobachtungen innerhalb des Films. Da sich filmanalytische Eigenschaften wie Kamerabewegungen, Einstellungsgrößen oder Tonqualitäten im Verlauf eines Films ständig ändern, müssen die Annotationen an spezifische Zeitabschnitte gebunden sein. Mit "Segment X" können wir durch zusätzliche Tripel (z.B. "hat Timecode von") den genauen zeitlichen Bereich definieren, für den die Annotation gilt - sei es eine Einstellung, ein Frame oder eine frei gewählte Zeitspanne.

````

## Sektion II: Verständnis der AdA-Filmontologie
### Frage 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice5 = [{
    "question": """Welche Aussage beschreibt am besten die Struktur der AdA-Filmontologie?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Eine einfache Liste filmanalytischer Begriffe ohne hierarchische Struktur",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie ist keine einfache Liste oder zweigliedrige Struktur, sondern folgt einer dreistufigen hierarchischen Organisation (Ebenen, Typen, Werte), die eine detaillierte und strukturierte Erfassung filmischer Eigenschaften ermöglicht."""
        },
        {
            "answer": "Eine zweigliedrige Struktur aus Filmszenen und deren Eigenschaften",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie ist keine einfache Liste oder zweigliedrige Struktur, sondern folgt einer dreistufigen hierarchischen Organisation (Ebenen, Typen, Werte), die eine detaillierte und strukturierte Erfassung filmischer Eigenschaften ermöglicht."""
        },
        {
            "answer": "Eine hierarchische Struktur aus Leveln (Ebenen), Typen und Werten",
            "correct": True,
            "feedback": """✓ Korrekt! Die AdA-Filmontologie ist hierarchisch in Ebenen (Levels), Typen und Werte gegliedert. Diese Struktur ermöglicht eine präzise und differenzierte Erfassung filmanalytischer Konzepte sowie die Umsetzung der Relation in eine Triple-Struktur."""
        },
        {
            "answer": "Eine zufällige Sammlung von Triples ohne übergeordnete Organisation",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie ist keine einfache Liste oder zweigliedrige Struktur, sondern folgt einer dreistufigen hierarchischen Organisation (Ebenen, Typen, Werte), die eine detaillierte und strukturierte Erfassung filmischer Eigenschaften ermöglicht."""
        }
    ]
}]

display_quiz(multiple_choice5, colors=colors.jupyterquiz)
```


### Frage 6
A. Annotation Level  
B. Annotation Type  
C. Annotation Value  
D. Annotation Level


```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice6 = [{
    "question": "Ordnen Sie die folgenden filmanalytischen Begriffe der richtigen Strukturebene in der Ontologie zu",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Kamera, B. Kamerabewegung Tempo, C. Langsam, D. Montage",
            "correct": True,
            "feedback": "✓ Ausgezeichnet! Sie verstehen die hierarchische Struktur der AdA-Filmontologie und können filmanalytische Begriffe korrekt den entsprechenden Ebenen zuordnen."
        },
        {
            "answer": "A. Kamerabewegung Tempo, B. Kamera, C. Langsam, D. Montage",
            "correct": False,
            "feedback": "x Nicht korrekt. Überprüfen Sie die hierarchische Struktur der AdA-Filmontologie und die korrekte Zuordnung der Begriffe zu den Ebenen."
        },
        {
            "answer": "A. Kamera, B. Langsam, C. Kamerabewegung Tempo, D. Montage",
            "correct": False,
            "feedback": "x Nicht korrekt. Überprüfen Sie die hierarchische Struktur der AdA-Filmontologie und die korrekte Zuordnung der Begriffe zu den Ebenen."
        },
        {
            "answer": "A. Montage, B. Kamera, C. Kamerabewegung Tempo, D. Langsam",
            "correct": False,
            "feedback": "x Nicht korrekt. Überprüfen Sie die hierarchische Struktur der AdA-Filmontologie und die korrekte Zuordnung der Begriffe zu den Ebenen."
        }
    ]
}]

display_quiz(multiple_choice6, colors=colors.jupyterquiz)
```

### Frage 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice7 = [{
    "question": """Welche der folgenden Eigenschaften treffen auf die AdA-Filmontologie zu? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie umfasst 8 Beschreibungsebenen, darunter Akustik und Kamera",
            "correct": True,
            "feedback": """✓ Sehr gut! Die AdA-Filmontologie hat diese Eigenschaften, die sie zu einem umfassenden und flexiblen Tool für die filmanalytische Arbeit machen."""
        },
        {
            "answer": "Sie basiert auf der eMAEX-Methode zur Analyse audiovisueller Bewegungsbilder",
            "correct": True,
            "feedback": """✓ Sehr gut! Die AdA-Filmontologie hat diese Eigenschaften, die sie zu einem umfassenden und flexiblen Tool für die filmanalytische Arbeit machen."""
        },
        {
            "answer": "Sie ist als Linked Open Data (LOD) zugänglich",
            "correct": True,
            "feedback": """✓ Sehr gut! Die AdA-Filmontologie hat diese Eigenschaften, die sie zu einem umfassenden und flexiblen Tool für die filmanalytische Arbeit machen."""
        },
        {
            "answer": "Sie unterscheidet zwischen verschiedenen Annotationsarten wie FreeTextAnnotationType und PredefinedValuesAnnotationType",
            "correct": True,
            "feedback": """✓ Sehr gut! Die AdA-Filmontologie hat diese Eigenschaften, die sie zu einem umfassenden und flexiblen Tool für die filmanalytische Arbeit machen."""
        },
        {
            "answer": "Sie kann als Framework nur mit der Software Advene verwendet werden",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie ist zwar in Advene implementiert, aber grundsätzlich toolagnostisch konzipiert. Das bedeutet, dass ihre Prinzipien und Logik theoretisch in verschiedene Tools implementiert werden könnten, auch wenn die Ontologie derzeit angepasst ist auf das Tool Advene."""
        }
    ]
}]

display_quiz(multiple_choice7, colors=colors.jupyterquiz)
```

### Frage 8

Erläutern Sie, welche Vorteile die Verwendung einer ontologiebasierten Annotation gegenüber reinen Freitextannotationen bietet. Berücksichtigen Sie dabei sowohl methodische als auch praktische Aspekte.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_c-8')
```

````{admonition} Lösung
:class: solution, dropdown

**Hilfestellung zur Antwort: **

Gehen Sie dabei auf die Standardisierung und Vergleichbarkeit ein und reflektieren Sie, inwiefern bestimmte automatisierte Funktionen bei der Analyse größerer Datenmengen helfen können.

````

### Frage 9


```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice9 = [{
    "question": """Was bedeutet das Syntaxelement [TO] in der AdA-Filmontologie?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Es kennzeichnet einen Timecode-Offset für den Beginn einer Annotation",
            "correct": False,
            "feedback": """× Das Syntaxelement [TO] hat eine spezifische Bedeutung in der AdA-Filmontologie: Es beschreibt eine kontinuierliche Entwicklung zwischen zwei Werten. Es bezieht sich nicht auf Timecodes, Pausen oder Typenwechsel."""
        },
        {
            "answer": "Es definiert eine \"Time Out\"-Pause in der Annotation",
            "correct": False,
            "feedback": """× Das Syntaxelement [TO] hat eine spezifische Bedeutung in der AdA-Filmontologie: Es beschreibt eine kontinuierliche Entwicklung zwischen zwei Werten. Es bezieht sich nicht auf Timecodes, Pausen oder Typenwechsel."""
        },
        {
            "answer": "Es beschreibt eine kontinuierliche Entwicklung zwischen zwei Werten (z.B. \"hell [TO] dunkel\")",
            "correct": True,
            "feedback": """✓ Korrekt! Das Syntaxelement [TO] wird verwendet, um eine kontinuierliche Entwicklung zwischen zwei Werten darzustellen, wie beispielsweise den graduellen Wechsel von einer hellen zu einer dunklen Beleuchtung."""
        },
        {
            "answer": "Es markiert den Übergang zu einem anderen Annotationstyp",
            "correct": False,
            "feedback": """× Das Syntaxelement [TO] hat eine spezifische Bedeutung in der AdA-Filmontologie: Es beschreibt eine kontinuierliche Entwicklung zwischen zwei Werten. Es bezieht sich nicht auf Timecodes, Pausen oder Typenwechsel."""
        }
    ]
}]

display_quiz(multiple_choice9, colors=colors.jupyterquiz)
```


## Sektion III: Praxisnahe Anwendung und Transfer

### Frage 10

Sie planen ein eigenes Forschungsvorhaben mit dem Schwerpunkt „Bildproduktionen und Klimawandel“. Überlegen Sie, welche analytischen Dimensionen (Levels) der AdA-Filmontologie besonders relevant sein könnten und begründen Sie Ihre Auswahl. 

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_B-10')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiel für eine mögliche Antwort:**

1.	Akustik: In vielen Filmen und Videos zur Klimakrise spielt die akustische Dimension eine wichtige Rolle für die emotionale Wirkung. Besonders relevante Typen wären Musik Stimmung, um die emotionale Färbung von Szenen zu erfassen, und die Gestendynamik von Geräuschen, um dramatische Akzente wie bei Naturkatastrophendarstellungen zu analysieren.

2.	Bildkomposition: Die visuelle Darstellung von Umweltveränderungen ist zentral für viele Filme. Durch die Analyse von Farbspektren und Lichtverhältnissen könnten kontrastierende Darstellungen (z.B. intakte vs. zerstörte Natur) systematisch erfasst werden. Ebenso werden oftmals Animationsgrafiken  sowie animierte Muster/Elemente verwendet, um abstrakte Phänomene auch in der bildlichen Darstellung greifbar zu machen.

3.	Kamera: Kamerabewegungen und -perspektiven können rhetorische Strategien offenlegen, z.B. könnten Vogelperspektiven für Überblicksdarstellungen globaler Phänomene oder dynamische Kamerafahrten für dramatische Inszenierungen von Veränderungsprozessen verwendet werden.

````
