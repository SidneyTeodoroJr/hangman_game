import random

# Lista de palavras para escolher
palavras = ["python", "programacao", "computador", "teclado", "mouse", "tela", "internet", "software", "hardware", "programador", "desenvolvimento", "linguagem", "codigo", "algoritmo", "banco", "dados", "tecnologia", "redes", "cpu", "dedo", "boca", "teatro", "sistema", "servidor", "cliente", "web", "mobile", "game", "java", "javascript", "php", "html", "mesa", "computador", "livro", "caneta", "cachorro", "gato", "borboleta", "abelha", "formiga", "sapato", "camisa", "celular", "televisão", "planta", "rato", "maria", "pedro", "paula", "sidney", "teodoro", "eduardo"]

# Palavra secreta a ser adivinhada
palavra = random.choice(palavras)

# Lista de letras já escolhidas pelo jogador
letras_escolhidas = []

# Número máximo de tentativas
max_tentativas = 6

# Inicializa a variável de tentativas
tentativas = 0

# Inicializa a variável de acertos
acertos = 0

# Cria uma lista com traços correspondentes às letras da palavra
palavra_escondida = ["_" for letra in palavra]

# Loop principal do jogo
while tentativas < max_tentativas and acertos < len(palavra):

    # Imprime a palavra escondida na tela
    print(" ".join(palavra_escondida))

    # Solicita uma letra ao jogador
    letra = input("Digite uma letra em minúsculo: ").lower()

    # Verifica se a letra já foi escolhida antes
    if letra in letras_escolhidas:
        print("Você já escolheu essa letra antes. Tente outra.")
        continue

    # Adiciona a letra à lista de letras escolhidas
    letras_escolhidas.append(letra)

    # Verifica se a letra está na palavra secreta
    if letra in palavra:

        # Atualiza a palavra escondida com a letra encontrada
        for i in range(len(palavra)):
            if palavra[i] == letra:
                palavra_escondida[i] = letra

        acertos += 1
        print("Letra encontrada!")

    else:
        tentativas += 1
        print("Letra não encontrada. Você tem mais {} tentativa(s).".format(max_tentativas - tentativas))

# Verifica se o jogador ganhou ou perdeu
if acertos == len(palavra):
    print("Parabéns! Você acertou a palavra {}.".format(palavra))
else:
    print("Que pena. Você não conseguiu acertar a palavra {}.".format(palavra))
