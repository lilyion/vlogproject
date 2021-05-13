from django.shortcuts import get_object_or_404,redirect, render
from .models import Vlog
from django.utils import timezone
from .forms import CreatePostForm
# Create your views here.

def home(request):
    vlogs = Vlog.objects
    return render(request,'home.html',{'vlogs':vlogs})

def detail(request, vlog_id):
    vlog_detail = get_object_or_404(Vlog, pk=vlog_id)
    return render(request, 'detail.html',{'vlog_detail':vlog_detail}) 

def create(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            vlog = form.save(commit=False)
            vlog.date = timezone.datetime.now()
            vlog.save()
        return redirect('/detail/'+str(vlog.id))
    else:
        form = CreatePostForm()
    return render(request, 'create.html',{'form':form})

def update(request,vlog_id):
    vlog = Vlog.objects.get(id=vlog_id)
    if request.method == "POST" :
        form = CreatePostForm(request.POST, instance=vlog)
        if form.is_valid():
            vlog = form.save()
            return redirect('/detail/'+str(vlog_id))
    else:
        form = CreatePostForm(instance=vlog)
        return render(request, 'create.html',{'form':form})

def delete(request,vlog_id):
        vlog = Vlog.objects.get(id=vlog_id)
        vlog.delete()
        return redirect('home')