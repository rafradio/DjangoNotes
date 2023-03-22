from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Note
from .forms import NoteForm
from django.views.generic import DetailView, UpdateView, DeleteView
import datetime

def index(request):
    notes = Note.objects.all().order_by('-date')
    data = {'notes': notes}
    return render(request, 'main/index.html', data)

def create_new(request):
    if request.method == 'POST': 
        print("Это POST запрос")
        d = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "title": request.POST['title'],
            "body": request.POST['body'],
            "date": d
        }
        form = NoteForm(data)
        for el in form:
            print(el.value())
        form.save()
    return render(request, 'main/new.html')

def notesDetailView(request, pk):
    if request.method == 'POST':   
        Note.objects.filter(id=pk).update(title=request.POST['title'], body=request.POST['body'])
        return redirect('main')
    note = Note.objects.get(id=pk)
    data = {'note': note}
    return render(request, 'main/edit.html', data)

# class NotesDetailView(DetailView):
#     model = Note
#     template_name = 'main/edit.html'
#     context_object_name = 'note'

def notesDelete(request, pk):
    if request.method == 'POST':
        deleteNews = Note.objects.get(id=pk)
        deleteNews.delete()   
    return redirect('main')