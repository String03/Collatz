numero = int(input("Ingresar un número \n"))

def collatz(n):
  result = [n]
  while n > 1:
    if (n % 2) == 0:
      n = (n/2)
    else:
      n = (n*3 + 1)
    
    result.append(n)
 
  
  print(len(result) - 1)

collatz(numero)
