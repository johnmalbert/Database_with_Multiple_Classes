from django.shortcuts import render, redirect
from .models import Dojos, Ninjas

# Create your views here.
def index(request):
    context = {
        "all_dojos" : Dojos.objects.all(),
        "all_ninjas" : Ninjas.objects.all()
    }
    return render(request, "index.html", context)

def create_ninja(request):
    #do some Post capturing, create a new ninja
    request.session['error2'] = False
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    dojo_id = request.POST['dojo_id']
    print("The dojo id passed was ",dojo_id)
    try:
        Ninjas.objects.create(dojo_id=Dojos.objects.get(id=dojo_id),first_name=first_name,last_name=last_name)
        print("creating a ninja", first_name, last_name, dojo_id)
    except:
        request.session['error2'] = True
    return redirect('/')

def create_dojo(request):
    #do some Post capturing, create a new dojo
    request.session['error1'] = False
    name = request.POST['name']
    city = request.POST['city']
    state = request.POST['state']
    try:
        Dojos.objects.create(name=name, city=city, state=state)
    except:
        request.session['error1'] = True

    print("creating a dojo with name", name, city, state)
    return redirect('/')

def delete_dojo(request, number):
    print("delete the dojo", number)
    delete_item = Dojos.objects.get(id=number)
    for ninja in delete_item.ninjas.all():
        print("Delete ", ninja.first_name)
        ninja.delete()
    delete_item.delete()
    return redirect('/')