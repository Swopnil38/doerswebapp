from django.shortcuts import render
from homepage.models import doersdetails,willingdoersdetails,emaillist
from django.contrib import messages


def Insertdoersdetails(request):
    if request.method=='POST':
        if request.POST.get('doers_name') and request.POST.get('doers_profession') and request.POST.get('doers_timeinfield') and request.POST.get('doersimpactdesc') and request.POST.get('doers_willingness') and request.POST.get('doers_contact'):
            savedetails = doersdetails()
            savedetails.doers_name=request.POST.get('doers_name')
            savedetails.doers_profession=request.POST.get('doers_profession')
            savedetails.doers_timeinfield=request.POST.get('doers_timeinfield')
            savedetails.doersimpactdesc=request.POST.get('doersimpactdesc')
            savedetails.doers_willingness=request.POST.get('doers_willingness')
            savedetails.doers_contact=request.POST.get('doers_contact')
            savedetails.save()
            messages.success(request,'Your Record Has been Added')
            return render(request,'home.html')
        elif request.POST.get('willingdoers_name') and request.POST.get('willingdoers_experties') and request.POST.get('willingdoers_skillset') and request.POST.get('willingdoers_want') and request.POST.get('willingdoers_education') and request.POST.get('willingdoers_contact'):
            savedetails = willingdoersdetails()
            savedetails.willingdoers_name=request.POST.get('willingdoers_name')
            savedetails.willingdoers_experties=request.POST.get('willingdoers_experties')
            savedetails.willingdoers_skillset=request.POST.get('willingdoers_skillset')
            savedetails.willingdoers_want=request.POST.get('willingdoers_want')
            savedetails.willingdoers_education=request.POST.get('willingdoers_education')
            savedetails.willingdoers_contact=request.POST.get('willingdoers_contact')
            savedetails.save()
            messages.success(request,'Your Record Has been Added')
            return render(request,'home.html')
        elif request.POST.get('email'):
            savedetails = emaillist()
            savedetails.email = request.POST.get('email')
            savedetails.save()
            messages.success(request,'Your Record Has been Added')
            return render(request,'home.html')
    else:
            return render(request,'home.html')
 