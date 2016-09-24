#!/usr/bin/python3

import getopt
import sys

registrace = open("registrace.csv", 'r')
vysledky = open("vysledky.csv", 'r')

celkove = []
for radek_vysledky in vysledky:
    vysledek = radek_vysledky.strip().split(';')

    for radek_registrace in registrace:
        ucastnik = radek_registrace.strip().split(';')
        if ucastnik[0] == vysledek[2]:
            vysledek_ucastnik = vysledek + ucastnik
            # print(vysledek_ucastnik)
            celkove.append(vysledek_ucastnik)
            registrace.seek(0)
            break

registrace.close()
vysledky.close()

# print(celkove)

vysledky_kategorie = {}

for radek in celkove:
    vysledky_kategorie[radek[8]] = []

for radek in celkove:
    vysledky_kategorie[radek[8]].append(radek)

opts, args = getopt.getopt(sys.argv[1:], "ak", ["help", "output="])

for o, a in opts:
    if o == "-a":

        print("Poradi;Startovni cislo;Cas;Jmeno;Prijmeni;Rocnik;Kategorie")
        for vysledek in celkove:
            print("%s;%s;%s;%s;%s;%s;%s" %
                (vysledek[0],
                vysledek[2],
                vysledek[1],
                vysledek[5],
                vysledek[6],
                vysledek[7],
                vysledek[8]
                )
            )

        print()
        print()

    if o == "-k":
        for kategorie in vysledky_kategorie.keys():
            print("Kategorie: %s" % kategorie)
            print("Poradi;Startovni cislo;Cas;Jmeno;Prijmeni;Rocnik;Kategorie")
            poradi = 1
            for vysledek_kategorie in vysledky_kategorie[kategorie]:
                print("%d;%s;%s;%s;%s;%s;%s" %
                    (poradi,
                    vysledek_kategorie[2],
                    vysledek_kategorie[1],
                    vysledek_kategorie[5],
                    vysledek_kategorie[6],
                    vysledek_kategorie[7],
                    vysledek_kategorie[8]
                    )
                )
                poradi = poradi + 1
        
            print()