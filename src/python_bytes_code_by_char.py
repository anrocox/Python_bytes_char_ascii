#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

In Python, How to get the character from the numeric code in bytes objects?

En Python, ¿Cómo obtener el carácter a partir del código numérico en los
objetos bytes?
'''

#this method return a single character based on the integer value.
c = chr(80)
print(c)

#create a list with integers in the range 0 through 255
l = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 101, 97, 115, 121]

#create a bytes object from a list of integers in the range 0 through 255.
b = bytes(l)
print(b)
