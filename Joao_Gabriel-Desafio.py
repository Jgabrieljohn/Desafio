# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 21:04:25 2017

@author: João Gabriel John
"""

from selenium import webdriver

 #Inclusão das credenciais do Twitter
user = input("Digite o Usuário do Twitter")
password = input("Digite o Password do Twitter")
driver = webdriver.Chrome()
def rastreartwitter(htmltwitter):    
    driver.get(htmltwitter)
    #Teste para verificar se página existe
    try:
        elem = driver.find_element_by_name('session[username_or_email]')
    except:
        print('Página não encontrada')
        exit
    #Busca a Tag referente as credenciais
    elem = driver.find_element_by_name('session[username_or_email]')
    elem.clear()
    elem.send_keys(user)
    elem = driver.find_element_by_name("session[password]")
    elem.clear()
    elem.send_keys(password)
    elem.submit()
    #Busca a Tag do Twitter referente aos Twits
    elements = driver.find_elements_by_class_name('TweetTextSize')
    #Verifica se existe twit
    if elements == []:
        #verifica se entrou na página de falha nas credenciais
        elem = driver.find_element_by_class_name('message-text')
        if elem != []:
            print('Credenciais Inválidas. Por favor, tente novamente')
            exit
        else:
            print('Nenhum twit encontrado')
    tweets = list()
    #Listagens de todos os twits como texto
    for value in elements:
        tweets.append(value.text)    
    return tweets
def rastrearsite(htmlsite):  
    driver.get(htmlsite)
    #Verifica se o site existe e se os campos com os conteúdos existe    
    try:
        elements = driver.find_elements_by_class_name('post-content__title')
    except:
        print('Página inválida')
        exit
    pub = list()
    for value in elements:
        pub.append(value.text)
   
    return pub
class Teste:
    def __init__(self):
        pass
    def verificartwites(self,htmltwitter,htmlsite):
        pub = rastrearsite(htmlsite)
        tweets = rastreartwitter(htmltwitter)        
        count = 0
        twitada = list()
        ntwitada = list()
        controle = 0
        #comparação de cada texto da página com os valores twitados
        for titulopublicado in pub:
            controle = 0
            for titulotweet in tweets:
                #se o título da publicação for semelhante (ou menor) que o twit
                #armazenar esse valor no twitado, 
                #se não adicionar no não twitado
                if titulopublicado in titulotweet:
                    controle = 1
                    count += 1
            if controle == 1:
                twitada.append(titulopublicado)
            else:
                ntwitada.append(titulopublicado)
        print("--------------------------------------------------")
        print("%d das últimas %d publicações foram twitadas" % (count, len(pub)))
        print("--------------------------------------------------")
        print("Twitada: \n")
        for tw in twitada:
            print(tw)
        print("--------------------------------------------------")
        print("Não twitada: \n")
        for ntw in ntwitada:
            print(ntw)
objeto = Teste()
htmltwitter = "https://twitter.com/SocialBaseBR"
htmlsite = "https://www.culturacolaborativa.com/"
resultado = objeto.verificartwites(htmltwitter, htmlsite)
driver.quit()
input()
