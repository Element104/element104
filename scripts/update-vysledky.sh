#!/bin/bash

while true; do cp tabulka.csv vysledky.csv; ../scripts/zpracuj.py -w > vysledky-static.html; scp vysledky-static.html wds:/var/www/html/vysledky.html; sleep 60; done