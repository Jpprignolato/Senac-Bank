#Imports

import os
from time import sleep
from sys import exit
from random import randint
from classes import ContaPoupanca
os.system('cls')

class BancoSenac:
      def StartSystem(logged = False):
#Menu Offline            
            if logged == False:
                  
                  while True:
                        opcoes = ['Registrar', 'Sair']
                        
                        for i in range(len(opcoes)):
                              print(f'[{i + 1}] {opcoes[i]}')
                              
                        opcao_escolhida = int(input('\nEscolha uma das opções: ')) -1
                        
                        #Registrar user
                        if opcao_escolhida == 0:
                        
                              nome = str(input("Digite seu nome: ")).title().split(' ')
                              numero_da_conta = randint(100, 999)
                              
                              while True:
                                    try:
                                          primeiro_deposito = float(input("Digite o valor do primeiro deposito: R$"))
                                          
                                          if primeiro_deposito <= 0:
                                                print("Você precisa depositar um valor maior que 0!")
                                                
                                          else:
                                                global usuariol
                                                usuariol = ContaPoupanca(nome, numero_da_conta, primeiro_deposito, 0)
                                                break
                                    except ValueError:
                                          print("Digite apenas numeros!")
                                          
                              # Sair
                              if opcao_escolhida == 1:
                                    BancoSenac.stopSystem()
                                    
                              else:
                                    print("Digite uma opção válida! \n")
                                    
                              BancoSenac.StartSystem(True)                
                              
#Menu

                        elif logged == True:
                              os.system('cls')
                              
                              while True:
                                    opcoes = ['Sacar', 'Depositar', 'Aplicar', 'Resgatar', 'Mostrar Dados', 'Sair']
                                    
                                    for i in range(len(opcoes)):
                                          print(f'[{i + 1}] {opcoes[i]}')  
                                    opcao_escolhida = int(input("\n Escolha uma das opções")) - 1
                                    
#Opção Sacar
                                    # Sacar
                        if opcao_escolhida == 0:
                              print(f'Saldo Atual: R${usuariol.get_saldo_corrente()}')
                              valor_saque = float(input('Quanto voce quer sacar? R$'))

                        usuariol.sacar_saldo_corrente(valor_saque)
                        print(f'-> Saldo Atual{usuariol.get_saldo_corrente()}')
                        sleep(5)

#Opção Depositar
                        if opcao_escolhida == 1:
                               print(f'Saldo Atual: R${usuariol.get_saldo_corrente()}')
                               valor_saque = float(input('Quanto voce quer depositar? R$'))

                        usuariol.depositar_saldo_corrente(valor_saque)
                        print(f'-> Saldo Atual{usuariol.get_saldo_corrente()}')
                        sleep(5)
# Opção Aplicar
                        if opcao_escolhida == 2:
                              print(f'Saldo Atual: R${usuariol.get_saldo_corrente()}')
                              valor_saque = float(input('Quanto voce quer aplicar? R$'))

                        usuariol.aplicar_saldo(valor_saque)
                        print(f'-> Saldo Atual{usuariol.get_saldo_corrente()}')
                        sleep(5)

# Opção Resgatar