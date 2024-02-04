from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
from datetime import datetime
from sqlalchemy import false
import numpy as np
from google.oauth2.service_account import Credentials
from google.auth import default
from oauth2client.service_account import ServiceAccountCredentials
from selenium.webdriver.common.by import By
Options = Options()
Options.add_argument('window-size=1280,800')


navegador = webdriver.Chrome(options=Options)

itens = []
   
ultima_pagina = '30'

for i in range(1, int(ultima_pagina)):
    url_pag = 'https://www.pichau.com.br/hardware' + "?page="+ f'{i}'
    navegador.get(url_pag)
    sleep = (2)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


       

    item = 1
    for i in range(36):

        link = navegador.find_element(By.XPATH,f'//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[{item}]/a')
        url = link.get_attribute('href')

        
        item += 1

        itens.append([url])
           


dados = pd.DataFrame(itens, columns=['url'])
print(dados)
ultimo_item = dados.index[-1]
itens2 = []
for i in range(0, int(ultimo_item)):
    
    

    linkurl = dados.iat[i, 0]

    navegador.get(linkurl)

    pagina = navegador.page_source
    
    site = BeautifulSoup(pagina, 'html.parser')
    

    try:
        nomepro = site.find('h1', attrs={'MuiTypography-root'}).text
        preço = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/div[1]').text

        characters = "R$ "
        preço = ''.join( x for x in preço if x not in characters)

        preço = float(preço.replace('.','').replace(',','.'))
        porcentagem = float(preço*15/100)
        valorfinal = preço-porcentagem
        valorfinal = round(valorfinal, 2)
        valorfinal = str(valorfinal).replace('.',',')
        fornecedor = "PICHAU"

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')


        itens2.append([nomepro, valorfinal, linkurl,fornecedor, data_texto])
    except NoSuchElementException:
        break




data_texto2 = data.strftime('%d-%m-%Y')
df = pd.DataFrame(itens2,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
df.to_csv(f'{data_texto2}-{fornecedor}.csv',mode='a',index=False, header=True, encoding='utf-8')
print(df)



    
  ##################################################################################
  #PERIFERICO







itens = []




   
ultima_pagina = '30'

for i in range(1, int(ultima_pagina)):
    url_pag = 'https://www.pichau.com.br/perifericos' + "?page="+ f'{i}'
    navegador.get(url_pag)
    sleep = (2)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


       

    item = 1
    for i in range(36):
        
        link = navegador.find_element(By.XPATH,f'//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[{item}]/a')
        url = link.get_attribute('href')

        
        item += 1

        itens.append([url])
           


dados = pd.DataFrame(itens, columns=['url'])
print(dados)
ultimo_item = dados.index[-1]
itens2 = []
for i in range(0, int(ultimo_item)):
    
    

    linkurl = dados.iat[i, 0]

    navegador.get(linkurl)

    pagina = navegador.page_source
    
    site = BeautifulSoup(pagina, 'html.parser')
    

    try:
        nomepro = site.find('h1', attrs={'MuiTypography-root'}).text
        preço = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/div[1]').text

        characters = "R$ "
        preço = ''.join( x for x in preço if x not in characters)

        preço = float(preço.replace('.','').replace(',','.'))
        porcentagem = float(preço*15/100)
        valorfinal = preço-porcentagem
        valorfinal = round(valorfinal, 2)
        valorfinal = str(valorfinal).replace('.',',')
        fornecedor = "PICHAU"

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')


        itens2.append([nomepro, valorfinal, linkurl,fornecedor, data_texto])
    except NoSuchElementException:
        break




data_texto2 = data.strftime('%d-%m-%Y')
df = pd.DataFrame(itens2,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
df.to_csv(f'{data_texto2}-{fornecedor}.csv',mode='a',index=False, header=False, encoding='utf-8')
print(df)
#############################################################################
#COMPUTADORES

#############################################################################
#MONITORES

itens = []
 
   
ultima_pagina = '5'

for i in range(1, int(ultima_pagina)):
    url_pag = 'https://www.pichau.com.br/monitores' + "?page="+ f'{i}'
    navegador.get(url_pag)
    sleep = (2)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


       

    item = 1
    for i in range(36):

        link = navegador.find_element(By.XPATH,f'//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[{item}]/a')
        url = link.get_attribute('href')

        
        item += 1

        itens.append([url])
           


dados = pd.DataFrame(itens, columns=['url'])
print(dados)
ultimo_item = dados.index[-1]
itens2 = []
for i in range(0, int(ultimo_item)):
    
    

    linkurl = dados.iat[i, 0]

    navegador.get(linkurl)

    pagina = navegador.page_source
    
    site = BeautifulSoup(pagina, 'html.parser')
    

    try:
        nomepro = site.find('h1', attrs={'MuiTypography-root'}).text
        preço = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/div[1]').text

        characters = "R$ "
        preço = ''.join( x for x in preço if x not in characters)

        preço = float(preço.replace('.','').replace(',','.'))
        porcentagem = float(preço*15/100)
        valorfinal = preço-porcentagem
        valorfinal = round(valorfinal, 2)
        valorfinal = str(valorfinal).replace('.',',')
        fornecedor = "PICHAU"

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')


        itens2.append([nomepro, valorfinal, linkurl,fornecedor, data_texto])
    except NoSuchElementException:
        break




data_texto2 = data.strftime('%d-%m-%Y')
df = pd.DataFrame(itens2,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
df.to_csv(f'{data_texto2}-{fornecedor}.csv',mode='a',index=False, header=False, encoding='utf-8')
print(df)
#############################################################################
#CADEIRAS

itens = []

   
ultima_pagina = '6'

for i in range(1, int(ultima_pagina)):
    url_pag = 'https://www.pichau.com.br/cadeiras/gamer' + "?page="+ f'{i}'
    navegador.get(url_pag)
    sleep = (2)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


       

    item = 1
    for i in range(36):

        link = navegador.find_element(By.XPATH,f'//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[{item}]/a')
        url = link.get_attribute('href')

        
        item += 1

        itens.append([url])
           


dados = pd.DataFrame(itens, columns=['url'])
print(dados)
ultimo_item = dados.index[-1]
itens2 = []
for i in range(0, int(ultimo_item)):
    
    

    linkurl = dados.iat[i, 0]

    navegador.get(linkurl)

    pagina = navegador.page_source
    
    site = BeautifulSoup(pagina, 'html.parser')
    

    try:
        nomepro = site.find('h1', attrs={'MuiTypography-root'}).text
        preço = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/div[1]').text

        characters = "R$ "
        preço = ''.join( x for x in preço if x not in characters)

        preço = float(preço.replace('.','').replace(',','.'))
        porcentagem = float(preço*15/100)
        valorfinal = preço-porcentagem
        valorfinal = round(valorfinal, 2)
        valorfinal = str(valorfinal).replace('.',',')
        fornecedor = "PICHAU"

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')


        itens2.append([nomepro, valorfinal, linkurl,fornecedor, data_texto])
    except NoSuchElementException:
        break




data_texto2 = data.strftime('%d-%m-%Y')
df = pd.DataFrame(itens2,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
df.to_csv(f'{data_texto2}-{fornecedor}.csv',mode='a',index=False, header=False, encoding='utf-8')
print(df)
#############################################################################
#REDE WIRELLESS
navegador.get('https://www.pichau.com.br/redes-wireless')



itens = []




   
ultima_pagina = '6'

for i in range(1, int(ultima_pagina)):
    url_pag = 'https://www.pichau.com.br/redes-wireless' + "?page="+ f'{i}'
    navegador.get(url_pag)
    sleep = (2)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


       

    item = 1
    for i in range(36):

        link = navegador.find_element(By.XPATH,f'//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[{item}]/a')
        url = link.get_attribute('href')

        
        item += 1

        itens.append([url])
           


dados = pd.DataFrame(itens, columns=['url'])
print(dados)
ultimo_item = dados.index[-1]
itens2 = []
for i in range(0, int(ultimo_item)):
    
    

    linkurl = dados.iat[i, 0]

    navegador.get(linkurl)

    pagina = navegador.page_source
    
    site = BeautifulSoup(pagina, 'html.parser')
    

    try:
        nomepro = site.find('h1', attrs={'MuiTypography-root'}).text
        preço = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/div[1]').text

        characters = "R$ "
        preço = ''.join( x for x in preço if x not in characters)

        preço = float(preço.replace('.','').replace(',','.'))
        porcentagem = float(preço*15/100)
        valorfinal = preço-porcentagem
        valorfinal = round(valorfinal, 2)
        valorfinal = str(valorfinal).replace('.',',')
        fornecedor = "PICHAU"

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')


        itens2.append([nomepro, valorfinal, linkurl,fornecedor, data_texto])
    except NoSuchElementException:
        break




data_texto2 = data.strftime('%d-%m-%Y')
df = pd.DataFrame(itens2,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
df.to_csv(f'{data_texto2}-{fornecedor}.csv',mode='a',index=False, header=False, encoding='utf-8')
print(df)
#############################################################################
#NOTEBOOK







itens = []



   
ultima_pagina = '3'

for i in range(1, int(ultima_pagina)):
    url_pag = 'https://www.pichau.com.br/notebooks' + "?page="+ f'{i}'
    navegador.get(url_pag)
    sleep = (2)
    pagina = navegador.page_source
    site = BeautifulSoup(pagina, 'html.parser')


       

    item = 1
    for i in range(36):

        link = navegador.find_element(By.XPATH,f'//*[@id="__next"]/main/div[2]/div/div[1]/div[2]/div[{item}]/a')
        url = link.get_attribute('href')

        
        item += 1

        itens.append([url])
           


dados = pd.DataFrame(itens, columns=['url'])
print(dados)
ultimo_item = dados.index[-1]
itens2 = []
for i in range(0, int(ultimo_item)):
    
    

    linkurl = dados.iat[i, 0]

    navegador.get(linkurl)

    pagina = navegador.page_source
    
    site = BeautifulSoup(pagina, 'html.parser')
    

    try:
        nomepro = site.find('h1', attrs={'MuiTypography-root'}).text
        preço = navegador.find_element(By.XPATH, '//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[3]/div[2]/div[1]').text

        characters = "R$ "
        preço = ''.join( x for x in preço if x not in characters)

        preço = float(preço.replace('.','').replace(',','.'))
        porcentagem = float(preço*15/100)
        valorfinal = preço-porcentagem
        valorfinal = round(valorfinal, 2)
        valorfinal = str(valorfinal).replace('.',',')
        fornecedor = "PICHAU"

        data = datetime.now()
        data_texto = data.strftime('%d/%m/%Y %H:%M')


        itens2.append([nomepro, valorfinal, linkurl,fornecedor, data_texto])
    except NoSuchElementException:
        break




data_texto2 = data.strftime('%d-%m-%Y')
df = pd.DataFrame(itens2,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
df.to_csv(f'{data_texto2}-{fornecedor}.csv',mode='a',index=False, header=False, encoding='utf-8')
print(df)


















