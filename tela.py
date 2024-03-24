import tkinter as tk
import numpy as np
import generateletters
import string
import Madaline

alfabet = string.ascii_uppercase
# Configurações da tela
largura = 12
altura = 12
tamanho_pixel = 30  # Tamanho em pixels de cada quadrado na grade

def criar_grid():
    # Desenha as linhas verticais do grid
    for i in range(1, largura):
        canvas.create_line(i * tamanho_pixel, 0, i * tamanho_pixel, altura * tamanho_pixel)

    # Desenha as linhas horizontais do grid
    for j in range(1, altura+1):
        canvas.create_line(0, j * tamanho_pixel, largura * tamanho_pixel, j * tamanho_pixel)

# Função para desenhar um quadrado na posição (x, y)
def desenhar_quadrado(x, y):
    canvas.create_rectangle(x * tamanho_pixel, y * tamanho_pixel,
                            (x + 1) * tamanho_pixel, (y + 1) * tamanho_pixel,
                            fill='black')
    matriz[y][x] = 1  # Atualiza a matriz para representar o quadrado desenhado

# Função para salvar a matriz
def salvar_matriz():
    matriz_numpy = np.array(matriz)
    matriz_lista = matriz_numpy.flatten()
    for j in range(len(matriz_lista)):
        if(matriz_lista[j]==0):
            matriz_lista[j]=-1
        else:
            matriz_lista[j]=1
    print('Matriz salva com sucesso!')
    print(matriz_lista)
    letra = Madaline.teste(matriz_lista,treino[0],treino[1],treino[2])
    label_teste.config(text=f"Letra Identificada:\n{letra}")
    return matriz_lista

def limpar_tela():
    canvas.delete('all')  # Remove todos os elementos desenhados na tela
    criar_grid()
    # Reinicializa a matriz para representar uma tela em branco (12x12 de zeros)
    global matriz
    matriz = [[0 for _ in range(largura)] for _ in range(altura)]
    label_teste.config(text="Letra Identificada: ")
    print('Tela limpa!')

def treinar():
    with open('Ent.txt','w') as iniciando:
       iniciando.write("") 
    generateletters.letra_pra_matriz(alfabet,'arial')
    global treino
    treino = Madaline.treino()
    label_treino.config(text="Treinada!")
    print("Treinar alfabeto")

# Inicializa a janela e a tela
janela = tk.Tk()
janela.title('Tela de Desenho 12x12')

canvas = tk.Canvas(janela, width=largura * tamanho_pixel, height=altura * tamanho_pixel)
canvas.grid(row=0, column=0, padx=0, pady=(0,0))
# canvas.pack()
#cria o grid
criar_grid()

# Inicializa a matriz para representar a tela (12x12)
matriz = [[0 for _ in range(largura)] for _ in range(altura)]

# Evento de clique do mouse para desenhar um quadrado na posição clicada
def clique_mouse(event):
    x = event.x // tamanho_pixel
    y = event.y // tamanho_pixel
    desenhar_quadrado(x, y)
    # print(matriz)  # Exibe a matriz após cada desenho (opcional)

canvas.bind('<Button-1>', clique_mouse)

# Cria uma label para exibir a letra identificada
label_teste = tk.Label(janela, text='Letra Identificada: ')
label_teste.grid(row=1, column=0, padx=(0,250), pady=(0,60))
# label_teste.pack()

# Botão para salvar a matriz
botao_salvar = tk.Button(janela, text='Identificar letra', command=salvar_matriz)
botao_salvar.grid(row=1, column=0, padx=(0,250), pady=(20,20))
# botao_salvar.pack()

botao_limpar = tk.Button(janela, text='Limpar Tela', command=limpar_tela)
botao_limpar.grid(row=1, column=0, padx=(0,0), pady=(20,20))
# botao_limpar.pack()

botao_treinar = tk.Button(janela, text='Treinar Alfabeto', command=treinar)
botao_treinar.grid(row=1, column=0, padx=(250,0), pady=(20,20))
# botao_treinar.pack()

# Cria uma label para exibir a letra identificada
label_treino = tk.Label(janela, text='Não Treinada')
label_treino.grid(row=1, column=0, padx=(250,0), pady=(0,60))
# label_treino.pack()

janela.mainloop()
