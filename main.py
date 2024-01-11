import openai
from dotenv import load_dotenv

import os
from loguru import logger

from ec.llm.service.inference_service import InferenceService

# function = lambda x: x ** 2
#
# print(list(map(function, range(10))))

load_dotenv('./secrets/.env-dev')

print(os.getenv('OPENAI_API_KEY', 'kepler'))

# Solicitar al usuario que ingrese un texto
prompt = input("Por favor, ingrese su pregunta: ")
# Imprimir el texto ingresado
# print("Texto ingresado:", prompt)

service = InferenceService()

# print (service.invoke('2020'))
#logger.info(service.invoke('2020'))

# Suponiendo que `response` contiene el objeto ChatCompletion
response = service.invoke(prompt)

# Accede al contenido (content) del mensaje en la respuesta
content = response.choices[0].message.content

# Imprime el contenido
print(content)