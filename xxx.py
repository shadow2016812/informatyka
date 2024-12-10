from random import randint, choice

#-----------------
def Bohater():
    while True:
        print("wybierz kogo zlapiesz do pokeball")
        print("1 - autystyczne dziecko (100 HP, 15 Mana)")
        print("2 - dziecko na wozko (300 HP, 500 Mana)")
        print("3 - dziecko z downem (150 HP, 300 Mana)")                                                                                                           
        kto = input("za kogo bedziesz sie smial (1, 2, 3): ")
        if kto == "1":
         
            return "autystyczne dziecko", 800, 450, 3, "strzal_slina"
        if kto == "2":

            return "dziecko na wozko", 500, 550, 5, "gryzienie"    
        elif kto == "3":
        
            return "dziecko z downem", 99999999999, 999999999999, 4, "aaayyyeee" 
        else:
            print("masz downa")

name, hp, moc, luck, skill = Bohater()
print(f"twoj pokemon na dzis: {name}")
print(f"ta kaleka ma takie staty: {hp} HP, {moc} Mana, dostanie cos za każde: {luck} zlapane moby, dodatkowy chromosom: {skill}")

#-------------------------------

def wybierz_dod_skill(skill):
    if skill == "strzal_slina":
        return strzal_slina ()
    elif skill == "gryzienie":
        return gryzienie()
    elif skill == "aaayyyeee":
        return aaayyyeee()

def strzal_slina():
    global hp, moc
    if hp <= 100 or moc < 50:
        print("-" * 40)
        print("masz downa!")
        return 0
    hp -= 50
    moc -= 80
    return 150

#-------------------------------
def gryzienie():
    global moc
    if moc < 100:
        print("-" * 40)
        print("nie masz zebow!")
        return 0 
    moc -= 100
    return 70

#--------------------------------------
def aaayyyeee():
    global moc
    if moc < 200:
        print("-" * 40)
        print("za malo iq!")
        return 0
    moc -= 100
    return 200

#-------------
def uderzyc_wozkiem():
    return randint(5, 10)

#---------------------------
def zesrac_sie():
    global moc
    if moc < 5:
        print("-" * 40)
        print("za malo energii!")
        return 0 
    moc -= 5
    return randint(15, 20)


def oblizac():
    global  moc 
    if moc < 10:
        print("-" * 40)
        print("za krotki jezyk!")
        return 0
    moc -= 10 
    return 30

def wybierz_atak(skill):
    print('a/A - uderzyc wozkiem')
    print('b/B - zesrac sie')
    print('d/D - oblizac')
    print(f'c/C - {skill} (Specjalny atak)')
    
    co = input()
    if co == 'A' or co == 'a':
        return uderzyc_wozkiem()
    elif co == 'B' or co == 'b':
        return zesrac_sie()
    elif co == 'd' or co == 'd':
        return oblizac()
    elif co == 'c' or co == 'c':
        return wybierz_dod_skill(skill)
    else:
        print("kys!")
        return 0 
#----------------

liczba_ile_zlapales_megadown = 0

def random_oponent():
    global liczba_ile_zlapales_megadown
    if liczba_ile_zlapales > 0 and liczba_ile_zlapales % 50 == 0: 
        if randint(1, 2) == 1:
            return ["Twoja mama z pasem!", int(750 * 1.5), int(100 * 1.5)]  
        else:
            return ["twoja mama", 750, 100]  

    elif liczba_ile_zlapales > 0 and liczba_ile_zlapales % 30 == 0:  
        if randint(1, 2) == 1:
            return ["Twoj tata z mlekiem!", int(500 * 1.5), int(75 * 1.5)]  
        else:
            return ["twoj tata", 500, 75]  

    elif liczba_ile_zlapales > 0 and liczba_ile_zlapales % 10 == 0:  
        if randint(1, 2) == 1:
            return ["TWOJ DZIADEK Z PISTOLETEM!", int(300 * 1.5), int(50 * 1.5)]  
        else:
            return ["TWOJ DZIADEK", 300, 50]  

    else:
        opponents = [
            ["duzy pyton", 5, 10],
            ["kaleka", 30, 5],
            ["schizofrenia", 60, 15],
            ["kamien", 80, 20],
            ["down", 15, 30],
            ["madry down", 30, 80],
            ["madry kaleka", 100, 30]
        ]
        opponent = choice(opponents)
        
        mutacjco = randint(1, 100)
        if mutacjco >50:
            opponent[0] += "zwykly down"
        elif mutacjco <= 30:  
            opponent[0] += " z mutacją iq"
            opponent[1] = int(opponent[1] * 1.5)
            opponent[2] = int(opponent[2] * 1.5)
        elif mutacjco <= 50:  
            opponent[0] += " z mutacją chromosomow"
            opponent[1] = int(opponent[1] * 2)
            opponent[2] = int(opponent[2] * 2)
        elif mutacjco <= 60:  
            opponent[0] += " z mutacją calego wozka"
            opponent[1] = int(opponent[1] * 3)
            opponent[2] = int(opponent[2] * 3)
        
        return opponent

#--------------------------

def cos_zebniezdech():
    global hp, moc
    if liczba_ile_zlapales % luck == 0 and liczba_ile_zlapales > 0:
        if randint(1, 2) == 1:
            print("znalazles dodatkowe iq na +150 HP!")
            hp += 150
        else:
            print("znalazles swoje chromosomy +100 mocy!")
            moc += 100

fala = 11

def pozabiciub():
    global hp, moc
    if liczba_ile_zlapales % fala == 0 and liczba_ile_zlapales > 0:
        if randint(1, 2) == 1:
            print("znalazles kolege kaleke na +300 HP!")
            hp += 300
        else:
            print("kot +250 mocy!")
            moc += 250

#-------------------------
liczba_ile_zlapales = 0

while hp > 0:
    oponent = random_oponent()
    print("-" * 40)
    print(f"Nowy down: {oponent[0]} z {oponent[1]} HP i siłą {oponent[2]}!")

#---------------------
    if "twoja mama" in oponent[0] or "twoj tata" in oponent[0] or "TWOJ DZIADEK" in oponent[0]:
        liczba_ile_zlapales_megadown += 1
#-----------------------------------------
    while oponent[1] > 0 and hp > 0:
        print(f"{name} probuje zlapac {oponent[0]}")
        print(f"twoj down ma {oponent[1]} HP i bije cię na {oponent[2]} HP")

        hp -= oponent[2]
        if hp <= 0:
            break
        print(f"Masz {hp} HP i {moc} mocy.")   
        atak = wybierz_atak(skill)
        oponent[1] -= atak
        print(f"atakowales przeciwnika za {atak}.")

    if oponent[1] <= 0:
        print(f"zlapales {oponent[0]}!")
        liczba_ile_zlapales += 1

    if liczba_ile_zlapales % luck == 0 and liczba_ile_zlapales > 0:
        print("Znalazłeś napój bogów!")
        cos_zebniezdech()
    
    if liczba_ile_zlapales % fala == 0 and liczba_ile_zlapales > 0:
        print("fu....")
        pozabiciub()

print("-" * 40)
print("straciles wszystkie chromosomy")
print(f"zlapales {liczba_ile_zlapales} downow.")
print(f"zlapales {liczba_ile_zlapales_megadown} megadown")