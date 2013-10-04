from django.shortcuts import get_object_or_404, render
from django.db.models import Q
#from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from django.views import generic

from models import Account

def index(request):
    return HttpResponse("Hello, world. You're at the address book index.")
    
class DetailView(generic.DetailView):
    model = Account
    template_name = 'addressbook/account.html'
   


def search(request):
	words = request.GET.get("q","").split()
	results = Account.objects.filter(Q(last_name__contains=words[0]))
	for word in words:
		results = results | Account.objects.filter(Q(last_name__contains=word)) | Account.objects.filter(Q(first_name__contains=word))
	context = {'results': results}
	return render(request, 'addressbook/search.html', context)


def search2(request,query):
	words = query.split('_')
	results = Account.objects.filter(Q(last_name__contains=words[0]))
	for word in words:
		results = results | Account.objects.filter(Q(last_name__contains=word))
	context = {'results': results}
	return render(request, 'addressbook/search.html', context)