from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def set_name(request):
    if request.method == 'POST':
        name = request.POST['name']
        request.session['name'] = request.POST['name']
        return HttpResponse(f"Name {name} set in session")
    else:
        return render(request, 'sessionapp/set_name.html')

def get_name(request):
    name = request.session.get('name')
    if name:
        return HttpResponse(f"Name: {name}")
    else:
        return HttpResponse("Name not found in session")