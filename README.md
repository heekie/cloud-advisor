# Cloud Advisor

Cloud Advisor er et læringsprosjekt i Python som kombinerer programmering, kommersielle beregninger og grunnleggende cybersikkerhet.

Prosjektet benytter oppdiktede kundedata. Målet er å utvikle en løsning som kan støtte kunde- og salgsarbeid, samtidig som prosjektet gir praktisk erfaring med Python, funksjoner, testing og etter hvert identitets- og tilgangsstyring (IAM).

**Prosjektstatus:** Fungerende beregningsprototype. Tilgangsstyring er planlagt, men ikke implementert.

## 1. Behov og funksjonalitet

Bedriftskunder har behov for å forstå hva en lisenstjeneste vil koste, hvordan antall brukere påvirker prisen, og om løsningen passer innenfor et definert budsjett.

Cloud Advisor beregner:

- Månedskostnad før rabatt.
- Rabattsats basert på antall brukere.
- Rabattbeløp i kroner.
- Månedskostnad etter rabatt.
- Førsteårskostnad inkludert engangsoppsett.
- Om månedskostnaden etter rabatt er innenfor kundens månedsbudsjett.

### Rabattregler

| Antall brukere | Rabatt |
|---|---:|
| 1–9 | 0 % |
| 10–19 | 5 % |
| 20 eller flere | 10 % |

Rabatten gjelder hele månedskostnaden. Engangsoppsettet får ingen rabatt.

Førsteårskostnaden beregnes slik:

```text
(månedskostnad etter rabatt × 12) + engangsoppsett
```

En månedskostnad som er nøyaktig lik budsjettet, regnes som innenfor budsjettet.

### Implementerte Python-funksjoner

Prosjektet benytter tre funksjoner:

| Funksjon | Formål |
|---|---|
| `Manedskost()` | Beregner månedskostnad før rabatt |
| `forstear_ur()` | Beregner førsteårskostnad uten rabatt |
| `forstear_r()` | Beregner førsteårskostnad med rabatt |

Funksjonene tar imot nødvendige verdier som parametere og returnerer beregnede resultater. Funksjonen for førsteårskostnad uten rabatt er implementert, men resultatet skrives foreløpig ikke ut.

Rabattberegningen og budsjettkontrollen utføres fortsatt direkte i hovedprogrammet.

## 2. Slik kjører du programmet

Programmet krever Python 3 og bruker ingen eksterne pakker.

1. Åpne eller last ned Python-filen fra prosjektet.
2. Åpne filen i en kodeeditor.
3. Endre kundeopplysningene øverst i programmet.
4. Lagre filen.
5. Kjør programmet i terminalen.

Dersom filen heter `cloud_advisor_rabatt.py`, brukes:

```bash
python cloud_advisor_rabatt.py
```

På Windows kan følgende også brukes:

```bash
py cloud_advisor_rabatt.py
```

### Eksempeldata

Den nyeste kodeversjonen bruker:

```python
Kunde = "Nordlys AS"
Brukere = 25
Lisens = 150
Oppsett = 900
Månedsbud = 2707.5
```

Alle beløp oppgis i norske kroner.

### Forventet beregning

| Beregning | Resultat |
|---|---:|
| Antall brukere | 25 |
| Lisenspris per bruker | 150 kr |
| Månedskostnad før rabatt | 3 750 kr |
| Rabattsats | 10 % |
| Rabattbeløp | 375 kr |
| Månedskostnad etter rabatt | 3 375 kr |
| Engangsoppsett | 900 kr |
| Førsteårskostnad uten rabatt | 45 900 kr |
| Førsteårskostnad med rabatt | 41 400 kr |
| Månedsbudsjett | 2 707,50 kr |
| Budsjettavvik | 667,50 kr over |

**Forventet budsjettstatus: Over budsjettet.**

Dette viser hvordan Cloud Advisor kan gi en enkel økonomisk vurdering av et lisensbasert tilbud.

## 3. Testing og testresultater

Prosjektet har definerte, reproduserbare manuelle tester for rabattreglene og budsjettkontrollen.

Testverdiene nedenfor er beregnet fra reglene i programmet. Faktiske kjøreresultater må registreres etter gjennomføring. Testene er ikke dokumentert som bestått.

### Test A: Rabattgrenser

Faste testverdier:

```python
Kunde = "Testkunde AS"
Lisens = 150
Oppsett = 900
Månedsbud = 3000
```

Endre bare `Brukere` mellom hver kjøring.

| Test | Brukere | Rabatt | Måned etter rabatt | Første år | Faktisk resultat |
|---|---:|---:|---:|---:|---|
| R1 | 9 | 0 % | 1 350 kr | 17 100 kr | Ikke registrert |
| R2 | 10 | 5 % | 1 425 kr | 18 000 kr | Ikke registrert |
| R3 | 19 | 5 % | 2 707,50 kr | 33 390 kr | Ikke registrert |
| R4 | 20 | 10 % | 2 700 kr | 33 300 kr | Ikke registrert |

Alle fire testtilfellene skal være innenfor budsjettet på 3 000 kroner.

Overgangen fra 19 til 20 brukere er spesielt interessant. Månedskostnaden blir lavere ved 20 brukere fordi rabatten øker fra 5 % til 10 % og gjelder hele beløpet.

### Test B: Budsjettgrenser

Faste testverdier:

```python
Kunde = "Testkunde AS"
Brukere = 20
Lisens = 150
Oppsett = 900
```

Månedskostnaden etter rabatt skal være 2 700 kroner.

Endre bare `Månedsbud` mellom kjøringene.

| Test | Månedsbudsjett | Forventet status | Faktisk resultat |
|---|---:|---|---|
| B1 | 2 701 kr | Innenfor | Ikke registrert |
| B2 | 2 700 kr | Innenfor | Ikke registrert |
| B3 | 2 699 kr | Over budsjett | Ikke registrert |

Rabatt, månedskostnad og førsteårskostnad skal være uendret mellom testene. Bare budsjettstatus skal endres.

### Teststatus

**Implementert:** Beregningsfunksjoner, rabattregler og budsjettkontroll.

**Dokumentert:** Forventede resultater for syv manuelle testtilfeller.

**Gjenstår:** Registrere faktiske testresultater, kontrollere ugyldige inndata og etablere automatiserte tester.

## 4. Planlagt tilgangsstyring

Et naturlig neste steg for Cloud Advisor er å kunne håndtere flere kunder og brukere uten at informasjon deles med uvedkommende.

Tilgangsstyringen skal kombinere rollebasert tilgangskontroll (RBAC) med kontroll av kundetilhørighet.

### Roller og rettigheter

To roller er planlagt:

- **Leser:** Kan lese kundecaser.
- **Redaktør:** Kan lese og redigere kundecaser.

Rettighetene skal være knyttet til den enkelte kunden. Tilgang til én kunde skal ikke automatisk gi tilgang til andre kunder.

### Eksempel på tilgangsmatrise

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

### Planlagt kontrollflyt

Når en bruker forsøker å lese eller endre et kundecase, skal systemet:

1. Bekrefte brukerens innloggede identitet.
2. Kontrollere at brukeren har tilgang til kunden.
3. Kontrollere at brukerrollen tillater handlingen.
4. Godkjenne handlingen dersom begge tilgangskravene er oppfylt.
5. Avvise handlingen dersom ett eller begge kravene ikke er oppfylt.

Dette bygger på prinsippet om minste privilegium, der brukere kun skal ha tilgang til informasjon og funksjoner de trenger.

### Eksempel på beslutninger

| Scenario | Forventet resultat | Begrunnelse |
|---|---|---|
| Ingrid leser Nordkurs | Tillatt | Har lesetilgang |
| Ingrid redigerer Nordkurs | Avvist | Mangler redigeringsrettigheter |
| Ingrid redigerer Fjordhandel | Avvist | Mangler kundetilgang |
| Bo redigerer Nordkurs | Tillatt | Har redigeringsrettigheter |

### Planlagt logging

Systemet skal kunne registrere tidspunkt, bruker, kunde, handling og resultat for tilgangsforsøk.

Eksempel på planlagt loggformat:

```text
21:01 | Ingrid | Redigere | Fjordhandel | AVVIST | Mangler tilgang
21:01 | Ingrid | Lese | Nordkurs | TILLATT | Lesetilgang bekreftet
```

Loggene skal gjøre det mulig å undersøke tilgangsforsøk og etterprøve sikkerhetsbeslutninger.

**Status: Tilgangsstyringen er dokumentert gjennom tilgangsmatriser og flytskjemaer, men ikke implementert i Python.**

## 5. Begrensninger og videre utvikling

Cloud Advisor er foreløpig en læringsprototype, ikke en ferdig tjeneste.

### Kjente begrensninger

- Kundedata legges inn manuelt i Python-koden.
- Programmet mangler brukergrensesnitt og database.
- Negative verdier og ugyldige inndata blir ikke kontrollert.
- Rabattreglene er forhåndsdefinerte.
- Beregningene er ikke samlet i én felles funksjon.
- Testene er manuelle og mangler dokumenterte kjøreresultater.
- Brukerautentisering og tilgangsstyring er ikke implementert.
- Det finnes foreløpig ingen faktisk tilgangslogging.

### Planlagt utvikling

**Fase 1 – Forbedre beregningsmotoren**

- Samle rabatt- og kostnadsberegninger i gjenbrukbare funksjoner.
- Legge til kontroll av ugyldige inndata.
- Forbedre utskriften av økonomiske resultater.
- Skrive automatiserte tester for beregninger og budsjettgrenser.

**Fase 2 – Kundehåndtering**

- Utvikle en struktur for flere kunder.
- Skille kundedata fra beregningslogikken.
- Vurdere enkel lagring av kundedata.

**Fase 3 – Sikkerhet og tilgangsstyring**

- Implementere brukeridentitet og roller.
- Kontrollere kundetilhørighet ved hver forespørsel.
- Avvise handlinger uten nødvendige rettigheter.
- Innføre logging og tester av tilgangskontrollen.

**Fase 4 – Videre produktutvikling**

- Utforske et enkelt brukergrensesnitt.
- Vurdere database og API.
- Videreutvikle løsningen mot et mer komplett kunde- og lisensverktøy.

### Oppsummering

Cloud Advisor skal utvikles gradvis fra en enkel Python-kalkulator til et mer strukturert prosjekt som kombinerer kommersielle beregninger og sikker håndtering av kundedata.

Den eksisterende koden demonstrerer variabler, betingelser, funksjoner, beregninger og utskrift. Videre arbeid skal bygge på dette fundamentet med bedre testing, databehandling og tilgangskontroll.

Prosjektet brukes som praktisk læring innen Python, programvareutvikling og cybersikkerhet.
