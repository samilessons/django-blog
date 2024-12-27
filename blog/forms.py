from django import forms
from .models import Category, Author, ArticleTags
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


# Custom Validator
# @deconstructible
# class ArmenianValidator:
#     ALLOWED_CHARS = "ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔԵՎՕՖաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցուփքեօֆ0123456789-_ "
#     code = "armenian"

#     def __init__(self, message=None):
#         self.message = message if message else "Կարող եք գրել միայն հայատառ, թվեր, գծիկ, տակի գծիկ և բացատ"

# def __call__(self, value, *args, **kwds):
#     if not (set(value) <= set(self.ALLOWED_CHARS)):
#         raise ValidationError(self.message, self.code)


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        min_length=3,
        label="Վերնագիր",
        widget=forms.TextInput(attrs={"class": "red"}),
        error_messages={
            "min_length": "Մինիմում 3 տառ",
            "max_length": "255 տառից ավել արգելվում է",
            "required": "Անպայման պետք է լրացնեք",
        }
    )
    slug = forms.SlugField(
        required=False,
        label="URL",
        validators=[
            MinLengthValidator(3, message="Համոզվեք որ 3 տառից ավել եք գրել"),
            MaxLengthValidator(
                100, message="Համոզվեք որ 100 տառից պակաս եք գրել")
        ]
    )
    content = forms.CharField(widget=forms.Textarea(), label="Տեքստ")
    is_published = forms.BooleanField(label="Հրապարակել", initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(
    ), label="Կատեգորիա", empty_label="Ընտրել Կատեգորիա")
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(), label="Հեղինակ", empty_label="Ընտրել Հեղինակ")

    def clean_title(self):
        title = self.cleaned_data["title"]
        ALLOWED_CHARS = "ԱԲԳԴԵԶԷԸԹԺԻԼԽԾԿՀՁՂՃՄՅՆՇՈՉՊՋՌՍՎՏՐՑՈՒՓՔԵՎՕՖաբգդեզէըթժիլխծկհձղճմյնշոչպջռսվտրցուփքեօֆ0123456789-_ "

        if not (set(title) <= set(ALLOWED_CHARS)):
            raise ValidationError(
                "Կարող եք գրել միայն հայատառ, թվեր, գծիկ, տակի գծիկ և բացատ"
            )
