#Importar el modulo "Requests" para poder realizar consultas http:
import requests
#Importar la función "sleep" del módulo "time" para establecer esperas entre ciertas líneas de codigo:
from time import sleep

#Guardar en "math_request" el URI (Recurso) para acceder a los post del sitio Math:
math_request = "https://api.stackexchange.com/2.2/posts?order=desc&sort=activity&site=math&filter=!1PUIfKi(5TgRWjnGEVujv2pdMvcbzLC1D"

#Usar la función GET del modulo "request" para acceder al URI guardado en "math_request"
#Hay que entender que cuando se usa GET este mismo envía el request, recibe y guarda el
#response en la variable, de ahí que la variable se llame "math_response":
math_response = requests.get(math_request)

#Usar for para realizar la consulta de eventos en un rango de (N) veces:
for i in range(1,11): 
#Usar with para que el código corra aún si hay ERROR oder EXCEPTION, setear el "format" del valor "i" al field {} y setear el encoding a Unicode:
   with open(f"Math-Post-Events_{i:02d}.JSON", 'w', encoding='utf-8') as f:
       f.write(math_response.text)
       sleep(30)

#Written by Alezz
#Arcsight Support Engineer.
#alexander.eze.ruiz-mora@microfocus.com