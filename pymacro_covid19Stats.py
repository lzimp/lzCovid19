

import requests, random
import urllib.request
import numpy as np
import time
from bs4 import BeautifulSoup
from datetime import datetime as dt


def loadCovidList():
    user_agents = ["Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"]
    random_user_agent = random.choice(user_agents)
    headers = {'User-Agent': random_user_agent}
    url = 'http://www.nhc.gov.cn/yjb/s7860/new_list.shtml'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features="lxml")
    print(soup)
    data = soup.find_all("li")
    print(len(data), data)



def loadCovidData():

    user_agents = ["Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0"]
    random_user_agent = random.choice(user_agents)
    headers = {'User-Agent': random_user_agent}
    #print(headers)
    #url = 'http://www.nhc.gov.cn/yjb/s7860/202208/7bcb5ceeefe540ebb9289c37cc0afc41.shtml'
    #url = 'http://www.nhc.gov.cn/yjb/s7860/202208/e12653e6071944c4b5da52b7bd552f20.shtml' 
    #url = 'http://www.nhc.gov.cn/yjb/s7860/202208/8fbbe614bd0c4a5ca9cf8a9e4c289e9a.shtml'
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, features="lxml")
    #print(soup)

    # get all the paragraphes in the page 
    data = soup.find_all("p")
    #print(data)
    print(len(data))

    for ip in range(7):
        print("第 %d 段内容： "%(ip+1), data[ip].get_text())
        

def main():

    #loadCovidData()
    loadCovidList()

if __name__ == '__main__':
    main()
