from django.shortcuts import render,redirect
from . models import *
from AdminApp.models import *
from UserApp.models import *

def mreg(request):
    return render(request,"managerregister.html")

def mreginsert(request):
    if request.method == "POST":
        name = request.POST.get('mname')
        img = request.FILES.get('mimg')
        email = request.POST.get('memail')
        phone = request.POST.get('mpnum')
        password = request.POST.get('mpass')
        exp = request.POST.get('mexp')
        gender = request.POST.get('mradio')
        data = Manager(ManagerReg_Name=name,ManagerReg_Image=img,ManagerReg_Email=email,ManagerReg_PhNumber=phone,ManagerReg_Password=password,ManagerReg_Experience=exp,ManagerReg_Gender=gender)
        data.save()
    return redirect('login')

def managerlogout(request):
    del request.session['m_id']
    del request.session['m_phonenumber']
    del request.session['m_email']
    del request.session['m_name']
    del request.session['m_password']
    return redirect('login')

def mhome(request):
    locate = Locations.objects.all()
    uid = request.session['m_id']
    data = Manager.objects.filter(id=uid)
    return render(request,"managerhome.html",{'vmd':data,'vl':locate})

def mprofile(request):
    uid = request.session['m_id']
    data = Manager.objects.filter(id=uid)
    return render(request,"managerprofile.html",{'vmd':data})

def mvturfs(request,location):
    turf = Turfs.objects.filter(Turf_Location = location)
    return render(request,"mviewturfs.html",{'vt':turf})

def mvmturf(request,id):
    turf = Turfs.objects.filter(id=id)
    return render(request,"managerviewmore.html",{'vmt':turf})

def massignturf(request):
    name = request.session['m_name']
    turf = Turfs.objects.filter(Turf_Manager_Name=name)
    return render(request,"mturfassign.html",{'vt':turf})

def mturfbook(request):
    uid = request.session['m_name']
    data =  Booking.objects.filter(Booking_Turf=Turfs.objects.get(Turf_Manager_Name=uid),Booking_Status="Pending")
    print(data)
    return render(request,"mvturfbook.html",{'vtb':data})

def approve(request,id):
    Booking.objects.filter(id=id).update(Booking_Status="Approved")
    return redirect("mturfbook")

def decline(request,id):
    Booking.objects.filter(id=id).update(Booking_Status="Declined")
    return redirect("mturfbook")

# Create your views here.
