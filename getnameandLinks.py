import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
url = "https://www.start-up.ma/liste-des-startups-au-maroc/"

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the website using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extract the information you need from the website
startup_list = soup.find_all("div", class_="vc_pageable-slide-wrapper")
#print(startup_list)
#
dom = etree.HTML(str(startup_list))
print(dom.xpath('//a[@class="vc_gitem-link"]')[0].text)
print(dom.xpath('//a[@class="vc_gitem-link"]/@href')[0])
# Data to be written
dictionary ={
    "nameStratup" : "sathiyajith",
    "link" : "9976770500"
}

totalStartup = []
with open('json_data.json', 'w') as outfile:
 for i in range(0, len(dom.xpath('//a[@class="vc_gitem-link"]'))+1):

      print(i)
      dictionary.clear()
      if i==199 : break
      dictionary["nameStratup"]= dom.xpath('//a[@class="vc_gitem-link"]')[i].text
      print( dictionary["nameStratup"])
      dictionary["link"] = dom.xpath('//a[@class="vc_gitem-link"]/@href')[i]
      print( dictionary["link"])
      totalStartup.append(dictionary)

      # Using a JSON string

      outfile.write(str(dictionary)+",")
#     print("Name: ", name)
#     print("Description: ", description)
