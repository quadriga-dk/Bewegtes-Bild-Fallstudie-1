---
lang: de-DE
author: "Schnaitter, Hannes"
---

# Arbeitsnotizen

## Startseite
- Die erste Grafik zum Start ist super.
  - [ ] Vielleicht ist es möglich, das Bildschirmfoto noch etwas hochauflösender zu machen?
- [x] externe Links nach dem neuen Standard markieren (ich erstelle dazu einen Issue und einen Pull-Request [#2](https://github.com/quadriga-dk/Bewegtes-Bild-Fallstudie-1/pull/2))
- Absatz 2 in intro.md
  > Von einer tabbelarischen Annotation bis zur Visualisierung … nachvollzogen werden können.
  Ist ziemlich kompliziert, wenn man von der Hälfte der Wörter die korrekte Bedeutung in der Filmwissenschaft nicht kennt.
  - [ ] Ist das für die Zielgruppe verständlich?
  - [ ] Wer ist die Zielgruppe genau?
  - [ ] Werden diese Begriffe später noch definiert?
  
  Das ist ein Satz, bei dem auch ein Glossar helfen könnte. 
- [ ] Auszeichnung der Lernziele mit der Admonition `lernziele`
- [ ] Überarbeitung des Abschnitts `## Aufbau der Übungen

## `Kapitel_I/Einführung_in_die_datengestützte_Filmanalyse.md`
- [x] Ist die Phrase "das zentrale Telos" in der Filmwissenschaft geläufig?
- [ ] Literatur-Referenzen fehlen noch
- Zeile 10:
  > Um einen gibt es Analysen der sentiment analysis und des topic modelling, […]
  - [ ] sollte es nicht "die Analysen" oder "die Analysemethoden" heißen?
- Zeile 11:
  > Keine dieser Herangehensweisen betrachtet aber die grundlegende medienästhetische Qualität von Videos als zeitlich sich entfaltenden, audiovisuellen Bewegtbildern in den Blick.
  - [ ] Grammatikfehler
- [x] Zeile 17-18: Ggf. könnte die Definition der Zielgruppe schon in der Einleitung stehen
- [x] ~~Zeile 19-24: Lernziele in einem eigenen Abschnitt in einem neuen Teil (`part`) "Präambel"? (siehe Text FS1)~~
- [ ] ~~Zeile 26-42: Vielleicht als eigenständiger Abschnitt (`chapter`)~~
- [x] Zeile 38-42: Der kursiv-gesetzte Satzanfang ist grafisch nicht so gut mit der Auflistung von Satzenden verbunden. Wäre hier eine `###` passender? Zudem haben die Satzenden keinen abschließenden Punkt.

## `Kapitel_I/weiterführende_Informationen.md`
- [x] Umbenennung der Markdown-Datei in `weiterführende_Informationen.md`?
- [ ] Zeile 13: Zitat ohne Referenz!


## `Kapitel_I/Empirische_Methoden.md`
- [ ] `assets/eMAEX-Dreistufenmodell.png` ggf. in besserer Auflösung? Oder selbst "nachbauen".
  - Es ist auch noch teilweise eine Überschrift zu erkennen, aber lesbar ist sie nicht. Braucht es die, oder sollte die weg? Kann die Überschrift als Bildunterschrift eingebunden werden?
- [ ] `assets/eMAEX-Pathosszene-Abfolge.png`: Die untere Hälfte des Screenshots ist nicht so gut lesbar wie die obere. Die obere Hälfte kann meiner Meinung nach so genutzt werden.
- [ ] Die Datei heißt `Empirische_Methoden.md`, jedoch wird nur eine Methode vorgestellt. Umbenennung in `eMAEX-Methode.md`?

## `Kapitel_I/Untersuchungsgegenstand.md`
- keine inhaltlichen Anmerkungen


# Vorgeschlagene Änderungen (in diesem branch bereits durchgeführt)
- [x] Umwandlung der admonition am Ende von `intro.md` in einen Hinweis.
  - [x] Titel des Hinweises ggf. anpassen
  - [x] Gibt es eine Dopplung zum Abschnitt "Aufbau der Übungen"?
- `Kapitel_I/Einführung_in_die_datengestützte_Filmanalyse.md`:14:
  - [ ] Korrektur der grammatischen Fälle
- `Kapitel_I/Einführung_in_die_datengestützte_Filmanalyse.md`:33-35:
  - [ ] Umwandlung der admonition in `hinweis`
- [ ] `Kapitel_I/weiterführende_Informationen.md` Admonitions umgestellt auf QUADRIGA Varianten
  - [x] Umwandlung in eine Liste von Tools -> wurde rückgängig gemacht
  - [ ] Umwandlung von `###` Glossare in seealso
  - [ ] ist `hinweis` passend für die `margin`-Notiz?
- [ ] `Kapitel_I/Untersuchungsgegenstand.md`
  - Anpassungen der admonitions
  - Anpassung des Youtube-Links

# Internes Review

## Zielgruppe
> _(3+ Sätze)_
> 
> - Was denke ich, wer die Zielgruppe ist?
> - Wenn die Zielgruppe klar definiert ist, stimmt das aus meiner Sicht mit Inhalten und Voraussetzung überein?


## Technik
> _(3+ Sätze)_
> 
> - Sind Anleitungen für Installation o.ä. vorhanden und korrekt?
> - Ist die technische Umsetzung der Fallstudie nachvollziehbar?
> - Stimmt der Code? Gibt es Bugs? Funktionieren die Anleitungen für die Nutzung von Tools? Sind mögliche/häufige Fehler abgefangen bzw. gibt es Hinweise auf die Fehlerbehebung?


## Struktur
> _(3+ Sätze)_
> 
> - Ist der Inhalt übersichtlich und nachvollziehbar strukturiert?
> - Auf welche Bestandteile der Fallstudie fokussiert sich die OER?
> - Sind die einzelnen Abschnitte der OER in ihrem Umfang gut gestaltet? Gibt es (ausreichende und gekennzeichnete) Möglichkeiten zur Unterbrechung der Bearbeitung der OER?


## Lernziele, Didaktik, Übungen und Assessment
> _(6+ Sätze)_
> 
> - Welche Kompetenzen soll ich idealerweise erwerben? Welche Methoden soll ich erlernen?
> - Sind die Lernziele klar verständlich? Ist die Abfolge der Lernziele logisch? Gibt es Lücken oder implizite Voraussetzungen für die Zielgruppe?
> - Ist die didaktische Umsetzung der Fallstudie und dem Datentyp angemessen?
> - Gibt es genug (oder zu viele) Übungen? Sind Übungsaufgaben klar formuliert? (Ist es möglich Übungen zu überspringen, ohne wichtige Informationen für nachfolgende Abschnitte zu übersehen?)
> - Sind die Übungen für die Überprüfung des eigenen Lernfortschritts angemessen (formatives Assessment)?


## Konkrete Probleme und Fehler
> (nach Bedarf)
> 
> Konkrete Fehler und Probleme können entweder hier als Liste oder im jeweiligen GitHub-Repositorium als Issue vermerkt werden.


## Fragen der Autor\*innen an die Reviewer\*innen
> _(6+ Sätze)_


## Gesamteindruck

### 1-3 Stärken der OER

### 1-3 Schwächen der OER

