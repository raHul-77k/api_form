from django.shortcuts import render
from .forms import entryForm
# Create your views here.

def index(request):

    form = entryForm()
    
    if request.method == 'POST':
        print(request.POST)
        form = entryForm(request.POST)
        if form.is_valid():
            form.save()

    context ={'form':form}
    return render(request,'index.html', context)