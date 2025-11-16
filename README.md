# Sledovanie_zvykov
Jednoduchý program v Python3.10 kde sleduje zvyky pomocou API. Tento program sleduje pocet precitanych stran

## Vlastnosti

*   Graficke pouzivatelske rozhranie (GUI) pre jednoduche zadavanie udajov.
*   Uverejnovanie novych zaznamov pre konkretny datum.
*   Aktualizacia existujucich poloziek.
*   Priamy odkaz na zobrazenie grafu navykov vo webovom prehliadaci.

## Nastavenie

1.  **Predpoklady:** Python 3 a kniznica `requests`.
2.  **Instalacia:** Nainstalujte pozadovanu kniznicu pomocou pip: `pip install requests`.
3.  **Konfiguracia:**
    *   Zaregistrujte sa do uctu Pixela na adrese [https://pixe.la/](https://pixe.la/).
    *   Otvorte subor `main.py` a aktualizujte nasledujuce konstanty vlastnymi udajmi:
        *   `USER_NAME`: Vase pouzivatelske meno Pixela.
        *   `TOKEN`: Vas autentifikacny token Pixela.
        *   `GRAPH_ID`: ID grafu, do ktoreho chcete prispievat. Mozno budete musiet tento graf najprv vytvorit prostrednictvom API alebo upravit skript, aby ste tak urobili.

## Pouzitie

1.  Spustite skript `main.py`: `python main.py`.
2.  Zobrazi sa okno aplikacie.
3.  Pole `Datum` je vopred vyplnene aktualnym datumom vo formate `RRRRMMDD`. V pripade potreby ho mozete zmenit.
4.  Do pola `Mnozstvo` zadajte mnozstvo (napr. pocet precitanych stran).
5.  Kliknutim na tlacidlo "Pridat/aktualizovat polozku" ulozite udaje do Pixely.
6.  Kliknutim na tlacidlo "Zobrazit graf" otvorite graf sledovania navykov vo vychodiskovom webovom prehliadaci.
