Variabel=8
Variabel=Variabel+2
print(Variabel)

Kunde="Nordlys AS"
Brukere=20
Lisens=150
Oppsett=900

if Brukere<=9:
  Rabatt=0.00
elif Brukere<=19:
  Rabatt=0.05
elif Brukere>19:
  Rabatt=0.1

print("Rabatt:", (Rabatt*100), "prosent.")

Månedskost=Brukere*Lisens
print("Månedskostnad uten rabatt:", Månedskost)
Rabkost=Månedskost*Rabatt
print("Rabatt:", Rabkost)
Månedrabat=Månedskost-Rabkost
print("Månedskostnad med rabatt:", Månedrabat)
Førsteår=(Månedrabat*12)+Oppsett
print("Førsteårskostnad:", Førsteår)
print(Kunde, "har", Brukere, "som hver skal ha en lisenskostnad hver måned på:", Lisens, "kroner.", "Dere får en rabatt på:", 100*Rabatt, "prosent.", "Engangsoppsettet kommer på:", Oppsett, "og månedskostnaden vil bli", Månedrabat, "noe som tar den totale førsteårskostnaden til", Førsteår, "kroner.")
