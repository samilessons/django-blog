from django import forms
from django.core.exceptions import ValidationError
from .models import Category, Author, Article, Adv, ArticleTags


class AddPostForm(forms.ModelForm):
	category = forms.ModelChoiceField(
		queryset=Category.objects.all(),
		label="Կատեգորիա",
		empty_label="Ընտրել Կատեգորիա"
	)
	author = forms.ModelChoiceField(
		queryset=Author.objects.all(),
		label="Հեղինակ",
		empty_label="Ընտրել Հեղինակ"
	)
	
	adv = forms.ModelChoiceField(
		queryset=Adv.objects.all(),
		label="Գովազդներ",
		empty_label="Ընտրել Գովազդը",
		required=False
	)
	tags = forms.ModelMultipleChoiceField(
		queryset=ArticleTags.objects.all(),
		label="Թեգեր"
	)
	
	def clean_slug(self):
		slug = self.cleaned_data.get("slug")
		if Article.objects.filter(slug=slug).exists():
			raise ValidationError("Սլագները չպետք է կրկնվեն")
		
		return slug
	
	def clean_title(self):
		title = self.cleaned_data.get("title")
		if len(title) > 50:
			raise ValidationError("Վերնագիրը չի կարող 50 տառից ավել լինել")
		
		return title
	
	def save(self, commit=True):
		instance = super().save(commit=False)
		
		if commit:
			instance.save()
		
		if self.cleaned_data["tags"]:
			instance.tags.set(self.cleaned_data["tags"])
		
		return instance
	
	class Meta:
		model = Article
		fields = [
			"title", "slug", "content", "photo",
			"is_published", "tags", "category", "adv", "author"
		]
		widgets = {
			"title": forms.TextInput(attrs={"class": "red"}),
		}
		labels = {"slug": "URL"}


class UploadFileForm(forms.Form):
	file = forms.ImageField(label="file")
