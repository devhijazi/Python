#Case 1
name = input("Digite seu Login: ")
print('Olá',name,'você foi logado com sucesso!')

#Case 2 
size_input = input("Qual o tamanho da sua casa? (em pés quadrados): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8

print(f"{square_feet} em metros quadrados é {square_metres:.2f} metros quadrados.")