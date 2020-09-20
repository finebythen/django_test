from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .models import *


def index_pdf(request):
    db = PdfExportModel.objects.all()

    context = {'db': db}
    return render(request, 'app_pdf/index_pdf.html', context)


def single_customer_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    customer_pdf = get_object_or_404(PdfExportModel, pk=pk)

    template_path = 'app_pdf/view_single_pdf.html'
    context = {'customer_pdf': customer_pdf}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # --> in case of direct download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # --> in case of online viewing
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def all_customer_render_pdf_view(request):
    customer_pdf_1 = get_object_or_404(PdfExportModel, pk=1)
    customer_pdf_2 = get_object_or_404(PdfExportModel, pk=2)

    template_path = 'app_pdf/view_all_pdf.html'
    context = {'customer_pdf_1': customer_pdf_1, 'customer_pdf_2': customer_pdf_2}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # --> in case of direct download
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # --> in case of online viewing
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def all_customer_render_pdf_download(request):
    customer_pdf_1 = get_object_or_404(PdfExportModel, pk=1)
    customer_pdf_2 = get_object_or_404(PdfExportModel, pk=2)

    template_path = 'app_pdf/view_all_pdf.html'
    context = {'customer_pdf_1': customer_pdf_1, 'customer_pdf_2': customer_pdf_2}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # --> in case of direct download
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # --> in case of online viewing
    # response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
