# Cloud Advisor

Et læringsprosjekt i Python som beregner lisenskostnader, mengderabatt og førsteårskostnad, og kontrollerer om månedskostnaden er innenfor kundens budsjett.

Prosjektet bruker oppdiktede kundedata. Målet er å knytte programmering til praktiske spørsmål fra kunde- og salgsarbeid.

## Hva programmet gjør

Programmet beregner:

- Månedskostnad før rabatt.
- Rabattsats og rabattbeløp.
- Månedskostnad etter rabatt.
- Førsteårskostnad, inkludert engangsoppsett.
- Om månedskostnaden etter rabatt er innenfor budsjettet.

### Rabattregler

| Antall brukere | Rabatt |
|---|---:|
| Til og med 9 | 0 % |
| 10–19 | 5 % |
| Fra og med 20 | 10 % |

Rabatten gjelder hele månedskostnaden. Engangsoppsettet får ingen rabatt.

Førsteårskostnaden beregnes slik:

```text
(månedskostnad etter rabatt × 12) + engangsoppsett
```

En månedskostnad som er nøyaktig lik budsjettet, regnes som innenfor budsjettet.

## Slik kjører du programmet

Du trenger Python 3. Programmet bruker ingen eksterne pakker.

1. Last ned `cloud_advisor_rabatt.py`.
2. Åpne filen i en tekst- eller kodeeditor.
3. Endre eksempelverdiene øverst i filen:

```python
Kunde = "Nordlys AS"
Brukere = 20
Lisens = 150
Oppsett = 900
Månedsbud = 2700
```

`Lisens` er månedspris per bruker. `Oppsett` er engangskostnaden, og `Månedsbud` er kundens månedlige budsjett. Alle beløp oppgis i kroner.

4. Lagre filen.
5. Åpne en terminal i mappen der filen ligger, og kjør:

```bash
python cloud_advisor_rabatt.py
```

På Windows kan du alternativt bruke:

```bash
py cloud_advisor_rabatt.py
```

Med eksempelverdiene over skal programmet beregne 10 % rabatt, 2 700 kroner i månedskostnad etter rabatt og 33 300 kroner i førsteårskostnad. Kunden skal være innenfor budsjettet.

## Reproduserbare tester

Dette er manuelle tester. Endre inndata, lagre filen og kjør programmet på nytt for hver rad. Sammenlign utskriften med forventet resultat, og registrer faktisk resultat.

### 1. Rabattgrenser

Bruk disse faste verdiene:

```python
Kunde = "Testkunde AS"
Lisens = 150
Oppsett = 900
Månedsbud = 3000
```

Endre bare `Brukere` mellom kjøringene.

| Test | Brukere | Forventet rabatt | Forventet månedskostnad etter rabatt | Forventet førsteårskostnad | Faktisk resultat / bestått |
|---|---:|---:|---:|---:|---|
| R1 | 9 | 0 % | 1 350 kr | 17 100 kr | |
| R2 | 10 | 5 % | 1 425 kr | 18 000 kr | |
| R3 | 19 | 5 % | 2 707,50 kr | 33 390 kr | |
| R4 | 20 | 10 % | 2 700 kr | 33 300 kr | |

Alle fire tilfellene skal være innenfor budsjettet på 3 000 kroner.

Månedskostnaden blir litt lavere ved 20 enn ved 19 brukere. Det følger av at rabatten øker til 10 % på hele månedskostnaden.

### 2. Budsjettgrenser

Bruk disse faste verdiene:

```python
Kunde = "Testkunde AS"
Brukere = 20
Lisens = 150
Oppsett = 900
```

Månedskostnaden etter rabatt skal være 2 700 kroner. Endre bare `Månedsbud` mellom kjøringene.

| Test | Månedsbudsjett | Situasjon | Forventet budsjettstatus | Faktisk resultat / bestått |
|---|---:|---|---|---|
| B1 | 2 701 kr | Kostnaden er under budsjettet | Innenfor budsjettet | |
| B2 | 2 700 kr | Kostnaden er lik budsjettet | Innenfor budsjettet | |
| B3 | 2 699 kr | Kostnaden er over budsjettet | Over budsjettet | |

Rabatten, månedskostnaden og førsteårskostnaden skal være uendret mellom disse tre testene. Bare budsjettstatusen skal endres.

## Videre arbeid

- Kontrollere ugyldige inndata, som negative verdier.
- Samle beregningene i funksjoner.
- Automatisere testene.
- Videreutvikle prosjektstrukturen etter hvert som funksjonaliteten øker.
