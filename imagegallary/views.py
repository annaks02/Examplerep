from django.shortcuts import render
from .forms import ImageForm
from .models import ImageGallary
# Create your views here.
def index(request):
    if request.method=="POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=ImageForm()
    img=ImageGallary.objects.all()
    dic_form={
        'form':form,
        'img':img
    }
    return render(request,"imagegallary.html",dic_form)