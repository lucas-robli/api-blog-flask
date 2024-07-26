from requests.auth import HTTPBasicAuth
import requests

#fazendo login e pegando o token
resultado = requests.get('http://localhost:5000/login',
                         auth=('lucas', '123456'))

#acessando a lista de autores
resultado_autores = requests.get('http://localhost:5000/autores', headers={'x-access-token':resultado.json()['token']})
print(resultado_autores.json())