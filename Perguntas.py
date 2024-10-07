import random
class iteracaoChatBot():
    def __init__(self):
        global iteracao
        iteracao = ["Olá! Como posso te ajudar hoje? ",
                    "No que posso ser útil? ",
                    "Qual o motivo da sua visita? ",
                    "O que você espera encontrar aqui? ",
                    "Qual a sua principal dúvida no momento? "
                    ]
    def IteracaoRam(self):
        return random.choice(iteracao)