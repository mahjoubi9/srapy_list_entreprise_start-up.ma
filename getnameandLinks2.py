
import time as t
import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))#,options=options
url = "https://www.start-up.ma/liste-des-startups-a-casablanca/"

driver.get(url)
#driver.maximize_window()
t.sleep(3)
soup = BeautifulSoup(driver.page_source, 'lxml')
# # Send a GET request to the website
# response = requests.get(url)
#
# # Parse the HTML content of the website using BeautifulSoup
# soup = BeautifulSoup(response.content, "html.parser")

# Extract the information you need from the website
startup_list = soup.find_all("a", class_="vc_gitem-link vc_single_image-wrapper vc_box_border_grey",href=True)
print(len(startup_list))
dictionary ={
    "nameStratup" : "sathiyajith",
    "link" : "9976770500"
}
with open('allLinksPartie2.json', 'w') as outfile:
 for i in range(61):
   dictionary.clear()
   print(i)
   dictionary["link"] = str(startup_list[i]['href'])
   dictionary["nameStratup"] =str(startup_list[i]['title'])
   print(startup_list[i]['title'])
   print(startup_list[i]['href'])
   outfile.write(str(dictionary) + ",")
# for a in startup_list:
#     print(a['href'])
#
# #print(startup_list)
# for startup in startup_list:
#     dom = etree.HTML(str(startup))
#     print(dom)
#     print(dom.xpath('//img[@class="vc_single_image-img attachment-full"]/@href'))
#     print(startup.find("img", class_="vc_gitem-link vc_single_image-wrapper vc_box_border_grey"))


#print(startup_list.find("a", {"title": "Consulter"})[0].text)
# for startup in startup_list:
#     print(startup.find("a", {"title": "Consulter"}).text)
#print(startup_list)
#print(soup.find("h1", {"class": "vc_custom_heading"}).text)
# dom = etree.HTML(str(soup))
# print(len(dom.xpath('//a')))
# print(dom.xpath('//a')[6].text)
# print(dom.xpath('//a[@class="vc_general"]/@href')[0])
# #print(startup_list)
# #
# dom = etree.HTML(str(startup_list))
# print(dom.xpath('//a[@class="vc_general"]')[0].text)
# print(dom.xpath('//a[@class="vc_general"]/@href')[0])
# # Data to be written
# dictionary ={
#     "nameStratup" : "sathiyajith",
#     "link" : "9976770500"
# }
#
# totalStartup = []
# with open('casablanca_startup.json', 'w') as outfile:
#  for i in range(0, len(dom.xpath('//a[@class="vc_general"]'))+1):
#
#       print(i)
#       dictionary.clear()
#       if i==199 : break
#       dictionary["nameStratup"]= dom.xpath('//a[@class="vc_general"]')[i].text
#       print( dictionary["nameStratup"])
#       dictionary["link"] = dom.xpath('//a[@class="vc_general"]/@href')[i]
#       print( dictionary["link"])
#       totalStartup.append(dictionary)
#
#       # Using a JSON string
#
#       outfile.write(str(dictionary)+",")
# #     print("Name: ", name)
# #     print("Description: ", description)
