import random
v = input("Zasifrovat (s) alebo desifrovat (d)? ")

if v == "s":
    fr = open("vstupny_text.txt", "r")
else:
    fr = open("zasifrovany_text_2.txt", "r")
text = fr.readlines()
fr.close()

vysledok = ""

def sifroavnie():
    global vysledok
    for line in text:
        line = line.rstrip("\n")
        posun = random.randint(1,25)
        vysledok += str(chr(posun+96))
        for char in line:
            if char.islower() and (ord(char)>96 and ord(char)<123):
                a = ord(char)-97
                vysledok += chr((a+posun) % 26 + 97)
            else:
                vysledok += char
        vysledok += "\n"

def desifrovanie():
    global vysledok
    for line in text:
        line = line.rstrip("\n")
        posun = ord(line[0])-96
        for aa in range(1,len(line)):
            pismeno = line[aa]
            if pismeno.islower() and (ord(pismeno)>96 and ord(pismeno)<123):
                a = ord(pismeno)-97
                vysledok += chr((a - posun) % 26 + 97)
            else:
                vysledok += pismeno
        vysledok += "\n"

if v == "s":
    sifroavnie()
    fw = open("zasifrovany_text.txt", "w")
else:
    desifrovanie()
    fw = open("desifrovany_text.txt", "w")

fw.write(vysledok)
fw.close()