class conta_bancaria:
   def __init__(self,nome_titular, numero_conta, saldo_inicial=0):
      self.nome_titular = nome_titular
      self.numero_conta = numero_conta
      self.saldo = saldo_inicial

   def depositar(self, valor):
      if valor < 0:
         print("Valor de depósito inválido!")
      else:
         self.saldo += valor

   def sacar(self, valor):
      if valor > 0:
        if self.saldo >= valor:
         self.saldo -= valor
        else:
            print("Saldo insuficiente!")

   def consultar_saldo(self):
      return self.saldo
   
   def transferir(self, valor, outra_conta):
      if valor > 0:
         if self.saldo >= valor:
            self.saldo -= valor 
            outra_conta.depositar(valor)
            print("Transferéncia feita com sucesso!")
         else:
            print("Você não possui saldo necessário para transferir! deixew de ser liso!")
      else:
         print("Valor da tansferencia deve ser maior do que 0, deixe de doidiça.")

      
    