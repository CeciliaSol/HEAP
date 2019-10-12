import sys

from heap import Heap

def get_int():
    while True:
        try:
            i = int(input('ingrese un entero: ').strip())
        except Exception as e:
            print(e)
        else:
            return i


def encolar(h):
    h.enqueue(get_int())


def desencolar(h):
    if not h.is_empty():
        print(h.dequeue())
    else:
        print('La cola de prioridades está vacía...')


def salir(h):
    while True:
        answer = input('Desea salir? [y/N] ').strip()
        if answer.lower() == 'y':
            sys.exit(0)
        elif answer.lower() == 'n':
            return


def imprimir(h):
    print(h)


def ayuda(h):
    pass


OPTIONS = {
    'e': ('Encolar elemento en el heap', encolar),
    'd': ('Desencolar elemento del heap', desencolar),
    'x': ('Salir del programa', salir),
    'i': ('Imprimir el heap', imprimir),
}

PROMPT = 'e/d/a/x/i? '


def ayuda(h):
    for key in 'edaxi':
        print('{}: {}'.format(key, OPTIONS[key][0]))
    print()

OPTIONS['a'] = ('Imprimir esta ayuda', ayuda)
DEFAULT_OPTION = 'a'


def get_option():
    choice = input(PROMPT).strip()
    if choice not in OPTIONS:
        choice = DEFAULT_OPTION
    return OPTIONS[choice][-1]


if __name__ == '__main__':

    print()
    print('======= Uso interactivo del heap (cola de prioridades) =======')

    # Crear un heap para encolar o desencolar elementos en forma interactiva.
    h = Heap()

    ayuda(h)
    while True:
        option = get_option()
        option(h)

    print('======= Adiós! =======')
