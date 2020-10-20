from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request
import msvcrt as stop
from sys import exit
import time
import sys
import os

cmd_request_2 = 'color 2'
os.system(cmd_request_2)

Banner = """>> 1) Check (USD) Exchange Rate (LKR)

>> 2) Check Exchange Rates in Major Countries

        • Australian Dollar   (AUD)
        • British Pound       (GPB)
        • Canadian Dollar     (CAD)
        • Euro                (EUR)
        • Japanese Yen        (JPY)
        • New Zealand Dollar  (NZD)
        • Swiss Franc         (CHF)
        • US Dollar           (USD)

>> 3) Exit\n\n>>  """

def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_f(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0)
    
def Connect(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

if Connect():
    print_s(">> Connected!..\n>> Proseeding...")
    os.system("cls")
else:
    print_s(">> Connection Faild!..\n>> Please Check Your Connection & Try Again..\n>> Client Exiting...")
    exit()
while True:
    try:
        option = int(input(Banner))
        if option not in (1,2,3):
            print_s(">> Not a Valid Option!..")
            os.system("cls")
            continue

        if option == 1:

            USD_LKR_URL = Request("https://www.investing.com/currencies/usd-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            USD_LKR = urlopen(USD_LKR_URL).read()
            USD_SOUP = BeautifulSoup(USD_LKR, features = "html5lib")
            print_s(">> Done!\n\n")
            USD_RATE = USD_SOUP.find('span',{'class':'arial_26 inlineblock pid-2151-last'})
            print_f(">> (USD) Price : "),print_s(USD_RATE.text + " (LKR)")
            print("\n")
            print_s(">>Press Anything For Main Menu!")
            stop.getch()
            os.system("cls")
            continue
        
        if option == 2:

            AUD_LKR_URL = Request("https://www.investing.com/currencies/aud-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            AUD_LKR = urlopen(AUD_LKR_URL).read()
            AUD_SOUP = BeautifulSoup(AUD_LKR, features = "html5lib")
            AUD_RATE = AUD_SOUP.find('span',{'class':'arial_26 inlineblock pid-9403-last'})
            print("\n>> (AUD) Price : "+AUD_RATE.text +"  (LKR)")
            GPB_LKR_URL = Request("https://www.investing.com/currencies/gbp-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            GPB_LKR = urlopen(GPB_LKR_URL).read()
            GPB_SOUP = BeautifulSoup(GPB_LKR, features = "html5lib")
            GPB_RATE = GPB_SOUP.find('span',{'class':'arial_26 inlineblock pid-1771-last'})
            print(">> (GPB) Price : "+GPB_RATE.text +" (LKR)")
            CAD_LKR_URL = Request("https://www.investing.com/currencies/cad-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            CAD_LKR = urlopen(CAD_LKR_URL).read()
            CAD_SOUP = BeautifulSoup(CAD_LKR, features = "html5lib")
            CAD_RATE = CAD_SOUP.find('span',{'class':'arial_26 inlineblock pid-9470-last'})
            print(">> (CAD) Price : "+CAD_RATE.text +"  (LKR)")
            EUR_LKR_URL = Request("https://www.investing.com/currencies/eur-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            EUR_LKR = urlopen(EUR_LKR_URL).read()
            EUR_SOUP = BeautifulSoup(EUR_LKR, features = "html5lib")
            EUR_RATE = EUR_SOUP.find('span',{'class':'arial_26 inlineblock pid-1659-last'})
            print(">> (EUR) Price : "+EUR_RATE.text +" (LKR)")
            JPY_LKR_URL = Request("https://www.investing.com/currencies/jpy-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            JPY_LKR = urlopen(JPY_LKR_URL).read()
            JPY_SOUP = BeautifulSoup(JPY_LKR, features = "html5lib")
            JPY_RATE = JPY_SOUP.find('span',{'class':'arial_26 inlineblock pid-9782-last'})
            print(">> (JPY) Price : "+JPY_RATE.text+"  (LKR)")
            NZD_LKR_URL = Request("https://www.investing.com/currencies/nzd-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            NZD_LKR = urlopen(NZD_LKR_URL).read()
            NZD_SOUP = BeautifulSoup(NZD_LKR, features = "html5lib")
            NZD_RATE = NZD_SOUP.find('span',{'class':'arial_26 inlineblock pid-9902-last'})
            print(">> (NZD) Price : "+NZD_RATE.text+"  (LKR)")
            CHF_LKR_URL = Request("https://www.investing.com/currencies/chf-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            CHF_LKR = urlopen(CHF_LKR_URL).read()
            CHF_SOUP = BeautifulSoup(CHF_LKR, features = "html5lib")
            CHF_RATE = CHF_SOUP.find('span',{'class':'arial_26 inlineblock pid-9552-last'})
            print(">> (CHF) Price : "+CHF_RATE.text+"  (LKR)")
            USD_LKR_URL = Request("https://www.investing.com/currencies/usd-lkr", headers={'User-Agent': 'Mozilla/5.0'})
            USD_LKR = urlopen(USD_LKR_URL).read()
            USD_SOUP = BeautifulSoup(USD_LKR, features = "html5lib")
            USD_RATE = USD_SOUP.find('span',{'class':'arial_26 inlineblock pid-2151-last'})
            print(">> (USD) Price : "+USD_RATE.text+" (LKR)")
            print("\n")
            print_s(">>Press Anything For Main Menu!")
            stop.getch()
            os.system("cls")
            continue

        if option == 3:
            exit()
        
    except Exception as WORDERROR:
        print_s(">> Not a Valid Option!..")
        os.system("cls")
        continue
else:
    exit()
        
