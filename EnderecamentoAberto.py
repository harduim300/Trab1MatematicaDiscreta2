import random
import numpy as np 

num_contas = 1000
limite_inferior = 10000
limite_superior = 99999
numeros_conta = []

#Geração de valores
while len(numeros_conta) < num_contas:
    numero = np.random.randint(limite_inferior,limite_superior)
    numeros_conta.append(numero)

class TabelaHashComEnderecamentoAberto:
    
    def __init__(self, size):
        self.num_chaves_hash = size
        self.tabelaHash = [None for _ in range(self.num_chaves_hash)]
        self.todosDigitos = False
        self.estaCheiaContador = 0
        
    def funcaoHash(self, numero_conta):
        return numero_conta % self.num_chaves_hash
    
    def insertElemento(self, chave, valor):

        # Verifica se Tabela esta cheia
        if self.estaCheiaContador == self.num_chaves_hash:
            print("Tabela Hash cheia, nao pode ser adicionado novo elemento")
            return 0

        #Verifica se o caso se trata de um 3 digitos ou nao.
        if len(str(chave)) == 5:
            self.todosDigitos = True
            
        chaveHash = self.funcaoHash(chave)
        elementoLista = (chave,valor)

        # Verifica se a posica na tabela esta vazia e insere o elemento
        if self.tabelaHash[chaveHash] == None:
            self.tabelaHash[chaveHash] = elementoLista
            self.estaCheiaContador += 1
            
        # Verifica a proxima posicao da tabela caso encontre uma colisao
        # Alem de caso a colisao seja no final da tabela, reposiciona
        # para o comeco da tabela.
        else:
            
            i = 1
            while self.tabelaHash[self.funcaoHash(chaveHash + i) % self.num_chaves_hash] != None and i != self.num_chaves_hash:
                i += 1
            self.tabelaHash[self.funcaoHash(chaveHash + i) % self.num_chaves_hash] = (chave,valor)
            self.estaCheiaContador += 1
                  
    def buscaValores(self, valor):

        # identifica se a tabela foi instanciada para o caso
        # de 3 ou mais digitos.
        if self.todosDigitos == False:
                  
            chave = valor % 1000
            chaveHash = self.funcaoHash(chave)
            aux = self.tabelaHash[chaveHash]
        
        else: 
            chave = valor
            chaveHash = self.funcaoHash(chave)
            aux = self.tabelaHash[chaveHash]

        # Utilizando a funcao hash, salta para a posica com valor correspontente
        # Caso nao encontre avalia os valores posteriores.
        # Isso por meio de uma estrategia de Sondagem linear
        i = 0
        while i != self.num_chaves_hash and aux != None:
            if (aux[1] == valor):
                print(f'Valor {aux[1]} encontrado na Tabela Hash')
                return 0
            else:
                i += 1
                aux = self.tabelaHash[(chaveHash+i) % self.num_chaves_hash]
        print(f'Valor {valor} não encontrado na tabela Hash')
        return 0
    
import time

# Criacao das tabelas para ambos os métodos
# Enderecamento Aberto
tabela1Ab = TabelaHashComEnderecamentoAberto(1000)
tabela2Ab = TabelaHashComEnderecamentoAberto(1000)
# Insercao de valores nas tabelas
for conta in numeros_conta:
    # Insercao com chave de 3 digitos
    tabela1Ab.insertElemento((conta % 1000), conta)
    # Insercao por chave com todos os digitos
    tabela2Ab.insertElemento(conta, conta)

inicio = time.time()
tabela1Ab.buscaValores(93781)
fim = time.time()
print(f' Tempo de busca 3 digitos: {fim - inicio}')
print("----------------------------")
inicio = time.time()
tabela2Ab.buscaValores(93781)
fim = time.time()
print(f' Tempo de busca 5 digitos: {fim - inicio}')    