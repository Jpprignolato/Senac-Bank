#Classe Conta Corrente.
class ContaCorrente:
    def __init__(self, nome_titular, numero_conta, saldo_corrente):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo_corrente = saldo_corrente

# Saldo atual da conta corrente.

    def get_saldo_corrent(self):
        return self.__saldo_corrente

# Muda o saldo atual da conta corrente

    def set_saldo_corrente(self, operador, valor):
        
        if operador == '+':
            self.__saldo_corrente += valor

        elif operador == '-':
            self.__saldo_corrente -= valor

        else: 
            return print("Operador Invalido. ")


# Função Sacar

    def sacar_saldo_corrente(self, valor):
        self.set_saldo_corrente('-', valor)

# Função Depositar

    def depositar_saldo_corrente(self, valor):
        self.set_saldo_corrente('+', valor)

# Função Aplicar
    
    def aplicar_saldo(self, valor):
        self.set_saldo_corrente('-', valor)
        self.set_saldo_poupanca('+', valor)


# Classe Conta Poupança

class ContaPoupanca(ContaCorrente):
    def __init__(self, nome_titular, numero_conta, saldo_corrente, saldo_poupanca):
        super().__init__(nome_titular, numero_conta, saldo_corrente, saldo_poupanca)

        self.__saldo__poupanca = saldo_poupanca

# Saldo atual da conta poupança

    def get_saldo_poupanca(self):
        return self.__saldo__poupanca

# Muda o saldo da conta poupança

    def set_saldo_poupanca(self, operador, valor):

        if operador == '+':
            self.__saldo__poupanca += valor

        elif operador == '-':
            self.__saldo_poupanca -= valor

        else:
            return print("Operador Invalido.")

#Função resgate

    def resgatar_saldo(self, valor):
        self.set_saldo_poupanca('-', valor)
        self.set_saldo_corrente('+', valor)