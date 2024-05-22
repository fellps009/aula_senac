class Pessoa:
    def __init__(self,nome,idade,peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self.crescer(0.5)
            
    def engordar(self, peso):
        self.peso += peso
        
    def emagrecer(self, peso):
        self.peso -= peso
        return self.peso

    def crescer(self, altura):     
         self.altura += altura
    
    def __str__(self):
        return f"Nome: {self.nome}, idade: {self.idade}, peso: {self.peso}, Altura: {self.altura} "

pesso1 = Pessoa("joão", 20, 150, 1.65)
print("Dados Iniciais")
print(pesso1)

pesso1.envelhecer()
pesso1.engordar(10)

print("Dados após envelhecer e engordar: ")
print(pesso1)
      