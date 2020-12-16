from django.shortcuts import render, get_object_or_404, reverse
from .models import Todo, Pdf
from django.http import HttpResponseRedirect, FileResponse
from django.contrib.auth.decorators import login_required, user_passes_test
import django_rq
from .pdf import generate_pdf
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# def group_required(*group_names):
#     def in_groups(u):
#         if u.is_authenticated:
#             if bool(u.groups.filter(name__in=group_names)) | u.is_superuser:
#                 return True
#             return False
#     return user_passes_test(in_groups)

@login_required
# @group_required('customer')
def index(request):
    if request.method == "POST":
        Todo.create_todo(request.user, request.POST['text'])
    todos = Todo.objects.all().filter(user=request.user)
    django_rq.enqueue(generate_pdf, {
        'user':request.user,
        'todos': todos,
    })
    
    context = {
        'todos': todos
    }
    return render(request, 'todo_app/index.html', context)

@login_required
def change_status(request):
    pk = request.POST['pk']
    todo = get_object_or_404(Todo, pk=pk)
    todo.change_status()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def completed_todos(request):
    todos = Todo.objects.filter(status=True).filter(user=request.user)
    context = {
        'todos': todos
    }
    return render(request, 'todo_app/completed_todos.html', context)

@login_required
def delete_todo(request):
   print(request.META['HTTP_REFERER'])
   pk = request.POST["pk"]
   todo = get_object_or_404(Todo, pk=pk)
   todo.delete()
   return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def todo_details(request):
    context = {}
    pk = request.GET.get('pk')
    todo = get_object_or_404(Todo, pk=pk)
    context = {
        'todo': todo
    }
    return render(request, 'todo_app/todo_details.html', context)


def pdf_download(request):
    myPdf = Pdf.objects.filter(user=request.user)
    print(type(myPdf[0].document))
    return HttpResponseRedirect(reverse('todo_app:index'))
