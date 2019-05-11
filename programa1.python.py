#ingrese datos
def ingreso():
    x=True
    while x==True:
      a1=int(input("ingrese cantidad:"))
      a2=int(input("ingrese cantidad:"))
      print("****************************")
      print("que opcion esea realizar?")
      print("1.sumar")
      print("2.restar")
      print("3.multiplicar")
      print("4.dividir")
      opcion=int(input("ingrese nuemro de opcion"))
      if opcion==1:
          suma(a1,a2)
      elif opcion ==2:
          resta(a1,a2)
      elif opcion ==3:
          multiplicacion(a1,a2)
      elif opcion ==4:
          division(a1,a2)
      #desea seguir operando o no
      x=input("desea seguir operando:")
      if decidir.lower()=="si":
          ingreso()
      elif decidir.lower()=="no":
          print("****************************")
          print("finalizar programa")
          x=False
          
    #sumar
def suma(a1,a2):
    total =a1+a2
    print(total)
    #restar
def resta(a1,a2):
    total=a1-a2
    print(total) 
    #multiplicar
def multiplicacion(a1,a2):
    total=a1*a2
    print(total)
    #dividir
def division(a1,a2):
    total=a1/a2
    print(total)
ingreso()



