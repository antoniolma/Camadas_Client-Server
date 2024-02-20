from enlace import *
import time
import numpy as np

serialName = "COM8"
contador = 0

com1 = enlace(serialName)
# Ativa comunicacao. Inicia os threads e a comunicação seiral 
com1.enable()

# Recebe byte de sacrifício e limpa o rxBuffer
print("esperando 1 byte de sacrifício")
rxBuffer, nRx = com1.getData(1)
com1.rx.clearBuffer()
time.sleep(.1)

while True:
    txLen = com1.rx.getBufferLen()
    rxBuffer, nRx = com1.getData(txLen)
    if nRx != 0:
        print(f"rxBuffer: {rxBuffer}")
        contador += 1
        print("Comando recebido!")
        print(f"contador: {contador}")
        if rxBuffer == b'\x88\x99':
            break

resposta = bytes([contador - 1])
# Caso de erro proposital hard coded
# resposta = bytes([contador + 5])
com1.sendData(bytearray(resposta))
print('Resposta enviada: {}' .format(resposta))