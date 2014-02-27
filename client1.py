import socket
import time

# Se establece la conexion
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8000))
s.send("hola")
datos = s.recv(1000)
print datos  
time.sleep(2)    
s.send("adios")    
datos = s.recv(1000)
print datos
s.close()

