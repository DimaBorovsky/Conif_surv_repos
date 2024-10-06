import selenium
from selenium import webdriver
import time
import requests
import undetected_chromedriver as a

My_driver = webdriver.Chrome()
My_driver_2 = a.Chrome(headless=True,use_subprocess=False)


pop = ['''AKL,AMS,ATL,BCN,BKK,BOG,BOM,CDG,CGK,CHI,CPH,CPT,DEN,DET,DFW,DUB,DUS,DXB,EWR,EZE,FRA,GRU,HAN,HKG,HOU,IAD,IST,JKT,JNB,KOR,KUL,LAX,LHR,LIM,LON,MAD,MED,MEL,MEX,MIA,MNL,MSK,MXP,NDL,NYC,ORD,OSK,QRO,RIO,SAO,SCL,SEA,SIN,SJC,STC,STO,SYD,TKO,TOR,TPE,VAN,VIE,WAR,YUL,ZRH
''']
Server = ["ogw, anl, bh"]

server_to_zeroise = input(f"which server needs to be zeroised{Server}.{pop}")
server_url = My_driver.get(f"https://{server_to_zeroise}.{pop}.zamsh.incapsula.mobi/config_survivability_change_revlite_repository?global=0&sites_and_accounts=0&confirm=yes")


#server names will appear here in a large string unless any better way to do it for ogw,s



#tries to bypass the ReCaptcha
My_driver_2.get(f"{server_url}")
My_driver_2.save_screenshot(f"{server_url}")



def login(username,password):
    username = input("pleae enter the username")
    password = input("please enter the password")
    if username != ["anl_.","bh_.", "ogw_."]:
        print("Wrong user name please check Vault for credentials ")


if server_to_zeroise != Server:
    print("This is the wrong server")



# finds the survivabilty tab and cliks the dropdown
My_driver.find_element(by="id",value="headingThree").click()

#find the HTML value of the global repos to zeroise
My_driver.find_element(by="type",value="global").send_keys("0")

#finds the HTML value of the S&A repos to zeroise
My_driver.find_element(by="type",value="sites_and_accounts").send_keys("0")


#confimrs the zeroised repos Presses the confirm
My_driver.find_element(by="type", value="confirm").click()

#closes the Chrome driver
My_driver.close()

#web scrapping PD incidnets page and the trigerred alerts
# My_driver_2.get(f"https://incapsula.pagerduty.com/incidents?status=triggered")
# My_driver_2.find_element()
