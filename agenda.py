def adicionar_contato(contatos):
    print("\nPreencha os dados do contato")
    nome = input("Nome do contato: ")
    telefone = input("DDD + Número: ")
    email = input("Email: ")
    favorito = False
    contatos.append([nome, telefone, email, favorito])
    print(f"\nContato {nome} adicionado.")
    return

def contatos_cadastrados(contatos):
    print("\n Lista de Contatos")
    for indice, contatos in enumerate(contatos, start=1):
        print(f"{indice}. Nome: {contatos[0]} - Telefone: {contatos[1]} - Email: {contatos[2]}")
    return

def editar_contato(contatos):
    contatos_cadastrados(contatos)
    indice_contato = int(input("Qual contato deseja alterar? ")) -1
    contato = contatos[indice_contato]
    print("1. Editar nome.")
    print("2. Editar DDD/número.")
    print("3. Editar email.") 
    print("4. Sair de Edição.")
    opcao_editar = input("Qual alteração deseja fazer? ")

    if opcao_editar == "1":
        novo_nome = input("\nDgite o novo nome: ")
        contato[0] = novo_nome

    if opcao_editar == "2":
        novo_telefone = input("\n Digite o novo telefone: ")
        contato[1] = novo_telefone

    if opcao_editar == "3":
        novo_email = input("\nDigite o novo email: ")
        contato[2] = novo_email

    if opcao_editar == "4":
         print("Saindo de edição...")
    return

def marcar_desmarcar_favorito(contatos):
    contatos_cadastrados(contatos)
    indice_contato = int(input("\nDigite o número do contato que deseja marcar/desmarcar como favorito: ")) - 1
    contato = contatos[indice_contato]

    if contato[3]:
        contato[3] = False
        print(f"\nContato {contato[0]} desmarcado como favorito!")
    else:
        contato[3] = True
        print(f"\nContato {contato[0]} marcado como favorito!")

def contatos_favoritos(contatos):
    print("\nLista de Contatos Favoritos") 
    for indice, contato in enumerate(contatos, start=1):
        if contato[3]:
            print(f"{indice}. Nome: {contato[0]} - Telefone: {contato[1]} - Email: {contato[2]}")
    return

def excluir_contato(contatos):
    contatos_cadastrados(contatos)
    indice_contato = int(input("\nQual contato deseja excluir? ")) -1
    contato = contatos[indice_contato]
    contatos.remove(contato)
    print("O contato foi excluído.")
    return
    

contatos = []

while True:
    print("\n Menu - Agenda de Contatos")
    print("1. Adicionar um contato")
    print("2. Contatos cadastrados")
    print("3. Editar um contato")
    print("4. Marcar/Desmarcar um contato como favorito")
    print("5. Contatos favoritos")
    print("6. Apagar um contato")
    print("7. Sair da Agenda")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_contato(contatos)
    
    if opcao == "2":
        contatos_cadastrados(contatos)

    if opcao == "3":
        editar_contato(contatos)

    if opcao == "4":
        marcar_desmarcar_favorito(contatos)

    if opcao == "5":
        contatos_favoritos(contatos)

    if opcao == "6":
        excluir_contato(contatos)

    if opcao == "7":
        print("Saindo da Agenda...")
        break

