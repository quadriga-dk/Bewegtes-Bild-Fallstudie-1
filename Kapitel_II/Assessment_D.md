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

**Geschätzte Zeit**: 30-45 Min.

Viel Erfolg!
````
## Sektion I: Verständnis der Filmontologie und Grundfunktionen von Advene

### Frage 1

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors


multiple_choice1 = [{
    "question": """Was ist der Hauptunterschied zwischen der Arbeit mit der AdA-Filmontologie und den im vorherigen Kapitel beschriebenen Freitextannotationen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Bei der AdA-Filmontologie können keine eigenen Annotationen erstellt werden",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie schränkt die Erstellung eigener Annotationen nicht ein, sondern bietet ein strukturiertes Vokabular. Sie ist nicht auf Filmwissenschaftler beschränkt und erlaubt durchaus individuelle Anpassungen und Erweiterungen."""
        },
        {
            "answer": "Die AdA-Filmontologie arbeitet mit einem standardisierten Vokabular in einer festgelegten hierarchischen Struktur",
            "correct": True,
            "feedback": """✓ Genau! Der zentrale Unterschied besteht in der Nutzung eines standardisierten Vokabulars in einer hierarchischen Struktur (Ebenen, Typen, Werte), während Freitextannotationen keine feste Terminologie vorgeben."""
        },
        {
            "answer": "Die AdA-Filmontologie kann nur von Filmwissenschaftlern genutzt werden",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie schränkt die Erstellung eigener Annotationen nicht ein, sondern bietet ein strukturiertes Vokabular. Sie ist nicht auf Filmwissenschaftler beschränkt und erlaubt durchaus individuelle Anpassungen und Erweiterungen."""
        },
        {
            "answer": "Die AdA-Filmontologie erlaubt keine individuellen Anpassungen",
            "correct": False,
            "feedback": """× Die AdA-Filmontologie schränkt die Erstellung eigener Annotationen nicht ein, sondern bietet ein strukturiertes Vokabular. Sie ist nicht auf Filmwissenschaftler beschränkt und erlaubt durchaus individuelle Anpassungen und Erweiterungen."""
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
    "question": """Welche Vorteile bietet die Arbeit mit der AdA-Filmontologie? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Vergleichbarkeit der Daten durch standardisiertes Vokabular",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Aspekte sind tatsächlich Vorteile der Arbeit mit der AdA-Filmontologie gegenüber reinen Freitextannotationen."""
        },
        {
            "answer": "Zeiteffizientere Annotationsarbeit durch Quick-Fill-Optionen",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Aspekte sind tatsächlich Vorteile der Arbeit mit der AdA-Filmontologie gegenüber reinen Freitextannotationen."""
        },
        {
            "answer": "Maschinenlesbarkeit und Bereitstellung als Linked Open Data (LOD)",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Aspekte sind tatsächlich Vorteile der Arbeit mit der AdA-Filmontologie gegenüber reinen Freitextannotationen."""
        },
        {
            "answer": "Einsatz (semi-)automatischer Erkenneralgorithmen",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Aspekte sind tatsächlich Vorteile der Arbeit mit der AdA-Filmontologie gegenüber reinen Freitextannotationen."""
        },
        {
            "answer": "Völlige Freiheit bei der Benennung analytischer Beobachtungen",
            "correct": False,
            "feedback": """× Die Arbeit mit der AdA-Filmontologie bietet zwar viele Vorteile, schränkt aber bei einigen Typen die freie Benennung filmischer Phänomene zugunsten eines standardisierten Vokabulars ein. Dies ist ein bewusster Kompromiss, um Vergleichbarkeit und Maschinenlesbarkeit zu gewährleisten."""
        }
    ]
}]

display_quiz(multiple_choice2, colors=colors.jupyterquiz)
```

### Frage 3
A. Automatische Schnitterkennung  
B. Überprüfung und Korrektur der Schnittgrenzen  
C. Import von Untertiteln  
D. Prüfung von Annotationswerten auf Fehler 



```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice3 = [{
    "question": """Ordnen Sie die folgenden Funktionen den richtigen Phasen im Arbeitsprozess mit der AdA-Filmontologie zu""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "A. Process Video , B. Checker Function, C. Import File , D. Shot Validation",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Checker Function, B. Process Video, C. Import File, D. Shot Validation",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Checker Function, B. Process Video, C. Import File , D. Shot Validation ",
            "correct": False,
            "feedback": """× Nicht korrekt! """
        },
        {
            "answer": "A. Process Video, B. Shot Validation, C. Import File, D. Checker Function",
            "correct": True,
            "feedback": """Ausgezeichnet! Sie verstehen die verschiedenen Phasen des Arbeitsprozesses mit der AdA-Filmontologie und können die entsprechenden Funktionen in Advene korrekt zuordnen."""
        }
    ]
}]

display_quiz(multiple_choice3, colors=colors.jupyterquiz)
```

## Sektion II: Arbeiten mit dem AdA-Template in Advene

### Frage 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice4 = [{
    "question": """Welche Funktion hat die AdA Corpus Analysis View im Kontext der Arbeit mit dem AdA-Template?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie analysiert automatisch den gesamten Filmkorpus",
            "correct": False,
            "feedback": """× Die AdA Corpus Analysis View ist keine automatische Analysefunktion, sondern eine vordefinierte Auswahl von Annotationstypen als Grundlage für die Annotation. Sie generiert keine Annotationen selbstständig und dient nicht der Fehleranzeige."""
        },
        {
            "answer": "Sie generiert selbstständig alle notwendigen Annotationen",
            "correct": False,
            "feedback": """× Die AdA Corpus Analysis View ist keine automatische Analysefunktion, sondern eine vordefinierte Auswahl von Annotationstypen als Grundlage für die Annotation. Sie generiert keine Annotationen selbstständig und dient nicht der Fehleranzeige."""
        },
        {
            "answer": "Sie stellt eine Basisauswahl an Annotationstypen für die Analyse bereit",
            "correct": True,
            "feedback": """✓ Korrekt! Die AdA Corpus Analysis View bietet eine Basisauswahl an Annotationstypen, die als Ausgangspunkt für die vergleichende Analyse dient und bei Bedarf erweitert werden kann."""
        },
        {
            "answer": "Sie zeigt fehlerhafte Annotationen an",
            "correct": False,
            "feedback": """× Die AdA Corpus Analysis View ist keine automatische Analysefunktion, sondern eine vordefinierte Auswahl von Annotationstypen als Grundlage für die Annotation. Sie generiert keine Annotationen selbstständig und dient nicht der Fehleranzeige."""
        }
    ]
}]

display_quiz(multiple_choice4, colors=colors.jupyterquiz)
```


### Frage 5

Beschreiben Sie den Prozess der automatischen Schnitterkennung und der anschließenden manuellen Überprüfung mit der Shot Validation View in Advene.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_D-5')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiel für korrekte Antwort:**

Die automatische Schnitterkennung wird über 'File > Process Video' mit dem Filter 'Scene change detection' gestartet. Dadurch werden Einstellungswechsel automatisch erkannt und als Annotationen im Typ 'Scene change' gespeichert. Anschließend werden diese mit der Shot Validation View überprüft, indem jeder erkannte Schnitt manuell validiert wird. Bei falsch erkannten Schnitten kann 'Merge' genutzt werden, um sie zu entfernen; fehlende Schnitte können durch Drücken von [CTRL] und Klicken auf den ersten Frame der neuen Einstellung hinzugefügt werden. Nach der Korrektur müssen die Einstellungen in der Regel renummeriert und in die Annotationstypen 'Shot' und 'Shot Duration' kopiert werden.

**Feedback:** 
Der Prozess der Schnitterkennung und -validierung ist ein wesentlicher erster Schritt bei der Arbeit mit dem AdA-Template, da die Einstellungsgrenzen die Grundlage für viele weitere Annotationstypen bilden.

````

### Frage 6

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice6 = [{
    "question": """Welche der folgenden automatischen Erkennungs- und Importfunktionen bietet Advene? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Schnitterkennung (Scene change detection)",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Funktionen werden tatsächlich von Advene unterstützt und können die Annotationsarbeit erheblich vereinfachen."""
        },
        {
            "answer": "Lautstärkeverlauf (Sound envelope)",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Funktionen werden tatsächlich von Advene unterstützt und können die Annotationsarbeit erheblich vereinfachen."""
        },
        {
            "answer": "Bewegungsdynamik (Motion Dynamics Extractor)",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Funktionen werden tatsächlich von Advene unterstützt und können die Annotationsarbeit erheblich vereinfachen."""
        },
        {
            "answer": "Import von Untertiteln",
            "correct": True,
            "feedback": """✓ Sehr gut! All diese Funktionen werden tatsächlich von Advene unterstützt und können die Annotationsarbeit erheblich vereinfachen."""
        },
        {
            "answer": "Automatische Erkennung von Einstellungsgrößen",
            "correct": False,
            "feedback": """× Die automatische Erkennung von Einstellungsgrößen wird derzeit von Advene nicht unterstützt. Diese Parameter müssen manuell annotiert werden, wobei die Quick-Fill- und Quick-Edit-Funktionen den Prozess beschleunigen können."""
        }
    ]
}]

display_quiz(multiple_choice6, colors=colors.jupyterquiz)
```

### Frage 7
Sie haben die automatische Schnitterkennung durchgeführt und möchten nun mehrere Annotationstypen (wie Field Size, Camera Angle) nach dem Einstellungsprinzip annotieren. Beschreiben Sie, wie Sie vorgehen würden.

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_D-7')
```

````{admonition} Lösung
:class: solution, dropdown
**Beispiel für korrekte Antwort:**

Nachdem die Schnitterkennung validiert und im Annotationstyp 'Shot' gespeichert wurde, kopiere ich diese Segmentierung in die anderen Typen, die nach dem Einstellungsprinzip annotiert werden sollen. Dazu ziehe ich den 'Shot'-Annotationstyp per Drag-and-Drop auf die Zielspur und wähle 'Duplicate all annotations'. Anschließend nutze ich die 'Search/replace content'-Funktion, um den Inhalt aller kopierten Annotationen zu löschen (beide Felder leer lassen). Dann verwende ich Quick Fill mit den vordefinierten Werten der AdA-Filmontologie oder Quick Edit für die Annotation. Nach jeder Annotation kann ich mit der [Tab]-Taste zur nächsten springen. Um die Vollständigkeit und Korrektheit zu überprüfen, nutze ich abschließend die Checker-Funktion.

````


### Frage 8

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice8 = [{
    "question": """Was bewirkt die Quick Fill-Funktion bei der Annotation mit dem AdA-Template?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sie füllt automatisch alle Annotationen mit dem gleichen Wert",
            "correct": False,
            "feedback": """× Die Quick Fill-Funktion füllt nicht automatisch alle Annotationen mit dem gleichen Wert, erkennt keine Werte automatisch und nutzt auch kein maschinelles Lernen für Vorschläge. Sie ist ein manuelles, aber sehr effizientes Eingabewerkzeug für vordefinierte Werte."""
        },
        {
            "answer": "Sie erkennt automatisch den passenden Wert für jede Annotation",
            "correct": False,
            "feedback": """× Die Quick Fill-Funktion füllt nicht automatisch alle Annotationen mit dem gleichen Wert, erkennt keine Werte automatisch und nutzt auch kein maschinelles Lernen für Vorschläge. Sie ist ein manuelles, aber sehr effizientes Eingabewerkzeug für vordefinierte Werte."""
        },
        {
            "answer": "Sie ermöglicht die schnelle Eingabe vordefinierter Werte über Zahlentasten",
            "correct": True,
            "feedback": """✓ Korrekt! Die Quick Fill-Funktion ermöglicht es, vordefinierte Werte schnell über die Zahlentasten einzugeben, wobei jede Ziffer einem bestimmten Wert entspricht. Dies beschleunigt den Annotationsprozess erheblich."""
        },
        {
            "answer": "Sie generiert Vorschläge basierend auf maschinellem Lernen",
            "correct": False,
            "feedback": """× Die Quick Fill-Funktion füllt nicht automatisch alle Annotationen mit dem gleichen Wert, erkennt keine Werte automatisch und nutzt auch kein maschinelles Lernen für Vorschläge. Sie ist ein manuelles, aber sehr effizientes Eingabewerkzeug für vordefinierte Werte."""
        }
    ]
}]

display_quiz(multiple_choice8, colors=colors.jupyterquiz)
```


### Frage 9

A. Beschreibt zwei kontrastierende Werte innerhalb einer Annotation  
B. Annotationen mit einem oder mehreren Werten aus der Ontologie  
C. Beschreibt eine kontinuierliche Entwicklung zwischen zwei Werten  
D. Annotationen ohne spezifische Ontologie-Referenz


```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice9 = [{
    "question": """Ordnen Sie die folgenden Syntaxelemente oder Annotationsarten der AdA-Filmontologie ihrer korrekten Beschreibung zu""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": """A. [VS], B. PredefinedValuesAnnotationType, C. [TO], D. FreeTextAnnotationType""",
            "correct": True,
            "feedback": "Ausgezeichnet! Sie verstehen die verschiedenen Syntaxelemente und Annotationsarten der AdA-Filmontologie und können sie korrekt beschreiben."
        },
        {
            "answer": """A. [VS], B. FreeTextAnnotationType, C. PredefinedValuesAnnotationType, D. [TO]""",
            "correct": False,
            "feedback": "x Nicht korrekt. "
        },
        {
            "answer": """A. FreeTextAnnotationType, B. PredefinedValuesAnnotationType, C. [VS], D. [TO]""",
            "correct": False,
            "feedback": "x Nicht korrekt. "
        },
        {
            "answer": """A. [TO], B. FreeTextAnnotationType, C. [VS], D. PredefinedValuesAnnotationType""",
            "correct": False,
            "feedback": "x Nicht korrekt. "
        }
    ]
}]

display_quiz(multiple_choice9, colors=colors.jupyterquiz)
```

### Frage 10

```{code-cell} ipython3
:tags: [remove-input]

from jupyterquiz import display_quiz
import sys
sys.path.append("..")
from quadriga import colors

multiple_choice10 = [{
    "question": """Welche der folgenden Fehlertypen kann die Checker-Funktion in Advene identifizieren? (Wählen Sie alle zutreffenden Optionen)""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Sich überlappende Annotationen (Overlapping)",
            "correct": True,
            "feedback": """✓ Sehr gut! Die Checker-Funktion kann tatsächlich all diese Fehlertypen identifizieren, was bei der Qualitätssicherung der Annotationen hilft."""
        },
        {
            "answer": "Undefinierte Keywords, die von der Ontologie abweichen (Completions)",
            "correct": True,
            "feedback": """✓ Sehr gut! Die Checker-Funktion kann tatsächlich all diese Fehlertypen identifizieren, was bei der Qualitätssicherung der Annotationen hilft."""
        },
        {
            "answer": "Annotationen ohne Inhalt (Empty Content)",
            "correct": True,
            "feedback": """✓ Sehr gut! Die Checker-Funktion kann tatsächlich all diese Fehlertypen identifizieren, was bei der Qualitätssicherung der Annotationen hilft."""
        },
        {
            "answer": "Annotationen ohne Dauer (Duration)",
            "correct": True,
            "feedback": """✓ Sehr gut! Die Checker-Funktion kann tatsächlich all diese Fehlertypen identifizieren, was bei der Qualitätssicherung der Annotationen hilft."""
        },
        {
            "answer": "Semantisch falsche Annotationen",
            "correct": False,
            "feedback": """× Die Checker-Funktion kann technische Fehler wie Überlappungen oder fehlende Inhalte erkennen, aber keine semantischen Fehler beurteilen. Die inhaltliche Korrektheit der Annotationen muss durch menschliche Überprüfung sichergestellt werden."""
        }
    ]
}]

display_quiz(multiple_choice10, colors=colors.jupyterquiz)
```

### Frage 11

Sie finden in einem Annotationspaket folgende Fehler: Überlappende Annotationen im Typ 'Setting', zwei Einstellungen im Typ 'Shot', die gemerged wurden und fehlende Werte im Typ 'Field Size'. Beschreiben Sie, wie Sie diese Fehler beheben würden.


```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_D-11')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiel für korrekte Antwort:**

Für überlappende Annotationen im Typ 'Setting': Ich würde den Checker öffnen, zum Tab 'Overlapping' wechseln und die überlappenden Annotationen identifizieren. Dann würde ich die betroffenen Annotationen durch Bearbeitung ihrer Start- und Endzeiten oder durch Zusammenführen korrigieren.

Für die "verschmolzenen" Einstellungen: Ich würde die betreffende Annotation im Typ 'Shot' auswählen und mit der 'Split at current player position'-Funktion an der richtigen Stelle teilen. Danach würde ich die Shot-Nummern anpassen und dann die Änderung in alle anderen nach dem Einstellungsprinzip annotierten Typen übertragen.
Für fehlende Werte im Typ 'Field Size': Ich würde den Checker nutzen, um im Tab 'EmptyContent' die Annotationen ohne Inhalt zu identifizieren, und dann mit Quick Fill oder Quick Edit die fehlenden Werte ergänzen.

````

## Sektion III: Methodenreflexion

### Frage 12
Diskutieren Sie Grenzen und Herausforderungen der AdA-Filmontologie anhand konkreter Beispiele. Welche filmischen Aspekte sind schwierig zu erfassen und wie könnten diese Herausforderungen adressiert werden?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_D-12')
```

````{admonition} Lösung
:class: solution, dropdown

**Beispiel für mögliche Antworten:**

- Eine klare Bestimmung von Einstellungsgrößen ist nicht immer möglich, insbesondere bei 2D-Animationen, in denen es keine klaren physischen Referenzobjekte gibt, anhand derer das Größenverhältnis gemessen werden könnte
- Offscreen-Kompositionen können nicht immer abgedeckt werden 
- Frage nach diegetischen oder non-diegetischen Elementen kann nicht immer erfasst werden
- Leerstellen bei der Erfassung bestimmter gestalterischer Elemente wie Split-Screens oder visueller Muster
- Mögliche Lösungsansätze: Erweiterung der Ontologie um spezifische Annotationstypen, flexible Interpretationen vorhandener Typen, Kombination mit freien Textannotationen

````

### Frage 13

Basierend auf Ihrer Erfahrung mit der AdA-Filmontologie: Für welche Art von filmanalytischen Forschungsfragen eignet sich dieser Ansatz besonders gut, und bei welchen Fragestellungen könnten Grenzen auftreten?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")  # Adjust path as needed
from assessment import create_answer_box

create_answer_box('Assessment_D-13')
```

````{admonition} Hilfestellung zur Antwort
:class: solution, dropdown

Reflektieren Sie darüber, wie die AdA-Filmontologie die Analyse formaler, stilistischer und kompositorischer Elemente unterstützt. Überlegen Sie, welche Arten von Forschungsfragen gut durch die systematische Erfassung audiovisueller Muster und Rhythmen beantwortet werden können. Denken Sie auch darüber nach, wo die Grenzen liegen könnten, etwa bei narrativen oder inhaltsanalytischen Fragestellungen.

````