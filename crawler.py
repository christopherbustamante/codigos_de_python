from selenium import webdriver
from lxml import html
from PIL import Image
from selenium.webdriver.support.select import Select
from lxml import etree
import requests
import re
import urllib
import time
import cv2
import pytesseract
import socket
import numpy as np

Url_Get_MovieID = 'https://movie.douban.com/j/subject_suggest?q='
Url_DouBan = 'https://movie.douban.com/subject/'

def MidString(content,startStr,endStr):                     
    startIndex = content.index(startStr)                    
    if startIndex>=0:                                       
        startIndex += len(startStr)                         
        endIndex = content.index(endStr)                    
        return content[startIndex:endIndex]                 

def html():
    Movie_Name = input("Nombre de pelicula:")
    #      , directamente accesible, se rechazará
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    r_1 = requests.get(Url_Get_MovieID + Movie_Name,headers=headers)
    JSON = str(r_1.json)
    GetTxt = r_1.text
    # Defina el regular, el propósito es extraer la información deseada de HTML
    str_title = '"title":"' + Movie_Name + '"'  
    Get_Name = re.search(str_title,GetTxt)
    str_id = '"id":"'+ '[0-9]*'
    Get_Id = re.search(str_id,GetTxt)
    if Get_Name == None and Get_Id == None:
        print("?????????")
    else:
        ID = MidString(str(Get_Id),"id\":\"","'>")
        r_2 = requests.get(Url_DouBan + ID,headers=headers)
        s_1 = etree.HTML(r_2.text)
        #sendero de generación automática #xpath
        #Movie_Called = s_1.xpath('/html/body/div[3]/div[1]/h1/span[1]')
        #print(Movie_Called)
        Movie_Inter = s_1.xpath('//*[@id="link-report"]/span[1]/span/text()[1]')#hombre de Acero        
        if len(Movie_Inter) == 0:
            print("11111")
            Movie_Inter = s_1.xpath('//*[@id="link-report"]/span[1]/text()[1]')#        
            if len(Movie_Inter) == 0:
                print("??????????????????")
            else:
                print(Movie_Inter[0].lstrip())
        else:
            print("22222")
            print(Movie_Inter[0].lstrip())
    



if __name__ == "__main__":
    #SATRT()
    html()