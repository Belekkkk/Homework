from django.shortcuts import render, redirect

from apps.hompage.models import Hompage


def index(request):
    hompage = Hompage.objects.all()
    return render(request, 'index.html', locals())

def create(request):
    if request.method == 'HOMPAGE':
        name = request.HOMPAGE['title']
        description = request.HOMPAGE['text']
        hompage = Hompage.objects.create(title = name,text = description)
        return redirect('hompage')
    return render(request,'create.html')

def retrieve(request, pk):
    hompage = Hompage.objects.get(id=pk)
    return render(request, 'detail.html', locals())

def update(request, pk):
    if request.method == 'HOMPAGE':
        name = request.HOMPAGE['title']
        description = request.HOMPAGE['text']
        hompage = Hompage.objects.get(id=pk)
        hompage.title = name
        hompage.text = description
        hompage.save()
        return redirect('detail', hompage.id)
    return render(request, 'update.html')

def destroy(request, pk):
    hompage = Hompage.objects.get(id=pk)
    hompage.delete()
    return redirect('hompages')

def add_done_task(task_list, task):
    task_list.append((task, True))

def display_tasks(task_list):
    for index, (task, done) in enumerate(task_list, start=1):
        status = "✅" if done else "❌" 