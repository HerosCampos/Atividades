from random import randint


class Personagem:
    # Atributos da Classe
    sociedade = []
    def __init__(self, nome: str, saude = 5, energia = 5, ataque = 5, defesa = 5):
        # Atributos
        self.nome = nome
        self.saude = saude
        self.energia = energia
        self.ataque = ataque
        self.defesa = defesa

        # A executar
        Personagem.sociedade.append(self)

    # Métodos
    def atacar(self):
        self.energia = self.energia - 10
        return randint(0, self.ataque)

    def defender(self):
        self.energia = self.energia - 5
        return randint(0, self.defesa)

    def descansar(self):
        self.energia = 100

    def golpe_especial(self):
        return int(((self.ataque + self.defesa) / 2) * 2)
    
    def __repr__(self):
        return f"Personagem({self.nome}, {self.saude}, {self.energia}, {self.ataque}, {self.defesa})"


class Ranger(Personagem):
    def __init__(self, nome: str, saude=5, energia=5, ataque=5, defesa=5, rastrear=5):
        super().__init__(nome, saude, energia, ataque, defesa)
        self.rastrear = rastrear

    def rastreando(self, alvo):
        self.energia -= 10
        print(f"{self.nome} está rastreando {alvo}")
 
    def __repr__(self):
        return f"Ranger({self.nome}, {self.saude}, {self.energia}, {self.ataque}, {self.defesa})"

    
boromir = Personagem("Boromir")
frodo = Personagem("Frodo")
aragorn = Ranger("Aragorn", 100, 100, 50, 80)
#print(f"Dano causado: {aragorn.atacar()}")
#print(f"Dano bloqueado: {aragorn.defender()}")
#print(f"{aragorn.nome} está com {aragorn.energia} de energia")
#aragorn.descansar()
#print(f"{aragorn.nome} está com {aragorn.energia} de energia")
#print(f"Especial: {aragorn.golpe_especial()}")

#print(Personagem.sociedade)
#for p in Personagem.sociedade:
#    print(p.nome, p.saude)

print(Personagem.sociedade)
print(frodo)
for p in Personagem.sociedade:
    print(p.nome, p.saude)


# Conferindo se o método Rastreando do Ranger está funcionando
#print(aragorn.energia)
#aragorn.rastreando('Hobbits')
#print(aragorn.energia)


# Podemos notar que Aragorn, mesmo sendo Ranger aparece na lista dos personagem
#for p in Personagem.sociedade:
#    print(p.nome)


# Conferindo a sobreposição do __repr__
#print(aragorn)

