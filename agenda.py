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

#Função para editar um contato
def edit_contact():
  see_contact()
  if not contacts:
    print("Não há contatos na lista.")
    return
  try:
    index = int(input("Selecione o contato que deseja editar pelo número: ")) - 1

    if index < 0 or index >= len(contacts):
      print("Número de contato inválido!")
      return
    
    contact = contacts[index]

    print(f"\nEditando contato: {contact}")

    new_nome = input(f"Nome ({contact.nome}): ") or contact.nome
    new_telefone = input(f"Telefone ({contact.telefone}): ") or contact.telefone
    new_email = input(f"Email ({contact.email}): ") or contact.email
    favorito_input = input(f"Favorito ({'Sim' if contact.favorito else 'Não'})? 1-Sim 2-Não: ")
    new_favorito = True if favorito_input == "1" else False if favorito_input =="2" else contact.favorito

    contact.nome = new_nome
    contact.telefone = new_telefone
    contact.email = new_email
    contact.favorito = new_favorito

    print(f"Contato {new_nome} atualizado com sucesso!")

  except ValueError:
    print("Por favor, digite um número válido.")


def fav_contact():
  see_contact()
  if not contacts:
    print("Não há contatos na lista.")
    return
  try:
    index = int(input("Selecione o contato que deseja favoritar pelo número: ")) - 1

    if index < 0 or index >= len(contacts):
      print("Número de contato inválido!")
      return
    
    contact = contacts[index]

    if contact.favorito:
      verify = input("Este contato já é um favorito, deseja desfavoritar? 1-Sim 2-Não: ")
      if verify == "1":
        contact.favorito = False
        print(f" Contato {contact.nome} desfavoritado com sucesso!")
      else:
        return

    else:
      contact.favorito = True
      print(f"Contato {contact.nome} favoritado com sucesso!")

  except ValueError:
    print("Por favor digite um número valido.")


def see_fav():
  favorites = [contact for contact in contacts if contact.favorito]
  if not favorites:
    print("Nenhum contato favorito encontrado.")
    return
  
  print("\n------------Contatos Favoritos------------")
  for i, contact in enumerate(favorites, 1):
    print(f"{i}. {contact}")
  print("------------------------")

def del_contact():
  see_contact()
  if not contacts:
    print("Não há contatos na lista.")
    return
  try:
    index = int(input("Selecione o contato que deseja deletar pelo número: ")) - 1

    if index < 0 or index >= len(contacts):
      print("Número de contato inválido!")
      return

    contact = contacts.pop(index)
    print(f"Contato {contact.nome} removido com sucesso!")
  
  except ValueError:
    print("Por favor, digite um número válido")
    

while True:
  print("Olá, bem vindo a sua agenda, o que deseja fazer?" 
        "\n" "1 - Adicionar um contato"
        "\n" "2 - Visualizar lista de contatos"
        "\n" "3 - Editar um contato"
        "\n" "4 - Marcar/desmarcar um contato como favorito"
        "\n" "5 - Ver contatos Favoritos"
        "\n" "6 - Apagar um contato"
        "\n" "0 - Sair da agenda")

  opcao = input("Digite sua opção:")

  match opcao:
    case "1":
      add_contact()

    case "2":
      see_contact()

    case "3":
      edit_contact()

    case "4":
      fav_contact()

    case "5":
      see_fav()

    case "6":
      del_contact()

    case "0":
      print("Saindo da agenda...")
      break

    case _:
      print("Opção inválida!")