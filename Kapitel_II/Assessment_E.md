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
## Sektion I: Grundverständnis der AdA-Timeline

### Frage 1

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_ada1 = [{
    "question": """Was ist der Hauptzweck der AdA-Timeline?""",
    "type": "multiple_choice",
    "answers": [
        {"answer": "Die Erstellung neuer Annotationen für filmisches Material", "correct": False,
         "feedback": "× Die AdA-Timeline ist ein Visualisierungswerkzeug für bereits erstellte Annotationen und nicht für deren Erstellung gedacht."},
        {"answer": "Die automatische Erkennung von Einstellungen und Szenen", "correct": False,
         "feedback": "× Diese Funktion wird in Advene durchgeführt, nicht durch die AdA-Timeline."},
        {"answer": "Die Visualisierung bereits erstellter Annotationsdaten zur Datenexploration und Hypothesenpräsentation", "correct": True,
         "feedback": "✓ Richtig! Die AdA-Timeline dient primär der Visualisierung bereits erstellter Annotationsdaten."},
        {"answer": "Die Korrektur fehlerhafter Annotationen aus dem Advene-Template", "correct": False,
         "feedback": "× Die AdA-Timeline bietet keine direkte Funktion zur Korrektur von Annotationen."}
    ]
}]

display_quiz(multiple_choice_ada1, colors=colors.jupyterquiz)
```

### Frage 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors


multiple_choice_ada2 = [{
    "question": """Welche der folgenden Eigenschaften treffen auf die AdA-Timeline zu? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {"answer": "Sie ermöglicht eine dynamische, partiturähnliche Darstellung filmischer Gestaltungsweisen", "correct": True,
         "feedback": "✓ Korrekt. Diese Darstellung berücksichtigt die zeitliche Struktur filmischer Mittel."},
        {"answer": "Sie stellt verschiedene Annotationstypen als synchrone Spuren untereinander dar", "correct": True,
         "feedback": "✓ Genau! Die Timeline zeigt unterschiedliche Annotationstypen parallel."},
        {"answer": "Sie erlaubt das Zoomen in spezifische Zeitabschnitte eines Films", "correct": True,
         "feedback": "✓ Richtig. Dies hilft bei der detaillierten Analyse bestimmter Filmsequenzen."},
        {"answer": "Sie kann für Präsentationen und Publikationen als Bild exportiert werden", "correct": True,
         "feedback": "✓ Ja, die Exportfunktion erleichtert die Weiterverwendung der Visualisierungen."},
        {"answer": "Sie kann Annotationen automatisch erkennen und kategorisieren", "correct": False,
         "feedback": "× Diese Funktion wird durch Advene bereitgestellt, nicht durch die Timeline selbst."}
    ]
}]

display_quiz(multiple_choice_ada2, colors=colors.jupyterquiz)
```

### Frage 3
Erläutern Sie, warum die AdA-Timeline als partiturähnliche Darstellung konzipiert wurde und wie dies mit der zeitlichen Natur von Filmen zusammenhängt.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_E-3')
```
````{admonition} Lösung
:class: solution, dropdown
**Beispiel für korrekte Antwort:**

Die AdA-Timeline wurde als partiturähnliche Darstellung konzipiert, um der zeitlichen Erscheinungsweise filmischer Bilder gerecht zu werden. Filme sind zeitbasierte Medien, deren ästhetische Erfahrung sich durch das Zusammenspiel verschiedener Gestaltungsebenen über die Zeit entfaltet. Ähnlich wie in einer musikalischen Partitur, wo verschiedene Instrumentenlinien synchron dargestellt werden, ermöglicht die AdA-Timeline die synchrone Darstellung verschiedener filmischer Elemente (Kamerabewegung, Musik, Farbe etc.) auf parallelen Spuren. Dies erlaubt es, sowohl den zeitlichen Verlauf einzelner Parameter als auch deren Zusammenwirken zu einem bestimmten Zeitpunkt zu erfassen. Diese Darstellungsform versucht, die in traditionellen deskriptiven Methoden oft vernachlässigte zeitliche Dynamik und Synchronizität filmischer Elemente einzuholen und damit die Diskrepanz zwischen analytischer Betrachtung und tatsächlicher Wahrnehmungserfahrung zu verringern.

````

## Sektion II: Bedienung und Konfiguration der AdA-Timeline

### Frage 4

```{code-cell} ipython3
:tags: [remove-input]

import sys
sys.path.append("../quadriga")
from assessment import DragDropQuiz

quiz = DragDropQuiz()

quiz.create_matching_quiz(
    title="Ordnen Sie die folgenden Schritte zur Öffnung und Konfiguration der AdA-Timeline in der richtigen Reihenfolge an:",
    descriptions=[
        "Syntaxelemente im Edit-Fenster anpassen",
        "AdA-Template-Annotationspaket in Advene öffnen",
        "W3-Symbol in der Icon-Leiste klicken und Timeline-Variante auswählen",
        "‚Edit‘-Button klicken, um das Edit-Fenster zu öffnen",
        "Änderungen mit ‚OK‘ bestätigen, um die Timeline neu zu laden",
        "Im Browser öffnet sich die Timeline mit Standardkonfiguration"
    ],
    options=["1", "2", "3", "4", "5", "6"],
    correct_mapping={
        "AdA-Template-Annotationspaket in Advene öffnen": "1",
        "W3-Symbol in der Icon-Leiste klicken und Timeline-Variante auswählen": "2",
        "Im Browser öffnet sich die Timeline mit Standardkonfiguration": "3",
        "‚Edit‘-Button klicken, um das Edit-Fenster zu öffnen": "4",
        "Syntaxelemente im Edit-Fenster anpassen": "5",
        "Änderungen mit ‚OK‘ bestätigen, um die Timeline neu zu laden": "6"
    }
)
```

### Frage 5

```{code-cell} ipython3
:tags: [remove-input]

import sys
sys.path.append("../quadriga")
from assessment import DragDropQuiz

quiz = DragDropQuiz()

quiz.create_matching_quiz(
    title="Ordnen Sie die folgenden Darstellungsformen der AdA-Timeline ihrer korrekten Beschreibung zu:",
    descriptions=[
        "Annotationen werden in Zeilen mit eigenen Farben als Balken angezeigt",
        "Geeignet für Annotationstypen ohne Überlappungen von Werten",
        "Breite und Höhe der Blöcke entsprechen der Dauer einer Annotation",
        "Darstellung für numerische Werte mit Ausschlägen in beide Richtungen"
    ],
    options=["Balkendiagramm (rect)", "Einzeilige Darstellung (single_line)", "Säulenansicht (hist)", "Wellenform (wave)"],
    correct_mapping={
        "Annotationen werden in Zeilen mit eigenen Farben als Balken angezeigt": "Balkendiagramm (rect)",
        "Geeignet für Annotationstypen ohne Überlappungen von Werten": "Einzeilige Darstellung (single_line)",
        "Breite und Höhe der Blöcke entsprechen der Dauer einer Annotation": "Säulenansicht (hist)",
        "Darstellung für numerische Werte mit Ausschlägen in beide Richtungen": "Wellenform (wave)"
    }
)
```

### Frage 6

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_ada6 = [{
    "question": """Wie kann eine angepasste Konfiguration der AdA-Timeline am besten gespeichert werden?""",
    "type": "multiple_choice",
    "answers": [
        {"answer": "Über den \"Save\"-Button im Edit-Fenster", "correct": False,
         "feedback": "× Diese Funktion speichert die Konfiguration nicht dauerhaft."},
        {"answer": "Durch Speichern des gesamten Browser-Fensters als HTML-Datei", "correct": False,
         "feedback": "× Diese Methode sichert nicht die Konfigurationsdaten."},
        {"answer": "Durch Kopieren des Inhalts des Edit-Fensters in ein Textprogramm", "correct": True,
         "feedback": "✓ Richtig! So kann die Konfiguration später wieder verwendet werden."},
        {"answer": "Die Konfiguration wird automatisch in Advene gespeichert", "correct": False,
         "feedback": "× Nein, eine automatische Speicherung erfolgt nicht."}
    ]
}]

display_quiz(multiple_choice_ada6, colors=colors.jupyterquiz)
```

### Frage 7 (a)

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

fill_in_blank_question1 = [{
    "question": "In der AdA-Timeline werden Syntaxelemente mit dem Zeichen ________ voneinander getrennt.",
    "type": "string",
    "answers": [
        {
            "answer": "&",
            "correct": True,
            "feedback": "Excellent!"
        }
    ]
}]


display_quiz(fill_in_blank_question1, colors=colors.jupyterquiz)

```

### Frage 7 (b)

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

fill_in_blank_question2 = [{
    "question": "Um einen spezifischen Zeitabschnitt festzulegen, wird das Syntaxelement ________ verwendet, gefolgt von Start- und Endzeit, getrennt durch ein ________. Bitte geben Sie Ihre Antworten in der folgenden Form ein: Antwort1, Antwort2",
    "type": "string",
    "answers": [
        {
            "answer": "&t=, Komma",
            "correct": True,
            "match_case": False,
            "feedback": "Sehr gut!"
        },
        {
            "answer": "&t=,Komma",
            "correct": True,
            "match_case": False,
            "feedback": "Sehr gut!"
        }
    ]
}]


display_quiz(fill_in_blank_question2, colors=colors.jupyterquiz)

```

### Frage 7 (c)

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

fill_in_blank_question3 = [{
    "question": """Die Darstellungsoptionen für einzelne Annotationstypen werden in ________ nach der ID des Typs angegeben. Möchte man mehrere Darstellungsoptionen für einen Typ definieren, werden diese durch ein ________ voneinander getrennt. Bitte geben Sie Ihre Antworten in der folgenden Form ein: Antwort1, Antwort2""",
    "type": "string",
    "answers": [
        {
            "answer": "Klammern, Leerzeichen",
            "correct": True,
            "match_case": False,
            "feedback": "Richtig!"
        },
        {
            "answer": "Klammern,Leerzeichen",
            "correct": True,
            "match_case": False,
            "feedback": "Richtig!"
        },
        {
            "answer": "brackets, space",
            "correct": True,
            "match_case": False,
            "feedback": "Richtig!"
        },
        {
            "answer": "brackets,space",
            "correct": True,
            "match_case": False,
            "feedback": "Richtig!"
        }
    ]
}]


display_quiz(fill_in_blank_question3, colors=colors.jupyterquiz)

```


### Frage 8

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice_ada8 = [{
    "question": """Welche der folgenden Darstellungsoptionen können in der AdA-Timeline konfiguriert werden? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {"answer": "representation (Darstellungsform wie rect, hist, wave)", "correct": True,
         "feedback": "✓ Ja, dies legt die Visualisierungsart fest."},
        {"answer": "height (Höhe der Darstellung in Pixeln)", "correct": True,
         "feedback": "✓ Genau, zur Festlegung der visuellen Höhe."},
        {"answer": "legend (Anzeige einer Legende)", "correct": True,
         "feedback": "✓ Ja, für die Anzeige einer Legende zu den Farben und Formen."},
        {"answer": "colorscheme (Farbschema für die Darstellung)", "correct": True,
         "feedback": "✓ Richtig, zur Änderung der Farbgestaltung."},
        {"answer": "labels (Anzeige einer Timecode-Leiste)", "correct": True,
         "feedback": "✓ Korrekt, dient der besseren zeitlichen Orientierung."}
    ]
}]

display_quiz(multiple_choice_ada8, colors=colors.jupyterquiz)
```

## Sektion III: Datenexploration, Interpretation und Methodenreflexion 

### Frage 9
Erläutern Sie, wie die AdA-Timeline zur Exploration und Interpretation audiovisueller Inszenierungsmuster genutzt werden kann. Beziehen Sie sich dabei auf konkrete Beispiele wie Schnittrhythmus, Bewegungsdynamik oder Farbgestaltung.


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_E-9')
```

````{admonition} Hilfestellung zur Antwort
:class: solution, dropdown

Gehen Sie näher auf den Zusammenhang zwischen der Visualisierung und der Identifikation von Mustern ein – was wird sichtbar?

Wie kann die Synchronizität verschiedener Parameter analytisch greifbar gemacht werden? Reflektieren Sie über die Rolle der Visualisierung im Interpretationsprozess und berücksichtigen Sie sowohl quantitative als auch qualitative Aspekte der Dateninterpretation.

````

### Frage 10

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice10 = [{
    "question": """Welche der folgenden Aussagen beschreibt die Rolle der AdA-Timeline-Visualisierung im filmanalytischen Prozess am treffendsten?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Visualisierung ersetzt die qualitative Interpretation des filmischen Materials",
            "correct": False,
            "feedback": """× Die Visualisierung ersetzt nicht die qualitative Interpretation, sondern ergänzt sie. Sie dient nicht ausschließlich der Validierung vorgefasster Hypothesen, sondern kann auch neue Erkenntnisse generieren. Sie ist mehr als ein technisches Hilfsmittel und hat eigenständigen Erkenntniswert im Forschungsprozess."""
        },
        {
            "answer": "Die Visualisierung dient ausschließlich der empirischen Validierung vorgefasster Hypothesen",
            "correct": False,
            "feedback": """× Die Visualisierung ersetzt nicht die qualitative Interpretation, sondern ergänzt sie. Sie dient nicht ausschließlich der Validierung vorgefasster Hypothesen, sondern kann auch neue Erkenntnisse generieren. Sie ist mehr als ein technisches Hilfsmittel und hat eigenständigen Erkenntniswert im Forschungsprozess."""
        },
        {
            "answer": "Die Visualisierung ist ein Medium des Denkens, das sowohl zur Exploration als auch zur Präsentation von Erkenntnissen dient",
            "correct": True,
            "feedback": """✓ Genau! Die AdA-Timeline-Visualisierung ist als Medium des Denkens zu verstehen, das sowohl der Exploration neuer Muster und Zusammenhänge als auch der Präsentation und Kommunikation von Erkenntnissen dient. Sie ist ein wesentlicher Bestandteil eines abduktiven Forschungsprozesses."""
        },
        {
            "answer": "Die Visualisierung ist ein rein technisches Hilfsmittel ohne eigenständigen Erkenntniswert",
            "correct": False,
            "feedback": """× Die Visualisierung ersetzt nicht die qualitative Interpretation, sondern ergänzt sie. Sie dient nicht ausschließlich der Validierung vorgefasster Hypothesen, sondern kann auch neue Erkenntnisse generieren. Sie ist mehr als ein technisches Hilfsmittel und hat eigenständigen Erkenntniswert im Forschungsprozess."""
        }
    ]
}]

display_quiz(multiple_choice10, colors=colors.jupyterquiz)
```

### Frage 11

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")
from assessment import DragDropQuiz

quiz = DragDropQuiz()

quiz.create_matching_quiz(
    title="Ordnen Sie die folgenden Visualisierungsformen der AdA-Timeline dem richtigen Anwendungsfall zu:",
    descriptions=[
        "Visualisierung kategorischer Werte wie Einstellungsgrößen oder Kamerabewegungstypen",
        "Darstellung des Schnittrhythmus und der Einstellungsdauern",
        "Visualisierung der Farbgestaltung und Farbwechsel im Film",
        "Darstellung numerischer Werte wie Lautstärke oder Bewegungsintensität"
    ],
    options=["Balkendiagramm (rect)", "Säulendiagramm (hist)", "Farbwerte (colorfield:parsed)", "Wellenform (wave)"],
    correct_mapping={
        "Visualisierung kategorischer Werte wie Einstellungsgrößen oder Kamerabewegungstypen": "Balkendiagramm (rect)",
        "Darstellung des Schnittrhythmus und der Einstellungsdauern": "Säulendiagramm (hist)",
        "Visualisierung der Farbgestaltung und Farbwechsel im Film": "Farbwerte (colorfield:parsed)",
        "Darstellung numerischer Werte wie Lautstärke oder Bewegungsintensität": "Wellenform (wave)"
    }
)
```

### Frage 12
Reflektieren Sie über die Grenzen und Potenziale der AdA-Timeline für die filmwissenschaftliche Analyse. Wo sehen Sie Stärken und wo Einschränkungen dieses Visualisierungsansatzes?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_E-12')
```

````{admonition} Lösung
:class: solution, dropdown

**Mögliche Aspekte für die Reflexion:**

- Stärken: Visualisierung synchroner Muster, Exploration temporaler Dynamiken, Vermittlung zwischen quantitativen Daten und qualitativer Interpretation
- Grenzen: Abhängigkeit von der Qualität der zugrunde liegenden Annotationen, begrenzte Darstellbarkeit komplexer interpretativer Nuancen, technische Einschränkungen der Visualisierung
- Potenziale: Weiterentwicklung für kollaborative Forschung, Integration zusätzlicher analytischer Funktionen, Kombination mit anderen Analysemethoden
- Methodologische Reflexion: Verhältnis zwischen Quantifizierung und Interpretation, Rolle der Visualisierung im hermeneutischen Prozess

````

