from django.shortcuts import render,redirect
from . models import *
from UserApp.models import *
from ManagerApp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def ahome(request):
    location = Locations.objects.all().count()
    turf = Turfs.objects.all().count()
    rmanager = Manager.objects.filter(ManagerReg_Status="Pending").count()
    amanager = Manager.objects.filter(ManagerReg_Status="Approved").count()
    users = Uregister.objects.all().count()
    bookings = Booking.objects.all().count()
    feedback = Feedback.objects.all().count()
    return render(request,"adminhome.html",{'countloc':location,'countturf':turf,'countmanager':rmanager,'countamanager':amanager,'countuser':users,'countbook':bookings,'countfeedback':feedback})

def location(request):
    return render(request,"addlocations.html")

def linsert(request):
    if request.method == 'POST':
        name = request.POST.get('lname')
        img = request.FILES.get('limg')
        data = Locations(Location_Name=name,Location_Image=img)
        data.save()
    return redirect('location')

def turfs(request):
    locate = Locations.objects.all()
    data = Manager.objects.filter(ManagerReg_Status='Approved')
    return render(request,"addturfs.html",{'vtl':locate,'vmd':data})

def tinsert(request):
    if request.method == 'POST':
        name = request.POST.get('tname')
        img = request.FILES.get('timg')
        price = request.POST.get('tbprice')
        facilities = request.POST.get('tfacl')
        location = request.POST.get('tlocate')
        manager = request.POST.get('tmname')
        time = request.POST.get('ttime')
        data = Turfs(Turf_Name=name,Turf_Image=img,Turf_Booking_price=price,Turf_Facilities=facilities,Turf_Location=location,Turf_Manager_Name=manager,Turf_Working_time=time)
        data.save()
    return redirect('turfs')

def vlocat(request):
    locate = Locations.objects.all()
    return render(request,"viewlocations.html",{'vtl':locate})

def ledit(request,id):
    details = Locations.objects.filter(id=id)
    return render(request,"editlocations.html",{'vld':details})

def ldelete(request,id):
    Locations.objects.filter(id=id).delete()
    return redirect('vlocat')

def lupdate(request,id):
    if request.method == 'POST':
        name = request.POST.get('lname')
        try:
            img_c = request.FILES['limg']
            fs = FileSystemStorage()
            limg = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            limg = Locations.objects.get(id=id).Location_Image
        Locations.objects.filter(id=id).update(Location_Name=name,Location_Image=limg)
    return redirect('vlocat')

def vturf(request):
    turf = Turfs.objects.all()
    return render(request,"viewturfs.html",{'vt':turf})

def vedit(request,id):
    data = Manager.objects.filter(ManagerReg_Status='Approved')
    locate = Locations.objects.all()
    details = Turfs.objects.filter(id=id)
    return render(request,"editturfs.html",{'vtd':details,'vtl':locate,'vmd':data})

def vdelete(request,id):
    Turfs.objects.filter(id=id).delete()
    return redirect('vturf')

def vupdate(request,id):
    if request.method == 'POST':
        name = request.POST.get('tname')
        price = request.POST.get('tbprice')
        facilities = request.POST.get('tfacl')
        location = request.POST.get('tlocate')
        manager = request.POST.get('tmname')
        time = request.POST.get('ttime')
        try:
            img_c = request.FILES['timg']
            fs = FileSystemStorage()
            timg = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            timg = Turfs.objects.get(id=id).Turf_Image
        Turfs.objects.filter(id=id).update(Turf_Name=name,Turf_Image=timg,Turf_Booking_price=price,Turf_Facilities=facilities,Turf_Location=location,Turf_Manager_Name=manager,Turf_Working_time=time)
    return redirect('vturf')

def vmanager(request):
    data = Manager.objects.filter(ManagerReg_Status = 'Pending')
    return render(request,"viewmanagers.html",{'vmd':data})

def msupdate(request,id):
    Manager.objects.filter(id=id).update(ManagerReg_Status = "Approved")
    return redirect('vmanager')

def vamanager(request):
    data = Manager.objects.filter(ManagerReg_Status = 'Approved')
    return render(request,"approvedmanagers.html",{'vmd':data})

def vuserbook(request):
    data = Booking.objects.all()
    return render(request,"viewuserbookings.html",{'vub':data})

def vfeedback(request):
    data = Feedback.objects.all()
    return render(request,"viewfeedbacks.html",{'vuf':data})

def vusers(request):
    data = Uregister.objects.all()
    return render(request,"viewusers.html",{'vud':data})

# Create your views here.
