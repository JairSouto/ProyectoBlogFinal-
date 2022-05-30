

from django.http import HttpResponse
from django.template import Template,Context, loader


def probandoT(self):
    nom = 'jair'
    ap ='souto'
    diccionario = {'nombres':nom, 'apellidos':ap}
    """
    #encoding=”utf-8” para no cambiar los /
    plantilla = Template(myTemplate1.read())
    myTemplate1.close()
    myContexto = Context(diccionario)

                            """
    plantilla = loader.get_template('template.html')
    documento = plantilla.render(diccionario)
    return HttpResponse()