#Encapsulamnto, ele é determinado pela especificaca oda classe, sendo public, private, ou public
#
#Classe
#class Pessoa:
    #def __init__(self, nome, idade, email):
        #self.nome = nome                       #public (SEM NADA)
        #self._idade = idade                    # protectic (_)
        #self.__email = email                   #privete (__)

class Pessoa:
    def __init__(self, nome, idade, email):
        self.__nome = nome # private
        self.__idade = idade # private
        self.__email = email #privete

    #metodos de acesso
    #def get_nome(self):
        #return self.__nome
    
    #def set_nome(self, nome):
        #self.__nome = nome

    #def get_idade(self):
        #return self.__idade
    
    #def set_idade(self, idade):
        #self.__nome = idade

    #def get_email(self):
        #return self.__email
    
    #def set_email(self, email):
        #self.__nome = email
    #______________________________________
    #metodo de acesso correto de fazer

    #metodo GET NOME
    @property
    def nome(self):
        return self.__nome
    
    #metodo SET NOME
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    #metodo GET IDADE
    @property
    def idade(self):
        return self.__idade
    
    #metodo SET IDADE
    @idade.setter
    def idade(self, nome):
        self.__idade = idade

    #metodo GET EMAIL
    @property
    def email(self):
        return self.__email
    
    #metodo SET EMAIL
    @email.setter
    def nome(self, email):
        self.__email = email

