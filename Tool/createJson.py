import json
import Tool
import socket
from uuid import getnode as get_mac


mac_ad = get_mac()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

web = {}


class createJson():
    def __init__(self, json_name, extension=True):
        self.json_name = json_name
        self.extractor = Tool.extractor(arr_wifi=[], arr_pass=[], dict_rete=web)


        self.info = {
            "Hostname": hostname,
            "Mac Address": mac_ad,
            "Ip Address": IPAddr,
            "Extracted Web": self.extractor.extractWeb()
        }

        if extension == True:
            with open(f"{self.json_name}.json", "w") as file:
                json.dump(self.info, file, indent=3)
        else:
            with open(f"{self.json_name}", "w") as file:
                json.dump(self.info, file, indent=3)

