from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import date
from PySimpleGUI import PySimpleGUI as sg

# acessar o site https://www.guiadoscuriosos.com.br/curiosidade_dia_cat/curiosidade-do-dia
driver = webdriver.Chrome()
driver.get('https://www.guiadoscuriosos.com.br/curiosidade_dia_cat/curiosidade-do-dia')

# extrair curiosidade do dia
# xPath //tag[@atributo='valor']
curiosidade = driver.find_elements(By.XPATH,"//*[@id]/div[2]/div/p")

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Data: '), sg.Text(data_em_texto)],
    [sg.Text('Curiosidade: '), sg.Multiline(curiosidade[0].text , size = (50))]
]

# Janela
janela = sg.Window('Curiosidade do dia', layout)

while True:
    eventos = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

# como entregar para o cliente