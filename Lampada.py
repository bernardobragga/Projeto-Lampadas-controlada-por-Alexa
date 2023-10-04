class Lampada:
    def __init__(self, marca, voltagem, forca):
        self.marca = marca
        self.voltagem = voltagem
        self.forca = forca
        self.acesa = False


    def verificar_estado(self):
        return self.acesa

    def ligar(self):
        if self.verificar_estado() == False:
           self.acesa = True
           print("A "+self.marca+" está acesa!!")
        else:
            print("A "+self.marca+" já está acesa!")

    def desligar(self):
        if self.verificar_estado() == True:
            self.acesa = False
            print("A "+self.marca+" foi desligada")
        else:
            print("A "+self.marca+" já está desligada")


class Comodo:
    def __init__(self,nome):
        self.nome = nome
        self.lampadas = []

    def ligar_todas_lampadas(self):
        for lampada in self.lampadas:
            lampada.ligar()

    def desligar_todas_lampadas(self):
        for lampada in self.lampadas:
            lampada.desligar()

    def adicionar_lampada(self, lampada_nova):
        # Se a lista de lampadas está vazia
        if self.lampadas == []:
            self.lampadas.append(lampada_nova)
        else:
            # Se não, procura na lista se existe alguma igual
            existe_lampada_igual = False

            for lampada_cadastrada in self.lampadas:
                if (
                        lampada_cadastrada.marca == lampada_nova.marca and
                        lampada_cadastrada.voltagem == lampada_nova.voltagem and
                        lampada_cadastrada.forca == lampada_nova.forca
                ):
                  existe_lampada_igual = True
                  break

            # Se existir, não adiciona
            # caso contrário, adiciona na lista
            if existe_lampada_igual:
                print("Lampada já cadastrada")
            else:
                self.lampadas.append(lampada_nova)

class AssistenteVirtual:
    def __init__(self, nome, capacidade):
        self.nome = nome
        self.capacidade = capacidade
        self.comodos = []

    def AdicionarComodoNovo(self, comodo):
        if len(self.comodos) < self.capacidade:
            self.comodos.append(comodo)
        else:
            print("Capacidade máxima de cômodos atingida")

    def executar(self, comando):
        acao, _, local = comando.partition(' da ')
        if local == 'casa':
            for comodo in self.comodos:
                if acao == 'Ligar todas as lampadas':
                    comodo.ligar_todas_lampadas()
                elif acao == 'Desligar todas as lampadas':
                    comodo.desligar_todas_lampadas()
        else:
            for comodo in self.comodos:
                if comodo.nome == local:
                    if acao == 'Ligar todas as lampadas':
                        comodo.ligar_todas_lampadas()
                    elif acao == 'Desligar todas as lampadas':
                        comodo.desligar_todas_lampadas()
                    break
            else:
                print("Comodo não encontrado")


lamp1 = Lampada("Philips", 120, 9)
lamp2 = Lampada("Samsung", 120, 9)
lamp3 = Lampada("Xiaomi", 120, 9)
lamp4 = Lampada("Intelbras", 120, 9)
lamp5 = Lampada("Logitech", 120, 9)
lamp6 = Lampada("Positivo", 120, 9)
lamp7 = Lampada("Sonoff", 120, 9)
lamp8 = Lampada("Osram", 120, 9)
lamp9 = Lampada("GE", 120, 9)
lamp10 = Lampada("Cree", 120, 9)
lamp11 = Lampada("EcoSmart", 120, 9)
lamp12 = Lampada("Hue", 120, 9)
lamp13 = Lampada("Crompton", 120, 9)


sala = Comodo("Sala")
sala.adicionar_lampada(lamp1)
sala.adicionar_lampada(lamp2)

garagem = Comodo("Garagem")
garagem.adicionar_lampada(lamp3)
garagem.adicionar_lampada(lamp4)

quarto1 = Comodo("Quarto1")
quarto1.adicionar_lampada(lamp5)

quarto2 = Comodo("Quarto2")
quarto2.adicionar_lampada(lamp6)

quarto3 = Comodo("Quarto3")
quarto3.adicionar_lampada(lamp7)

quarto4 = Comodo("Quarto4")
quarto4.adicionar_lampada(lamp8)

banheiro1 = Comodo("Banheiro1")
banheiro1.adicionar_lampada(lamp9)

banheiro2 = Comodo("Banheiro2")
banheiro2.adicionar_lampada(lamp10)

cozinha = Comodo("Cozinha")
cozinha.adicionar_lampada(lamp11)

varanda = Comodo("Varanda")
varanda.adicionar_lampada(lamp12)

corredor1 = Comodo("Corredor1")


alexa = AssistenteVirtual("Alexa", 10)

alexa.AdicionarComodoNovo(sala)
alexa.AdicionarComodoNovo(garagem)
alexa.AdicionarComodoNovo(quarto1)
alexa.AdicionarComodoNovo(quarto2)
alexa.AdicionarComodoNovo(quarto3)
alexa.AdicionarComodoNovo(quarto4)
alexa.AdicionarComodoNovo(banheiro1)
alexa.AdicionarComodoNovo(banheiro2)
alexa.AdicionarComodoNovo(cozinha)
alexa.AdicionarComodoNovo(varanda)

alexa.executar("Desligar todas as lampadas da Garagem")








# alexa.executar("Ligar todas as lampadas da casa")
# alexa.executar("Desligar todas as lampadas da garagem")
# alexa.executar("Desligar todas as lampadas da sala")
# alexa.executar("Ligar todas as lampadas da casa")