Variabel=8
Variabel=Variabel+2
print(Variabel)

Kunde="Nordlys AS"
Brukere=25
Lisens=150
Oppsett=900
Månedsbud = 2707.5

if Brukere <= 9:
  Rabatt= 0.00
elif Brukere <= 19:
  Rabatt = 0.05
elif Brukere > 19:
  Rabatt = 0.1

print("Rabatt:", (Rabatt * 100), "prosent.")

def Manedskost(Brukere, Lisens):
  Manedskost = Brukere * Lisens
  return(Manedskost)
print(Manedskost(Brukere, Lisens))
Månedskost = Manedskost(Brukere, Lisens)
def forstear_ur(Brukere, Lisens, Oppsett):
  """
    Beregner førsteårskostnaden uten rabatt.
    Parametere:
    Brukere, Lisens, Oppsett.
    Returnerer:
    (Brukere * Lisens) * 12 + Oppsett
    """
  forstear_ur = (Brukere * Lisens) * 12 + Oppsett
  return(forstear_ur)
Førsteår_ur = forstear_ur(Brukere, Lisens, Oppsett)

print("Førsteårskostnad uten rabatt er:" , førsteår_ur)

def forstear_r(Brukere, Lisens, Oppsett, Rabatt):
  """
    Beregner førsteårskostnaden med rabatt.
    Parametere:
    Brukere, Lisens, Oppsett, Rabatt.
    Returnerer:
    (Brukere * Lisens)*(1 - Rabatt) * 12 + Oppsett
    """
  forstear_r = ((Brukere * Lisens) * (1 - Rabatt)) * 12 + Oppsett
  return(forstear_r)
Førsteår = forstear_r(Brukere, Lisens, Oppsett, Rabatt)

print("Månedskostnad uten rabatt:", Månedskost)
Rabkost = Månedskost * Rabatt
print("Rabatt:", Rabkost)
Månedrabat = Månedskost - Rabkost
print("Månedskostnad med rabatt:", Månedrabat)
print("Førsteårskostnad:", Førsteår)
print(Kunde, "har", Brukere, "som hver skal ha en lisenskostnad hver måned på:", Lisens, "kroner.", "Dere får en rabatt på:", 100 * Rabatt, "prosent.", "Engangsoppsettet kommer på:", Oppsett, "og månedskostnaden vil bli", Månedrabat, "noe som tar den totale førsteårskostnaden til", Førsteår, "kroner.")
if Månedrabat <= Månedsbud:
  print(Kunde, "er innenfor budsjettet")
else: 
  print(Kunde, "er over sitt budsjett og kan ikke kjøpe til denne prisen")
