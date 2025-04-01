#Definição de classe e lista
class Contact:
  def __init__(self, nome, telefone, email="", favorito=False):
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.favorito = favorito

  def __str__(self):
    return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}, Favorito: {'Sim' if self.favorito else 'Não'}"

#Lista para armazenar
contacts = []

#função para add contatos
def add_contact():
  nome = input("Insira o nome do contato: ")
  telefone = input("Insira o telefone: ")
  email = input("Insira o email: ")
  favorito_input = input("Marcar como favorito? 1-Sim 2-Não: ")

  favorito = True if favorito_input == "1" else False

  new_contact = Contact(nome, telefone, email, favorito)

  contacts.append(new_contact)

  print(f"Contato {nome} adicionado com sucesso!")

#Função para mostrar lista de contatos
def see_contact():
  if not contacts:
    print("Nenhum contato cadastrado.")
    return
  
  print("\n---------- Lista de contatos----------")
  for i, contact in enumerate(contacts, 1):
    print(f"{i}.{contact}")
  print("-----------------------------")





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
    add_contact()

  case "2":
    see_contact()