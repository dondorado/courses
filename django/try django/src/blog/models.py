from django.conf import settings
from django.db import models # deo koji omogucava stavljenje podataka u bazu, mora kao klasa. Kad god se menja, rade se migracije python manage.py makemigrations i migrate
from django.db.models import Q #
from django.utils import timezone
# python manage.py shell - komanda za koriscenje pythona za django, sa izmenjenim nacinom rada (moze save u bazu itd)
# Create your models here.

User = settings.AUTH_USER_MODEL #default nacin da se nekom dodele privilegije



class BlogPostQuerySet(models.QuerySet):
	def published(self):
		now = timezone.now()
		return self.filter(publish_date__lte=now) #lte je less then, double underscore ide, get_queryset je isto sto i BlogPost.get_objects

	def search(self, query):
		lookup = (
			Q(title__icontains=query) | #icontains je modul koji dozvoljava da nesto sadrzi pretrag, a Q je modul djanga koji moze da pretrazuje na osnovu vise parametara koristeci | (pipe)
			Q(content__icontains=query) |
			Q(slug__icontains=query) |
			Q(user__email__icontains=query) |
			Q(user__username__icontains=query)
			)
		return self.filter(lookup) 

class BlogPostManager(models.Manager): #built-in model djanga 
	
	def get_queryset(self):
		return BlogPostQuerySet(self.model, using=self._db) # koriscenje modela, kao i njegove baze

	def published(self):
		return self.get_queryset().published()

	def search(self, query=None):
		if query is None:
			return self.get_queryset().none()
		return self.get_queryset().published().search(query) #uzima search modul iz BlogPostQuerySet-a i radi pretragu samo blogova koji su objavljeni 		

class BlogPost(models.Model): #ovo je klasa gde se definisu polja koja ce biti u blogu. blogpost_set je built in modul za class modela koji omogucava vracanja svih blogova koje je napisao odredjeni user, npr nemanja.blogpost_set.all() vraca taj query
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL) #default 1 je superuser(admin), on_delete je komanda da prilikom brisanja nekog usera da se brisu sve stvari koje imaju veze sa njim(opcija cascade ili set_null da se postave na null vrednosti)
	image = models.ImageField(upload_to='image/', blank=True, null=True) # slike kad se upload, nalaze se u folderu koji je oznacen u setting (MEDIA_ROOT), da bi moglo da se pise ImageField, a ne FileField, treba da se instalira pillow. Razlika je sto ce traziti islkjucivo prilokom upload image file, a ne bilo koji
	title = models.CharField(max_length = 120)
	slug = models.SlugField(unique=True) # ako se ostavi bez default, moze u cmd da se stavi. Sa unique se obezbedjuje da svaki post ima svoj jedinstveni slug
	content = models.TextField(null = True, blank = True) # moze se koristiti sintaksa from blog.models import BlogPost gde je blog ime aplikacije. Blank ako se stavi True, mora da se ubace podaci tamo
	publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True) #moze biti i DateField ako ne treba tacno vreme vec samo datum
	timestamp = models.DateTimeField(auto_now_add=True) #ovo je opcija koja kad se doda, dobija automatski vreme prema vremenskoj zoni u podesavanjima i ne moze da se menja
	updated = models.DateTimeField(auto_now=True) #ovo je opcija koja kad se doda, dobija vreme prema vremenskoj zoni u podesavanjima kad je azurirana

	objects = BlogPostManager()

	class Meta:
		ordering = ['-publish_date', '-updated', '-timestamp'] # minus se stavlja ako nesto hocemo kontra, od najstarijeg do najnovijeg

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"{self.get_absolute_url()}/edit"

	def get_delete_url(self):
		return f"{self.get_absolute_url()}/delete"
