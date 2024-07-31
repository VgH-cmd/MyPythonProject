# IMPORTANT!!! IMPORTANTE!!!
# Para o funcionamento correto do codigo utilize as bibliotecas pyautogui e time
# For the code to work correctly, use the pyautogui and time libraries


# Passo a passo do projeto / step by step 
# Passo 1: Entrar no sistema da empresa / join the company system
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui as pi
import time 

# pyautogui.write -> escrever um texto / write a text
# pyautogui.press -> apertar 1 tecla / tap 1 key
# pyautogui.click -> clicar em algum lugar da tela / click on someplace on the screnn
# pyautogui.hotkey -> combinação de tecla / key combination

pi.PAUSE = 0.6

# abrir o navegador (chrome) / open browser

pi.press('win')
pi.write('Edge')
pi.press('enter')

# entrar no link / join link
pi.click(x=338, y=77)
pi.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pi.press('enter')
time.sleep(3)

# Passo 2: Fazer login / make login
# selecionar o campo de email / select the email field
pi.click(x=693, y=450)
pi.write('emailteste@gmail.com')
pi.press('tab')
pi.write('teste2123')
pi.click(x=911, y=653)
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar / import data base to register
import pandas as pd 

tabela = pd.read_csv('produtos.csv')

print(tabela)

# Passo 4: Cadastrar um produto / register the product

for linha in tabela.index: 
    # clicar no campo de código / click on code field
    pi.click(x=602, y=305)
    # pegar da tabela o valor do campo que a gente quer preencher / get from the table the value of the camp that we have to fill
    pi.write(str(tabela.loc[linha, 'codigo']))
    # preencher o campo / fill the camp
    
    # passar para o próximo campo / pass to the next field
    pi.press('tab')
    pi.write(str(tabela.loc[linha, 'marca']))
    pi.press('tab')
    pi.write(str(tabela.loc[linha, 'tipo']))
    pi.press('tab')

    pi.write(str(tabela.loc[linha, 'categoria']))

    pi.press('tab')
    pi.write(str(tabela.loc[linha, 'preco_unitario']))
    pi.press('tab')
    pi.write(str(tabela.loc[linha, 'custo']))
    pi.press('tab')
    obs = tabela.loc[linha, 'obs']
    
    if not pd.isna(obs):
        pi.write(str(tabela.loc[linha, 'obs']))
    pi.press('tab')
    pi.press('enter')

    pi.scroll(5000)
