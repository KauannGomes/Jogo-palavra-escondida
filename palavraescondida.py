from os import system
palavra = 'perfume'
letras_acertadas = ''
tentativa = 0
while True:
    
    palavra_correta = False
    try:
        letra_digitada = input('Digite uma letra: ')
        if len(letra_digitada) > 1:
            print('Por favor digite apenas uma letra')
        elif letra_digitada.isalpha() == False:
            print('Por favor digite uma letra do alfabeto')  
        else:
            pass
        if letra_digitada in palavra:
            letras_acertadas += letra_digitada
        palavra_formada = ''
        for letra in palavra:
            if letra in letras_acertadas:
                palavra_formada += letra
            else:
                 palavra_formada += '*'
        print(palavra_formada)


        tentativa += 1
        if palavra_formada == palavra:
            palavra_correta = True
            system('cls')
        if palavra_correta:

            break
    except :
        print(f'erro ')
    
print(f'Voce descobriu a palavra "{palavra}" \nO total de tentativas foi: {tentativa} tentativas.')