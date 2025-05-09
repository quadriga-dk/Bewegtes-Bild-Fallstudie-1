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

## Frage 1

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice1 = [{
    "question": """Worin besteht der Hauptunterschied zwischen einer tabellarischen Annotation (behandelt im vorherigen Kapitel) und den digitalen Annotationen mit Tools wie Advene und ELAN?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Digitale Tools erlauben nur die Annotation bestimmter vordefinierter Parameter",
            "correct": False,
            "feedback": """× Bei den digitalen Tools in diesem Kapitel besteht der Hauptvorteil in der Verknüpfung von Player und Annotationsdokument in einer Benutzeroberfläche. Tatsächlich arbeiten wir in diesem Kapitel mit Freitextannotationen ohne standardisiertes Vokabular, und die Parameter können frei definiert werden."""
        },
        {
            "answer": "Die Verknüpfung von Player und Annotationsdokument in einer Benutzeroberfläche",
            "correct": True,
            "feedback": """✓ Genau! Der entscheidende Unterschied liegt in der direkten Verknüpfung von Videoplayer und Annotationsdokument innerhalb einer gemeinsamen Benutzeroberfläche. Dies ermöglicht eine präzisere Annotation und bessere Erfassung zeitlicher Dynamiken."""
        },
        {
            "answer": "Digitale Tools benötigen ein standardisiertes Vokabular für die Annotation",
            "correct": False,
            "feedback": """× Bei den digitalen Tools in diesem Kapitel besteht der Hauptvorteil in der Verknüpfung von Player und Annotationsdokument in einer Benutzeroberfläche. Tatsächlich arbeiten wir in diesem Kapitel mit Freitextannotationen ohne standardisiertes Vokabular, und die Parameter können frei definiert werden."""
        },
        {
            "answer": "Freitextannotationen sind bei digitalen Tools nicht möglich",
            "correct": False,
            "feedback": """× Bei den digitalen Tools in diesem Kapitel besteht der Hauptvorteil in der Verknüpfung von Player und Annotationsdokument in einer Benutzeroberfläche. Tatsächlich arbeiten wir in diesem Kapitel mit Freitextannotationen ohne standardisiertes Vokabular, und die Parameter können frei definiert werden."""
        }
    ]
}]

display_quiz(multiple_choice1, colors=colors.jupyterquiz)
```

## Frage 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice2 = [{
    "question": """Welche Vorteile bieten digitale Annotationstools im Vergleich zur tabellarischen Annotation? (Wählen Sie alle zutreffenden Antworten aus)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Präzisere Erfassung von Zeitsegmenten",
            "correct": True,
            "feedback": """✓ Richtig! Digitale Tools ermöglichen eine frame-genaue Markierung von Zeitsegmenten, was in tabellarischen Aufzeichnungen nur schwer möglich ist."""
        },
        {
            "answer": "Bessere Darstellung von Verlaufsdynamiken",
            "correct": True,
            "feedback": """✓ Richtig! Die visuelle Darstellung von Annotationen auf Zeitlinien macht komplexe Dynamiken und Entwicklungen im Filmmaterial besser erkennbar."""
        },
        {
            "answer": "Exportmöglichkeiten in verschiedene Datenformate",
            "correct": True,
            "feedback": """✓ Richtig! Die meisten digitalen Tools bieten verschiedene Exportoptionen (XML, CSV, etc.), die eine Weiterverarbeitung der Daten in anderen Anwendungen erleichtern."""
        },
        {
            "answer": "Direktes Verhältnis zwischen Annotationsdaten und Filmmaterial",
            "correct": True,
            "feedback": """✓ Richtig! Die Integration von Player und Annotation in einer Benutzeroberfläche schafft eine unmittelbare Verbindung zwischen Beobachtung und Dokumentation."""
        },
        {
            "answer": "Automatische Erkennung aller filmanalytischen Parameter",
            "correct": False,
            "feedback": """× Die automatische Erkennung aller filmanalytischen Parameter ist nicht gegeben. In diesem Kapitel arbeiten wir mit Freitexteingaben, und auch fortgeschrittenere Tools können nicht alle filmanalytischen Parameter automatisch erkennen."""
        }
    ]
}]

display_quiz(multiple_choice2, colors=colors.jupyterquiz)
```

## Frage 3
A. Annotationszeilen in ELAN  
B. Format für den Inhalt einer Annotation  
C. Standardformat zur Angabe des Dateityps und Inhalts  
D. Methoden unabhängig von spezifischen Werkzeugen anwenden  


```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice3 = [{
    "question": """Ordnen Sie die Begriffe ihren korrekten Definitionen zu:
 """,
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Mime Type, B. Tiers, C. Toolagnostische Perspektive, D. Content Type",
            "correct": False,
            "feedback": """× Nicht korrekt. """
        },
        {
            "answer": "A. Tiers, B. Content Type, C. Mime Type, D. Toolagnostische Perspektive",
            "correct": True,
            "feedback": """✓ Sehr gut! """
        },
        {
            "answer": "A. Mime Type, B. Tiers, C. Content Type , D. Toolagnostische Perspektive ",
            "correct": False,
            "feedback": """× Nicht korrekt."""
        },
        {
            "answer": "A. Tiers, B. Mime Type, C. Content Type, D. Toolagnostische Perspektive",
            "correct": False,
            "feedback": """× Nicht korrekt."""
        }
    ]
}]

display_quiz(multiple_choice3, colors=colors.jupyterquiz)
```

## Frage 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice4 = [{
    "question": """Was muss in Advene zunächst getan werden, bevor mit der eigentlichen Annotation begonnen werden kann?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Annotationstypen müssen aus einer vordefinierten Liste ausgewählt werden",
            "correct": False,
            "feedback": """× In Advene müssen wir zunächst das Video mit dem Package verknüpfen und unsere Annotationstypen selbst erstellen. Es gibt keine vordefinierte Liste, und ein Schema ist für Freitextannotationen nicht erforderlich. Das Laden von Templates ist eine Option, aber kein notwendiger erster Schritt."""
        },
        {
            "answer": "Ein Schema mit standardisiertem Vokabular muss importiert werden",
            "correct": False,
            "feedback": """× In Advene müssen wir zunächst das Video mit dem Package verknüpfen und unsere Annotationstypen selbst erstellen. Es gibt keine vordefinierte Liste, und ein Schema ist für Freitextannotationen nicht erforderlich. Das Laden von Templates ist eine Option, aber kein notwendiger erster Schritt."""
        },
        {
            "answer": "Das Video muss mit dem Package verknüpft und Annotationstypen müssen erstellt werden",
            "correct": True,
            "feedback": """✓ Richtig! Der erste wichtige Schritt besteht darin, das Video mit dem Advene-Package zu verknüpfen und die eigenen Annotationstypen (Parameter) zu erstellen."""
        },
        {
            "answer": "Ein vorhandenes Annotationspaket muss als Template geladen werden",
            "correct": False,
            "feedback": """× In Advene müssen wir zunächst das Video mit dem Package verknüpfen und unsere Annotationstypen selbst erstellen. Es gibt keine vordefinierte Liste, und ein Schema ist für Freitextannotationen nicht erforderlich. Das Laden von Templates ist eine Option, aber kein notwendiger erster Schritt."""
        }
    ]
}]

display_quiz(multiple_choice4, colors=colors.jupyterquiz)
```

## Frage 5
Wie kann in Advene eine neue Annotation mit höchstmöglicher Präzision erstellt werden?


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_B-5')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiel für korrekte Antwort:**

Durch Rechtsklick auf die gewünschte Spur und Auswahl von 'New annotation at player time', da dies den aktuellen Videoplayer-Timecode verwendet, was präziser ist als die Positionierung per Mauszeiger. Für noch präzisere Grenzen kann die Frametaste in der Wiedergabesteuerung genutzt werden.

````

## Frage 6

In Advene möchten Sie eine Annotation duplizieren und ihren Wert ändern. Beschreiben Sie die Schritte bei diesem Vorgehen:

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_B-6')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiel für korrekte Antwort:**

- Rechtsklick auf die zu duplizierende Annotation
- Option 'Duplicate' wählen
- Die duplizierte Annotation wird erstellt
- Anschließend auf die neue Annotation klicken und mit 'Enter' das Textfeld öffnen
- Den Text ändern und erneut 'Enter' drücken, um die Änderung zu speichern
````
## Frage 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice7 = [{
    "question": """Was ist bei der Einrichtung eines neuen Projekts in ELAN im Vergleich zu Advene anders? (Wählen Sie alle zutreffenden Antworten aus)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "In ELAN können keine Freitextannotationen erstellt werden",
            "correct": False,
            "feedback": """× ELAN unterstützt durchaus Freitextannotationen, erlaubt die Anpassung von Annotationszeilen und bietet auch die Möglichkeit, Templates zu erstellen. Der Unterschied liegt in der Notwendigkeit, explizit die automatische Sicherheitskopie zu aktivieren."""
        },
        {
            "answer": "In ELAN muss zusätzlich die automatische Sicherheitskopie aktiviert werden",
            "correct": True,
            "feedback": """✓ Richtig! Ein wichtiger Unterschied ist, dass in ELAN explizit die automatische Sicherheitskopie aktiviert werden sollte, um Datenverluste zu vermeiden."""
        },
        {
            "answer": "ELAN erlaubt keine Anpassung der Annotationszeilen",
            "correct": False,
            "feedback": """× ELAN unterstützt durchaus Freitextannotationen, erlaubt die Anpassung von Annotationszeilen und bietet auch die Möglichkeit, Templates zu erstellen. Der Unterschied liegt in der Notwendigkeit, explizit die automatische Sicherheitskopie zu aktivieren."""
        },
        {
            "answer": "In ELAN können keine Templates erstellt werden",
            "correct": False,
            "feedback": """× ELAN unterstützt durchaus Freitextannotationen, erlaubt die Anpassung von Annotationszeilen und bietet auch die Möglichkeit, Templates zu erstellen. Der Unterschied liegt in der Notwendigkeit, explizit die automatische Sicherheitskopie zu aktivieren."""
        }
    ]
}]

display_quiz(multiple_choice7, colors=colors.jupyterquiz)
```

## Frage 8

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice8 = [{
    "question": """Welche dieser Funktionen bietet ELAN bei der Arbeit mit Annotationen? (Wählen Sie alle zutreffenden Antworten aus)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Annotationen können zwischen Zeilen kopiert werden",
            "correct": True,
            "feedback": """✓ Sehr gut! ELAN ermöglicht das Kopieren von Annotationen zwischen verschiedenen Zeilen, was die Arbeit mit ähnlichen Inhalten erleichtert."""
        },
        {
            "answer": "Annotationen können in ihrer Länge verändert werden",
            "correct": True,
            "feedback": """✓ Sehr gut! ELAN erlaubt das flexible Anpassen der Annotationslänge durch einfaches Ziehen der Ränder, was eine präzise zeitliche Markierung ermöglicht."""
        },
        {
            "answer": "Annotationen können aufgeteilt werden",
            "correct": True,
            "feedback": """✓ Sehr gut! ELAN bietet die Möglichkeit, bestehende Annotationen in mehrere Teile aufzuteilen, was besonders bei längeren Segmenten hilfreich ist."""
        },
        {
            "answer": "Die Wiedergabegeschwindigkeit kann angepasst werden",
            "correct": True,
            "feedback": """✓ Sehr gut! ELAN erlaubt die Anpassung der Wiedergabegeschwindigkeit, was die genaue Analyse von schnellen Sequenzen oder die Erfassung feiner Details erleichtert."""
        },
        {
            "answer": "Automatische Erkennung von Einstellungswechseln",
            "correct": False,
            "feedback": """× Die automatische Erkennung von Einstellungswechseln ist keine Funktion, die in der Standard-Version von ELAN angeboten wird. Diese müssten manuell annotiert werden."""
        }
    ]
}]

display_quiz(multiple_choice8, colors=colors.jupyterquiz)
```

## Frage 9

In welchen Fällen ist die Anpassung der Wiedergabegeschwindigkeit in ELAN besonders sinnvoll?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_B-9')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiel für korrekte Antwort:**

Die Anpassung der Wiedergabegeschwindigkeit ist besonders sinnvoll bei schnellen Einstellungswechseln oder komplexen Bewegungen, die in normaler Geschwindigkeit schwer zu erfassen sind. Die Verlangsamung ermöglicht es, Details präziser zu beobachten und den eigenen Annotationsrhythmus anzupassen, um sicherzustellen, dass alle wichtigen Elemente erfasst werden.
````

## Frage 10

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice10 = [{
    "question": """Welche der folgenden Aussagen treffen auf beide Tools (Advene und ELAN) zu? (Wählen Sie alle zutreffenden Antworten aus)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie ermöglichen die Annotation auf einer Timeline",
            "correct": True,
            "feedback": """✓ Sehr gut! Beide Tools bieten eine Timeline-basierte Annotationsschnittstelle, die eine visuelle Darstellung der zeitlichen Verteilung von Annotationen ermöglicht."""
        },
        {
            "answer": "Sie erlauben die Einbettung von Videos",
            "correct": True,
            "feedback": """✓ Sehr gut! Sowohl Advene als auch ELAN integrieren den Videoplayer direkt in die Benutzeroberfläche, was ein simultanes Arbeiten mit Video und Annotation ermöglicht."""
        },
        {
            "answer": "Sie bieten Exportmöglichkeiten in andere Formate",
            "correct": True,
            "feedback": """✓ Sehr gut! Beide Tools verfügen über Exportfunktionen, die es ermöglichen, Annotationsdaten in verschiedenen Formaten (wie XML, CSV) für die weitere Verarbeitung zu speichern."""
        },
        {
            "answer": "Sie ermöglichen präzisere Annotationen als tabellarische Methoden",
            "correct": True,
            "feedback": """✓ Sehr gut! Durch die direkte Verknüpfung mit dem Videomaterial und frame-genaue Markierungsmöglichkeiten bieten beide Tools eine höhere Präzision als tabellarische Methoden."""
        },
        {
            "answer": "Sie erfordern ein standardisiertes Vokabular",
            "correct": False,
            "feedback": """× Weder Advene noch ELAN erfordern in der Grundkonfiguration ein standardisiertes Vokabular. Beide erlauben Freitextannotationen, wie in diesem Kapitel beschrieben."""
        }
    ]
}]

display_quiz(multiple_choice10, colors=colors.jupyterquiz)
```

## Frage 11

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice11 = [{
    "question": """Was bedeutet der Begriff "toolagnostisch" im Kontext dieser Fallstudie?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Dass die verwendeten Tools keine Annotationen unterstützen",
            "correct": False,
            "feedback": """× Der Begriff "toolagnostisch" bezieht sich darauf, dass die grundlegenden Konzepte und Methoden mit verschiedenen Tools umgesetzt werden können. Es geht nicht um Betriebssystemkompatibilität, fehlende Annotationsunterstützung oder Vorkenntnisse, sondern um die Übertragbarkeit der methodischen Prinzipien."""
        },
        {
            "answer": "Dass die Tools unabhängig vom Betriebssystem funktionieren",
            "correct": False,
            "feedback": """× Der Begriff "toolagnostisch" bezieht sich darauf, dass die grundlegenden Konzepte und Methoden mit verschiedenen Tools umgesetzt werden können. Es geht nicht um Betriebssystemkompatibilität, fehlende Annotationsunterstützung oder Vorkenntnisse, sondern um die Übertragbarkeit der methodischen Prinzipien."""
        },
        {
            "answer": "Dass die Methoden und Konzepte unabhängig von spezifischen Werkzeugen anwendbar sind",
            "correct": True,
            "feedback": """✓ Genau! Toolagnostisch bedeutet, dass die Methoden und Konzepte prinzipiell mit verschiedenen Tools umgesetzt werden können und nicht an ein spezifisches Werkzeug gebunden sind."""
        },
        {
            "answer": "Dass die Tools keine Vorkenntnisse erfordern",
            "correct": False,
            "feedback": """× Der Begriff "toolagnostisch" bezieht sich darauf, dass die grundlegenden Konzepte und Methoden mit verschiedenen Tools umgesetzt werden können. Es geht nicht um Betriebssystemkompatibilität, fehlende Annotationsunterstützung oder Vorkenntnisse, sondern um die Übertragbarkeit der methodischen Prinzipien."""
        }
    ]
}]

display_quiz(multiple_choice11, colors=colors.jupyterquiz)
```
## Frage 12

Erstellen Sie einen kurzen Annotationsplan für ein Video Ihrer Wahl mit dem Schwerpunkt Klimakrise mit folgenden Anforderungen:

- Wählen Sie mind. 5 relevante Parameter aus, die sie an die Gestaltungsweise des ausgewählten Videos anpassen 
- Entscheiden Sie für jeden Parameter, ob er nach Einstellungen oder nach Verläufen annotiert werden sollte
- Begründen Sie Ihre Entscheidungen

## Frage 13

Welche Herausforderungen könnten bei der Annotation eines längeren Videos/Films mit den vorgestellten Tools auftreten? Wie würden Sie diese Herausforderungen methodisch angehen?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_B-9')
```

````{admonition} Lösung
:class: solution, dropdown

**Hilfestellung zur Antwort:**

Überlegen Sie, welche spezifischen Herausforderungen ein längerer Film mit sich bringt (Datenmenge, Konsistenz der Annotation, zeitlicher Aufwand). Reflektieren Sie, wie diese Herausforderungen durch methodische Ansätze (z.B. Arbeit mit Templates, Segmentierung in kleinere Einheiten, Entwicklung eines einheitlichen Annotationsschemas) adressiert werden könnten.
````