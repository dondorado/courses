from django.contrib.auth.decorators import login_required #built in za login required django
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404 #ovo je naziv za gresku kad stranica nije nadjena, cela funkcija dole moze da se stavi u try-except blok, pa onda raise Http404
from django.shortcuts import render, get_object_or_404, redirect #get_object je built-in metod koji pravi objekat ili vraca gresku

# Create your views here.

from blog.models import BlogPost
from blog.forms import BlogPostModelForm


# def blog_post_detail_page(request, slug): # kreiranje template, post_id vuce iz urls fajla kao putanjy
# 	# if queryset.count() == 0:
# 	# 	raise Http404    		#ovo se radi, ako slug nije stavljen na unique
# 	# obj = queryset.first()
# 	#queryset = BlogPost.objects.filter(slug=slug) # isto kao i donji,  query (id je broj objekta u bazi koji je kreiran), samo sto donji izbacuje gresku 404 prilikom nepronalazenja stranice
# 	obj		      = get_object_or_404(BlogPost, slug=slug) #stavljanje query da gleda prema string definisanom u slug, get metod trazi samo jedan objekat
# 	template_name = "blog_post_detail.html"
# 	context		  = {"object":obj}
# 	return render(request, template_name, context)


def blog_post_list_view(request):
	# izlistava objekte, moze se koristi i kao search
	#qs 			  = BlogPost.objects.filter(title__icontains = "Ne") # queryset - izlistava sve objekte u bazi prema zadatom filteru
	qs 			  = BlogPost.objects.all().published() # queryset - izlistava sve objekte u bazi, a ako hocemo samo published moze da se doda naknadno jer je definisan u modelu
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct() # razlika u postovima izmedju ukupnog qs i customized (prema ulogovanom useru), njih izbacuje
	template_name = "blog/list.html"
	context 	  = {"object_list": qs}
	return render(request, template_name, context)

@staff_member_required #dekorator koji automatski redirect za stranicu za logovanje. Mora user da ima privilegije editovanja neke stranice
#@login_required(login_url='/login') #dovoljno je staviti samo dekorator
def blog_post_create_view(request):
	# kreiraju se objekti
	form = BlogPostModelForm(request.POST or None, request.FILES or None) # ako se koristi BlogPostModelForm, to je built in metod Djanga, koji se deklarise u forms koja polja ima i onda form.save() koji ide samo uz model
	if form.is_valid():
		#obj = BlogPost.objects.create(**form.cleaned_data) # ** su sintaksa za otpakivanje recnika, obj je precica za python obj = BlogPost() obj.title = 'neki title' i obj.save()
		
		obj = form.save(commit=False) #- ako necu cuvanje forme, jer mi trebaju podaci
		obj.user = request.user # cuvanje informacije ko je kreirao blog
		obj.save()

		form = BlogPostModelForm()
		# obj.title = form.cleaned_data.get('title') + '0' - dodavanje necega na polje, jer form.cleaned_data je recnk
		# obj.save()
	template_name = "form.html"
	context 	  = {"form": form}
	return render(request, template_name, context)
	
def blog_post_detail_view(request, slug):
	obj		  	  = get_object_or_404(BlogPost, slug=slug)
	template_name = "blog/detail.html"
	context 	  = {"object": obj}
	return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
	obj		  	  = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		form.save()
	template_name = "form.html"
	context 	  = {"title": f"Update {obj.title}", "form": form}
	return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
	obj		  	  = get_object_or_404(BlogPost, slug=slug)
	template_name = "blog/delete.html"
	if request.method == "POST": #
		obj.delete()
		return redirect("/blog") #metod importovan iz shortcuts, koji prilikom brisanja vraca na stranicu koja je stavljena
	context 	  = {"object": obj}
	return render(request, template_name, context)