import time
import random
from limpar_tela import limpar_tela

class Personagem():
  def __init__(self, nome, vida, nivel):
    self.__nome = nome
    self.__vida = vida
    self.__nivel = nivel

  def get_nome(self):
    return self.__nome
  
  def get_vida(self):
    return self.__vida
  
  def get_nivel(self):
    return self.__nivel
  
  def barra_de_vida(self,vida):
    total = 20 #tamanho total da barra como 20 caracteres
    preenchido = int((vida / 100) * total)
    return "[" + "#" * preenchido + "-" * (total - preenchido) + "]"
  
  def exibir_detalhes(self):
    return f"Nome: {self.get_nome()}\nVida: {self.get_vida()} {self.barra_de_vida(self.get_vida())}\nNivel: {self.get_nivel()}"
  
  def receber_ataque(self, dano):
    self.__vida -= dano
    if self.__vida < 0:
      self.__vida = 0
  
  def atacar(self, alvo):
    dano = random.randint(self.__nivel * 2, self.__nivel * 4)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")
  
class Heroi(Personagem):
  def __init__(self, nome, vida, nivel, habilidade):
    super().__init__(nome, vida, nivel)
    self.__habilidade = habilidade
  
  def get_habilidade(self):
    return self.__habilidade
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
  
  def habilidade_especial(self, alvo):
    dano = random.randint(self.__nivel * 5, self.__nivel * 7)
    alvo.receber_ataque(dano)
    print(f"{self.get_nome()} usou habilidade especial em {alvo.get_nome()} e causou {dano} de dano")
  

class Inimigo(Personagem):
  def __init__(self, nome, vida, nivel, tipo):
    super().__init__(nome, vida, nivel)
    self.__tipo = tipo

  def get_tipo(self):
    return self.__tipo
  
  def exibir_detalhes(self):
    return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
  
class Jogo():
  def __init__(self):
    self.heroi = Heroi(nome="Heroi", vida=100, nivel=5, habilidade="Super Força")
    self.inimigo = Inimigo(nome="Inimigo", vida=50, nivel=5, tipo="Voador")
  
  def iniciar_batalha(self):
    limpar_tela()
    print("Iniciando batalha...⚔️")
    time.sleep(1)

    while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
      limpar_tela()
      print("\nDetalhes dos personagens:\n")
      print(self.heroi.exibir_detalhes())
      print(self.inimigo.exibir_detalhes())

      input('Pressione Enter para atacar...')
      escolha = input('Escolha (1 - Ataque Normal, 2 - Ataque Especial): ')

      if escolha == "1":
        limpar_tela()
        self.heroi.atacar(self.inimigo)
        time.sleep(1)
      elif escolha == "2":
        limpar_tela()
        self.heroi.habilidade_especial(self.inimigo)
        time.sleep(1)
      else:
        limpar_tela()
        print("\nEscolha errada, tente novamente")
        time.sleep(1)

      if self.inimigo.get_vida() > 0:
        limpar_tela()
        self.inimigo.atacar(self.heroi)
        time.sleep(1)

    if self.heroi.get_vida() > 0:
      print("\n🥳🎉Parabens você ganhou!!")
    else:
      print("\n😿Você foi derrotado!!")


jogo = Jogo()
jogo.iniciar_batalha()
