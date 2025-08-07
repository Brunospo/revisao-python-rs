import tkinter as tk
import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self._nome = nome
        self._vida = vida
        self._nivel = nivel

    def get_nome(self):
        return self._nome

    def get_vida(self):
        return self._vida

    def get_nivel(self):
        return self._nivel

    def esta_vivo(self):
        return self._vida > 0

    def receber_ataque(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0

    def atacar(self, alvo):
        dano = random.randint(self._nivel * 2, self._nivel * 4)
        alvo.receber_ataque(dano)
        return f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano"

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self._habilidade = habilidade

    def habilidade_especial(self, alvo):
        dano = random.randint(self._nivel * 5, self._nivel * 7)
        alvo.receber_ataque(dano)
        return f"{self.get_nome()} usou {self._habilidade} em {alvo.get_nome()} e causou {dano} de dano"

    def recuperar_vida(self, quantidade):
        self._vida += quantidade
        if self._vida > 100:
            self._vida = 100

    def subir_nivel(self):
        self._nivel += 1

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self._tipo = tipo

def barra_de_vida(vida):
    total = 20
    preenchido = int((vida / 100) * total)
    return "[" + "#" * preenchido + "-" * (total - preenchido) + "]"

class JogoGUI:
    def __init__(self, root):
        self.heroi = Heroi("Herói", 100, 5, "Super Força")
        self.fase = 0
        self.inimigos = [
            Inimigo("Goblin", 40, 3, "Terrestre"),
            Inimigo("Esqueleto", 60, 4, "Morto-vivo"),
            Inimigo("Dragão", 100, 6, "Voador"),
        ]
        self.inimigo = self.inimigos[self.fase]

        self.root = root
        self.root.title("Batalha Épica ⚔️")

        self.texto = tk.Label(root, text="Bem-vindo ao jogo!", font=("Arial", 14))
        self.texto.pack(pady=10)

        self.status = tk.Label(root, text="", font=("Courier", 12), justify="left")
        self.status.pack()

        self.btn_ataque = tk.Button(root, text="Ataque Normal", command=self.ataque_normal)
        self.btn_ataque.pack(pady=5)

        self.btn_especial = tk.Button(root, text="Ataque Especial", command=self.ataque_especial)
        self.btn_especial.pack(pady=5)

        self.atualizar_status()

    def atualizar_status(self):
        status_text = (
            f"🌟 Fase {self.fase + 1}\n"
            f"👨‍🚀 {self.heroi.get_nome()} - Vida: {self.heroi.get_vida()} {barra_de_vida(self.heroi.get_vida())}\n"
            f"👾 {self.inimigo.get_nome()} - Vida: {self.inimigo.get_vida()} {barra_de_vida(self.inimigo.get_vida())}"
        )
        self.status.config(text=status_text)

    def ataque_normal(self):
        if self.heroi.esta_vivo() and self.inimigo.esta_vivo():
            resultado = self.heroi.atacar(self.inimigo)
            self.texto.config(text=resultado)
            self.verificar_batalha()
        self.atualizar_status()

    def ataque_especial(self):
        if self.heroi.esta_vivo() and self.inimigo.esta_vivo():
            resultado = self.heroi.habilidade_especial(self.inimigo)
            self.texto.config(text=resultado)
            self.verificar_batalha()
        self.atualizar_status()

    def verificar_batalha(self):
        if not self.inimigo.esta_vivo():
            self.texto.config(text=f"✅ Você derrotou {self.inimigo.get_nome()}!")
            self.heroi.recuperar_vida(20)
            self.heroi.subir_nivel()
            self.fase += 1
            if self.fase < len(self.inimigos):
                self.inimigo = self.inimigos[self.fase]
                self.texto.config(text=f"🚀 Avançando para a fase {self.fase + 1}!")
            else:
                self.texto.config(text="🏆 Você venceu todas as fases!")
                self.btn_ataque.config(state="disabled")
                self.btn_especial.config(state="disabled")
        else:
            resposta = self.inimigo.atacar(self.heroi)
            self.texto.config(text=self.texto.cget("text") + "\n" + resposta)
            if not self.heroi.esta_vivo():
                self.texto.config(text="💀 Você foi derrotado!")
                self.btn_ataque.config(state="disabled")
                self.btn_especial.config(state="disabled")

        self.atualizar_status()

# Executar a interface
root = tk.Tk()
jogo = JogoGUI(root)
root.mainloop()