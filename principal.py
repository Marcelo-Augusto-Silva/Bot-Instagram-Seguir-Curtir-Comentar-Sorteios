from selenium import webdriver
import pyautogui
from time import sleep


#dados para logar

email = str(input('Digite o email: '))
senha = str(input('Digite a senha: '))
perfil = str(input('Perfil para começar a seguir: '))
#entrando no instagram
navegador = webdriver.Chrome(executable_path=r'chromedriver.exe') # localizar o executavel do selenium
navegador.get('https://www.instagram.com/')
sleep(10)
navegador.find_element_by_name('username').click()
pyautogui.write(email)
navegador.find_element_by_name('password').click()
pyautogui.write(senha)
sleep(2)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
sleep(10)

#começando
#clicar na barra de pesquisa
navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
sleep(5)
#digitar na barra de pesquisa
pyautogui.write(perfil)
sleep(5)
pyautogui.press('enter')
pyautogui.press('enter')
sleep(5)

#seguir os usuarios
navegador.find_element_by_xpath('//a[@class="-nal3 "]').click()
sleep(5)
itens = navegador.find_elements_by_xpath('//div[@class="                     Igw0E   rBNOH          YBx95   ybXk5    _4EzTm                      soMvl                                                                                        "]')
for c in range(0,10):
    itens[c].click()
    sleep(1.5)
