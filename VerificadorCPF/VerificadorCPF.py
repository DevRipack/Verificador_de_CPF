cpf_recebido = input("Digite seu cpf:").replace('.','').replace('.','').replace('-','')
nove_digitos = cpf_recebido[:9]
dez_digitos = cpf_recebido[:10]
contador_regressivo = 10
resultado = 0
contador_regressivo2 = 11
resultado2 = 0

for digito in nove_digitos:
	resultado += int(digito)*contador_regressivo
	contador_regressivo -= 1
	digito = resultado * 10 % 10
	
print('-=' *22)
if digito <= 9:
    print('Resultado é 0')
else:
    print('resultado é o valor da conta')
    
print(f'O primeiro digito do CPF verificado é {digito}')

for digito in dez_digitos:
	resultado2 += int(digito)*contador_regressivo2
	contador_regressivo2 -= 1
 	
digito2=(resultado2*10)%11
if digito2 > 9:
    print('Valido')
else:
    print('resultado é o valor da conta')
print('-='*22)    
print(f'O segundo digito verificado do CPF é {digito2}')

cpf_gerado = f'{nove_digitos},{digito},{digito2}'
if cpf_recebido == cpf_gerado:
    print(f'CPF valido {cpf_recebido}')
else:
    print(f'CPF não valido {cpf_recebido}')
	
	
	

    


