import Tool
from Tool.gui import ToolGUI
from Tool.web import webSite

l_wifi = []
l_pass = []
d_web = {}

extractor = Tool.wifiExtractor(l_wifi, l_pass, d_web)

wifi = extractor.extractWifi()
passwords = extractor.extractPassword()
webs = extractor.extractWeb()

print(wifi, end="\n\n")
print(passwords, end="\n\n")
print(webs, end="\n\n")

ToolGUI().mainloop()

scelta = input("Vuoi avviare il sito ?")
if scelta == "si":
    webSite.run()
else:
    pass