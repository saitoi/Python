class Objeto(object):

    list_objetos = []    

    def __init__(self, codigo):
        self.codigo = codigo

# x------------------------------------x

class ObjetoA(Objeto):

    list_objetos_a = []    

    def __init__(self, codigo):
        super().__init__(codigo)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, ObjetoA):
            return abs(self.codigo - other.codigo) < 3
        return False

# x------------------------------------x

class objeto_b(objeto):

    set_objetos_b = set()

    def __init__(self, codigo):
        super().__init__(codigo)

    def __eq__(self, other: object) -> bool:
        if isinstance(self, objeto_a):
            return abs(self.codigo - other.codigo) < 10
        return False
        
    def __hash__(self) -> int:
        return hash(self.codigo)

# x------------------------------------x

def menu():
    print("""" x--- MENU ---x
1. Criar objetos do tipo A
2. Criar objetos do tipo B
3. Listar todos os objetos
4. Listar objetos do tipo A
5. Listar objetos do tipo B
6. Sair do programa
""")

def input_valido():
    while True:
        try:
            return int(input("Digite uma opção: "))
        except ValueError:
            print("Digite um número inteiro válido!")

# main

while True:
    menu()
    opcao = input_valido()


# Arraylist guarda todos os objetos
# Linked List guarda os objetos A
    # Diferença de 2 unidades
# HashSet guarda os objetos B
    # Diferença de 10 unidades
