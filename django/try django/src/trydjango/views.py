
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template #metod koji pravi template
from .forms import MyForm
from blog.models import BlogPost

# kreiranje pocetne stranice

def home_page(request):
	my_title = "Hello there..."
	qs = BlogPost.objects.all()[:5]
	context = {"title": "Welcome to Try Django", 'blog_list': qs}
	# if request.user.is_authenticated:
	# 	context = {"title":my_title, "my_list":[1, 2, 3, 4, 5]} # drugi nacin koriscenja da se nesto uradi ako je korisnik verifikovan

	return render(request, "home.html", context) 				# kreiranje varijable za django naslov django_rendered_doc = "<h1>{{title}}</h1>".format(title = title)
																# moze da mu se dodeli varijabla ili samo string
																# render moze bilo cega, string, txt file

def about_page(request):
	return render(request, "about.html", {"title": "About"})

def contact_page(request):
	if request.method == 'POST':
		form = MyForm(request.POST, extra=request.POST.get('extra_field_count'))
        if form.is_valid():
			print("valid!")
    	else:
        	form = MyForm()
	return render(request, "template", { 'form': form })

def example_page(request):
	# ako hocu neki loop da uradim, ne idem na html, nego ovde u python
	my_title = 'Hello there'
	context 		= {"title": "Example"}
	#template_name = 'title.txt' ako je neka druga vrste fajla i ne moze sa render, onda ide HttpResponse
	template_name 	= "home.html"
	template_obj 	= get_template(template_name) # ovo je string
	return HttpResponse(template_obj.render(context))
