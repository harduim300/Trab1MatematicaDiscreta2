import random
import numpy as np 

num_contas = 1000
limite_inferior = 10000
limite_superior = 99999
numeros_conta = []

# Geracao de valores de conta
while len(numeros_conta) < num_contas:
    numero = np.random.randint(limite_inferior,limite_superior)
    numeros_conta.append(numero)

class ListaEncadeada:
    def __init__(self, chaveConta, valor):
        self.chave = chaveConta
        self.valor = valor
        self.proximo = None

class TabelaHashContasEncadeamentoExterior:
    
    
    def __init__(self, size):
        self.num_chaves_hash = size
        self.tabelaHash = [None for _ in range(self.num_chaves_hash)]
        self.todosDigitos = False
        print(self.tabelaHash)
        
        
    def funcaoHash(self, numero_conta):
        return numero_conta % self.num_chaves_hash
    
    
    def insertElemento(self, chave, valor):
        
        if len(str(chave)) == 5:
            self.todosDigitos = True
            
        chaveHash = self.funcaoHash(chave)
        elementoLista = ListaEncadeada(chave,valor)
        
        if self.tabelaHash[chaveHash] == None:
            self.tabelaHash[chaveHash] = elementoLista
            
        else:
            
            aux = self.tabelaHash[chaveHash]
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = elementoLista
    
    
            
    def buscaValores(self,valor):
        
        if self.todosDigitos == False:
            chave = valor % 1000
            chaveHash = self.funcaoHash(chave)
            aux = self.tabelaHash[chaveHash]
        
        else: 
            chave = valor
            chaveHash = self.funcaoHash(chave)
            aux = self.tabelaHash[chaveHash]
        
        while aux != None:
            
            if aux.valor == valor:
                print(f' Valor {aux.valor} encontrado na Tabela')
                return 0
            aux = aux.proximo
    
        print(f'Valor {valor} não encontrado na tabela Hash')
        return 0
    
import time

# Criacao das tabelas para ambos os métodos

# Encadeamento Exterior
tabela1Ex = TabelaHashContasEncadeamentoExterior(9)
tabela2Ex = TabelaHashContasEncadeamentoExterior(9)


# Insercao de valores nas tabelas
for conta in numeros_conta:
    # Insercao com chave de 3 digitos
    tabela1Ex.insertElemento((conta % 1000), conta)
    # Insercao por chave com todos os digitos
    tabela2Ex.insertElemento(conta, conta)

inicio = time.time()
tabela1Ex.buscaValores(93781)
fim = time.time()
print(f' Tempo de busca 3 digitos: {fim - inicio}')
print("----------------------------")
inicio = time.time()
tabela2Ex.buscaValores(93781)
fim = time.time()
print(f' Tempo de busca 5 digitos: {fim - inicio}')