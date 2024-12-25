from django import forms
from .models import Category, Author, ArticleTags


class AddPostForm(forms.Form):
	title = forms.CharField(
		max_length=255,
		min_length=3,
		label="Վերնագիր",
		widget=forms.TextInput(attrs={"class": "red"}),
		error_messages={
			"min_length": "Մինիմում 3 տառ",
			"max_length": "255 տառից ավել արգելվում է",
			"required": "Անպայման պետք է լրացնեք"
		}
	)
	slug = forms.SlugField(max_length=255, required=False, label="URL")
	content = forms.CharField(widget=forms.Textarea(), label="Տեքստ")
	is_published = forms.BooleanField(label="Հրապարակել", initial=True)
	category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Կատեգորիա", empty_label="Ընտրել Կատեգորիա")
	author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Հեղինակ", empty_label="Ընտրել Հեղինակ")