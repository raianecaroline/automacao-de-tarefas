import pyautogui
import time


pyautogui.PAUSE = 1

# Passo 1 - Entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

pyautogui.press("enter")
time.sleep(3)


# Passo 2 - Fazer login
pyautogui.click(x=644, y=362)

pyautogui.write("seuemail@gmail.com")
pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.click(x=695, y=513)
time.sleep(2)


# Passo 3 - Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)


# Passo 4 - Cadastrar um produto
for linha in tabela.index:
    pyautogui.click(x=434, y=250)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
   
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(5000)