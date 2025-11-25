import customtkinter as ctk

class BDProductCard(ctk.CTkFrame):
  def __init__(self, master, name, qty, value):
    super().__init__(master)
    self.label = ctk.CTkLabel(
      self,
      text=f" {name} - {qty} db - Érték {value}"
    )
    self.label.pack(pady=5, padx=10)