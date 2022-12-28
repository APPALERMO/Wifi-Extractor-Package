import tkinter as tk
import tkinter.font as tkfont


class Notifica(tk.Toplevel):
    def __init__(self, titolo, esito, testo):

        super().__init__()
        self.titolo = titolo
        self.esito = bool(esito)
        self.testo = testo

        Fatto = "Tool\\Immagini\\Fatto.png"
        Errore = "Tool\Immagini\\Errore.png"

        FattoIco = "Tool\\Immagini\\FattoIco.ico"
        ErroreIco = "Tool\\Immagini\\ErroreIco.ico"

        self.title(self.titolo)
        self.geometry("450x185")
        self.resizable(False, False)
        self.attributes("-topmost", True)

        self.positivo = tk.PhotoImage(file=Fatto)
        self.negativo = tk.PhotoImage(file=Errore)

        if self.esito:
            self.immagine = tk.Label(self, image=self.positivo)
            self.immagine.grid(row=0, column=0)
            self.iconbitmap(FattoIco)
            # print("Si")
        else:
            self.immagine = tk.Label(self, image=self.negativo)
            self.immagine.grid(row=0, column=0)
            self.iconbitmap(ErroreIco)
            # print("No")

        self.labelTesto = tk.Label(self, text=self.testo, wraplength=275, font=tkfont.Font(family="Helvetica", size=10, weight="bold"))
        self.labelTesto.grid(row=0, column=1)

        self.tastok = tk.Button(self, text="Ok, Ho capito!", font=tkfont.Font(family="Helvetica", size=10), fg="#ff0000", command=self.ok)
        self.tastok.grid(row=1, column=1, sticky="WE")

    def ok(self):
        self.destroy()