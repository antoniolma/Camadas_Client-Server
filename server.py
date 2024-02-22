from enlace import *
import time

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
        if rxBuffer == b'\x88\x99':
            break
        else:
            contador += rxBuffer.count(b'\x22')
            comandos = rxBuffer.rsplit(b'\x22')

resposta = bytes([contador])
# Caso de erro proposital hard coded
# resposta = bytes([contador + 5])
com1.sendData(bytearray(resposta))

print('\033[94mResposta enviada: {}\033[0m' .format(resposta))
print("Comandos recebidos:")

for comando in comandos[:len(comandos)-1]:
    print(comando)