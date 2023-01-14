
import time as t
import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))#,options=options


url=[]


totalStartup = []
with open('nameAndLinks.json') as json_file:
    data = json.load(json_file)
i=0
with open('allinformation.json', 'w') as outfile:
    for p in data:
        print(i)
        i=i+1
        dictionary = {
            "nameStratup": str(p['nameStratup']),
            "link": str(p['link']),
            "details": " ",
            "website": " ",
            "phone": " ",
            "email": " ",
            "facebook": " ",
            "instagram": " ",
            "linkdin": " "

        }
        dictionary.clear()
        dictionary["nameStratup"] = str(p['nameStratup'])
        dictionary["link"] = str(p['link'])
        # Send a GET request to the website

        #response = requests.get(p['link'])

        # Parse the HTML content of the website using BeautifulSoup
        driver.get(p['link'])
        #driver.maximize_window()
        t.sleep(3)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        try:
            dictionary["details"] = str(soup.find("h1", {"class": "vc_custom_heading"}).text)
        except:
            print("except details")
            dictionary["details"] = "null"
        #soup = BeautifulSoup(response.content, "html.parser")
        a_href = soup.find_all("a", {"data-vc-gradient-1": "#0061ff"})
        for a in a_href:
            print("eeeeeeeeeeeeeeeeeeeee")
            if a.text == " Envoyer un Email":
                print(a.text)
                dictionary["email"] = a.get('href')
                url = a.get('href')
                # print(a)
                print(url)
            if a.text == " Page Linkedin":
                print(a.text)
                dictionary["linkdin"] = a.get('href')
                url = a.get('href')
                print(url)
            if a.text == " Appeler":
                print(a.text)
                dictionary["phone"] = a.get('href')
                url = a.get('href')
                print(url)
            if a.text == " Page Facebook":
                print(a.text)
                dictionary["facebook"] = a.get('href')
                url = a.get('href')
                print(url)
            if a.text == " Site web":
                print(a.text)
                dictionary["website"] = a.get('href')
                url = a.get('href')
                print(url)
            if a.text == " Page Instagram":
                print(a.text)
                dictionary["instagram"] = a.get('href')
                url = a.get('href')
                print(url)
            print(dictionary)
            outfile.write(str(dictionary) + ",")

        # dom = etree.HTML(str(soup))
        # print(soup)
        # alltextbutton = dom.xpath('//div[@class="wpb_column vc_column_container vc_col-sm-3"]//a[@data-vc-gradient-1]')[0]
        # print(str(alltextbutton.text))
        # dictionary.clear()
       #
       #
       #  dictionary["nameStratup"] = str(p['nameStratup'])
       #  dictionary["link"] = str(p['link'])
       #  try:
       #   dictionary["details"] = str(dom.xpath('//div[@class="wpb_wrapper"]//span')[0].text)
       #  except:
       #   print("except details")
       #   dictionary["details"] ="null"
       #  try:
       #   j=0
       #   for website in alltextbutton :
       #       print(str(alltextbutton))
       #       if website.text==" Site web":
       #          print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
       #          dictionary["website"] = str(dom.xpath('//div[@class="vc_btn3-container vc_btn3-center"]/a[@data-vc-gradient-1]/@href'))[j]
       #          print(dictionary["website"])
       #         # dictionary["website"] = str(dom.xpath('//a[@class="vc_btn-gradient-btn-63c20f20106e2"]/@href'))
       #   j = j + 1
       #  except:
       #   print("except website")
       #   dictionary["website"] ="null"
       #  try:
       #   dictionary["phone"] = str(dom.xpath('//a[@class="vc_btn-gradient-btn-63c20f201081f"]/@href'))
       #  except:
       #   print("except phone")
       #   dictionary["phone"] ="null"
       #  try:
       #   dictionary["email"] = str(dom.xpath('//a[@class="vc_btn-gradient-btn-63c20f201093b"]/@href'))
       #  except:
       #    print("except email")
       #    dictionary["email"] ="null"
       #  try:
       #    dictionary["linkdin"] = str(dom.xpath('//a[@class="vc_btn-gradient-btn-63c20f2010a9c"]/@href'))
       #  except:
       #    print("except linkdin")
       #    dictionary["linkdin"] ="null"
       #  try:
       #     dictionary["facebook"] = str(dom.xpath('//a[@class="vc_btn-gradient-btn-63c211d3beac1"]/@href'))
       #  except:
       #     print("except facebook")
       #     dictionary["facebook"] ="null"
       #  try:
       #     dictionary["instagram"] = str(dom.xpath('//a[@class="vc_btn-gradient-btn-63c211d3beac1"]/@href'))
       #  except:
       #     print("except instagram")
       #     dictionary["instagram"] ="null"
       #  totalStartup.append(dictionary)
       #
       #   # Using a JSON string
       # # print(str(dictionary))
       #  outfile.write(str(dictionary) + ",")
       #
       #
       #
