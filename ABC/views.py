from django.shortcuts import render
from django.http import HttpResponse
from ABC.models import *
from .forms import StudentForm, PaymentDetailsForm
# Create your views here.

def view_getpaymentdetail(request):
    if request.method=='GET':
       return render(request, "abc/pay.html")
    elif  request.method=='POST':
        sid=int(request.POST.get('txtsid',0))
        stu=Student.objects.get(id=sid)
        allpay=stu.paymentdetails_set.all()
        d1={'payments':allpay,'stu':stu}
        return render(request,'ABC/pay.html',context=d1)
    

def view_course(request):
    allc=Course.objects.all()
    d1={'courses':allc}
    c=Course.objects.get(id=1)
    allstu=c.students.all()
    d1['cid']=c.id
    d1['cname']=c.name
    d1['students']=allstu
    if request.method=='GET':        
        return render(request,'ABC/student.html',context=d1)
    elif request.method=='POST':
        cid=int(request.POST.get('txtCourse', 0))
        c=Course.objects.get(id=cid)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        return render(request,'ABC/student.html',context=d1)
    
def view_studenform(request):
    if request.method=='GET':
        frm_unbound=StudentForm()
        d1={'forms':frm_unbound}
        return render(request,'ABC/stufrm.html',context=d1)
    elif request.method=='POST':
        frm_bound=StudentForm(request.POST,files=request.FILES)
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("<h1>Student Save Successfully</h1>")
        else:
             frm_bound=StudentForm()
             d1={'forms':frm_bound}
             return render(request,'ABC/stufrm.html',context=d1)

def view_paymentform(request):
    if request.method=='GET':
        frm_unbound=PaymentDetailsForm()
        d1={'forms':frm_unbound}
        return render(request,'ABC/payfrm.html',context=d1)
    elif request.method=='POST':
        frm_bound=PaymentDetailsForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            return HttpResponse("<h1>Payment Save Successfully</h1>")
        else:
            frm_bound=PaymentDetailsForm()
            d1={'forms':frm_bound}
            return render(request,'ABC/payfrm.html',context=d1)
        

def view_show_student_with_img(request,sid):
    stu=Student.objects.get(id=sid)
    d1={'stu':stu}
    return render(request,'ABC/stuimg.html',context=d1)        


def view_static_media(request):
    return render(request,'ABC/staticmedia.html')