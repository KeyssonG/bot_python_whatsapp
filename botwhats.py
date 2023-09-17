from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com")
time.sleep(60)

mensagem = """ Oii, espero que esteja!
Essa é uma mensagem automática de um projeto que estou
desenvolvendo no WhatsApp usando python
"""

lista_contatos = ["Meu numero", "Grupo teste 1", "grupo teste 2", "Marcos", "grupo teste 3", "grupo teste 4"]

# Enviar a mensagem para o meu número para depois encaminhar 

# clicar na lupa
nav.find_element('xpath', '//*[@id="side"]/div[1]/div/div/button/div[2]/span').click()
# escrever Meu numero
# dar enter

# encaminhar a mensagem para a lista de contatos 



