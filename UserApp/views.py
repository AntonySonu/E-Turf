from django.shortcuts import render,redirect
from . models import *
from AdminApp.models import *
from ManagerApp.models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError

def uhome(request):
    locate = Locations.objects.all()
    return render(request,"userhome.html",{'vl':locate})

def uturf(request,location):
    turf = Turfs.objects.filter(Turf_Location = location)
    return render(request,"userturfs.html",{'vt':turf})

def vmturf(request,id):
    turf = Turfs.objects.filter(id=id)
    return render(request,"viewmoreturf.html",{'vmt':turf})

def login(request):
    return render(request,"login.html")

def uregister(request):
    return render(request,"uregister.html")

def ureg(request):
    if request.method == "POST":
        name = request.POST.get('rname')
        email = request.POST.get('remail')
        password = request.POST.get('rpass')
        phone = request.POST.get('rpnum')
        data = Uregister(UserReg_Name=name,UserReg_Email=email,UserReg_Password=password,UserReg_PhNumber=phone)
        data.save()
    return redirect('login')

def chklogin(request):
    if request.method == "POST":
        email=request.POST.get('lemail')
        password=request.POST.get('lpass')
        if Uregister.objects.filter(UserReg_Email=email,UserReg_Password=password).exists():
           data = Uregister.objects.filter(UserReg_Email=email,UserReg_Password=password).values('UserReg_Name','UserReg_PhNumber','id').first()
           request.session['u_id'] = data['id']
           request.session['u_name'] = data['UserReg_Name']
           request.session['u_phonenumber'] = data['UserReg_PhNumber'] 
           request.session['u_email'] = email
           request.session['u_password'] = password
           return redirect('uhome')
        elif Manager.objects.filter(ManagerReg_Email=email,ManagerReg_Password=password,ManagerReg_Status='Approved').exists():
                data = Manager.objects.filter(ManagerReg_Email=email,ManagerReg_Password=password).values('ManagerReg_Name','ManagerReg_Image','ManagerReg_PhNumber','ManagerReg_Experience','ManagerReg_Gender','id').first()
                request.session['m_id'] = data['id']
                request.session['m_name'] = data['ManagerReg_Name']
                request.session['m_phonenumber'] = data['ManagerReg_PhNumber'] 
                request.session['m_email'] = email
                request.session['m_password'] = password
                request.session['m_image'] = data['ManagerReg_Image']
                request.session['m_experience'] = data['ManagerReg_Experience'] 
                request.session['m_gender'] = data['ManagerReg_Gender'] 
                request.session['m_status'] = 'Approved'
                return redirect('mhome')
        elif "admin@gmail.com"==email and "admin"==password:
                return redirect('ahome')
        else:
            return render(request,'login.html',{'msg':'invalid user credentials'})
    else:
        return redirect('login')

def userlogout(request):
    del request.session['u_id']
    del request.session['u_phonenumber']
    del request.session['u_email']
    del request.session['u_name']
    del request.session['u_password']
    return redirect('login')

def bturf(request,id):
    uid = request.session['u_id']
    details = Uregister.objects.filter(id=uid)
    data = Turfs.objects.filter(id=id)
    return render(request,"bookturf.html",{'btd':data,'bud':details})

def book(request):
    if request.method == 'POST':
        user_id = request.session['u_id']
        turf_id = request.POST.get('tid')
        date = request.POST.get('bdate')
        time = request.POST.get('btime')
        data = Booking(Booking_User=Uregister.objects.get(id=user_id),Booking_Turf=Turfs.objects.get(id=turf_id),Booking_Date=date,Booking_Time=time)
        data.save()
    return redirect('/')

def bhistory(request):
    uid = request.session['u_id']
    data = Booking.objects.filter(Booking_User=uid)
    return render(request,"bookhistory.html",{'vbd':data})

def contact(request):
    return render(request,"contact.html")

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        email = request.POST.get('femail')
        subject = request.POST.get('fsubject')
        message = request.POST.get('fmessage')
        data = Feedback(Feedback_Name=name,Feedback_Email=email,Feedback_Subject=subject,Feedback_Message=message)
        data.save()
    return redirect('contact')

# Create your views here.
