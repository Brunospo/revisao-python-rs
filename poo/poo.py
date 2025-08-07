from abc import ABC, abstractmethod

class Veiculo(ABC):
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass


class Carro(Veiculo):
  def __init__(self):
    pass

  def ligar(self):
    return 'ligando carro...'
  
  def desligar(self):
    return 'desligando carro...'


carro = Carro()
print(carro.ligar())