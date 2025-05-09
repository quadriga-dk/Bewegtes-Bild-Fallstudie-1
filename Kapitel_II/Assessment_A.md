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

## Sektion I: Verständnis von Filmsegmentierung und Basisparametern

#### Frage 1

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice1 = [{
    "question": """Welche der folgenden Einheiten gilt als die kleinste filmische Einheit?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Szene",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Einstellung ist die kleinste vollständige filmische Einheit - eine ununterbrochene Aufnahme ohne Schnitt. Während Frames technisch gesehen kleinere Elemente sind, handelt es sich dabei um einzelne Standbilder, die Einstellungen bilden, nicht um vollständige Filmeinheiten. Szenen und Sequenzen sind größere Einheiten, die aus mehreren Einstellungen bestehen."""
        },
        {
            "answer": "Sequenz",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Einstellung ist die kleinste vollständige filmische Einheit - eine ununterbrochene Aufnahme ohne Schnitt. Während Frames technisch gesehen kleinere Elemente sind, handelt es sich dabei um einzelne Standbilder, die Einstellungen bilden, nicht um vollständige Filmeinheiten. Szenen und Sequenzen sind größere Einheiten, die aus mehreren Einstellungen bestehen."""
        },
        {
            "answer": "Einstellung",
            "correct": True,
            "feedback": """✓ Richtig! Eine Einstellung gilt als die kleinste vollständige filmische Einheit - eine ununterbrochene Aufnahme ohne Schnitt, die aus mehreren Frames besteht."""
        },
        {
            "answer": "Frame (Einzelbild)",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Einstellung ist die kleinste vollständige filmische Einheit - eine ununterbrochene Aufnahme ohne Schnitt. Während Frames technisch gesehen kleinere Elemente sind, handelt es sich dabei um einzelne Standbilder, die Einstellungen bilden, nicht um vollständige Filmeinheiten. Szenen und Sequenzen sind größere Einheiten, die aus mehreren Einstellungen bestehen."""
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
from quadriga_config import colors

multiple_choice2 = [{
    "question": """Welche der folgenden Basisparameter sind korrekt definiert? (Wählen Sie alle zutreffenden Optionen aus)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Einstellungsgröße: Das Größenverhältnis des abgebildeten Subjekts (Person)/Objekts zur Kadrage (Bildfeld)",
            "correct": True,
            "feedback": """✓ Ausgezeichnet! Diese Parameter sind korrekt definiert (vgl. Kurzdefinition der Parameter)."""
        },
        {
            "answer": "Kameraperspektive: Die Bewegung der Kamera durch den Raum",
            "correct": False,
            "feedback": """× Achtung bei diesen Definitionen. Die Kameraperspektive bezieht sich auf die Blickorientierung der Kamera auf ein Objekt/Subjekt, nicht auf ihre Bewegung. Ton umfasst alle hörbaren Elemente einschließlich Musik, Umgebungsgeräusche und Effekte – nicht nur Dialog. Überprüfen Sie hier die Parameterdefinitionen."""
        },
        {
            "answer": "Montage/Schnitt: Verbindung der einzelnen Einstellungen zueinander, Zusammenfügung von Bild- und Toneinheiten",
            "correct": True,
            "feedback": """✓ Ausgezeichnet! Diese Parameter sind korrekt definiert (vgl. Kurzdefinition der Parameter)."""
        },
        {
            "answer": "Ton: Nur Dialog und gesprochene Worte, die in einem Film zu hören sind",
            "correct": False,
            "feedback": """× Achtung bei diesen Definitionen. Die Kameraperspektive bezieht sich auf die Blickorientierung der Kamera auf ein Objekt/Subjekt, nicht auf ihre Bewegung. Ton umfasst alle hörbaren Elemente einschließlich Musik, Umgebungsgeräusche und Effekte – nicht nur Dialog. Überprüfen Sie hier die Parameterdefinitionen."""
        },
        {
            "answer": "Licht: Gestaltung der Hell-Dunkel-Kontraste sowie Lichtstärke",
            "correct": True,
            "feedback": """✓ Ausgezeichnet! Diese Parameter sind korrekt definiert (vgl. Kurzdefinition der Parameter)."""
        }
    ]
}]

display_quiz(multiple_choice2, colors=colors.jupyterquiz)
```

### Frage 3
A. Größte Einheit, die narrative oder formal-ästhetische Stränge verbindet
B. Teilabschnitt eines Films mit Kontinuität von Raum, Zeit und Figuren
C. Ununterbrochene Aufnahme ohne Schnitt
D. Einzelbild, für das menschliche Auge kaum sichtbar

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice3 = [{
    "question": """Ordnen Sie die filmischen Segmentierungseinheiten ihren korrekten Definitionen zu:

 """,
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Szene - B. Sequenz - c. Einstellung - D. Frame",
            "correct": False,
            "feedback": """× Nicht korrekt"""
        },
        {
            "answer": "A. Sequenz - B. Szene -  C. Einstellung - D. Frame",
            "correct": True,
            "feedback": """✓ Sehr gut! Sie verstehen die Hierarchie der filmischen Segmentierungseinheiten von der größten (Sequenz) bis zur kleinsten (Frame)."""
        },
        {
            "answer": "A. Sequenz - B. Szene - C. Frame - D. Einstellung",
            "correct": False,
            "feedback": """× Nicht korrekt"""
        },
        {
            "answer": "A. Frame - B. Einstellung - C. Szene - D. Sequenz",
            "correct": False,
            "feedback": """× Nicht korrekt"""
        }
    ]
}]

display_quiz(multiple_choice3, colors=colors.jupyterquiz)
```

## Sektion II: Erstellung und Diskussion tabellarischer Annotationen

### Frage 4

Ordnen Sie die folgenden Schritte zur Durchführung einer tabellarischen Annotationsanalyse in der richtigen Reihenfolge an:

1. Bestimmung der Basisparameter für die zu analysierenden Segmente
2. Auswahl einer geeigneten Segmentierungslogik (z.B. Einstellungen)
3. Segmentierung des Videos entsprechend der gewählten Logik
4. Erstellung der tabellarischen Annotation durch Zuordnung von Werten zu Parametern

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice_4 = [{
    "question": """Welche Reihenfolge ist korrekt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "1 → 2 → 3 → 4",
            "correct": True,
            "feedback": """✓ Richtig! Dies ist der korrekte Arbeitsablauf für die tabellarische Filmannotation. Die Einhaltung eines systematischen Ansatzes gewährleistet, dass Ihre Analyse umfassend und methodisch ist."""
        },
        {
            "answer": "2 → 1 → 3 → 4",
            "correct": False,
            "feedback": """× Nicht korrekt. Obwohl es sinnvoll erscheinen mag, zuerst die Segmentierungslogik festzulegen, sollten die zu untersuchenden Parameter zuerst bestimmt werden, um den Analyserahmen zu definieren."""
        },
        {
            "answer": "2 → 3 → 1 → 4",
            "correct": False,
            "feedback": """× Nicht korrekt. Die Basisparameter sollten bereits vor der Segmentierung festgelegt werden, damit klar ist, welche Aspekte in den einzelnen Segmenten untersucht werden sollen."""
        },
        {
            "answer": "4 → 1 → 2 → 3",
            "correct": False,
            "feedback": """× Nicht korrekt. Die tabellarische Annotation (4) ist der letzte Schritt im Prozess und kann erst erfolgen, nachdem die Parameter bestimmt und das Video segmentiert wurde."""
        }
    ]
}]

display_quiz(multiple_choice_4, colors=colors.jupyterquiz)
```

### Frage 5
Warum könnte eine Segmentierung nach Dynamiken für bestimmte analytische Zwecke nützlicher sein als eine Segmentierung nach Einstellungen?


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_A-5')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiel für korrekte Antwort:**
Die Segmentierung nach Dynamiken ermöglicht es, kontinuierliche Entwicklungen und Muster (wie Veränderungen der Lichtverhältnisse oder der Einsatz eines musikalischen Stückes) zu erfassen, die über einzelne Einstellungen hinausgehen. Dieser Ansatz berücksichtigt den zeitlichen Verlauf audiovisueller Gestaltungsmittel besser und kann Muster aufzeigen, die über Einstellungsgrenzen hinweg inszeniert werden.


**Feedback:**
Das Verständnis alternativer Segmentierungsmethoden ist entscheidend für eine umfassende Filmanalyse. Während die einstellungsbasierte Segmentierung üblich ist, können dynamikbasierte Ansätze besser für analytische Qualifizierungen des Gegenstandes geeignet sein.

````
## Sektion III: (Methodologische) Reflexion

### Frage 6

Vergleichen Sie die Vor- und Nachteile der tabellarischen Annotation als Methode der deskriptiven Filmanalyse. Wie könnten digitale Annotationstools einige dieser Nachteile adressieren?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_A-6')
```

````{admonition} Lösung
:class: solution, dropdown

**Feedback:**
Eine durchdachte Reflexion über methodische Ansätze demonstriert Ihr Verständnis nicht nur darüber, wie Analysen durchzuführen sind, sondern auch über die Stärken und Grenzen verschiedener Analysewerkzeuge.

````
### Frage 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice7 = [{
    "question": """Welches der folgenden Antwortmöglichkeiten ist kein Nachteil tabellarischer Annotationsmethoden?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Fehlen eines standardisierten Vokabulars für konsistente Analysen",
            "correct": False,
            "feedback": """× Obwohl die tabellarische Annotation mehrere Einschränkungen bezüglich Standardisierung, Erfassung von Dynamiken und Datenexport aufweist, ist sie durchaus in der Lage, grundlegende visuelle und auditive Elemente des Films zu dokumentieren. Ihre primären Schwächen liegen in anderen Bereichen."""
        },
        {
            "answer": "Schwierigkeit, zeitliche Dynamiken über Einstellungsgrenzen hinweg zu erfassen",
            "correct": False,
            "feedback": """× Obwohl die tabellarische Annotation mehrere Einschränkungen bezüglich Standardisierung, Erfassung von Dynamiken und Datenexport aufweist, ist sie durchaus in der Lage, grundlegende visuelle und auditive Elemente des Films zu dokumentieren. Ihre primären Schwächen liegen in anderen Bereichen."""
        },
        {
            "answer": "Unfähigkeit, Daten effizient für weitere Analysen zu exportieren",
            "correct": False,
            "feedback": """× Obwohl die tabellarische Annotation mehrere Einschränkungen bezüglich Standardisierung, Erfassung von Dynamiken und Datenexport aufweist, ist sie durchaus in der Lage, grundlegende visuelle und auditive Elemente des Films zu dokumentieren. Ihre primären Schwächen liegen in anderen Bereichen."""
        },
        {
            "answer": "Unfähigkeit, grundlegende visuelle und auditive Elemente des Films zu dokumentieren",
            "correct": True,
            "feedback": """✓ Richtig! Die tabellarische Annotation kann grundlegende visuelle und auditive Elemente effektiv dokumentieren. Ihre Grenzen liegen in der Standardisierung, der Erfassung zeitlicher Beziehungen und der Dateninteroperabilität – nicht in der Dokumentation grundlegender Elemente."""
        }
    ]
}]

display_quiz(multiple_choice7, colors=colors.jupyterquiz)
```

### Frage 8

Basierend auf Ihrer Erfahrung mit tabellarischer Annotation, welche Aspekte der audiovisuellen Analyse waren am schwierigsten im tabellarischen Format zu erfassen und warum?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_A-8')
```

````{admonition} Lösung
:class: solution, dropdown
**Hilfestellung zur Antwort:**
Überlegen Sie, welche zeitlichen oder relationalen Aspekte schwierig zu dokumentieren waren. Reflektieren Sie, wie die Segmentierungsmethode Ihre den Prozess der Analyse beeinflusst haben könnte.

**Feedback:**
Diese Reflexion hilft Ihnen, die Stärken und Grenzen verschiedener analytischer Ansätze zu erkennen. Das Verständnis dieser Grenzen ist entscheidend für die Entwicklung eines umfassenderen analytischen Instrumentariums und für die Auswahl geeigneter Methoden für unterschiedliche Forschungsfragen.


````


