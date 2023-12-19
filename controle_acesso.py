#Importação dos módulos
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep

#Configuração do setmode da GPIO
GPIO.setmode(GPIO.BCM)

#Configuração das GPIO
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

#Desabilita os avisos
GPIO.setwarnings(False)

#Inicialização do objeto
leitor = SimpleMFRC522()

#Inicialização das GPIO em nível lógico baixo
GPIO.output(26, False)
GPIO.output(19, False)

#Loop infinito para leitura da tag, retorno da ID e concessão de acesso (liga o led correspondente)
while True:
    print("Aproxime a tag do leitor para ler")
    id, texto = leitor.read()
    print("ID: {}\n".format(id))
    if str(id) == "427707964172":
        print("Acesso Concedido")
        GPIO.output(26, True)
    else:
        print("Acesso Negado")
        GPIO.output(19, True)
    sleep(3)
    GPIO.output(26, False)
    GPIO.output(19, False)