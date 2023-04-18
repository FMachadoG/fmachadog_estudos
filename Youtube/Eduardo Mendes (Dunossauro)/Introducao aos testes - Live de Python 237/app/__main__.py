from app.app import converte_F_pra_C, converte_C_pra_F

# INPUT
temperatura = float(input(' - Qual a temperatura: '))
opcao = input(' - Para Celsius(C) ou Fahrenheit(F)?: ').upper()

# OPCOES
match opcao:
    case 'F':
        fahrenheit = converte_C_pra_F(c_temp=temperatura)
        print(f'A temperatura convertida para Fahrenheit é: {fahrenheit}')

    case 'C':
        celsius = converte_F_pra_C(f_temp=temperatura)
        print(f'A temperatura convertida para Celsius é: {celsius}')

    case _:
        print('Valor informado é inválido!')
