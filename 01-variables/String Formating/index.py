# Case 1 ( Mais usada )
name = "Hitechline"
gretting = f"Olá, {name}"

print(gretting)

# Case 2 using Formating

name = "Hitechline & Hostaqui"
gretting = "Bem vindos a: {}"
with_name = gretting.format(name)

print(with_name)

# Case 3 using a longer template

frase = "Olá somos da empresa {} e {}"
formatted = frase.format('Hitechline Tecnologia LTDA','Hostaqui WebHosting')

print(formatted)