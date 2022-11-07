# ---------- WHILE LOOP ----------#
number = 7

while True:
  user_input = input('Você deseja jogar ? (S/n')

  if user_input == "n":
    break

  user_input =int(input('Escolha um número mágico: '))
  if user_input == number:
    print('Parabéns você é um fodendo genio')
  elif abs(user_input - number) == 1:
    print('Não pode ser 1')
  else: 
    print('Ta errado burrão')
