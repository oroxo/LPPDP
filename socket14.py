#!/usr/bin/env python
# -*- coding: utf-8 -*-

# diguito69

import socket

def main():
    # Creamos el socket.
    server = socket.socket()

    # Conecta el socket con la direccion.
    server.bind(("localhost", 6969))

    # Empieza a escuchar conexiones.
    server.listen(1)

    # Aceptamos una conexion, se bloquea hasta que alguien se conecte.
    print "Esperando conexion..."
    socket_cliente, datos_cliente = server.accept()

    # Esperamos que el cliente mande un mensaje y lo imprimimos.
    print "Esperando mensaje..."
    datos = socket_cliente.recv(1000)
    print "El mensaje es:", datos
    
    # Le enviamos chau al cliente.
    socket_cliente.send("chau")  

    print "Cerrando..."
    # Cerramos ambos sockets.
    socket_cliente.close()
    server.close()

if __name__ == "__main__":
    main()

