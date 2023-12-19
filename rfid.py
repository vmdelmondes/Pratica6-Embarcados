#Importação dos módulos
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

#Desabilita warnings
GPIO.setwarnings(False)

#Inicialização do objeto
leitor = SimpleMFRC522()

#Texto a ser escrito
texto = "8149"

#Comando para o usuário aproximar a tag
print("Aproxime a tag do leitor para gravar")

#Escrita do texto
leitor.write(texto)

#Feedback de escrita concluída
print("Concluído")

#Comando para o usuário aproximar a tag
print("Aproxime a tag do leitor para ler")

#Loop infinito de leitura e print da ID e do texto excrito
while True:
    id, texto = leitor.read()
    print("ID: {}\n: {}".format(id, texto))
    sleep(3)

