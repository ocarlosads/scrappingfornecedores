
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from datetime import datetime

import numpy as np
import gspread

from google.oauth2.service_account import Credentials
from google.auth import default
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.by import By
Options = Options()
Options.add_argument('window-size=400,800')


navegador = webdriver.Chrome(options=Options)
itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')


navegador.get('https://www.kabum.com.br/hardware?&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched&page_size=100&')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')





ultima_pagina = '43'

for i in range(2, int(ultima_pagina)):
    url_pag = 'https://www.kabum.com.br/hardware?&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched&page_size=100&' + "page_number="+ f'{i}'
    navegador.get(url_pag)
    sleep = (5)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


    anuncios = site.findAll('div', attrs={'productCard'})

 
    for anuncio in anuncios:

        nome = anuncio.find('span', attrs={'nameCard'}).text
        
        
        try:
        
            preco = anuncio.find('span', attrs={'priceCard'}).text
            characters = "R$ "
            preco = ''.join( x for x in preco if x not in characters)
            
            print(preco)
            num_preco = preco[2:]
            sleep(2)
        except:
            num_preco ='0'
        
        url_anuncio = anuncio.find('a').get('href')
        link = 'https://www.kabum.com.br'+url_anuncio

        nome_site = 'KABUM'

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')
        
        


        itens.append([nome, preco, link, nome_site, data_texto])
        
        


        
dados = pd.DataFrame(itens,columns=['Nome', 'Preço','link','fornecedor', 'Data'])
index_names = dados[dados['Preço'] == ' ---'].index
dados.drop(index_names, inplace = True)

data_texto2 = data.strftime('%d-%m-%Y')

   


dados.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=True, encoding='utf-8')

print(dados) 

###################################################################################

navegador.get('https://www.kabum.com.br/perifericos?page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')





ultima_pagina = '43'

for i in range(2, int(ultima_pagina)):
    url_pag = 'https://www.kabum.com.br/perifericos?page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched&' + "page_number="+ f'{i}'
    navegador.get(url_pag)
    sleep = (5)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


    anuncios = site.findAll('div', attrs={'productCard'})

 
    for anuncio in anuncios:

        nome = anuncio.find('span', attrs={'nameCard'}).text
        
        
        try:
        
            preco = anuncio.find('span', attrs={'priceCard'}).text
            characters = "R$ "
            preco = ''.join( x for x in preco if x not in characters)
            
            print(preco)
            num_preco = preco[2:]
            sleep(2)
        except:
            num_preco ='0'
        
        url_anuncio = anuncio.find('a').get('href')
        link = 'https://www.kabum.com.br'+url_anuncio

        nome_site = 'KABUM'

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')
        
        


        itens.append([nome, preco, link, nome_site, data_texto])
        
        


        
dados = pd.DataFrame(itens,columns=['Nome', 'Preço','link','fornecedor', 'Data'])
index_names = dados[dados['Preço'] == ' ---'].index
dados.drop(index_names, inplace = True)

data_texto2 = data.strftime('%d-%m-%Y')

   


dados.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=False, encoding='utf-8')

print(dados) 

###############################################################################


navegador.get('https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?&page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched&')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')





ultima_pagina = '5'

for i in range(2, int(ultima_pagina)):
    url_pag = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?&page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched&' + "page_number="+ f'{i}'
    navegador.get(url_pag)
    sleep = (5)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


    anuncios = site.findAll('div', attrs={'productCard'})

 
    for anuncio in anuncios:
        nome = anuncio.find('span', attrs={'nameCard'}).text
        try:
            
            preco = anuncio.find('span', attrs={'priceCard'}).text
            characters = "R$ "
            preco = ''.join( x for x in preco if x not in characters)
            
            print(preco)
            num_preco = preco[2:]
            sleep(2)
        except:
            num_preco ='0'
        
        url_anuncio = anuncio.find('a').get('href')
        link = 'https://www.kabum.com.br'+url_anuncio

        nome_site = 'KABUM'

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')
        
        


        itens.append([nome, preco, link, nome_site, data_texto])
        
        


        
dados = pd.DataFrame(itens,columns=['Nome', 'Preço','link','fornecedor', 'Data'])
index_names = dados[dados['Preço'] == ' ---'].index
dados.drop(index_names, inplace = True)

data_texto2 = data.strftime('%d-%m-%Y')

   


dados.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=False, encoding='utf-8')

print(dados) 

##############################################################################



navegador.get('https://www.kabum.com.br/computadores?&page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')





ultima_pagina = '5'

for i in range(2, int(ultima_pagina)):
    url_pag = 'https://www.kabum.com.br/computadores?&page_size=100&facet_filters=eyJrYWJ1bV9wcm9kdWN0IjpbInRydWUiXX0=&sort=most_searched' + "page_number="+ f'{i}'
    navegador.get(url_pag)
    sleep = (5)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


    anuncios = site.findAll('div', attrs={'productCard'})

 
    for anuncio in anuncios:

        nome = anuncio.find('span', attrs={'nameCard'}).text
        
        
        try:
        
            preco = anuncio.find('span', attrs={'priceCard'}).text
            characters = "R$ "
            preco = ''.join( x for x in preco if x not in characters)
            
            print(preco)
            num_preco = preco[2:]
            sleep(2)
        except:
            num_preco ='0'
        
        url_anuncio = anuncio.find('a').get('href')
        link = 'https://www.kabum.com.br'+url_anuncio

        nome_site = 'KABUM'

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')
        
        


        itens.append([nome, preco, link, nome_site, data_texto])
        
        


        
dados = pd.DataFrame(itens,columns=['Nome', 'Preço','link','fornecedor', 'Data'])
index_names = dados[dados['Preço'] == ' ---'].index
dados.drop(index_names, inplace = True)


data_texto2 = data.strftime('%d-%m-%Y')

   


dados.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=False, encoding='utf-8')

print(dados) 
