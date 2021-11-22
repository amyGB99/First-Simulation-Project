# First-Simulation-Project
## Amanda González Borrell C411



 ### Ejercicio 1: La Cocina de Kojo (Kojo’s Kitchen)

La cocina de Kojo es uno de los puestos de comida rápida en un centro comercial. El centro comercial está abierto entre las 10:00 am y las 9:00 pm cada día. En este lugar se sirven dos tipos de productos: sándwiches y sushi. Para los objetivos de este proyecto se asumir´a que existen solo dos tipos de consumidores: unos consumen solo sándwiches y los otros consumen solo productos de la gama del sushi. En Kojo hay dos períodos de hora pico durante un día de trabajo; uno entre las 11:30 am y la 1:30 pm, y el otro entre las 5:00 pm y las 7:00 pm. El intervalo de tiempo entre el arribo de un consumidor y el de otro no es homogéneo pero, por conveniencia, se asumir´a que es homogéneo. El intervalo de tiempo de los segmentos homogéneos, distribuye de forma exponencial. Actualmente dos empleados trabajan todo el día preparando sándwiches y sushi para los consumidores. El tiempo de preparación depende del producto en cuestión. Estos distribuyen de forma uniforme, en un rango de 3 a 5 minutos para la preparación de sándwiches y entre 5 y 8 minutos para la preparación de sushi. El administrador de Kojo está muy feliz con el negocio, pero ha estado recibiendo quejas de los consumidores por la demora de sus peticiones. El está interesado en explorar algunas opciones de distribución del personal para reducir el número de quejas. Su interés está  centrado en comparar la situación actual con una opción alternativa donde se emplea un tercer empleado durante los períodos más ocupados. La medida del desempeño de estas opciones estará dada por el porciento de consumidores que espera m´as de 5 minutos por un servicio durante el curso de un día de trabajo. Se desea obtener el porciento de consumidores que esperan m´as de 5 minutos cuando solo dos empleados están trabajando y este mismo dato agregando un empleado en las horas pico.

### Ideas Generales y Modelo utilizado :

El modelo utilizado fue el de n servidores montados en paralelos con ciertos cambios.

La idea general del ejercicio es simular un centro rápido de comida en donde un cliente llega y es atendido si no hay nadie en espera .

Son dos tipos de simulaciones , la primera es con dos trabajadores(servidores) q preparan la comida, son dos tipos de comidas (Sushi y Sándwiches ) y la segunda simulación  es donde un tercer trabajador entra en apoyo en ciertos periodos de tiempo pico en donde la demanda es mayor.

Para simular el tiempo en que llega un cliente utilizaré una exponencial con dos parámetro lambda uno para los segmentos de horario pico y el otro para los horarios restantes, el primero con un valor mayor que el segundo ya que la frecuencia con q llegan los clientes en el horario pico es mayor, asumiremos que el medio es homogéneo en cada uno de los segmentos descritos.  

Que quise decir con el párrafo anterior que para generar un cliente se genera un valor que sigue una distribución  exponencial con un lambda determinado y si este tiempo de arribo cae dentro de uno de los segmentos picos el próximo arribo se generará con el otro valor de lambda .

La simulación esta medida mediante un tiempo t que se actualiza cada vez q sucede un evento,estos eventos son arribo de un cliente, salida de un cliente, esta salida del cliente puede ser cuando aun se permiten arribos o cuando ya el horario de atención terminó .

Cada cliente tiene un tiempo de llegada, un tiempo en que pasa a pedir su plato y un tiempo de salida, veremos que  el tiempo de llegada y de pedir el plato no es el mismo ya que los trabajadores pueden estar atendiendo a otro cliente y este nuevo q arribó deberá esperar en la cola. Cuando el cliente arriba el tiempo transcurrido desde el inicio de la simulación pasa a ser el tiempo de arribo del cliente y si uno de los dos trabajadores esta vacío entonces procedemos a generar  el tiempo de salida del cliente el cual coincide con el tiempo en el q el trabajador al q se le asigna la elaboración del plato lo termina, el tiempo de preparación de su plato esta descrito por una variable aleatoria uniforme en un intervalo a,b por tanto el tiempo de salida del cliente una vez q es generado es el tiempo actual mas el valor de la variable aleatoria del tiempo del plato, como tenemos dos tipos de platos y ambos tienen la misma probabilidad de ser escogidos utilizamos un random entre 0 y 1 para escoger el plato q pedirá el cliente.

Si un cliente esta en la cola esta claro que no podemos generar su tiempo de salida pues este depende del momento en que uno de los trabajadores se desocupe o sea depende de que ocurra un evento de salida.

Entonces sintetizado el proceso para dos trabajadores :

El evento q se realiza es el de menor tiempo por tanto si tengo en servicio a dos clientes uno atendido por el trabajador uno y el otro por el dos y tengo ya mi tiempo de arribo generado actualizo el tiempo con el mínimo  valor entre el tiempo de arribo generado y los tiempos de salida de los clientes, si el mínimo  es el de arribo paso a hacer el evento de arribo y sino el de salida.

 Cabe mencionar que genero tiempo de arribo mientras este sea menor que el tiempo que dura la simulación que son 11 horas 660 min una vez el tiempo de arribo sobrepase este valor se cierra la tienda y el único evento q se realiza es el llamado (salida después del cierre) que en el mismo solo se avanza el tiempo hasta cada uno de los tiempos de salida de los clientes q aun están en el sistema.

De esta misma manera pasa para la segunda simulación (3 trabajadores) con la peculiaridad de que en el de dos en cualquier horario que se produzca un arribo cualquiera de los dos trabajadores si están libres pueden tomar un nuevo pedido ya sea q arribo nuevo o que estaba en la cola, en el caso del tercer trabajador si esta libre solo podrá tomar pedido de la cola y de arribo en unos segmentos de tiempo definidos $90 \leq t \leq 210$ y  $420 \leq t \leq 540$. El tercer trabajador podrá tomar cualquier pedido de un cliente en el tiempo pico sin importar que el tiempo de salida de este cliente ya no este en el tiempo pico. También quiere decir que si el trabajador tres termina con un pedido fuera del tiempo pico no puede tomar otro hasta que no vuelva otro tiempo pico. 

Variables de Tiempo

t = 0 tiempo de simulación 

t_D1 = math.inf tiempo en que termina de atender al cliente cada trabajador

t_D2 = math.inf

t_D3 = math.inf

 **Variables Contadoras**

NA = 0  cantidad de arribos 

ND1 =0 cantidad de atendidos por cada trabajador 

ND2 = 0

ND3 = 0

**Variables de Estado**

queue : una cola con los clientes que aun esperan por  ser atendidos.

workers = [ 3] ahí tendremos el cliente que esta atendiendo cada trabajador 

n = 0 cantidad de clientes en el sistema

test = True: es verdadero si estoy en la prueba de simulación con tres trabajadores.

result= [] donde se añadirán los clientes q ya hayan abandonado el sistema 

### Resultados :

Como resultados notamos una mejoría en la media de eficiencia dada por el porciento de las personas que esperan por ser atendidas más de 5 min : o sea que si para un cliente su Tiempo de salida - tiempo de llegada - el tiempo de elaboración q se demora el plato es mayor que 5 este forma parte de ese porciento .

O sea que con colocar un trabajador disminuyo considerablemente el porciento de personas q esperan mas de 5 min por ser atendidas.

De la simulación con 2 trabajadores :

Cantidad de Clientes atendidos en el Dia:196
Cantidad de Clientes atendidos en el Día por el Trabajador 1:104
Cantidad de Clientes atendidos en el Día por el Trabajador 2:92


Cantidad de Clientes que esperan mas de 5 min por ser atendidos: 101 y el porciento es 51.53061224489796

De la simulación con 2 trabajadores y uno en los tiempos picos:

Cantidad de Clientes atendidos en el Día: 201                                                                           

Cantidad de Clientes atendidos en el Día por el Trabajador 1: 93       

Cantidad de Clientes atendidos en el Día por el Trabajador 2: 72                                                         

Cantidad de Clientes atendidos en el Día por el Trabajador 3: 36  

Cantidad de Clientes que esperan mas de 5 min por ser atendidos: 19 y el porciento es 9.45273631840796

###  Código 
