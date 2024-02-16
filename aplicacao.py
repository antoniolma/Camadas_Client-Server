#####################################################
# Camada Física da Computação
#Carareto
#11/08/2022
#Aplicação
####################################################


#esta é a camada superior, de aplicação do seu software de comunicação serial UART.
#para acompanhar a execução e identificar erros, construa prints ao longo do código! 


from enlace import *
import time
import numpy as np

# voce deverá descomentar e configurar a porta com através da qual ira fazer comunicaçao
#   para saber a sua porta, execute no terminal :
#   python -m serial.tools.list_ports
# se estiver usando windows, o gerenciador de dispositivos informa a porta

#use uma das 3 opcoes para atribuir à variável a porta usada
#serialName = "/dev/ttyACM0"           # Ubuntu (variacao de)
#serialName = "/dev/tty.usbmodem1411" # Mac    (variacao de)
serialName = "COM6"                  # Windows(variacao de)


def main():
    try:
        print("Iniciou o main")
        #declaramos um objeto do tipo enlace com o nome "com". Essa é a camada inferior à aplicação. Observe que um parametro
        #para declarar esse objeto é o nome da porta.
        com1 = enlace(serialName)
        
    
        # Ativa comunicacao. Inicia os threads e a comunicação seiral 
        com1.enable()
        #Se chegamos até aqui, a comunicação foi aberta com sucesso. Faça um print para informar.
        print("Abriu a comunicação")
        
        # TRANSMISSÃO DE IMAGEM
        # imagemR = "./img/cat.png" # imagem em bytes!
        # imagemW = "./img/recebidoCopia.png"
        # print("Carregando imagem para ser transmitida :")
        # print(" - {}".format(imagemR))
        # txBuffer = open(imagemR, 'rb').read()

        # TRANSMISSÃO DE UM ARRAY DE BYTES
        txBuffer = b'\x12\x13\xAB\xCD'  #isso é um array de bytes
        
        # CONFERÊNCIA DO TAMANHO DO txBuffer (quantos bytes serão enviados)
        print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))
            
        #finalmente vamos transmitir os todos. Para isso usamos a funçao sendData que é um método da camada enlace.
        #faça um print para avisar que a transmissão vai começar.
        #Cuidado! Apenas trasmita arrays de bytes!
        print("Transmissão começando")
        
        # Método send chama o sendBuffer do arquivo enlaceTX
        # Em seguida, esse método salva no atributo transLen o tamanho do array de bytes, salva esse array no atributo buffer 
        # e, por fim, ativa a thread para que ela envie o array de bytes presentes no bufferTx para a camada UART
        com1.sendData(bytearray(txBuffer))  #as array apenas como boa pratica para casos de ter uma outra forma de dados
          
        # A camada enlace possui uma camada inferior, TX possui um método para conhecermos o status da transmissão
        # O método não deve estar funcionando quando usado como abaixo. deve estar retornando zero. Tente entender como esse método funciona e faça-o funcionar.
        txSize = com1.tx.getStatus()
        print('enviou = {}' .format(txSize))
        
        #Agora vamos iniciar a recepção dos dados. Se algo chegou ao RX, deve estar automaticamente guardado
        #Observe o que faz a rotina dentro do thread RX
        print("Recepção começando")
        #Será que todos os bytes enviados estão realmente guardadas? Será que conseguimos verificar?
        #Veja o que faz a funcao do enlaceRX  getBufferLen
      
        #acesso aos bytes recebidos
        txLen = len(txBuffer)
        # Para chamar o getData, é necessário fornecer o tamanho dos bytes que se deseja receber, pois o método getNData será usado
        rxBuffer, nRx = com1.getData(txLen)
        print(f"nRx (tamanho da mensagem que se espera receber) = {nRx}")
        print("recebeu {} bytes" .format(len(rxBuffer)))

        # print("Salvando dados no arquivo :")
        # print(" - {}".format(imagemW))
        # f = open(imagemW, 'wb')
        # f.write(rxBuffer)

        # f.close()
        
        for i in range(len(rxBuffer)):
            print("recebeu {}" .format(rxBuffer[i]))
        
        # Encerra comunicação
        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        

    #so roda o main quando for executado do terminal ... se for chamado dentro de outro modulo nao roda
if __name__ == "__main__":
    main()
