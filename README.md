# Raktárkezelő Program

Egy egyszerű program raktári termékek nyilvántartására.

## Mi ez?

Ez a program segít nyilvántartani, hogy milyen termékek vannak a raktárban. Be lehet írni a termék nevét és hogy hány darab van belőle, aztán a program kiszámolja és elmenti az adatokat **/data/inventory.json** fájlba.

## Hogyan működik?

A program customtkinter-rel készült, ami egy modernebb kinézetű GUI eszköz a Python-ban.

## Fájlok a projektben

- **main.py** - Ez indítja el a programot
- **app.py** - Itt van a fő program kódja
- **bd_tools.py** - Saját segédfüggvények
- **widgets/bd_product_card.py** - A termékek megjelenítéséhez
- **data/inventory.json** - Ide mentődnek az adatok

## Telepítés

Létrehozzuk a virtuális környezetet:

```bash
python3 -m .venv venv
```
Aktiválom a környezetet:

```bash
source .venv/bin/activate
```
ha majd már nem kell a környezet:

```bash
source .venv/bin/deactivate
```

Először telepítsük fel a customtkinter csomagot:

```bash
pip install customtkinter
```

Utána futtassuk a programot:

```bash
python main.py
```

## Mit tanultam a készítése közben?

### 1. Grafikus felület (customtkinter)

A customtkinter modernebb kinézetű ablakokat tud csinálni mint a sima tkinter. Könnyebb is használni.

```python
import customtkinter as ctk

ablak = ctk.CTk()
ablak.title("Program címe")
```

### 2. JSON mentés

A json modullal lehet Python adatokat fájlba menteni. Három függvényt használtam:

**json.dump()** - Fájlba ír
```python
json.dump(adatok, fajl, indent=2)
```

**json.load()** - Fájlból olvas be

**json.dumps()** - Szöveggé alakít

### 3. Saját függvény (bd_tools.py)

Csináltam egy függvényt ami kiszámítja egy termék értékét:

```python
def calculateBDValue(darabszam):
    return darabszam * 2.5
```

Minden darab 2.5 értéket ér, ezt számítja ki.

### 4. Saját osztály (BDProductCard)

Ez egy kis doboz ami megjeleníti egy termék adatait:

```python
class BDProductCard(ctk.CTkFrame):
    def __init__(self, master, nev, db, ertek):
        super().__init__(master)
        self.label = ctk.CTkLabel(self, text=f"{nev} – {db} db – {ertek} Ft")
        self.label.pack()
```

## A kód magyarázata

### main.py - Indítás

```python
from app import App
# Betöltjük a fő programot

if __name__ == "__main__":
# Ha ez a fájl fut (nem importálják)

    app = App()
    # Példányt csinálunk
    
    app.mainloop()
    # Elindítjuk az ablakot
```

### app.py - Import rész

```python
import customtkinter as ctk
# Ablakos programozáshoz

import json
# Fájl mentéshez/betöltéshez

from widgets.bd_product_card import BDProductCard
# Saját termékkártya osztály

from bd_tools import calculateBDValue
# Saját számító függvény
```

### Az App osztály

```python
class App(ctk.CTk):
# Létrehozom az "ablak" osztályt
    
    def __init__(self):
        super().__init__()
        # Szülő osztály indítása
        
        self.title("App")
        # Meghatározom az ablak címét
        
        self.geometry("500x550")
        # Meghatározom az ablak méretét
        
        self.inventory = []
        # Lista a "termékeknek"
```

### Beviteli mezők

```python
self.name_entry = ctk.CTkEntry(self, placeholder_text="Termék neve")
# Ide írja be a felhasználó a nevet

self.name_entry.pack(pady=5)
# Elhelyezi az ablakban, 5 pixel térköz

self.qty_entry = ctk.CTkEntry(self, placeholder_text="Darabszám")
# Ide jön a darabszám

self.qty_entry.pack(pady=5)
```

### Gombok

```python
add_btn = ctk.CTkButton(self, text="Hozzáadás", command=self.add_product)
# Gomb ami meghívja az add_product függvényt kattintásra

add_btn.pack(pady=10)
# Elhelyezés
```

Ez az eseménykezelés - amikor rákattintunk, lefut egy függvény.

### Termék hozzáadása

```python
def add_product(self):
    # Kiolvassuk a nevet
    name = self.name_entry.get().strip()
    
    # Kiolvassuk a darabszámot
    qty_text = self.qty_entry.get().strip()
    
    # Ellenőrzés
    if not name or not qty_text.isdigit():
        return  # Ha rossz, kilép
    
    # Szövegből számot készítek
    qty = int(qty_text)
    
    # SAJÁT FÜGGVÉNY használata
    value = calculateBDValue(qty)
    
    # Termék objektum product néven
    product = {"name": name, "qty": qty, "value": value}
    
    # Hozzáadás a listához
    self.inventory.append(product)
    
    # Megjeleníti a képernyőn
    card = BDProductCard(self.list_frame, name, qty, value)
    card.pack(fill="x", padx=10, pady=5)
    
    # Mezők törlése
    self.name_entry.delete(0, "end")
    self.qty_entry.delete(0, "end")
```

### Mentés

```python
def save_inventory(self):
    # Fájl megnyitása írásra
    with open("data/inventory.json", "w", encoding="utf-8") as f:
        # JSON modulal mentés
        json.dump(self.inventory, f, indent=2, ensure_ascii=False)
```

A `with` automatikusan bezárja a fájlt.

## Mit csinál a program?

1. Be lehet írni termék nevét
2. Be lehet írni hány darab van
3. Kiszámítja az értékét (darabszám × 2.5)
4. Kiírja a képernyőre
5. Elmenteni JSON fájlba

---