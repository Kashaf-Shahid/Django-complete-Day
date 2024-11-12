from django import forms
from news. models import BlogComment
class NameForm(forms.Form):
    f_name=forms.CharField(max_length=100)

class ContactForm(forms.Form):
   subject = forms.CharField(max_length=100)
   message = forms.CharField(widget=forms.Textarea)
   sender = forms.EmailField()
   cc_myself = forms.BooleanField(required=False)
   

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model=BlogComment
        fields=["name","comment"]
