from django.urls import path
from . import views

urlpatterns = [
    path('index/pdf/', views.index_pdf, name="IndexPDF"),
    path('index/pdf/view/single/<str:pk>/', views.single_customer_render_pdf_view, name="RenderSinglePdfView"),
    path('index/pdf/view/all/', views.all_customer_render_pdf_view, name="RenderAllPdfView"),
    path('index/pdf/download/', views.all_customer_render_pdf_download, name="RenderAllPdfDownload"),
]
