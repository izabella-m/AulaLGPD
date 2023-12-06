def cadastro():
    while True:
        nome = input('Digite o seu nome (ou 0 para encerrar): ')

        if nome == "0":
            break 
        idade = int(input('Digite sua idade: '))
        sexo = input('Digite o seu sexo (M ou F): ')
        telefone = input('Digite o seu telefone: ')

        with open('meu_nome.txt', 'a') as file:
            file.write(f'{nome}|{idade}|{sexo}|{telefone}\n')


def busca_usuario_pelo_nome(nome_procurado):
    with open('meu_nome.txt', 'r') as file:
        for linha in file:
            (nome, idade, sexo, telefone) = linha.split('|')

            if nome == nome_procurado or nome.find(nome_procurado) != -1:
                return [nome, idade, sexo, telefone]
    return []


if __name__ == "__main__":
    cadastro()

    usuarios_encontrados = busca_usuario_pelo_nome("Leonardo")

    if usuarios_encontrados:
        print(usuarios_encontrados)
    else:
        print("Nenhum usuário encontrado")