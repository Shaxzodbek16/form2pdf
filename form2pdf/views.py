import io
import uuid
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas


def make_pdf(data: dict[str, str], picture) -> bytes:
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica", 14)
    p.drawString(100, 800, "Fake University Application")
    p.drawString(100, 780, f"Name: {data.get('name', '')}")
    p.drawString(100, 760, f"Age: {data.get('age', '')}")
    p.drawString(100, 740, f"Email: {data.get('email', '')}")
    p.drawString(100, 720, f"Explanation: {data.get('explanation', '')}")
    if picture:
        try:
            img = ImageReader(picture)
            p.drawImage(img, 100, 550, width=150, height=150, preserveAspectRatio=True)
        except Exception:
            pass
    p.showPage()
    p.save()
    return buffer.getvalue()


def download(request):
    path = request.session.get('pdf_path')
    if not path:
        return HttpResponse('No PDF found', status=404)
    with default_storage.open(path, 'rb') as f:
        pdf = f.read()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="application.pdf"'
    return response


def get_form_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        explanation = request.POST.get('explanation')
        picture = request.FILES.get('picture')
        data = {
            'name': name,
            'age': age,
            'email': email,
            'explanation': explanation,
        }
        pdf_bytes = make_pdf(data, picture)
        file_name = f"{uuid.uuid4()}.pdf"
        path = default_storage.save(file_name, ContentFile(pdf_bytes))
        request.session['pdf_path'] = path
        return render(request, 'apply.html')
    return render(request, 'form_filling.html')
