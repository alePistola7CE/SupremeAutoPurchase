import time
import sys
import os
import requests
from bs4 import BeautifulSoup
from splinter import Browser

product = "tops-sweaters/lh6fienmo/xe56n8acm"
mainUrl = "http://www.supremenewyork.com/shop/all"
baseUrl = "http://supremenewyork.com"
checkoutUrl = "https://www.supremenewyork.com/checkout"
selectOption = "Large"
namefield = "John Doe"
emailfield = "Test@example.com"
phonefield = "5555555555"
addressfield = "1600 Pennsylvania Avenue NW"
cityfield = "Paris" 
zipfield = "20500"
statefield = "FR" #have to use the value "FR" OR "IT", for more information see the html of the dropdown menu on the supreme page
cctypefield = "master"  # "master" "visa" "american_express"
ccnumfield = "5274576954806318"  # Randomly Generated Data (aka, this isn't mine)
ccmonthfield = "06"  # Randomly Generated Data (aka, this isn't mine)
ccyearfield = "2019"  # Randomly Generated Data (aka, this isn't mine)
cccvcfield = "800"  # Randomly Generated Data (aka, this isn't mine)


def main():
    print("")
    r = requests.get(mainUrl).text
    if product in r:
        parse(r)


def parse(r):
    soup = BeautifulSoup(r, "html.parser")
    for a in soup.find_all('a', href=True):
        link = a['href']
        checkproduct(link)


def checkproduct(l):
    if product in l:
        prdurl = baseUrl + l
        print(prdurl)
        buyprd(prdurl)
    else 
	print("Product <" + prdurl + "> not found")
	return


def buyprd(u):
    executable_path = {'executable_path':'C:\\Users\\Paolo\\AppData\\Local\\Google\\chromedriver'} #need to install chromedriver and add the executable path to the constructor
    browser = Browser('chrome', **executable_path )
    url = u
    browser.visit(url)
    # 10|10.5
    browser.find_option_by_text(selectOption).first.click()
    browser.find_by_name('commit').click()
    if browser.is_text_present('item'):
        print("Added to Cart")
    else:
        print("Error")
        return
    print("checking out")
    browser.visit(checkoutUrl)
    print("Filling Out Billing Info")
    browser.fill("order[billing_name]", namefield)
    browser.fill("order[email]", emailfield)
    browser.fill("order[tel]", phonefield)

    print("Filling Out Address")
    browser.fill("order[billing_address]", addressfield)
    browser.fill("order[billing_city]", cityfield) #added by alePistola7CE
    browser.fill("order[billing_zip]", zipfield)
    browser.select("order[billing_country]", statefield) #country not state
    print("Filling Out Credit Card Info")

    browser.select("credit_card[type]", cctypefield)
    browser.fill("credit_card[cnb]", ccnumfield)
    browser.select("credit_card[month]", ccmonthfield)
    browser.select("credit_card[year]", ccyearfield)
    browser.fill("credit_card[vval]", cccvcfield) # not credit_card[verification_value] but "credit_card[vval]"
    browser.find_by_css('.terms').click()
    print("Submitting Info")
    browser.find_by_name('commit').click()
    time.sleep(3)
    print(browser.find_by_id("order-no").value)
    sys.exit(0)


i = 0

while (True):
    main()
    i = i + 1
    print("On try number " + str(i))
    time.sleep(2)
