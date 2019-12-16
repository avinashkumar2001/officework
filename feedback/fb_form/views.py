from django.shortcuts import render
from .forms import fb_form_Form

def index(request):
    if request.method== 'POST':
        form = fb_form_Form(request.POST)

        if(form.is_valid()):
            form.save()

            return render(request,'fb_form/thanks.html')
        else:
            return render(request, 'fb_form/than.html')
    else:
        form= fb_form_Form()
    return render(request,'fb_form/fb_form.html',{'form':form})