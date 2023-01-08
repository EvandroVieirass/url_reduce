from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from core.forms import FormLink
from . models import Links

# Create your views here.
def home(request):
	formlink = FormLink()
	status = request.GET.get('status')
	return render(request,'home.html',{'form':formlink, 'status':status})

def valida_link(request):
	form = FormLink(request.POST)
	link_encurtado = form.data['link_encurtado']
	links = Links.objects.filter(link_encurtado = link_encurtado)
	
	if len(links)> 0:
		return redirect('/?status=0')
	if form.is_valid():
		try:
			url_padrao = request.build_absolute_uri()
			form.save()
			url_padrao = str(url_padrao)
			tamanho =  len('valida_link/')
			url = url_padrao[:-tamanho]
			link_final = f'{url}/{link_encurtado}'
			return render(request,'home.html',{'link_final':link_final})
		except:
			return HttpResponse('Erro interno do sistema')


def redirecionar(request,link):
	links = Links.objects.filter(link_encurtado = link)

	if len(links)== 0:
		return redirect('/')
	
	else:
		return redirect(links[0].link_redirecionado)
