# Mini Raktárkezelő alkalmazás

Modern Python alapú raktárkezelő alkalmazás grafikus felülettel.

## 📋 Projekt áttekintés

Ez a program egy egyszerű raktárkezelő rendszer, amely lehetővé teszi termékek nyilvántartását, értékük számítását és adatok JSON formátumban történő mentését.

## 🎯 Teljesített követelmények

**Grafikai modul**: customtkinter
**Tanult modul**: json (3 függvénnyel bemutatva)
**Saját modul**: bd_tools.py (BD monogrammal)
**Saját függvény**: calculateBDValue() (BD monogrammal)
**Saját osztály**: BDProductCard (BD monogrammal)
**Eseménykezelés**: gombok onClick eseményei
**Soronkénti magyarázat**: teljes dokumentáció

## 📁 Projekt struktúra

```
projekt/
│
├── main.py                    # Belépési pont
├── app.py                     # Főablak és logika
├── bd_tools.py                # Saját modul BD függvénnyel
│
├── widgets/
│   └── bd_product_card.py     # Saját BDProductCard osztály
│
└── data/
    └── inventory.json         # Mentett adatok
```

## 🚀 Telepítés és futtatás

### Követelmények
```bash
pip install customtkinter
```

### Futtatás
```bash
python main.py
```

## 📚 Modulok bemutatása

### 1. Grafikai modul – customtkinter

A **customtkinter** egy modern Python GUI-keretrendszer, amely a beépített tkinter továbbfejlesztett változata.

**Előnyök:**
- Modern, "flat" design
- Sötét/világos mód támogatása
- Szebb widgetek (gombok, entry-k, frame-ek)
- Egyszerűbb API
- Kompatibilis a natív tkinterrel

**Használat a projektben:**
```python
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Modern ablak és widgetek
```

### 2. Tanult modul – json

A **json** modul Python objektumok és JSON formátum közötti átalakítást tesz lehetővé.

**3 használt függvény:**

#### 1. `json.dump()`
Python listát vagy szótárt JSON fájlba ír:
```python
json.dump(self.inventory, f, indent=2, ensure_ascii=False)
```

#### 2. `json.load()`
JSON fájl beolvasása Python objektummá (használható betöltéshez).

#### 3. `json.dumps()`
Objektum string formátumba alakítása (debug célokra).

### 3. Saját modul – bd_tools.py

**Fájl:** `bd_tools.py`

**Függvény:** `calculateBDValue()`

```python
def calculateBDValue(qty):
    """
    Termék értékének kiszámítása darabszám alapján.
    Minden darab 2.5 értéket képvisel.
    
    Args:
        qty (int): Termék darabszáma
        
    Returns:
        float: Kiszámított érték
    """
    return qty * 2.5
```

**Jellemzők:**
- BD monogram a függvény nevében ✅
- Egyszerű logika
- Raktárkészlet értékének számítása

### 4. Saját osztály – BDProductCard

**Fájl:** `widgets/bd_product_card.py`

```python
class BDProductCard(ctk.CTkFrame):
    """
    Egyedi termékkártya widget a GUI-ban.
    Megjeleníti a termék nevét, darabszámát és értékét.
    """
    def __init__(self, master, name, qty, value):
        super().__init__(master)
        self.label = ctk.CTkLabel(
            self, 
            text=f"{name} – {qty} db – Érték: {value}"
        )
        self.label.pack(pady=5)
```

**Jellemzők:**
- BD monogram az osztály nevében ✅
- CTkFrame leszármazott (öröklődés)
- Dinamikusan generált GUI elemek
- Termék adatok vizuális megjelenítése


### main.py

```python
from app import App
# Importáljuk az App osztályt az app.py-ból

if __name__ == "__main__":
# Python belépési pont, innen indul a program

    app = App()
    # Létrehozunk egy App példányt (fő ablak)
    
    app.mainloop()
    # Elindítjuk az eseménykezelő ciklust
```

### app.py – Import szekció

```python
import customtkinter as ctk
# Grafikai modul betöltése

import json
# Tanult modul: JSON fájlkezelés

from widgets.bd_product_card import BDProductCard
# Saját osztály importálása

from bd_tools import calculateBDValue
# Saját modul és függvény importálása
```

### App osztály inicializálás

```python
class App(ctk.CTk):
# Főablak osztály, CTk bővítése

    def __init__(self):
        super().__init__()
        # Ősosztály konstruktor meghívása
        
        self.title("Mini Raktárkezelő – BD")
        # Ablak címének beállítása
        
        self.geometry("500x550")
        # Ablak méretének beállítása (szélesség x magasság)
        
        self.inventory = []
        # Üres lista a termékek tárolására
```

### Input mezők létrehozása

```python
self.name_entry = ctk.CTkEntry(self, placeholder_text="Termék neve")
# Szövegbeviteli mező terméknévhez

self.name_entry.pack(pady=5)
# Elhelyezés 5 pixel függőleges térközzel

self.qty_entry = ctk.CTkEntry(self, placeholder_text="Darabszám")
# Szövegbeviteli mező darabszámhoz

self.qty_entry.pack(pady=5)
# Elhelyezés padding-gel
```

### Gombok és eseménykezelés

```python
add_btn = ctk.CTkButton(self, text="Hozzáadás", command=self.add_product)
# Gomb létrehozása eseménykezelővel

add_btn.pack(pady=10)
# Gomb elhelyezése

# command=self.add_product → kattintásra meghívódik az add_product() metódus
# Ez az eseménykezelés (kötelező elem)
```

### Görgethető lista keret

```python
self.list_frame = ctk.CTkScrollableFrame(self)
# Görgethető keret a termékkártyáknak

self.list_frame.pack(fill="both", expand=True)
# Kitölti a rendelkezésre álló helyet
```

### Mentés gomb

```python
save_btn = ctk.CTkButton(self, text="Mentés", command=self.save_inventory)
# Mentés gomb eseménykezelővel

save_btn.pack(pady=10)
# Elhelyezés
```

### add_product() metódus – Termék hozzáadása

```python
def add_product(self):
    """Új termék hozzáadása a raktárhoz"""
    
    name = self.name_entry.get().strip()
    # Név beolvasása, whitespace eltávolítása
    
    qty_text = self.qty_entry.get().strip()
    # Darabszám beolvasása szövegként
    
    if not name or not qty_text.isdigit():
        return
    # Validáció: ha üres vagy nem szám, kilép
    
    qty = int(qty_text)
    # Szöveg → egész szám konverzió
    
    value = calculateBDValue(qty)
    # SAJÁT FÜGGVÉNY HÍVÁSA: érték kiszámítása
    
    product = {"name": name, "qty": qty, "value": value}
    # Szótár létrehozása termékadatokkal
    
    self.inventory.append(product)
    # Hozzáadás a lista végéhez
    
    card = BDProductCard(self.list_frame, name, qty, value)
    # SAJÁT OSZTÁLY PÉLDÁNYOSÍTÁSA: GUI kártya létrehozása
    
    card.pack(fill="x", padx=10, pady=5)
    # Kártya elhelyezése a keretben
    
    self.name_entry.delete(0, "end")
    self.qty_entry.delete(0, "end")
    # Input mezők törlése következő bevitelhez
```

### save_inventory() metódus – Mentés JSON-ba

```python
def save_inventory(self):
    """Készlet mentése JSON fájlba"""
    
    with open("data/inventory.json", "w", encoding="utf-8") as f:
    # Fájl megnyitása írásra, UTF-8 kódolással
    # 'with' biztosítja az automatikus bezárást
    
        json.dump(self.inventory, f, indent=2, ensure_ascii=False)
        # JSON MODUL HASZNÁLATA:
        # - self.inventory: Python lista konvertálása
        # - indent=2: olvasható formázás
        # - ensure_ascii=False: magyar karakterek támogatása
```

## 🎨 Funkcionalitás

1. **Termék hozzáadása**: Név és darabszám megadása
2. **Automatikus értékszámítás**: calculateBDValue() függvénnyel
3. **Vizuális megjelenítés**: BDProductCard osztállyal
4. **Adatok mentése**: JSON formátumban a data/ mappába
5. **Eseménykezelés**: Gombok onClick eseményei


## 👨‍💻 Szerző

**Monogram:** BD  
**Projekt:** Mini Raktárkezelő Rendszer  
**Nyelv:** Python 3.x  
**Framework:** customtkinter

---
