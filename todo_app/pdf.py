from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, FileResponse
from django.urls import reverse
from .models import Todo, Pdf
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
import io
import django_rq
from django.core.files import File



def generate_pdf(my_dict):
    user = my_dict['user']
    todos = my_dict['todos']
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    x = 50
    y = 10.5
    for i, todo in enumerate(todos):
        textobject = p.beginText()
        textobject.setTextOrigin(x, (y-i/2)*inch)
        textobject.setFont("Helvetica", 12)
        textobject.textLines(f'{todo.text}')
        p.drawText(textobject)
    p.showPage()
    p.save()

    buffer.seek(0)

    with open(f'{user.username}-report.pdf', 'wb') as f:
        f.write(buffer.getbuffer())
        print(buffer)
        # Pdf.create_pdf(user, f)
    
    # if Pdf.objects.filter(user=user):
    #     Pdf.update_pdf(f'{user.username}-report.pdf')
    #     print("update")
    # else:
    # Pdf.create_pdf(user, f'{user.username}-report.pdf')
    #     print("create")
    
    

    # f = open(buffer)
    # myfile = File(f)
    # Pdf.create_pdf(user, myfile)