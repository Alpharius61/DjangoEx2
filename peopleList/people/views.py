from stat import FILE_ATTRIBUTE_NORMAL
from django.shortcuts import render
from django.template import context
from people.models import people
# Create your views here.

def peopleView(request):
    peopls = people.objects.all()

    HTML = f''

    for Personne in peopls :
        if Personne.Sexe == 'F':
            cssClass = 'Feminin'
        else :
            cssClass = 'Masculin'   

        HTML += f'<li> <a href="/people/{Personne.id}" class="{cssClass} name"> {Personne.name} </a> </li>'      

    context = {
        'people' : HTML    
    }
    return render(request, 'people\people.html', context)


def peopleDetail(request, id):
    personne = people.objects.get(id=id)
    return render(request, 'people\peopleDetail.html', {'personne' : personne})