# -*- coding: utf-8 -*-
import webbrowser
import requests
from bs4 import BeautifulSoup
import re
from .fileHandler import write_file, read_file
from utilities.GeneralUtilities import print_say
from colorama import Fore
import six

def showsearch(string):
    url = "https://www.google.com/search?q={}".format(string.replace("for", ""))
    webbrowser.open(url)

def urlsearch(string, self):
    print_say("How many results to you want?", self)
    if six.PY2:
	answer = raw_input()
    else:
	answer = input()
    results = int(answer)
    page = requests.get("https://www.google.com/search?q={}&num={}".format(string.replace("for",""), results))
    soup = BeautifulSoup(page.content, "html5lib")
    links = soup.findAll("a")
    index = 0
    urlList = {}
    for link in links :
	link_href = link.get('href')
	if "url?q=" in link_href and not "webcache" in link_href:
	     l = (link.get('href').split("?q=")[1].split("&sa=U")[0])
	     urlList[index] = l
	     index += 1
    x = 0
    index1 = 0
    for x in range(0, len(urlList)):
	print(str(index1) + ": " + str(urlList[x]))
	x += 1
	index1 += 1
    print_say("To open a link type the index: ", self)
    if six.PY2:
        idx = raw_input()
    else:
	idx = input()
    try:
        int(idx)
        if int(idx) > index:
              print_say("Not a valid index sir", self)
              return
    except:
         print_say("Not a valid index sir", self)
         return
    webbrowser.open(urlList[int(idx)])




