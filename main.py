from classes import *

#entrada de ddos
if __name__ == '__main__':
    nome = input('Informe o seu nome: ')
    idade = int(input('Informe a sua idade: '))
    email = input('Informe o seu e-mail: ')

#instanciacao da classe
usuario = Pessoa(nome, idade, email)

#saida de dados
print(f'Nome: {usuario.nome}.')
print(f'Idade: {usuario.idade}.')
print(f'E-mail: {usuario.email}.')



