import multiprocessing
import ctypes
import time


def function1(value, start):
    if start.value:     # Na primeira função ele não entra nesse if por que o valor inicial da variavel start e False
        res = value.value + 10
        start.value = False
    else:   # então ele entra aqui no else
        res = value.value + 20  # cria uma variavel res que pega o valor que inicial da varial value que e 100 e soma 20
        value.value = 200   # aqui ele altera o valor da variavel value para 200
        start.value = True  # aqui ele muda o status da variavel status para True

    print(f'O resultado da função 1 é {res}')   # aqui ele mostra o resultado da variavel res que e 120.
    time.sleep(0.001)


def function2(value, start):
    if start:   # quando a função 2 e chamada a variavel start esta com o valor true, pois foi alterada na função 1
        res = value.value + 30  # aqui ele soma 30 no value que ta com o valor 200, pois foi alterado na função 1
        start.value = False # aqui ele muda o start para False novamente
    else:
        res = value.value + 40
        value.value = 400
        start.value = True

    print(f'O resultado da função 2 é {res}')   # Aqui ele mostra o resultado que e 230
    time.sleep(0.001)


if __name__ == '__main__':
    val = multiprocessing.Value('i', 100)   # cria um variavel compartilhada iniciando com o valor 100
    status = multiprocessing.Value(ctypes.c_bool, False)   # cria uma variavel compartilhada começa como False

    process1 = multiprocessing.Process(target=function1, args=(val, status))  # Aqui ele inicia a função 1 passando o parametro Value = 100 e o paramentro Status igual a False
    process2 = multiprocessing.Process(target=function2, args=(val, status))  # aqui ele inicia a função 2 passando o parametro Value que agora e 200 e o passando o paramentro Status que agora e True

    process1.start()
    process2.start()

    process1.join()
    process2.join()
