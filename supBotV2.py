import time
import sys
import os
import requests
from bs4 import BeautifulSoup
from splinter import Browser


category = "/jackets"
productName = "Shadow Plaid Wool Overcoat"
product = "jackets/jqotka3zd/baft9gw5k"
mainUrl = "http://www.supremenewyork.com/shop/all"
baseUrl = "http://supremenewyork.com"
checkoutUrl = "https://www.supremenewyork.com/checkout"
selectOption = "Large"
namefield = "John Doe"
emailfield = "mario.rossi@gmail.com"
phonefield = "5555555555"
addressfield = "1600 Pennsylvania Avenue NW"
cityfield = "Paris"
Hset = 17
Mset = 4
Sset = 6
zipfield = "20500"
statefield = "FR" #have to use the value "FR" OR "IT", for more information see the html of the dropdown menu on the supreme page
cctypefield = "master"  # "master" "visa" "american_express"
ccnumfield = "5274576954806318"  # Randomly Generated Data (aka, this isn't mine)
ccmonthfield = "06"  # Randomly Generated Data (aka, this isn't mine)
ccyearfield = "2019"  # Randomly Generated Data (aka, this isn't mine)
cccvcfield = "800"  # Randomly Generated Data (aka, this isn't mine)


def main():
    print("")
    print("[i] Bot started correctly")
    parse()


def parse():
    if category != "" and productName != "":
        print("[i] Looking for " + productName)
        search_by_keyword(productName)
    else:
        print("[i] Looking for "+ product)
        search_by_link()



def search_by_link():
    r = requests.get(mainUrl).text
    soup = BeautifulSoup(r, "html.parser")
    for a in soup.find_all('a', href=True):
        link = a['href']
        checkproduct(link)


#beta def search_by_keyword(kw)
def search_by_keyword(productName):
    r = requests.get(mainUrl + category)
    soup = BeautifulSoup(r.content, "html.parser")
    for item in soup.find_all('a', {'class': 'name-link'}):
        if productName == item.text:
            print ('[i] Product ' + productName + ' found: url -> "' + item['href'] + '"')
            product = item['href']
            checktime(baseUrl + product)


def checkproduct(l):
    if product in l:
        prdurl = baseUrl + l
        print("[i] Product url found:" + prdurl)
        checktime(prdurl)
    else:
	    prdurl = baseUrl + l
	    print("[x] Product <" + prdurl + "> not found")
	    return

def checktime(prdurl):
	prdurl = prdurl
	localtime = time.localtime(time.time())
	realH = localtime[3]
	realM = localtime[4]
	realS = localtime[5]
	if realH == Hset:
		if realM >= Mset:
			if realS >= Sset:
				buyprd(prdurl)
			else:
				print("[x] Retry in: " + str(Sset - realS) + "second/s")
				time.sleep(Sset - realS)
				checktime(prdurl)
		else:
			print("[x] Retry in: " + str(Mset-realM) + "minute/s and " + str(Sset) + "seconds")
			time.sleep(2)
			checktime(prdurl)
	else:
		print("[x] Too early brooo, retry tomorrow :D")
		sys.exit(0)


def buyprd(u):
    localtime = time.localtime(time.time())
    #print("[i] Ora inizio acquisto : %s" % str(time.localtime()))
    print("[i] Ora inizio acquisto : %s:%s:%s" % (str(localtime[3]), str(localtime[4]), str(localtime[5])))
    url = u
    browser.visit(url)
    # 10|10.5
    browser.find_option_by_text(selectOption).first.click()
    browser.find_by_name('commit').click()
    if browser.is_text_present('item'):
        print("[i] Added to Cart")
    else:
        print("[x] Error")
        return
    print("[i] Checking out")
    browser.visit(checkoutUrl)
    print("[i] Filling Out Billing Info")
    browser.fill("order[billing_name]", namefield)
    browser.fill("order[email]", emailfield)
    browser.fill("order[tel]", phonefield)

    print("[i] Filling Out Address")
    browser.fill("order[billing_address]", addressfield)
    browser.fill("order[billing_city]", cityfield) #added by alePistola7CE
    browser.fill("order[billing_zip]", zipfield)
    browser.select("order[billing_country]", statefield) #country not state
    print("[i] Filling Out Credit Card Info")

    browser.select("credit_card[type]", cctypefield)
    browser.fill("credit_card[cnb]", ccnumfield)
    browser.select("credit_card[month]", ccmonthfield)
    browser.select("credit_card[year]", ccyearfield)
    browser.fill("credit_card[vval]", cccvcfield) # not credit_card[verification_value] but "credit_card[vval]"
    browser.find_by_css('.terms').click()
    print("[i] Submitting Info")
    browser.find_by_name('commit').click()
    time.sleep(3)
    print(browser.find_by_id("order-no").value)
    #print("[i] Ora fine acquisto : %s" % str(time.localtime()))
    localtime = time.localtime(time.time())
    print("[i] Ora fine acquisto : %s:%s:%s" % (str(localtime[3]), str(localtime[4]), str(localtime[5])))
    sys.exit(0)


i = 0

while (True):
    #I open now the browser only because of this is a faster way to manage the flow of the application
    executable_path = {'executable_path':'C:\\Users\\YourUsername\\AppData\\Local\\Google\\chromedriver'} #need to install chromedriver and add the executable path to the constructor
    browser = Browser('chrome', **executable_path )
    browser.visit("http://www.google.it")
    localtime = time.localtime(time.time())
    main()
    i = i + 1
    print("On try number " + str(i))
    time.sleep(2)
