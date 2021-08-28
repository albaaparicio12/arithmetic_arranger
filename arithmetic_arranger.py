#Funcion para convertir un array en un string
def convertToString(lista):
  cad = ""
  for i in lista:
    cad += str(i)
  return cad

#Funcion que realiza la operacion
def calcularResultado(problem):
  if(problem[1] == "+"):
    return int(problem[0]) + int(problem[2])
  elif(problem[1] == "-"):
    return int(problem[0]) - int(problem[2])
  else:    
    return "Error: Operator must be '+' or '-'."

#Funcion que calcula la longitud de una linea, por ejemplo, si el numero mas grande
#es el denominador con 3 cifras entonces la linea debe medir 3 espacios + 2, uno mas 
#para el simbolo y otro mas para dejar un espacio entre el simbolo y el numero
def lengDigits(problem):
  number1 = len(problem[0])
  number2 = len(problem[2])
  if(number1 >= number2):
      return number1+2
  else:
    return number2+2

#Funcion que factoriza con los espacios correspondientes y en el orden debido una operacion
def factorizarLinea(problem,arriba,abajo,linea,resultado,error,last = False):
  arriba.append(' '*(lengDigits(problem)- len(problem[0]))) #deja los espacios en blanco correspondientes de acuerdo con la longitud del numero
  if(problem[0].isdigit()):
    if(len(problem[0])>4):
      error.append("Error: Numbers cannot be more than four digits.")
      return error
    else:
      #añade el numerador
      arriba.append(problem[0])
  else:
    error.append("Error: Numbers must only contain digits.")
    return error

  if((problem[1] == "-") or (problem[1] == "+")): 
    #añade el simbolo y los espacios
    abajo.append(problem[1])
    abajo.append(' '*(lengDigits(problem)-len(problem[2])-1))
  else:
    error.append("Error: Operator must be '+' or '-'.")
    return error

  if(problem[2].isdigit()):
    if(len(problem[2])>4):
      error.append("Error: Numbers cannot be more than four digits.")
      return error
    else:
      #añade el denominador
      abajo.append(problem[2])    
  else:
    error.append("Error: Numbers must only contain digits.")
    return error
  #añade la linea de operacion
  linea.append('-'*lengDigits(problem))
  #Si no es la ultima operacion añade espacios entre operacion y operacion
  if(last == False):
    arriba.append('    ')
    abajo.append('    ')
    linea.append('    ')


def arithmetic_arranger(problems,result = False):
  arriba = [];
  abajo = [];
  linea = [];
  resultado = [];
  error = []
  if(len(problems) > 5): #Si en el array de problemas hay mas de 5 se produce un error
    return "Error: Too many problems."
  for index,problem in enumerate(problems):
    problem = problem.split(" ");
    if(index == len(problems)-1): 
      #Se comprueba si el problema es el ultimo de la lista para no poner espacios en blanco al final
      factorizarLinea(problem,arriba,abajo,linea,resultado,error,True)
    else:
      factorizarLinea(problem,arriba,abajo,linea,resultado,error,False)
    if(len(error) > 0):
      return error[0]
    
    if(result):
      #Si se especifica que se muestren los resultados de cada operacion se calculan aqui y se muestran con los espacios correspondientes
      numResult = calcularResultado(problem)
      resultado.append(' '*(lengDigits(problem)-len(str(numResult))))
      resultado.append(numResult)
      if(index != len(problems)-1):
        resultado.append('    ')
    

  if(result == False):
    stringFinal = convertToString(arriba) +"\n"+ convertToString(abajo) + "\n" + convertToString(linea)
  else:
    stringFinal = convertToString(arriba) +"\n"+ convertToString(abajo) + "\n" + convertToString(linea) + "\n" + convertToString(resultado)
  
  return stringFinal

  
  