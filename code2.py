from scipy import stats
import numpy as np 
from queue import Queue
import math
import random

class Client:
    #arrival time, preparation time and departure time
    def __init__(self,t_a, t_p, t_d):
        self.T_A = t_a
        self.T_P = t_p
        self.T_D = t_d

class KojosKitchen:    
    def __init__(self):
        self.t = 0 
        self.T = 660  
        self.test = False  
    def Simulation2Workers(self): 
        #time variables
        self.t = 0
        self.t_A = 0
        self.t_D1 = math.inf
        self.t_D2 = math.inf 
        
        #counting variables
        self.NA = 0
        self.ND1 =0
        self.ND2 = 0
        
        #state variables
        self.queue = Queue()
        self.workers = [ Client(self.t_A,None,math.inf)  for _ in range(0,2)]
        
        self.n = 0
        self.result = []
        self.test = False
        
        self.t_A = ExponentialRandomVariable(0.5) 
        
        print("##################################################################################")
        print("##################################################################################")
        print("Inicio de la simulacion con dos Trabajadores")
        print("Primer Tiempo de Arribo :" + str(self.t_A)) 
        
        while (self.t < self.T or  self.n > 0):
            print("##################################################################################")
            print("Escoger evento  a desarrollar")
            print("Tiempo actual:"+ str(self.t))
            print("Cantidad de cliente en el sitema: " + str(self.n))
            if self.RushHour():
                print("Estamos en Horario Pico")
            min_ = min(self.t_A,self.t_D1,self.t_D2)  
            
            if min_== self.t_A and self.t_A <= self.T:
                print("Inicio de Evento de Arribo")
                self.ArrivalEvent() 
            elif min_ == self.t_A and self.t_A != math.inf and self.t_A > self.T:
                print(" Inicio del Evento de arribo fuera de tiempo: ")
                self.t_A = math.inf    
                if self.n ==0:
                    print("Como la cantidad de Clientes es 0 y culminó el tiempo de arribo se termina el proceso de simulación")
                    print("\n")
                    break
                    
            elif min_ != self.t_A and min_ <= self.T:
                print("Inicio del Evento Salida del Sistema")
                self.ExitEvent(min_)
            elif min_ != self.t_A and self.t_A > self.T  and self.n > 0:
                print("Salida de un cliente luego de cerrar el sistema")
                self.ClosingEvent(min_) 
                if self.n == 0:
                    print("Como la cantidad de Clientes es 0 y culminó el tiempo de arribo se termina el proceso de simulación")
                    print("\n")
            print("\n")
            print("Valores de Salida de Los clientes que estan siendo atendidos")             
            print("Cantidad de Clientes: " + str(self.n))         
            print("tiempo de salida cliente en servidor 1: "+ str(self.t_D1))
            print("tiempo de salida cliente en servidor 2:"+ str(self.t_D2))
                       
    def Simulation3Workers(self):
        #time variables
        self.t = 0
        self.t_A = 0
        self.t_D1 = math.inf
        self.t_D2 = math.inf
        self.t_D3 = math.inf
        #counting variables
        self.NA = 0
        self.ND1 =0
        self.ND2 = 0
        self.ND3 = 0
        
        #state variables
        self.queue = Queue()
        self.workers = [ Client(self.t_A,math.inf,math.inf)  for _ in range(0,3)]
        self.n = 0
        self.test = True
        self.result= []
       
        #primera iteracion
        self.t_A = ExponentialRandomVariable(0.5) 
        print("##################################################################################")
        print("##################################################################################")
        print("Inicio de la simulacion con 3 Trabajadores")
        print("Primer Tiempo de Arribo :" + str(self.t_A)) 
        while (self.t <= self.T or  self.n > 0):
            print("##################################################################################")
            print("Escoger evento  a desarrollar")
            print("Tiempo actual:"+ str(self.t))
            print("Cantidad de cliente en el sitema: " + str(self.n))
            
            if self.RushHour():
                print("Estamos en Horario Pico")
            min_ = min(self.t_D1,self.t_D2,self.t_A, self.t_D3) 
     
            if min_== self.t_A and self.t_A <= self.T:
                print("Inicio de Evento de Arribo")
                self.ArrivalEvent() 
            elif min_ == self.t_A and self.t_A != math.inf and self.t_A > self.T:
                print(" Inicio del Evento de arribo fuera de tiempo: ")
                self.t_A = math.inf    
                if self.n ==0:
                    print("Como la cantidad de Clientes es 0 y culminó el tiempo de arribo se termina el proceso de simulación")
                    print("\n")
                    break      
            elif min_ != self.t_A and min_ <= self.T:
                print("Inicio del Evento Salida del Sistema")
                self.ExitEvent(min_)
            elif min_ != self.t_A and self.t_A > self.T  and self.n > 0:
                print("Salida de un cliente luego de cerrar el sistema")
                self.ClosingEvent(min_) 
                if self.n == 0:
                    print("Como la cantidad de Clientes es 0 y culminó el tiempo de arribo se termina el proceso de simulación")
                    print("\n")
            print("\n")
            print("Valores de Salida de Los clientes que estan siendo atendidos")             
            print("Cantidad de Clientes: " + str(self.n))         
            print("tiempo de salida cliente en servidor 1: "+ str(self.t_D1))
            print("tiempo de salida cliente en servidor 2:"+ str(self.t_D2))
            print("tiempo de salida cliente en servidor 3:"+ str(self.t_D3))  
            
    
    def ArrivalEvent(self):
        self.t = self.t_A
        self.n += 1
        print("tiempo actual en arribo : "+ str(self.t))
        self.NA = self.NA + 1    
        lambda_= 0.2
        if self.RushHour():
            lambda_ = 0.5   
        self.t_A =  self.t_A + ExponentialRandomVariable(lambda_)
        print("nuevo tiempo de arribo generado: "+ str(self.t_A))
        
        if self.t_D1 == math.inf:
            self.workers[0].T_A= self.t
            self.UpdateValuesClient(0)
            self.t_D1 = self.workers[0].T_D
            print("El cliente pasa a ser atendido por el Trabajador 1 y su tiempo de salida: "+ str(self.t_D1))  
            
        elif self.t_D2 == math.inf:
            self.workers[1].T_A= self.t
            self.UpdateValuesClient(1)
            self.t_D2 = self.workers[1].T_D
            print("El cliente pasa a ser atendido por el Trabajador 2 y su tiempo de salida: "+ str(self.t_D2))  
        elif self.test and self.RushHour() and self.t_D3 == math.inf:
            self.workers[2].T_A= self.t
            self.UpdateValuesClient(2)
            self.t_D3 = self.workers[2].T_D
            print("El cliente pasa a ser atendido por el Trabajador 3 y su tiempo de salida: "+ str(self.t_D3))      
        else:
            self.queue.put( Client(self.t_A,math.inf,math.inf) )   
            print("El cliente pasa a la cola de espera")   
            
            
    def ClosingEvent(self,min_): 
        self.n -= 1 
        if min_ == self.t_D1:
            print("Abandona el cliente que está siendo atendido por el Trabajador 1 su T_D: " + str(min_ ))
            self.t = min_
            self.ND1 += 1
            self.result.append(self.workers[0]) 
            if not self.queue.empty():
                self.workers[0]= self.queue.get()
                print("El primer cliente de la cola pasa a ser atendido por el Trabajador 1") 
                self.UpdateValuesClient(0)
                self.t_D1 = self.workers[0].T_D
                print("Su tiempo de salida:"+ str(self.t_D1))
            else:
                self.workers[0]= Client(None,None,math.inf)
                self.t_D1 = math.inf    
        elif min_ == self.t_D2:
            print("Abandona el cliente que está siendo atendido por el Trabajador 2 su T_D: " + str(min_ ))
            self.t = min_
            self.ND2 += 1
            self.result.append(self.workers[1]) 
            if not self.queue.empty():
                self.workers[1]= self.queue.get()
                print("El primer cliente de la cola pasa a ser atendido por el Trabajador 2")
                self.UpdateValuesClient(1)
                self.t_D2 = self.workers[1].T_D 
                print("Su tiempo de salida:"+ str(self.t_D2))
            else:
                self.workers[1]= Client(None,None,math.inf)
                self.t_D2 = math.inf    
       
        elif self.test and min_ == self.t_D3: 
            print("Abandona el cliente que está siendo atendido por el Trabajador 3 su T_D: " + str(min_ ))
            self.t = min_
            self.ND3 += 1
            self.result.append(self.workers[2])  
            if not self.queue.empty() and self.RushHour():
                self.workers[2]= self.queue.get()
                print("El primer cliente de la cola pasa a ser atendido por el Trabajador 3")
                self.UpdateValuesClient(2)
                self.t_D3 = self.workers[2].T_D 
                print("Su tiempo de salida:"+ str(self.t_D3))
            else:
                self.workers[2]= Client(math.inf,math.inf,math.inf)
                self.t_D2 = math.inf    
                       
    
    def ExitEvent(self,min_):  
        self.t= min_ 
        self.n -= 1  
        if min_ == self.t_D1:
            print("Abandona el cliente que está siendo atendido por el Trabajador 1 su T_D: " + str(min_ ))
            self.result.append(self.workers[0])
            self.ND1 += 1
            if self.queue.empty():
                self.workers[0]= Client(None,None,math.inf)
                self.t_D1 = math.inf
            else :
                self.workers[0] = self.queue.get()
                print("El primer cliente de la cola pasa a ser atendido por el Trabajador 1")
                self.UpdateValuesClient(0)
                self.t_D1 = self.workers[0].T_D
        elif min_ == self.t_D2:
            self.ND2 += 1
            print("Abandona el cliente que está siendo atendido por el Trabajador 2 su T_D: " + str(min_ ))
            self.result.append(self.workers[1])
            if self.queue.empty():
                self.workers[1]= Client(None,None,math.inf)
                self.t_D2 = math.inf
            else:
                self.workers[1] = self.queue.get()
                print("El primer cliente de la cola pasa a ser atendido por el Trabajador 2")
                self.UpdateValuesClient(1)
                self.t_D2 = self.workers[1].T_D  
        elif self.test and min_==self.t_D3:
            self.ND3 += 1
            print("Abandona el cliente que está siendo atendido por el Trabajador 3 su T_D: " + str(min_ ))
            self.result.append(self.workers[2])
            if not self.queue.empty() and self.RushHour():
                self.workers[2] = self.queue.get()
                print("El primer cliente de la cola pasa a ser atendido por el Trabajador 3")
                self.UpdateValuesClient(2)
                self.t_D3 = self.workers[2].T_D 
            else:
                self.workers[2]= Client(None,None,math.inf)
                self.t_D3 = math.inf
                           
                                       
    def UpdateValuesClient(self,i):   
        self.workers[i].T_P = self.TimePreparation()
        self.workers[i].T_D = self.t +  self.workers[i].T_P  
    
    def TimePreparation(self): 
        if random.randint(0,2)==0 :#sandwiches 
            print("El cliente Ordenó Sandwiches")
            return  UniformRandomVariable(3,5)
        else:#sushi
            print("El cliente Ordenó Sushi")
            return UniformRandomVariable(5,8)                  
    def RushHour(self):
        if (self.t >=90 and self.t <= 210) or (self.t >= 420 and self.t >= 540):
            return True
        return False
    def Results(self): 
        print("Lista de clientes que ya obtuvieron sus pedidos" )
        count = 0
        for i in range(len (self.result)):
            print("tiempo de arribo del cliente: "+ str(self.result[i].T_A) )
            print("tiempo de salida del cliente: "+ str(self.result[i].T_D) ) 
            print("tiempo de preparacion del pedido: " + str(self.result[i].T_P) + "\n")
            if (self.result[i].T_D - self.result[i].T_A -  self.result[i].T_P) > 5:
                count += 1
        
        print("Cantidad de Clientes atendidos en el Dia:" + str(len(self.result)))
        print("Cantidad de Clientes atendidos en el Dia por el Trabajador 1:" + str(self.ND1))
        print("Cantidad de Clientes atendidos en el Dia por el Trabajador 2:" + str(self.ND2))
        if self.test:
            print("Cantidad de Clientes atendidos en el Dia por el Trabajador 3:"+ str(self.ND3))  
        print("\n")
        print("Cantidad de Clientes que esperan mas de 5 min por ser atendidos: " + str(count)+ " y el porciento es "+ str((count*100)/len(self.result)))   

def UniformRandomVariable(a,b):
    return a + (b - a)*np.random.uniform()   
def ExponentialRandomVariable(lambda_):
    return - (1/(lambda_))* math.log(np.random.uniform()) 

obj = KojosKitchen()
obj.Simulation2Workers()
print("#######################################################################################################################")
print("#######################################################################################################################")
print("#######################################################################################################################")
print("#######################################################################################################################")
obj1 = KojosKitchen()
obj1.Simulation3Workers()
print("#######################################################################################################################")
print("#######################################################################################################################")
print("#######################################################################################################################")
print("#######################################################################################################################")
print("Resultados con dos Trabajadores")
obj.Results()
print("#######################################################################################################################")
print("#######################################################################################################################")
print("#######################################################################################################################")
print("Resultados Con 3 Trabajadores")
obj1.Results()