import subprocess

class wifiExtractor:
    def __init__(self, arr_wifi, arr_pass, dict_rete):
        self.arr_wifi = arr_wifi
        self.arr_pass = arr_pass
        self.dict_rete = dict_rete


    def extractWifi(self):
        meta_data = subprocess.check_output("netsh wlan show profiles")

        try:
            data = meta_data.decode("UTF-8", errors="ignore")
        except:
            data = meta_data.encode("UTF-8").decode("UTF-8", errors="ignore")

        data = data.split("\n")

        for line in data:
            if "Tutti i profili utente    :" in line:
                newline = line.split("Tutti i profili utente    : ")
                wifi = newline[1]
                wifi = wifi.split("\r")
                self.arr_wifi.append(wifi[0])

        return self.arr_wifi

    def extractPassword(self):
        for wifi in self.arr_wifi:
            # print(wifi)
            # print("\n")

            meta_data = subprocess.check_output(f'netsh wlan show profile "{wifi}" key=clear')

            try:
                data = meta_data.decode("UTF-8", errors="backslashreplace")
            except:
                data = meta_data.encode("UTF-8").decode("UTF-8", errors="backslashreplace")

            data = data.split("\n")

            for line in data:
                if "Contenuto chiave            :" in line:
                    password = line.split("Contenuto chiave            :")[1]
                    password = password.split("\r")[0]
                    self.arr_pass.append(password)

        # self.arr_pass = [x for x in set(self.arr_pass)]

        return self.arr_pass

    def extractWeb(self):

        if int((len(self.arr_wifi) and len(self.arr_pass))) != 0:
            # print("si")
            # print(int((len(self.arr_wifi) and len(self.arr_pass))))
            pass
        else:
            # print("no")
            self.extractWifi()
            self.extractPassword()


        for wifi in self.arr_wifi:
            self.dict_rete[wifi] = self.arr_pass[self.arr_wifi.index(wifi)]

        return self.dict_rete





