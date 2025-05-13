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
from quadriga_config import colors

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
from quadriga_config import colors


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
sys.path.append("../quadriga_config")  # Adjust path as needed
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
1.	AdA-Template-Annotationspaket in Advene öffnen
2.	W3-Symbol in der Icon-Leiste klicken und Timeline-Variante auswählen
3.	Im Browser öffnet sich die Timeline mit Standardkonfiguration
4.	Änderungen mit "OK" bestätigen, um die Timeline neu zu laden
5.	Syntaxelemente im Edit-Fenster anpassen
6.	"Edit"-Button klicken, um das Edit-Fenster zu öffnen



```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice4 = [{
    "question": """Ordnen Sie die folgenden Funktionen den richtigen Phasen im Arbeitsprozess mit der AdA-Filmontologie zu""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "1 -> 2 -> 3 -> 4 -> 5 -> 6",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "1 -> 2 -> 3 -> 5 -> 6 -> 4",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "1 -> 3 -> 2 -> 5 -> 6 -> 4",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "1 -> 2 -> 3 -> 6 -> 5 -> 4",
            "correct": True,
            "feedback": """Ausgezeichnet! Sie verstehen den korrekten Workflow für die Öffnung und Konfiguration der AdA-Timeline. Diese systematische Vorgehensweise ist wichtig für die effiziente Arbeit mit dem Tool."""
        }
    ]
}]

display_quiz(multiple_choice4, colors=colors.jupyterquiz)
```

### Frage 5

A. Annotationen werden in Zeilen mit eigenen Farben als Balken angezeigt  
B. Geeignet für Annotationstypen ohne Überlappungen von Werten   
C. Breite und Höhe der Blöcke entsprechen der Dauer einer Annotation  
D. Darstellung für numerische Werte mit Ausschlägen in beide Richtungen


```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice5 = [{
    "question": """Ordnen Sie die folgenden Darstellungsformen der AdA-Timeline ihrer korrekten Beschreibung zu""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Balkendiagramm (rect), B. Einzeilige Darstellung (single_line), C. Wellenform (wave) , D. Säulenansicht (hist)",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Wellenform (wave), B. Balkendiagramm (rect), C. Einzeilige Darstellung (single_line), D. Säulenansicht (hist)",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Wellenform (wave), B. Einzeilige Darstellung (single_line), C. Balkendiagramm (rect), D. Säulenansicht (hist) ",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Balkendiagramm (rect), B. Einzeilige Darstellung (single_line), C. Säulenansicht (hist), D. Wellenform (wave)",
            "correct": True,
            "feedback": """Sehr gut! Sie verstehen die verschiedenen Darstellungsformen der AdA-Timeline und können sie korrekt ihren Beschreibungen zuordnen. Dieses Wissen ist entscheidend für die Auswahl der geeigneten Visualisierung für verschiedene Annotationstypen."""
        }
    ]
}]

display_quiz(multiple_choice5, colors=colors.jupyterquiz)
```

### Frage 6

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

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

### Frage 7

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

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

### Frage 8
Erläutern Sie, wie die AdA-Timeline zur Exploration und Interpretation audiovisueller Inszenierungsmuster genutzt werden kann. Beziehen Sie sich dabei auf konkrete Beispiele wie Schnittrhythmus, Bewegungsdynamik oder Farbgestaltung.


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_E-9')
```

````{admonition} Lösung
:class: solution, dropdown

**Hilfestellung zur Antwort:**

Gehen Sie näher auf den Zusammenhang zwischen der Visualisierung und der Identifikation von Mustern ein – was wird sichtbar?

Wie kann die Synchronizität verschiedener Parameter analytisch greifbar gemacht werden? Reflektieren sie über die Rolle der Visualisierung im Interpretationsprozess und berücksichtigen Sie sowohl quantitative als auch qualitative Aspekte der Dateninterpretation.

````

### Frage 9

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

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

### Frage 10

A. Visualisierung kategorischer Werte wie Einstellungsgrößen oder Kamerabewegungstypen  
B. Darstellung des Schnittrhythmus und der Einstellungsdauern  
C. Visualisierung der Farbgestaltung und Farbwechsel im Film  
D. Darstellung numerischer Werte wie Lautstärke oder Bewegungsintensität  

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

multiple_choice11 = [{
    "question": """Ordnen Sie die folgenden Visualisierungsformen der AdA-Timeline richtigen Anwendungsfall zu""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Balkendiagramm (rect), B. Säulendiagramm (hist), C. Wellenform (wave) , D. Farbwerte (colorfield:parsed)",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Wellenform (wave), B. Balkendiagramm (rect), C. Farbwerte (colorfield:parsed), D. Säulenansicht (hist)",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Wellenform (wave), B. Farbwerte (colorfield:parsed), C. Balkendiagramm (rect), D. Säulenansicht (hist) ",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Balkendiagramm (rect), B. Säulendiagramm (hist), C. Farbwerte (colorfield:parsed), D. Wellenform (wave)",
            "correct": True,
            "feedback": """Ausgezeichnet! Sie verstehen, welche Visualisierungsformen für welche Arten von Annotationsdaten am besten geeignet sind. Diese Zuordnung ist wichtig für die Auswahl der optimalen Darstellung verschiedener filmischer Parameter."""
        }
    ]
}]

display_quiz(multiple_choice11, colors=colors.jupyterquiz)
```
### Frage 11

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

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

### Frage 12

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

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

### Frage 13

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga_config import colors

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

### Frage 14
Reflektieren Sie über die Grenzen und Potenziale der AdA-Timeline für die filmwissenschaftliche Analyse. Wo sehen Sie Stärken und wo Einschränkungen dieses Visualisierungsansatzes?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga_config")  # Adjust path as needed
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

