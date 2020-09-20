from django.urls import path
from . import views

urlpatterns = [
    path('chatbox/', views.Chatbox, name="Chatbox"),
    path('count-characters/', views.CountCharacters, name="CountCharacters"),
    path('count-characters-widget-tweaks/', views.CountCharactersWidgetTweaks, name="CountCharactersWidgetTweaks"),
    path('create/ticket/<str:pk>/', views.Ticket, name="Ticket"),
    path('csv/', views.csv_df_group, name="CsvDfGroup"),

    path('csv/load-and-save/', views.csv_load_save, name="CsvLoadSave"),

    path('pdf/main/render-pdf-view/', views.CustomerListView.as_view(), name="RenderMainPdfView"),
    path('pdf/view/<str:pk>/', views.customer_render_pdf_view, name="RenderCustomerPdfView"),

    path('pdf/reportLab/view/', views.reportlab_view, name="ReportLabView"),

    path('index/', views.Index, name="Index"),
    path('navbar/', views.Navbar, name="Navbar"),
    path('progressbar/', views.ProgressBar, name="ProgressBar"),
    path('radio-buttons/', views.RadioButtons, name="RadioButtons"),
    path('table-filter/', views.table_filter, name="TableFilter"),

    path('time/filter/ask/', views.time_filter_ask, name="TimeFilterAsk"),
    path('time/filter/answer/', views.time_filter_answer, name="TimeFilterAnswer"),

    path('transport-data/post/', views.transport_post, name="TransportPost"),
    path('transport-data/get/', views.transport_get, name="TransportGet"),

    path('textarea/', views.TextAreaScrollable, name="Textarea"),
    path('view/<str:pk>/', views.View, name="View"),
]
