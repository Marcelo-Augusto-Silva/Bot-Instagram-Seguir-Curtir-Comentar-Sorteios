from selenium import webdriver
import pyautogui
from time import sleep


#dados para logar
print(' 1 = SEGUIR '
      '\n 2 = CURTIR FOTOS E COMENTAR'
      '\n 3 = SORTEIO'
      '\n 4 = COLETAR PERFILS ')

escolha = int(input('Escolha: '))
email = str(input('Digite o email: '))
senha = str(input('Digite a senha: '))
if escolha == 1:
    perfil = str(input('Perfil para começar a seguir: '))
elif escolha == 2:
    perfil = str(input('Perfil para curtir e comentar: '))
    comentario = str(input('O que vocé deseja comentar ?? '))
elif escolha == 3:
    perfil = str(input('Perfil do sorteio: '))
    quantidade = int(input('Quantas vezes voê quer comentar ??'))
#entrando no instagram
navegador = webdriver.Chrome(executable_path=r'chromedriver.exe') # localizar o executavel do selenium
navegador.get('https://www.instagram.com/')
sleep(1)
navegador.find_element_by_name('username').click()
pyautogui.write(email)
# pyautogui.write('marc)
navegador.find_element_by_name('password').click()
pyautogui.write(senha)
# pyautogui.write('gu281201')
sleep(2)
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
sleep(3)

#logado no instagram
while True:
    sleep(8)
    #pergunta de notificação
    try:
        navegador.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
    except:
        print('Não foi')

    #clicar para ir para a pagina inicial
    pagina_inicial = navegador.find_elements_by_xpath('//div[@class="Fifk5"]')
    pagina_inicial[0].click()
    sleep(0.4)

    try:
        navegador.find_element_by_xpath('//button[@class="aOOlW   HoLwm "]').click()
    except:
        print('Não foi')



    if escolha == 1:

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
        perfis_coletados = navegador.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
        perfil = []
        for c in range(0,10):
            itens[c].click()
            sleep(1.5)
            n = perfis_coletados[c].text
            perfil.append(n)
            print(n)
        print(perfil)
        continuar = str(input('Deseja executar outra ação ?? [S/N] ')).upper()
        if continuar[0] == 'N':
            navegador.quit()
            break
        else:
            print(' 1 = SEGUIR '
                  '\n 2 = CURTIR FOTOS E COMENTAR'
                  '\n 3 = SORTEIO'
                  '\n 4 = COLETAR PERFILS ')

            escolha = int(input('Escolha: '))
            if escolha == 1:
                perfil = str(input('Perfil para começar a seguir: '))
            elif escolha == 2:
                perfil = str(input('Perfil para curtir e comentar: '))
                comentario = str(input('O que vocé deseja comentar ?? '))
            elif escolha == 3:
                perfil = str(input('Perfil do sorteio: '))
            sleep(2)
            #apertar no X para sair
            sair = navegador.find_elements_by_xpath('//div[@class="QBdPU "]')
            sair[1].click()
            continue


    if escolha == 2:
        sleep(4)
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
        pyautogui.write(perfil)
        sleep(2)
        pyautogui.press('enter')
        pyautogui.press('enter')
        sleep(4)
        fotos = navegador.find_elements_by_xpath('//div[@class="_9AhH0"]')

        for c in range(0,3):
            try:
                fotos[c].click()
                sleep(4)
                #curtir
                curtir = navegador.find_elements_by_xpath('//div[@class="QBdPU "]')
                curtir[2].click()
                sleep(1)
                #comentar
                curtir[3].click()
                pyautogui.write(comentario)
                pyautogui.press('enter')
                sleep(1.7)
                #sair
                curtir[-1].click()
                sleep(1)

            except:
                print('ALgo deu errado')

        continuar = str(input('Deseja executar outra ação ?? [S/N] ')).upper()
        if continuar[0] == 'N':
            navegador.quit()
            break
        else:
            print(' 1 = SEGUIR '
                  '\n 2 = CURTIR FOTOS E COMENTAR'
                  '\n 3 = SORTEIO'
                  '\n 4 = COLETAR PERFILS ')

            escolha = int(input('Escolha: '))
            if escolha == 1:
                perfil = str(input('Perfil para começar a seguir: '))
            elif escolha == 2:
                perfil = str(input('Perfil para curtir e comentar: '))
                comentario = str(input('O que vocé deseja comentar ?? '))
            elif escolha == 3:
                perfil = str(input('Perfil do sorteio: '))
            sleep(5)

            continue

    if escolha == 3:
        arquivo = open('perfil.txt')
        # clicar na barra de pesquisa
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
        sleep(5)
        # digitar na barra de pesquisa
        pyautogui.write(perfil)
        sleep(2)
        pyautogui.press('enter')
        pyautogui.press('enter')
        sleep(4)



        # apertar na foto para comentar
        fotos = navegador.find_elements_by_xpath('//div[@class="_9AhH0"]')
        fotos[1].click()
        sleep(2)
        foto_aberta = navegador.find_elements_by_xpath('//div[@class="QBdPU "]')
        cont = controle = 0
        for c in arquivo:
            if controle == quantidade:
                continuarr = str(input('Deseja continuar comentando ?? [S/N] ')).upper()
                if continuarr[0] == 'N':
                    navegador.quit()
                    break
                else:
                    quantidade = int(input('Quer comentar mais quantas vezes ??'))
                    controle = 0

            sleep(2)
            if cont == 9:
                sleep(20)
                cont = 0
            foto_aberta[3].click()
            sleep(1)
            pyautogui.write('@'+c)
            sleep(2)
            pyautogui.press('enter')
            pyautogui.press('enter')
            try:
                foto_aberta[3].click()
                sleep(1)
                pyautogui.hotkey('ctrl', 'a', 'delete')
                sleep(2)
                cont += 1
                controle += 1

            except:
                print('nao foi')
                controle +=1

        continuar = str(input('Deseja executar outra ação ?? [S/N] ')).upper().strip()
        if continuar[0] == 'N':
            navegador.quit()
            break
        else:
            print(' 1 = SEGUIR '
                  '\n 2 = CURTIR FOTOS E COMENTAR'
                  '\n 3 = SORTEIO'
                  '\n 4 = COLETAR PERFILS ')

            escolha = int(input('Escolha: '))
            if escolha == 1:
                perfil = str(input('Perfil para começar a seguir: '))
            elif escolha == 2:
                perfil = str(input('Perfil para curtir e comentar: '))
                comentario = str(input('O que vocé deseja comentar ?? '))
            elif escolha == 3:
                perfil = str(input('Perfil do sorteio: '))
            sleep(5)
            # apertar no X para sair
            foto_aberta = navegador.find_elements_by_xpath('//div[@class="QBdPU "]')
            foto_aberta[-1].click()

            continue


    if escolha == 4:
        arquivo = open('perfil.txt','a')
        # clicar na barra de pesquisa
        navegador.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[1]').click()
        sleep(5)
        # digitar na barra de pesquisa
        pyautogui.write('nike')
        sleep(5)
        pyautogui.press('enter')
        pyautogui.press('enter')
        sleep(2)
        while True:
            try:
                #coletar perfil
                navegador.find_element_by_xpath('//a[@class="-nal3 "]').click()
                sleep(2)
                itens = navegador.find_elements_by_xpath('//div[@class="                     Igw0E   rBNOH          YBx95   ybXk5    _4EzTm                      soMvl                                                                                        "]')
                perfis_coletados = navegador.find_elements_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]')
                for c in range(0, 11):
                    sleep(1)
                    n = perfis_coletados[c].text
                    arquivo.write(n)
                    arquivo.write('\n')
                    print(n)
                sleep(2)
                pyautogui.press('f5')
                escolha = str(input('Quer continuar?? ')).strip()
                if escolha[0].upper() == 'N':
                    continuar = str(input('Deseja executar outra ação ?? [S/N] ')).upper().strip()
                    if continuar[0] == 'N':
                        navegador.quit()
                        break
                    else:
                        print(' 1 = SEGUIR '
                              '\n 2 = CURTIR FOTOS E COMENTAR'
                              '\n 3 = SORTEIO'
                              '\n 4 = COLETAR PERFILS ')

                        escolha = int(input('Escolha: '))
                        if escolha == 1:
                            perfil = str(input('Perfil para começar a seguir: '))
                        elif escolha == 2:
                            perfil = str(input('Perfil para curtir e comentar: '))
                            comentario = str(input('O que vocé deseja comentar ?? '))
                        elif escolha == 3:
                            perfil = str(input('Perfil do sorteio: '))
                        break
                else:
                    continue
            except:
                print('deu ruim')
                escolha = str(input('Quer continuar?? '))
                if escolha[0].upper() == 'N':
                    break
                continue
