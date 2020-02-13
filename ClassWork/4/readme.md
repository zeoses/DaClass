# Module
```python
from .<Namefile> 
``` 
currenty foulder
``` 
from ..<Namefile> 
``` 
back to root.
 . (dot) back to top folder

# Input and Output

## Format
a methode for string typing.

## File 
### file permissions : 
* 'r' : read
* 'w' : write
* 'r+' : read and write
* 'a' : Append
* 'x' : Create
### open File
```python
f = open('FileName','r')
f.read() # read all data of file
f.readline() # read first line
f.readlines() # read all lines with string format in list
list(f) # f.readlines()
```
when open a file must close it .

```python
f.close()
```

***notif :we can use  [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) for file and set is python file. must exist in first line.***

```python
#!/usr/bin/env python3
```
### with for file
Handing file in with scop
```python
with open('FileName', 'r') as f:
    data = f.read()
    print(data)
```
### argv 
read argoman from file

```python
import sys
sys.argv[]

--> python m.py file.txt <--
argv[0] : m.py
argv[1] : file.txt

```
# Exception Handling
Error Type:
* TypeError
* ZerDev
* ValueError
* ...
## Try/Except
```python
try:
    adad = int(input())
    print(adad+1)
except ValueError as E:
    print(E)
```

you can use multi except for any Exception or use tuple for this (v,e,...) .

use else when Not handling this error for Exception.
## reise
Genrate Error an raise it

```python
esm = input()
if esm == 'Ali':
    print('ok')
else:
    raise NameError('Faghat Ali')
```
## finally
run anyway .  
```python
try : 
    some...
except : 
    some...
finally :
    some

```
# Scop

```python

def Scop_test():
    def one():
        text = '1'# For thos function
    def two():
        nonlocal text
        text = '2' # for all Scop_test
    def three():
        global text # For all Script
        text = '3'

```

# OOP
