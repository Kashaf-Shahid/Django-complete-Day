from django.shortcuts import render
from .models import Article
from .form import ContactForm
from django.core.mail import send_mail

# Create your views here.

def year_archive(request, year):
   a_list = Article.objects.filter(pub_date__year=year)
   context = {'year': year, 'article_list': a_list}
   return render(request, 'news/year_archive.html', context)

def goHome (request):
  return render(request,"practice/home.html",{"dummy":"data"})

def loadContact(request):
   return render(request,"news/forms.html",{"data":"mydata"})


def getContact (request):
   if request.method=="POST":
      form = ContactForm(request.POST)
      if form.is_valid():
         subject = form.cleaned_data['subject']
         message = form.cleaned_data['message']
         sender = form.cleaned_data['sender']
         cc_myself = form.cleaned_data['cc_myself']
         recipients = ['info@example.com']

         if cc_myself:
          recipients.append(sender)

          send_mail(subject, message, sender, recipients)
          return render(request,'news/html',{'data':form.cleaned_data})

def loadComment(request):
   return render(request, "news/blogcomment.html", {"dummy":"123"})

def storeComment(request):
   return render(request, "news/home.html", {"data":"myform"})