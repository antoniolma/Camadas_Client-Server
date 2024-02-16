No console python, 'pip install pyserial'
Verificar em gerenciador qual porta com esta o aduino 
Talvez mudar a porta usb. Ou tirar e por quando nao tem autorizacao :-\

Esclarecimentos para Conceito B:
 - getBufferLen: Devolve o tamanho da mensagem (lista de bytes ou arrays) que se encontra no bufferTX ou bufferRX.

- getAllBuffer: Função exclusiva do enlaceRX, onde é devolvido o conteúdo presente no bufferRX e depois o bufferRX é esvaziado.

- getBuffer: Função exclusiva do enlaceRX, onde é requisitado um certo número de bytes, pegando assim somente um número específico de bytes que foi requisitado, devolvendo-os na função e apagando-os do bufferRX. Ex.: BufferRX = b'\x12\x13\xab', se rx.getBuffer(2), retorna b'\x12\x13' e BufferRX = b'\xab'.

- getNData: Função exclusiva do enlaceRX, que serve para chamar a função rx.getBuffer(size), porém que só irá realizar o chamado desta função após o numéro de bytes presentes no BufferRX ser maior ou igual ao número requisitado pelo valor "size" que recebe em sua construção. Caso o "size" seja maior que o tamanho da mensagem armazenada em BufferRX, então ele irá aguardar até que o tamanho da mensagem seja maior ou igual ao seu tamanho.

 - sendBuffer: Função exclusiva do enlaceTX, que recebe uma mensagem, armazena ela no BufferTX, guarda seu tamanho e abre o threadTX (self.threadMutex = True) para que a mensagem seja enviada para o Arduino.

 Pergunta: 
        Para a transmissao de bytes, o bufferTX aparentemente está sempre sendo atualizado, porém só ira passar o conteúdo nele presenta caso o Thread TX 
    esteja como True (self.threadMutex = True).
        Para o recebimento de bytes, o bufferRX só irá ser atualizado e enviado ao computador, caso o Thread RX esteja como True (self.threadMutex = True).
