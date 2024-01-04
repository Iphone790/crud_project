import fontTools.subset.svg
from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import UserForm
from .models import User
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = UserForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            obj = User(name=name, email= email, password=pwd)
            obj.save()
            fm = UserForm()
    else:
        fm = UserForm()
    emp = User.objects.all()
    return render(request, 'test/addshow.html', {'form':fm, 'emp':emp})


def delete_data(request, id):
    if request.method == 'POST':
        try:
            pk = User.objects.get(pk=id)
        except User.DoesNotExist:
            raise Http404("User does not exist....")
        pk.delete()
        return HttpResponseRedirect(reverse('home'))



def update_view(request, id):
    instance = get_object_or_404(User, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserForm(instance=instance)
    return render(request, 'test/update.html', {'form': form, 'instance': instance})
