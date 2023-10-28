
import pytest
import random as rand
        

class Angry_teacher():
    def __init__(self,n,t) -> None:
        #numero de casos
        self.t=t
        #numero de estudiantes
        self.n=n
        #lista de objetos assistance
        self.a=[]


    #Funcion para generar datos de cada caso
    #Modifica el atributo self.a
    def generator(self):
        for i in range(self.t):
            x=rand.randint(1,self.n)
            y=[]
            for j in range(self.n):
                c=rand.randint(-100,100)
                y.append(c)
            self.a.append(Assistance(x,y))
    #Metodo para examinar el funcionamiento de la solucion
    def tests(self):
        for i in range(self.t):
            p=self.a[i].threshold()
            print(self.a[i])
            if len(self.a[i].time)>=self.a[i].k:
                #Threshold deberia dar YES
                assert p=="YES"
            else:     
                assert p=="NO"
           

    



class Assistance():
    def __init__(self,k,times_array) -> None:
        #Numero minimo de estudiantes para dar la clase
        self.k=k
        #Arreglo de tiempos de llegada
        self.times_array=times_array
        #Lista para saber cuantos estudiantes llegaron a tiempo
        self.time=[]
        
    #Metodo para determinar si la clase se da o no
    def threshold(self):
        a="NO"
        self.time=[x for x in self.times_array if x<=0]
        l=len(self.time)
        print(self.time)
        print(l)
        if l>=self.k:
            a="YES"
        return a
    def __str__(self) -> None:
        return(f"Para la clase se esperan minimo {self.k} estudiantes y llegaron a tiempo {len(self.time)} ")
        

#Prueba de 500 estudiantes en 10 casos aleatorios
testObject=Angry_teacher(500,10)
testObject.generator()
testObject.tests()
    


        




