'''
Created on 20/02/2009
@author: Chuidiang
Ejemplo de cliente de socket.
Establece conexion con el servidor, envia "hola", recibe y escribe la
respuesta, espera 2 segundos, envia "adios", recibe y escribe la respuesta
y cierrra la conexion
'''
import socket
#import time

if __name__ == '__main__':
    # Se establece la conexion
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8000))
    cond = True
    while cond:
        #s.send(str(665))
        #a=s.recv(1000)
        #print a
        b = raw_input(">. ")
        #print type(b)
        if (b != ''):
            b = int(b)
            if (b <= 255) & (b >= 0):
                s.send(str(b))
            elif (b == 666):
                cond = False
                s.send(str(b))
                s.close()
                print "nojoda"
                s.close()
            elif (b == 665):
                s.send(str(b))
                a = s.recv(1000)
                print a
            else:
                print "el rango debe ser entre 0 y 255, 666 es para cerrar"


    # Se envia "hola"
    #s.send("hola")

    # Se recibe la respuesta y se escribe en pantalla
    #datos = s.recv(1000)
    #print datos
    #
    ## Espera de 2 segundos
    #time.sleep(2)
    #
    ## Se envia "adios"
    #s.send("adios")
    #
    ## Se espera respuesta, se escribe en pantalla y se cierra la
    ## conexion
    #datos = s.recv(1000)
    #print datos
    #s.close()
