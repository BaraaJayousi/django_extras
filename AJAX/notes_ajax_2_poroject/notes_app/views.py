from django.shortcuts import render, redirect
from django.views.generic import View
from django.template.loader import get_template
from .models import Note

# Create your views here.


def index(request):
  note_template = get_template('note_template.html')
  all_notes = Note.objects.all()
  context = {
    "note_template": note_template.render(request= request, context={"notes":all_notes})
  }
  return render(request, 'index.html', context)


class Notes(View):
  note_template = "note_template.html"
  context ={  }

  def get(self,request):
    self.context['notes'] =Note.objects.all()
    return render(request, self.note_template, self.context)
  
  def post(self, request):
    if request.POST['action'] == 'new_note':
      Note.objects.create(title= request.POST['note_title'])
    elif request.POST['action'] == 'edit_note':
      note = Note.objects.filter(id = request.POST['note_id']).first()
      if note:
        note.description = request.POST['description']
        note.save()
    elif request.POST['action'] == 'delete_note':
      note = Note.objects.filter(id = request.POST['note_id']).first()
      if note:
        note.delete()
    
    return redirect('/notes')