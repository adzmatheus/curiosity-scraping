from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import date
# from PySimpleGUI import PySimpleGUI as sg
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


servico = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless=new")
browser = webdriver.Chrome(options=chrome_options)

# acessar o site https://www.guiadoscuriosos.com.br/curiosidade_dia_cat/curiosidade-do-dia
browser.get('https://www.guiadoscuriosos.com.br/curiosidade_dia_cat/curiosidade-do-dia')

# extrair curiosidade do dia
# xPath //tag[@atributo='valor']
curiosidade = browser.find_elements(By.XPATH,"//*[@id]/div[2]/div/p")

data_atual = date.today()
data_em_texto = data_atual.strftime('%d/%m/%Y')

# # Layout
# sg.theme('Reddit')
# layout = [
#     [sg.Text('Data: '), sg.Text(data_em_texto)],
#     [sg.Text('Curiosidade: '), sg.Multiline(curiosidade[0].text , size = (80))]
# ]

# # Janela
# janela = sg.Window('Curiosidade do dia', layout)

# while True:
#     eventos = janela.read()
#     if eventos == sg.WINDOW_CLOSED:
#         break

with open("README.md", "w") as description:

    descricao = ['# curiosity-scraping', '![Budget](./execucao.png)', data_em_texto, '-' , curiosidade[0].text]

    for line in descricao:
        description.write(line + '\n')
