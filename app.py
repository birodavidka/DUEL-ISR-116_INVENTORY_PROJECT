import customtkinter as ctk
import json
from widgets.bd_product_card import BDProductCard
from bd_tools import calculateBDvalue


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Mini Raktárkezelő – BD")
        self.geometry("500x550")

        # Input mezők
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Termék neve")
        self.name_entry.pack(pady=5)

        self.qty_entry = ctk.CTkEntry(self, placeholder_text="Darabszám")
        self.qty_entry.pack(pady=5)

        # Gomb: hozzáadás
        add_btn = ctk.CTkButton(self, text="Hozzáadás", command=self.add_product)
        add_btn.pack(pady=10)

        # Lista keret
        self.list_frame = ctk.CTkScrollableFrame(self)
        self.list_frame.pack(fill="both", expand=True, pady=10)

        # Mentés gomb
        save_btn = ctk.CTkButton(self, text="Mentés", command=self.save_inventory)
        save_btn.pack(pady=10)

        # belső adattárolás
        self.inventory = []

    # ────────────────────────────────────────────────
    #    FELHASZNÁLÓI ESEMÉNYEK
    # ────────────────────────────────────────────────

    def add_product(self):
        """Gombnyomásra felvesz egy új terméket."""
        name = self.name_entry.get().strip()
        qty_text = self.qty_entry.get().strip()

        # Biztonsági ellenőrzés
        if not name or not qty_text.isdigit():
            return

        qty = int(qty_text)

        # Saját függvény → value számolása
        value = calculateBDvalue(qty)

        # Listához hozzáadjuk
        product = {"name": name, "qty": qty, "value": value}
        self.inventory.append(product)

        # GUI kártya létrehozása
        card = BDProductCard(self.list_frame, name, qty, value)
        card.pack(pady=5, padx=10, fill="x")

        # mezők ürítése
        self.name_entry.delete(0, "end")
        self.qty_entry.delete(0, "end")

    def save_inventory(self):
        """JSON fájlba menti az adatokat."""
        with open("data/inventory.json", "w", encoding="utf-8") as f:
            json.dump(self.inventory, f, indent=2, ensure_ascii=False)
