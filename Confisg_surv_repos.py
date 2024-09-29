from selenium import webdriver
import time

pop = ['''AKL,AMS,ATL,BCN,BKK,BOG,BOM,CDG,CGK,CHI,CPH,CPT,DEN,DET,DFW,DUB,DUS,DXB,EWR,EZE,FRA,GRU,HAN,HKG,HOU,IAD,IST,JKT,JNB,KOR,KUL,LAX,LHR,LIM,LON,MAD,MED,MEL,MEX,MIA,MNL,MSK,MXP,NDL,NYC,ORD,OSK,QRO,RIO,SAO,SCL,SEA,SIN,SJC,STC,STO,SYD,TKO,TOR,TPE,VAN,VIE,WAR,YUL,ZRH
''']


server_to_zeroise = input(f"which server needs to be zeroised.{pop}")
#server names will appear here in a large string unless any better way to do it for ogw,s

My_driver = webdriver.Chrome()
My_driver.get(f"https://{server_to_zeroise}.{pop}.zamsh.incapsula.mobi/config_survivability_change_revlite_repository?global=0&sites_and_accounts=0&confirm=yes")

My_driver.get(server_to_zeroise)

# finds the survivabilty tab and cliks the dropdown
My_driver.find_element(by="id",value="headingThree").click()

#find the HTML value of the global repos to zeroise
My_driver.find_element(by="type",value="global").send_keys("0")

#finds the HTML value of the S&A repos to zeroise
My_driver.find_element(by="type",value="sites_and_accounts").send_keys("0")
#keeps the browswer up for 5 minutes in order to verify keys are being sent
time.sleep(5)


