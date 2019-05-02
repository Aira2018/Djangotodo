from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm
from django.contrib import messages

def home(request):

	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request,("Item has been added to the List!"))
			context = List.objects.all
			return render(request, 'home.html', {'all_items': context})


	else: 
		context = List.objects.all
		return render(request, 'home.html', {'all_items': context})

def about(request):
	my_name = 'Reservez'
	all_items = List.objects.all
	context = {'first':'Reserxe', 'last':'Lame','all_items':all_items}
	return render(request, 'about.html', context)

def delete(request, list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request,("Item has been deleted from the List!"))
	return redirect('home')

def cross_off(request, list_id):
	item = List.objects.get(pk=list_id)
	item.compleated = True
	item.save()
	return redirect('home')

def cross(request, list_id):
	item = List.objects.get(pk=list_id)
	item.compleated = False
	item.save()
	return redirect('home')

def edit(request, list_id):
	if request.method == 'POST':
		item = List.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()
			messages.success(request,("Item has been edited!!"))
			return redirect('home')


	else: 
		item = List.objects.get(pk=list_id)
		return render(request, 'edit.html', {'item': item})
