from enlace import *
import time
import numpy as np
from functions import *

serialName = "COM6"

def main():
    try:
        print("Iniciou Main")
        com1 = enlace(serialName)

        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        time.sleep(.2)
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Abriu a comunicação\n")

        # =================================================================================================================================
        # Escolhe o numero de comandos
        rand_numero = random_numero()
        # Arrays a serem transmitiddos
        comandos = chama_comandos(rand_numero)

        # Cria protocolo para saber quando acabou
        protocolo = b'\x88\x99'

        print("Serao {} comandos!\n".format(rand_numero))

        # Byte de sacrificio
        print('='*100)
        print("\nByte de Sacrificio\n")
        com1.sendData(b'00')
        comando = bytearray()
        
        # Envia os comandos
        time.sleep(0.2)
        for i in range(0, rand_numero):
            comando += bytearray(comandos[i]) + b'\x22'

        com1.sendData(bytearray(comando))
        # Tamanho enviado
        txSize = com1.tx.getStatus()
        # print('enviou = {} bytes\n' .format(txSize))

        # =================================================================================================================================
        # Inicia espera da resposta

        start_time = time.time()

        # While esperando resposta
        while True:
            rxBufferLen = com1.rx.getBufferLen()
            if rxBufferLen != 0:
                respostaServer = com1.rx.getAllBuffer()
                respostaServer = int.from_bytes(respostaServer)
                break
            else:
                # Envia protocolo
                time.sleep(0.18)
                com1.sendData(bytearray(protocolo))
            
            if time.time() - start_time >= 5:
                print('='*100)
                print("\n\033[91mTimeOut: Resposta demorou mais que 5 segundos\033[0m")
                print("Resposta esperada: {}\n".format(rand_numero))
                break

        try:
            time.sleep(0.2)
            print('='*100)
            if respostaServer == rand_numero:
                print("\n\033[92mComunicacao BEM SUCEDIDA!!\033[0m")
            else:
                print("\n\033[91mErro na Comunicacao!\033[0m")
                print("Resposta esperada: {}".format(rand_numero))
            print("Resposta do Server: {} comandos\n".format(respostaServer))
            print('='*100)
        except:
            pass

        # Encerra comunicação
        print("\n-------------------------")
        print("Comunicação encerrada")
        print("-------------------------\n")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        
    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
