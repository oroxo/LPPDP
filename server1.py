import threading
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 8000))
server.listen(1)

#Clase con el hilo para atender a los clientes.
#En el constructor recibe el socket con el cliente y los datos del
#cliente para escribir por pantalla
class Cliente(Thread):
    def __init__(self, socket_cliente, datos_cliente):
        # LLamada al constructor padre, para que se inicialice de forma
        # correcta la clase Thread.
        Thread.__init__(self)
        # Guardamos los parametros recibidos.
        self.socket = socket_cliente
        self.datos = datos_cliente
 
    # Bucle para atender al cliente.       
    def run(self):
      # Bucle indefinido hasta que el cliente envie "adios"
      seguir = True
      while seguir:
         # Espera por datos
         peticion = self.socket.recv(1000)
         
         # Contestacion a "hola"
         if ("hola"==peticion):
             print str(self.datos)+ " envia hola: contesto"
             self.socket.send("pues hola")
             
         # Contestacion y cierre a "adios"
         if ("adios"==peticion):
             print str(self.datos)+ " envia adios: contesto y desconecto"
             self.socket.send("pues adios")
             self.socket.close()
             print "desconectado "+str(self.datos)
             seguir = False


# bucle para atender clientes
while 1:
	# Se espera a un cliente
	socket_cliente, datos_cliente = server.accept()
	# Se escribe su informacion
	print "conectado "+str(datos_cliente)
	# Se crea la clase con el hilo
	hilo = Cliente(socket_cliente, datos_cliente)
	# y se arranca el hilo
	hilo.start()
