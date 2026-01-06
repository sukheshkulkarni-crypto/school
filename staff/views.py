
from django.shortcuts import render,redirect
from .models import Staff
from .forms import StaffForm

def staff_list(request):
    q=request.GET.get('q')
    staffs=Staff.objects.all()
    if q:
        staffs=staffs.filter(name__icontains=q)
    return render(request,'list.html',{'staffs':staffs})

def staff_create(request):
    form=StaffForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{'form':form})

def staff_update(request,id):
    p=Staff.objects.get(id=id)
    form=StaffForm(request.POST or None,instance=p)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'form.html',{'form':form})

def staff_delete(request,id):
    Staff.objects.get(id=id).delete()
    return redirect('/')

