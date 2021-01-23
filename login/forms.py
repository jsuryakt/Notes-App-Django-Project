from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from login.models import Notes

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class notesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description','image','pdf','doc','video','audio']
        widgets = {
            'title': forms.TextInput(attrs={'class':'input form-control col-5 shadow p-3 mb-5 bg-white rounded'}),
            'description': forms.TextInput(attrs={'class':'input form-control form-control-lg col-8 shadow p-3 mb-5 bg-white rounded'}),
        }
    # def clean_pdf(self, *args,**kwargs):
    #     pdf = self.cleaned_data.get("pdf")
    #     if not pdf.endswith("pdf"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return pdf
    # def clean(self):
    #     cd = self.cleaned_data
    #     pdf = cd.get('pdf', None)
    #     if pdf is not None:
    #         main, sub = pdf.content_type.split('/')
    #         # main here would most likely be application, as pdf mime type is application/pdf, 
    #         # but I'd like to be on a safer side should in case it returns octet-stream/pdf
    #         if not (main in ["application", "octet-stream"] and sub == "pdf"):
    #             raise forms.ValidationError(u'Please use a PDF file')
        # return cd  
    # def clean_title(self,*args,**kwargs):
    #     title = self.cleaned_data.get("title")
    #     if "CFE" in title:
    #         return title
    #     if "news" not in title:
    #         raise forms.ValidationError("This is not a valid title")

    #     else:
    #         raise forms.ValidationError("This is not a valid title")