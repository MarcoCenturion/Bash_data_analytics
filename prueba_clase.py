class Clase():
    def __new__(cls):
        print('Hola 1')
        return super().__new__(cls)
    def __init__(self):
        print('Hola 2')

c=Clase()
