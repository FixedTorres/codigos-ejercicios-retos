igual, aux = 0, 0

texto = input("Ingrese la palabra que desea evaluar: ")

for ind in reversed(range(0, len(texto))): 
  if texto[ind] == texto[aux]:
    igual += 1
  aux += 1
  
if len(texto) == igual:
  print("El texto es palindromo :D")
else:
  print("El texto no es palindromo :(")