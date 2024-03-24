from PIL import Image, ImageDraw, ImageFont
import random
import string

def letra_pra_matriz(alfabeto,fonte):
    # Crie uma imagem em branco com fundo branco
    width,height = 12,12
    img = Image.new('RGB', (width, height), color = (255, 255, 255))

    d = ImageDraw.Draw(img)

    # Especifique a fonte e o tamanho da fonte. 
    font = ImageFont.truetype(fonte, 12)

    text = alfabeto
    cont = 0
    for i in range(len(text)):

        # Resetando o quadro para a proxima letra
        img = Image.new('RGB', (width, height), color = (255, 255, 255))
        d = ImageDraw.Draw(img)

        # Obtenha as dimensões do texto
        textwidth, textheight = font.getbbox(text[i])[2:4]

        # Calcule a posição x, y para centralizar o texto
        x = (img.width - textwidth) / 2
        y = (img.height - textheight) / 2

        # Desenhe o texto
        d.text((x, y), text[i], fill=(0,0,0), font=font)
        
        # Salve a imagem
        # img.save(f'letra{cont}.png')
        # cont+=1
        # Convertendo para preto e branco
        im = img.convert("L")
        # Transformando em matriz
        mat = list(im.getdata())
        for j in range((width*height)):
            if(mat[j]==255):
                mat[j]=-1
            else:
                mat[j]=1
        mat2 = create_vars(mat)
        mat3 = create_vars(mat)
        mat4 = other_font(text[i],'times')
        print(mat)
        insertxt(mat)
        # insertxt(mat2)
        # insertxt(mat3)
        # insertxt(mat4)

def insertxt(matriz):
    with open('Ent.txt','a') as entradas:
        for z in range(len(matriz)):
            entradas.write(f'{matriz[z]} ')
        entradas.write('\n')

def create_vars(matriz):
    cont = 0
    while(cont<4):
        indice = random.randint(0,len(matriz)-1)
        if(matriz[indice]==1):
            matriz[indice] = -1
            cont+=1
    return matriz

def other_font(alfabeto,fonte):
    # Crie uma imagem em branco com fundo branco
    width,height = 12,12
    img = Image.new('RGB', (width, height), color = (255, 255, 255))

    d = ImageDraw.Draw(img)

    # Especifique a fonte e o tamanho da fonte. 
    font = ImageFont.truetype(fonte, 12)

    text = alfabeto
    cont = 0

    # Obtenha as dimensões do texto
    textwidth, textheight = font.getbbox(text)[2:4]

    # Calcule a posição x, y para centralizar o texto
    x = (img.width - textwidth) / 2
    y = (img.height - textheight) / 2

    # Desenhe o texto
    d.text((x, y), text, fill=(0,0,0), font=font)
        
    # Salve a imagem
    # img.save(f'letra{cont}.png')
    # cont+=1
    # Convertendo para preto e branco
    im = img.convert("L")
    # Transformando em matriz
    mat = list(im.getdata())
    for j in range((width*height)):
        if(mat[j]==255):
            mat[j]=-1
        else:
            mat[j]=1
    return mat

# letra_pra_matriz(string.ascii_uppercase,'arial')
#     # im.save('letrabw.png')
