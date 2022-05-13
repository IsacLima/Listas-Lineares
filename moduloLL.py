#classe que usaremos para definir os produtos e os atributos dele, possui um nome e um
#codigo de barra
class Product:
    def __init__(self, name=None, barCode=None):
        self.name = name 
        self.barCode = barCode


class LinearList:
    #aqui fazemos a alocação dinamica baseada no valor passado por entrada pelo usuario
    def __init__(self, max):
        self.max = max
        self.vetor = [None] * self.max
        self.init = -1
        self.end = -1



    def insert(self, name, barCode, index):
        
        # aqui inserimos se,  lista nao estiver cheia, ou index maior que o tanaho de alocação 
        # ou index menor que zero

        if((self.init == 0 and self.end == self.max - 1) or (index > self.max) or (index < 0)):
            print("ERRO: Posição inválida")
        else:
        
            if(self.init == -1):
                self.init = 0
                self.end = 0
         
            #aqui movemos os valores da lista para encaixar o produto passado pelo usuario
            #se o fim da lista for igual ao valor maximo, movemos com passo negativo , ou seja, movemos
            #um pra tras e deixamos livre o espaço que o usuario vai usar
            else: 
                if(self.end != self.max -1):
                    for i in range(self.end, self.init + index - 2, -1):
                        self.vetor[i + 1] = self.vetor[i]
                    self.end = self.end + 1
                else:
                    for i in range(self.init, self.init + index):
                        self.vetor[i - 1] =self.vetor[i]
                    self.init = self.init - 1

            self.vetor[self.init + index - 1] = Product(name, barCode)



    def remove(self, index):
        print("\n",self.init, self.end, index ,"\n")
        if((index < 0) or index > self.max):
            print("ERRO: Posição inválida")

        # aqui removemos o valor na posição passada por argumento
        # e movemos todos uma casa pro lado dependendo de onde esta mais proximo
        
        else:
        #movendo da esquerda pra direita
            aux = self.vetor[self.init + index - 1]
            if(index - self.init > self.end - index):
                for i in range(self.init + index - 1, self.end, +1):
                    self.vetor[i] = self.vetor[i + 1]
                self.vetor[self.end] = None
                self.end = self.end - 1
        #movendo da direita pra esquerda    
            else:
                for i in range(self.init + index - 1, self.init, -1):
                    self.vetor[i] = self.vetor[i - 1]
                self.vetor[self.init] = None
                self.init = self.init + 1
            return aux


    # busca o produto pelo nome passado de argumento
    #só é verificado os nomes dentro do vetor dos produtos que sao diferentes de nulo
    def search(self, name):
        verificator = 0
        for i in range(self.max):
            if(self.vetor[self.init + i] != None):
                print(name, self.vetor[self.init + i].name, i)
                if(name == self.vetor[self.init + i].name):
                    verificator = verificator + 1
                    return i + 1
            
        if(verificator == 0):
            print("\n Não há o elemento na lista")


    #aqui fazemos a exibição da lista usando a ajuda de uma lista aux porque 
    #a lista principal mostra somente os endereços
    def showList(self):
        aux = []
        for i in range(self.max):
            if(self.vetor[i] != None):
                aux.append([self.vetor[i].name, self.vetor[i].barCode])
            else: 
                aux.append([ None ])
        print(aux)


    #aqui resetamos os valores iniciais da lista linear, zerando-a 
    def destroy(self):
        self.vetor = None
        self.init = -1
        self.end = -1
        self.max = 0

            


