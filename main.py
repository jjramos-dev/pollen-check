# A very simple Bottle Hello World app for you to get started with...
from bottle import route, run, template, response
import requests
import jsons

@route('/')
def hello_world():
    response.content_type = 'application/json'
    r = requests.get('https://www.eltiempo.es/granada/polen')

    lista=r.text.split("<tr>")

    estimacion={}

    for i in range(2,len(lista)):
        valores=lista[i].split("</tr>")


        valores2=valores[0].split("class=\"text-poppins text-poppins-bold\">")[1].split("</p>")

        nivel=0
        polen=valores2[0].strip()

        if valores2[1].find("pollen-provincevalue-null")!=-1:
            nivel=0
        elif valores2[1].find("pollen-provincevalue-nothing")!=-1:
            nivel=0
        elif valores2[1].find("pollen-provincevalue-very-low")!=-1:
            nivel=1
        elif valores2[1].find("pollen-provincevalue-low") != -1:
            nivel=2
        elif valores2[1].find("pollen-provincevalue-medium") != -1:
            nivel=3
        elif valores2[1].find("pollen-provincevalue-high") != -1:
            nivel=4

        estimacion[polen]=nivel

    return jsons.dump(estimacion)

# application = default_app()
run(host='0.0.0.0', port=10000)

