#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  server.py
#  
#  Copyright 2013 Jesus Orono <oroxo1989@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import os
import sys
import socket
import thread

port = 1941
global message
global lock
global file

def handler(connection):
    while 1:
            file = connection.makefile()
            file.flush()
            temp = file.readline()
            if temp == 'quit':
                break
            lock.acquire()
            message += temp
            lock.release()
            file.write(message)
    file.close()

acceptor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
acceptor.bind(('', port))
acceptor.listen(10)
lock = thread.allocate_lock()

while 1:
    connection, addr = acceptor.accept()
    thread.start_new_thread(handler, (connection,))
