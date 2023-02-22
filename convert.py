Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(2*3)
6
>>> priny(2**3)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    priny(2**3)
NameError: name 'priny' is not defined
>>> print(2**3)
8
>>> print(2/3)
0.6666666666666666
>>> def main():
	celsius = eval(input("what is the celsius  temperature?" ))
	fahrenheit = 9/5*celsius+32
	print("The temperature is",fahrenheit."degrees fahrenheit.")
