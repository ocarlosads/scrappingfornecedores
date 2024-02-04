
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
Options.add_argument('window-size=1280,')


navegador = webdriver.Chrome(options=Options)

navegador.get('https://empresas.americanas.com.br/categoria/informatica-e-acessorios/perifericos/f/loja-1p%7CAmericanas?sortBy=higherPriceRelevance&limit=24&offset=0')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')

item = 1
numero = navegador.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]/span').text

num1=int(numero[0:3])
print(num1)   

navegador.get(f'https://empresas.americanas.com.br/categoria/informatica-e-acessorios/perifericos/f/loja-1p%7CAmericanas?sortBy=higherPriceRelevance&limit={num1}&offset=0')

pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')

sleep(3)
for i in range(num1):
    
    
    nome = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[2]/div[2]/h3').text
    preço = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[3]/span[1]').text
    link = navegador.find_element(By.XPATH,f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a')
    url = link.get_attribute('href')

    nome_site = 'AMERICANAS'

    data = datetime.now()
    data_texto = data.strftime('%d/%m/%Y %H:%M')
    
    characters = "R$ "
    preço = ''.join( x for x in preço if x not in characters)
        


    itens.append([nome, preço, url, nome_site, data_texto])
        
    print(nome)
    
    item +=1


df = pd.DataFrame(itens,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
index_names = df[df['Preço'] == 'Ops!Jávendemostodooestoque.'].index
df.drop(index_names, inplace = True)



data_texto2 = data.strftime('%d-%m-%Y')

   


df.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=True, encoding='utf-8')

print(df) 


#########################################################################
#monitores
navegador.get('https://empresas.americanas.com.br/categoria/informatica-e-acessorios/monitor/f/loja-1p%7CAmericanas?sortBy=lowerPriceRelevance&limit=24&offset=0')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')

item = 1
numero = navegador.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]/span').text

num1=int(numero[0:3])
print(num1)   

navegador.get(f'https://empresas.americanas.com.br/categoria/informatica-e-acessorios/monitor/f/loja-1p%7CAmericanas?sortBy=lowerPriceRelevance&limit={num1}&offset=0')

pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')


for i in range(num1):
    
    
    nome = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[2]/div[2]/h3').text
    preço = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[3]/span[1]').text
    link = navegador.find_element(By.XPATH,f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a')
    url = link.get_attribute('href')

    nome_site = 'AMERICANAS'

    data = datetime.now()
    data_texto = data.strftime('%d/%m/%Y %H:%M')
    
    characters = "R$ "
    preço = ''.join( x for x in preço if x not in characters)
        


    itens.append([nome, preço, url, nome_site, data_texto])
        
    print(nome)
    
    item +=1


df = pd.DataFrame(itens,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
index_names = df[df['Preço'] == 'Ops!Jávendemostodooestoque.'].index
df.drop(index_names, inplace = True)



data_texto2 = data.strftime('%d-%m-%Y')

   


df.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=False, encoding='utf-8')

print(df) 
##############################################################################
#teclados
navegador.get('https://empresas.americanas.com.br/categoria/informatica-e-acessorios/perifericos/teclado/f/loja-1p%7CAmericanas?limit=24&offset=0')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')

item = 1
numero = navegador.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]/span').text

num1=int(numero[0:3])
print(num1)   

navegador.get(f'https://empresas.americanas.com.br/categoria/informatica-e-acessorios/perifericos/teclado/f/loja-1p%7CAmericanas?limit={num1}&offset=0')

pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')


for i in range(num1):
    
    
    nome = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[2]/div[2]/h3').text
    preço = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[3]/span[1]').text
    link = navegador.find_element(By.XPATH,f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a')
    url = link.get_attribute('href')

    nome_site = 'AMERICANAS'

    data = datetime.now()
    data_texto = data.strftime('%d/%m/%Y %H:%M')
    
    characters = "R$ "
    preço = ''.join( x for x in preço if x not in characters)
        


    itens.append([nome, preço, url, nome_site, data_texto])
        
    print(nome)
    
    item +=1


df = pd.DataFrame(itens,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
index_names = df[df['Preço'] == 'Ops!Jávendemostodooestoque.'].index
df.drop(index_names, inplace = True)



data_texto2 = data.strftime('%d-%m-%Y')

   


df.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=False, encoding='utf-8')

print(df) 
##########################################################
#cabos
navegador.get('https://empresas.americanas.com.br/categoria/informatica-e-acessorios/componentes/cabos-e-adaptadores/f/loja-1p%7CAmericanas?sortBy=lowerPriceRelevance&limit=24&offset=0')


itens = []


pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')

item = 1
sleep(2)
numero = navegador.find_element(By.XPATH,'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[2]/span').text

num1=int(numero[0:3])
print(num1)   

navegador.get(f'https://empresas.americanas.com.br/categoria/informatica-e-acessorios/componentes/cabos-e-adaptadores/f/loja-1p%7CAmericanas?sortBy=lowerPriceRelevance&limit={num1}&offset=0')

pagina = navegador.page_source

site = BeautifulSoup(pagina, 'html.parser')


for i in range(num1):
    
    
    nome = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[2]/div[2]/h3').text
    preço = navegador.find_element(By.XPATH, f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a/div[3]/span[1]').text
    link = navegador.find_element(By.XPATH,f'//*[@id="rsyswpsdk"]/div/main/div/div[3]/div[3]/div[{item}]/div/div/a')
    url = link.get_attribute('href')

    nome_site = 'AMERICANAS'

    data = datetime.now()
    data_texto = data.strftime('%d/%m/%Y %H:%M')
    
    characters = "R$ "
    preço = ''.join( x for x in preço if x not in characters)
        


    itens.append([nome, preço, url, nome_site, data_texto])
        
    print(nome)
    
    item +=1


df = pd.DataFrame(itens,columns=['Nome', 'Preço','link','Fornecedor', 'Data'])
index_names = df[df['Preço'] == 'Ops!Jávendemostodooestoque.'].index
df.drop(index_names, inplace = True)



data_texto2 = data.strftime('%d-%m-%Y')

   


df.to_csv(f'{data_texto2}-{nome_site}.csv',mode='a',index=False, header=False, encoding='utf-8')

print(df) 