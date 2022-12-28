import Tool
import socket
import tkinter as tk
import os
from flask import Flask
from flask import render_template
# from flask import request
# from flask_wtf import FlaskForm
# from wtforms import StringField
# from wtforms import RadioField
# from wtforms import IntegerField
from wtforms import HiddenField
from Tool.gui import *
from uuid import getnode as get_mac
from tkinter import filedialog


webSite = Flask(__name__)
webSite.config['SECRET_KEY'] = 'chiavemoltosegreta'
HiddenField()

l_wifi = []
l_pass = []
d_web = {}


extractor = Tool.wifiExtractor(l_wifi, l_pass, d_web)
mac_ad = get_mac()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
webs = extractor.extractWeb()



@webSite.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@webSite.route("/wifiexcract", methods=["GET", "POST"])
def extractor():
    return render_template("wifiexcract.html", web=webs, macad=mac_ad, hostname=hostname, IPAddr=IPAddr)


@webSite.route("/crea_file")
def seleziona_cartella():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    path = os.getcwd()
    # path = str(path)
    # path = path.split("\\")
    # path.reverse()
    # path = path[0]
    folder_path = filedialog.askdirectory(title="Sezione Percorso File", initialdir=path)
    # print(folder_path)

    return folder_path


@webSite.route("/aprigui")
def aprigui():
    ToolGUI().mainloop()
    return render_template("index.html")


@webSite.route("/whriteFile.html")
def fatto():
    try:
        os.chdir(seleziona_cartella())
        file = open(f"Info di {hostname}.txt", "w")
        file.write('INFORMAZIONI DI "{}"\n\n\n-Hostname: {}\n\n-Indirizzo MAC: {}\n\n-Indirizzo IP: {}\n\n-Reti estratte: {}'.format(hostname, hostname, mac_ad, IPAddr, webs))
        file.close()
    except:
        pass

    return render_template("whriteFile.html")