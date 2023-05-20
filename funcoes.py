from uteis import meu_email, meu_telegram
from uteis.meu_bd import select, con_banco
from uteis import meu_selenium
from uteis.meu_selenium import conf_selenium, click_, input_, texto_
from time import sleep
import os 

help(meu_selenium)
sleep(12000)
#meu_email.email_simples('gsantos@paranoa.com.br','teste')
#
#meu_email.email_zip('gsabino5667@gmail.com','teste','teste')
#
#meu_email.email_imagem('gsantos@paranoa.com.br','teste',r'C:\Users\gsantos\Desktop\Estudos','teste.png')

#ursor = con_banco('synchdb.datawake.com.br', 'datawake_painel', 'rpa_datawake', 'C@adead0')
#elect = select(cursor,'[dbo].[reclamacao_cliente]')
#rint(select)

dir_atu = os.getcwd()
navegador = conf_selenium(dir_atu, 'https://www.selenium.dev/')

click_(navegador,'//*[@id="main_navbar"]/ul/li[3]/a')
click_(navegador, 'navbarDropdown')
click_(navegador, '//*[@id="docsearch"]/button/span[1]/span')
sleep(1)
input_(navegador, 'docsearch-input', 'teste')
sleep(2)
txt = texto_(navegador, '/html/body/div[2]/div/div/div/section[1]')
print(txt)
print('1')
sleep(1200)
#navegador.find_element(By.XPATH, '//*[@id="main_navbar"]/ul/li[3]/a').click()


