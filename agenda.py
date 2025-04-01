#Definição de classe e lista
class Contato:
  def __init__(self, nome, telefone, email="", favorito=False):
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.favorito = favorito

  def __str__(self):
    return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Favorito: {'Sim' if self.favorito else 'Não'}"

#Lista para armazenar
contatos = []

#função para add contatos
def add_contato():
  nome = input("Insira o nome do contato: ")
  telefone = input("Insira o telefone: ")
  email = input("Insira o email: ")
  favorito_input = input("Marcar como favorito? 1-Sim 2-Não: ")

  favorito = True if favorito_input == "1" else False

  novo_contato = Contato(nome, telefone, email, favorito)

  contatos.append(novo_contato)

  print(f"Contato {nome} adicionado com sucesso!")


print("Olá, bem vindo a sua agenda, o que deseja fazer?" 
      "\n" "1 - Adicionar um contato"
      "\n" "2 - Visualizar lista de contatos"
      "\n" "3 - Editar um contato"
      "\n" "4 - Marcar um contato como favorito"
      "\n" "5 - Ver contatos Favoritos"
      "\n" "6 - Apagar um contato")

opcao = input("Digite sua opção:")

match opcao:
  case "1":
    add_contato()