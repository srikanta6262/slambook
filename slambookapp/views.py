from django.shortcuts import render,redirect
from django.http import HttpResponse
from slambookapp.models import Fillup
# Create your views here.
def first(request):
    return render(request,'index.html')
def task(request):
    return render(request,'fill.html')
def verify(request):
    if request.method=="POST":
        Firstname=request.POST["Name"]
        password=request.POST["Password"]
        if Firstname=="gayatri" and password=="123456":
            return redirect('/admin/')
        else:
            dict={"msg2":"Sorry Your Details is Incorrect..."}
            return render(request,'index.html',context=dict)
    else:
        return render(request,'index.html')



def data(request):
    if request.method=="POST":
        Firstname=request.POST["Firstname"]
        Lastname=request.POST["Lastname"]
        Nickname=request.POST["Nickname"]
        photo=request.FILES["myfiles"]
        ph=request.POST["ph"]
        add=request.POST["add"]
        dob=request.POST["dateofbirth"]
        zodiac=request.POST["zodiacsign"]
        gender=request.POST["gender"]
        fathername=request.POST["fathername"]
        mothername=request.POST["mothername"]
        brothername=request.POST["brothername"]
        sistername=request.POST["sistername"]
        Bestfriendname=request.POST["Bestfriendname"]
        twitter=request.POST["twitter"]
        facebook=request.POST["facebook"]
        instagram=request.POST["instagram"]
        txtmail=request.POST["txtmail"]
        about=request.POST["about"]
        Relation=request.POST["Relation"]
        likes=request.POST["like"]
        suggestions=request.POST["suggestion"]
        fetch=Fillup.objects.filter(Firstname=Firstname,Lastname=Lastname,phone=ph) | Fillup.objects.filter(phone=ph)
        count=len(fetch)
        if count>0:
            dict={"msg1":"Sorry your Details alreday submited"}
            return render(request,'index.html',context=dict)
        else:
            data=Fillup.objects.create(Firstname=Firstname,Lastname=Lastname,Nickname=Nickname,image=photo,phone=ph,add=add,
            dob=dob,zodiac=zodiac,gender=gender,fathername=fathername,mothername=mothername,brothername=brothername,sistername=sistername,
            Bestfriendname=Bestfriendname,twitter=twitter,facebook=facebook,instagram=instagram,txtmail=txtmail,about=about,Relation=Relation,
            likes=likes,suggestions=suggestions)
            data.save()
            dict={"msg":'''Thank you for being my friend, you have filled my life with pleasure and
            amusement and had spread so many colors around it,
            I wish to walk along with you till the last moment of my life.'''}
            return render(request,'index.html',context=dict)
    else:
        return render(request,'index.html')
