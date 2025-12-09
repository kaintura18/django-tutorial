from django.shortcuts import render
from .models import heroname
from django.shortcuts import get_object_or_404



def batman(request):
     heroes = heroname.objects.all()
     context = {'heroes': heroes}
     return render(request, "batman.html", context)

def hero_detail(request, hero_id):
     hero=get_object_or_404(heroname, pk=hero_id)
     return render(request,"hero_detail.html", {'hero': hero})

# Create your views here.
