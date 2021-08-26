from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import todoform
from .models import todo
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class listview(ListView):
    model=todo
    template_name ='index.html'
    context_object_name = 'task2'

class detailview(DetailView):
    model = todo
    template_name = 'detail.html'
    context_object_name = 'task4'

class updateview(UpdateView):
    model = todo
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('task','priority','date')

    def get_success_url(self):
        return reverse_lazy('detail',kwargs={'pk':self.object.id})




class deleteview(DeleteView):
    model = todo
    template_name = 'delete.html'
    context_object_name = 'task1'
    success_url = reverse_lazy('index')






def index(request):

    if request.method=='POST':
        task=request.POST.get('task','')
        prior=request.POST.get('prior','')
        date=request.POST.get('date','')
        task1=todo(task=task,priority=prior,date=date)
        task1.save()
    task2 = todo.objects.all()
    return render(request,'index.html',{'task2':task2})
def update(request,id):
      task=todo.objects.get(id=id)
      form=todoform(request.POST or None,instance=task)
      if form.is_valid():
          form.save()
          return redirect('/')
      return render(request,'update.html',{'task':task,'form':form})
def delete(request,id):
    task=todo.objects.get(id=id)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')