from moduloLL import LinearList

option = -1
first = True

while(option != 0):
    option = int(input("\n Selecione uma das opções a seguir:\n 1 - Iniciar a Lista Linear.\n 2 - Inserir elemento na lista.\n 3 - Remover um elemento da lista. \n 4 - Localizar a posição de um produto. \n 5 - Exibir a Lista Linear. \n 6 - Excluir todos elementos da lista. \n 0 - Sair\n\n"))

    if(option == 1):
        first = False 
        maxList = int(input("\nQuantos espaços na memória deseja alocar?  \n\n "))
        list = LinearList(maxList)
        print("\n Lista alocada na memória com ", maxList, "espaços")

    elif(option == 2):
        if(first):
            print("\n Nenhuma lista linear iniciada, por favor inicialize antes de inserir algum elemento.")
            pass
        else:
            productName = input("\n Qual o nome do produto?  \n\n")
            productBarCode = int(input("\n Qual o código de barras desse produto?  \n\n"))
            productIndex = int(input("\n Em qual posição da lista desejas inserir esse produto?  \n\n Lembrando que, a primeira inserção pode ser feita em qualquer posição da lista vazia. Após a primeira inserção, a posição onde foi inserido esse primeiro produto será o inicio da lista por contiguidade, ou seja, a posição '1'.(Exemplo: inseri o primeiro produto na posição 5 da lista, então na proxima inserção a posição 6 será a posiçao '2')\n\n"))
            list.insert(productName, productBarCode, productIndex)
            list.showList()
    
    elif(option == 3):
        if(first):
            print("\n Nenhuma lista linear iniciada, por favor inicialize uma lista linear.")
            pass
        else:
            removeIndex = int(input("\n Deseja remover o produto de qual posicao?  \n\n"))
            removeIndex = list.remove(removeIndex)
            list.showList()

    elif(option == 4):
        if(first):
            print("\n Nenhuma lista linear iniciada, por favor inicialize uma lista linear.")
            pass
        else:
            productNameSearch = input("\n Qual o nome do produto que será encontrado a posição?  \n\n")
            position = list.search(productNameSearch)
            print("\n O produto ", productNameSearch, " está na posição ", position, "\n\n")
            list.showList()

    elif(option == 5):
        if(first):
            print("\n Nenhuma lista linear iniciada, por favor inicialize uma lista linear.")
            pass
        else:
            list.showList()

    elif(option == 6):
        if(first):
            print("\n Nenhuma lista linear iniciada, por favor inicialize uma lista linear.")
            pass
        else:
            list.destroy()
            list.showList()
