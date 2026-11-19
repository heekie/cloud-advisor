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


## Planlagt tilgangsstyring i Cloud Advisor

### Formål

Cloud Advisor skal ha en tilgangsstyring som sikrer at brukere kun får tilgang til kundedata og funksjoner de har tillatelse til å benytte.

Løsningen skal bygge på rollebasert tilgangskontroll (RBAC) kombinert med kundetilhørighet. Dette innebærer at en bruker både må ha riktig tilgang til kunden og nødvendige rettigheter for handlingen.

Målet er å beskytte kundedata mot uautorisert innsyn og endring.

### 1. Roller og rettigheter

Det planlegges to hovedroller:

- **Leser:** Kan lese kundecaser, men ikke endre informasjon.
- **Redaktør:** Kan både lese og redigere kundecaser.

Rettighetene skal være knyttet til den enkelte kunden. En bruker med tilgang til én kunde skal ikke automatisk få tilgang til andre kunder.

### 2. Eksempel på tilgangsmatrise

Følgende tilgangsregler er definert for to eksempelbedrifter.

**Nordkurs**

| Bruker | Lese | Redigere |
|---|---|---|
| Ingrid | Tillatt | Ikke tillatt |
| Bo | Tillatt | Tillatt |
| Eva | Ikke tillatt | Ikke tillatt |

**Fjordhandel**

| Bruker | Lese | Redigere |
|---|---|---|
| Eva | Tillatt | Ikke tillatt |
| Ingrid | Ikke tillatt | Ikke tillatt |
| Bo | Ikke tillatt | Ikke tillatt |

### 3. Planlagt tilgangskontroll

Når en bruker forsøker å lese eller endre et kundecase, skal systemet gjennomføre følgende kontroller:

1. Bekrefte at brukeren er autentisert.
2. Kontrollere at brukeren har tilgang til den aktuelle kunden.
3. Kontrollere at brukerens rolle tillater handlingen.
4. Godkjenne handlingen dersom begge tilgangskravene er oppfylt.
5. Avvise handlingen dersom minst ett krav ikke er oppfylt.

Systemet skal følge prinsippet om minste privilegium. Brukere skal kun få de rettighetene de trenger for å utføre sine oppgaver.

### 4. Eksempler på tilgangskontroll

**Scenario A: Ingrid forsøker å redigere Nordkurs**

- Ingrid er innlogget.
- Ingrid har lesetilgang til Nordkurs.
- Ingrid har ikke redigeringsrettigheter.
- Systemet avviser handlingen.

**Resultat: AVVIST**

**Scenario B: Ingrid forsøker å lese Nordkurs**

- Ingrid er innlogget.
- Ingrid har tilgang til Nordkurs.
- Rollen tillater lesing.
- Systemet gir tilgang til kundecaset.

**Resultat: TILLATT**

**Scenario C: Ingrid forsøker å redigere Fjordhandel**

- Ingrid er innlogget.
- Ingrid har ikke tilgang til Fjordhandel.
- Systemet avviser handlingen.

**Resultat: AVVIST**

### 5. Logging og sporbarhet

Cloud Advisor skal etter planen registrere tilgangsforsøk slik at hendelser kan undersøkes i etterkant.

Loggen skal inneholde:

- Tidspunkt for handlingen
- Bruker
- Handling (lese eller redigere)
- Aktuell kunde
- Resultat (tillatt eller avvist)
- Begrunnelse ved avvisning

Eksempel på planlagt loggformat:

```text
21:01 | Ingrid | Redigere | Fjordhandel | AVVIST | Mangler tilgang
21:01 | Ingrid | Lese | Nordkurs | TILLATT | Lesetilgang bekreftet
```

### 6. Videre utvikling

Følgende funksjonalitet planlegges implementert i Cloud Advisor:

- Brukerautentisering og sikker innlogging.
- Rollebasert tilgangskontroll for lesere og redaktører.
- Kontroll av kundetilhørighet for hver forespørsel.
- Logging av godkjente og avviste handlinger.
- Tester som bekrefter at brukere ikke får tilgang til andre kunders data.

### Status

**Planleggingsfase – ikke implementert.**

Tilgangsmatrisen og flytskjemaene er utarbeidet som en del av læringsarbeidet innen identitets- og tilgangsstyring (IAM) og cybersikkerhet.

Neste steg er å implementere og teste tilgangskontrollen i Python før funksjonaliteten eventuelt kobles til Cloud Advisors øvrige tjenester.

## Videre arbeid

- Kontrollere ugyldige inndata, som negative verdier.
- Samle beregningene i funksjoner.
- Automatisere testene.
- Videreutvikle prosjektstrukturen etter hvert som funksjonaliteten øker.
