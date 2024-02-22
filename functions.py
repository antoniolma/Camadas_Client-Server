import random

Comando = {
    1: b'\x00\x00\x00\x00',
    2: b'\x00\x00\xFF\x00',
    3: b'\xFF\x00\x00',
    4: b'\x00\xFF\x00',
    5: b'\x00\x00\xFF',
    6: b'\x00\xFF',
    7: b'\xFF\x00',
    8: b'\x00',
    9: b'\xFF',
}

def random_numero():
    return random.randint(10,30)

def chama_comandos(repeticoes):
    ordem = []
    for i in range(0, repeticoes):
        ordem.append(Comando[random.randint(1,9)])
    return ordem
