# Ejemplos de modulos que pueden usarse en python 
import sys
print(sys.path)

import re
text = 'el numero del movil es 563 597 1258, codigo postal 45875 y fecha de nacimiento 9 de marzo de 1999'
result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
res = time.asctime(local)
print(res)