import time
from sys import stderr
import requests
import json

#==============================
# MEMBUAT LACAK IP DENGAN IPAPI
#==============================
# MOHON IZIN, APABILA INGIN RECODE TOOLS INI
def banner():
    time.sleep(0.5)
    stderr.writelines("""\033[36;1m
   .-.
   .'   `.          --------------------------------
   :g g   :         | GHOST - TRACKER - IP ADDRESS |
   : o    `.        |       @CODE BY HUNX04        |
  :         ``.     --------------------------------
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'
""")

def lacak_ip():
    ip_address = input("\033[37;1m\n Masukan Alamat IP Target : \033[36;1m")
    ip_request = requests.get(f"http://ip-api.com/json/{ip_address}")
    
    if ip_request.status_code == 200:
        ip_data = json.loads(ip_request.text)

        if ip_data["status"] == "success":
            print("\033[37;1m\n ----------------------------------------")
            print("\033[37;1m\n Alamat IP     :\033[36;1m", ip_data["query"])
            print("\033[37;1m Negara        :\033[36;1m", ip_data["country"])
            print("\033[37;1m Kode Negara   :\033[36;1m", ip_data["countryCode"])
            print("\033[37;1m Wilayah       :\033[36;1m", ip_data["region"])
            print("\033[37;1m Nama Wilayah  :\033[36;1m", ip_data["regionName"])
            print("\033[37;1m Kota          :\033[36;1m", ip_data["city"])
            print("\033[37;1m Kode Pos      :\033[36;1m", ip_data["zip"])
            lat =  ip_data["lat"]
            lon =  ip_data["lon"]
            print("\033[37;1m Garis Lintang :\033[36;1m", lat)
            print("\033[37;1m Garis Bujur   :\033[36;1m", lon)
            maps  =  f"https://www.google.com/maps/@{lat},{lon},9z"
            print("\033[37;1m Maps          :\033[36;1m", maps )
            print("\033[37;1m Zona Waktu    :\033[36;1m", ip_data["timezone"])
            print("\033[37;1m ORG           :\033[36;1m", ip_data["org"])
            print("\033[37;1m ISP           :\033[36;1m", ip_data["isp"])
            print("\033[37;1m Nama AS       :\033[36;1m", ip_data["as"] )     
banner()
lacak_ip()
