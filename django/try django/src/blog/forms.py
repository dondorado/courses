from django import forms
from blog.models import BlogPost

class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
	# title = forms.CharField() - overwrite ako treba nekog polja iz modela
	class Meta:
		model = BlogPost
		fields = ['title', 'image', 'slug', 'content', 'publish_date']

	def clean_title(self, *args, **kwargs):
		#print(dir(self)) - stampanje svih modula za self
		instance = self.instance
		#print(instance)
		title = self.cleaned_data.get('title')
		qs = BlogPost.objects.filter(title__iexact=title) # validiranje naziv bez obzira da li je upotreblajvaju mala ili velika slova, isto je Nemanja i NeMAnjA
		if instance is not None:
			qs = qs.exclude(pk=instance.pk) # pk je isto sto i id, ako postoji instance, iskljucuje ga iz query set (qs). Ovo se radi da bi bila mogucnost editovanja postojecih bloga kako ne bi izbacivao gresku prilikom cuvanja
		if qs.exists(): # validiranje naziv clanka, bez stavljanja unique klauzule u modelima kod polja
			raise forms.ValidationError('This title has already been used. Please try again')
		return title