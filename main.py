import random
jmeno = "Radim" #Proměnná se stringem (mým jménem). 1.
prijmeni = "Kočko" #Proměnná se stringem (mým příjmením). 2.
print(jmeno + prijmeni) #Vypíše proměnné do konzole. 3.
vek = input("Kolik vám je let? ") #Zeptá se uživatele na věk, který musí napsat do konzole. 4.
if vek.isdigit():
    print("Okay.")
else:
    print("Zadej svůj věk číslem!") #Vypíše program pokud uživatel napíše do konzole jinou hodnotu než celočíselnou.
delka_jmena = len(jmeno) #Příkaz (len) se používá pro zjíštění počtu písmen ve stringu. 5.
delka_prijmeni = len(prijmeni)
print(delka_jmena)
print(delka_prijmeni)            
a = 6 #Proměnná s přidanou hodnotou 6. 6.
for i in range(5): #Cyklus, při kterém se ke každému cyklu sečte s proměnnou číslo. 7.
    a += 3
    print("Výsledek po ukončení cyklu:", + a) #Vypíšou se finální výsledky pro každy cyklus. 8.
vek2 = input("Zadej věk: ") #Vyžaduje po uživateli zadat věk. 9.
if vek2.isdigit():
    print("Děkuji")  #Takto odpoví, pokud zadá celočíselnou hodnotu. 
else:
    print("Zadej jen celočíselnou hodnotu!") #Takto pokud zadá do konzole cokoliv jiného.
random_cislo = random.randint(1 , 10) #Přidává k proměnné náhodné číslo.
print("Vaše náhodně vygenerované číslo je: ", + random_cislo) #Příkaz pro vypsání náhodného čísla do konzole.   
    
