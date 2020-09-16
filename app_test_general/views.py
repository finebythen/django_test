from django.db import connections, transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from django_pandas.io import read_frame
from sqlalchemy import create_engine
from time import strftime
import numpy as np
import csv
import pandas as pd
from datetime import timedelta, date, time, datetime

from .models import *
from .forms import *
from .filters import *


def Index(request):
    customer_db = Customer.objects.all()
    project_db = Project.objects.all()
    cluster_db = Cluster.objects.all()

    with connections['second_Db'].cursor() as cursor:
        cursor.execute("SELECT * FROM app_test5_car")
        row = cursor.fetchall()

    # with connections['second_Db'].cursor() as cursor:
    #     cursor.execute("SELECT * FROM app_test5_car")
    #     transaction.commit(using='second_Db')

    print('DEFAULT Database:____________________')
    print(' ')
    print(read_frame(cluster_db))
    print(' ')
    print(' ')
    print('SECOND Database:____________________')
    print(' ')
    print(row)
    print(type(row))

    df_second_db = pd.DataFrame(row, columns=[
        'id',
        'driver',
        'manufacturer',
        'model',
        'fuel',
        'tacho',
        'date_created',
    ])

    print(df_second_db)

    context = {'customer_db': customer_db, 'project_db': project_db, 'cluster_db': cluster_db}
    return render(request, 'app_test_general/index.html', context)


def View(request, pk):
    cluster_db = Cluster.objects.get(id=pk)

    context = {'cluster_db': cluster_db}
    return render(request, 'app_test_general/view_cluster.html', context)


def Ticket(request, pk):
    cluster_db = Cluster.objects.get(id=pk)

    form = TicketForm()
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.customer = cluster_db.customer
            form.instance.project = cluster_db.project
            form.instance.cluster = cluster_db.name
            form.instance.user_created = request.user
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Der Eintrag wurde erfolgreich gespeichert!')
            return redirect('View', pk=pk)
        else:
            messages.add_message(request, messages.WARNING, 'Der Eintrag konnte nicht gespeichert werden!')

    context = {'formset': form, 'cluster_db': cluster_db}
    return render(request, 'app_test_general/create_ticket.html', context)


def RadioButtons(request):
    colors = Colorname.objects.all()

    context = {'colors': colors}
    return render(request, 'app_test_general/radio_buttons.html', context)


def CountCharacters(request):

    context = {}
    return render(request, 'app_test_general/count_characters.html', context)


def CountCharactersWidgetTweaks(request):
    date_today = strftime('%d.%m.%Y')
    form = ExampleForm()

    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        form.instance.date_str = date_today
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Der Eintrag wurde erfolgreich gespeichert!')
        return redirect("Index")
    else:
        messages.add_message(request, messages.SUCCESS, 'Der Eintrag konnte nicht gespeichert werden!')

    context = {'formset': form}
    return render(request, 'app_test_general/count_characters_widget_tweaks.html', context)


def Navbar(request):

    context = {}
    return render(request, 'app_test_general/navbar.html', context)


def ProgressBar(request):

    context = {}
    return render(request, 'app_test_general/progressbar.html', context)


def TextAreaScrollable(request):
    textexamples = TextareaInput.objects.all()

    context = {'textexamples': textexamples}
    return render(request, 'app_test_general/scrollable_textarea.html', context)


def Chatbox(request):

    context = {}
    return render(request, 'app_test_general/chatbox.html', context)


def csv_df_group(request):
    # --> get information from database
    db = CsvGroupModel.objects.all()
    # --> load into dataframe
    df = read_frame(db)
    print(df)
    # --> replace data
    # df.replace("none", np.NaN)
    df = pd.wide_to_long(df, stubnames=['object', 'amount'], i=['id', 'name'], j='Hi', suffix='\w', sep="_").dropna()
    df = df[df['amount'] > 0]

    list_obj = df['object'].tolist()
    list_amont = df['amount'].tolist()

    print(df)

    for i in range(len(list_obj)):
        print(list_obj[i], ' | ', list_amont[i])

    context = {}
    return render(request, 'app_test_general/csv_df_group.html', context)


def table_filter(request):
    coworker_db = table_filter_model.objects.all()

    f = CoworkerFilter(request.GET, queryset=coworker_db)
    coworker_db = f.qs

    context = {'coworker_db': coworker_db, 'filter': f}
    return render(request, 'app_test_general/table_filter.html', context)


def transport_post(request):
    form = TransportExampleForm()

    if request.method == 'POST':
        form = TransportExampleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    context = {'formset': form}
    return render(request, 'app_test_general/transport_data_post.html', context)


def transport_get(request):

    if request.method == 'POST':
        name_get = request.POST.get('name', None)
        date_get = request.POST.get('date', None)

    context = {'name_get': name_get, 'date_get': date_get}
    return render(request, 'app_test_general/transport_data_get.html', context)


def time_filter_ask(request):

    context = {}
    return render(request, 'app_test_general/time_filter_ask.html', context)


def time_filter_answer(request):
    # --> get data
    if request.method == 'POST':
        name_get = request.POST.get('name', None)
        date_start_get = request.POST.get('date-start', None)
        date_end_get = request.POST.get('date-end', None)

    # --> convert data for filter from '%d-%M-%Y' to '%Y-%M-%d'
    try:
        date_start_str = datetime.strptime(date_start_get, '%Y-%m-%d').date()
        date_end_str = datetime.strptime(date_end_get, '%Y-%m-%d').date()
    except Exception as e:
        except_name = type(e).__name__  # --> returns the name of the exception

    # --> query database with date filtering
    df = read_frame(TimeFilteringExamples.objects.filter(date_start__range=[date_start_str, date_end_str]))
    # db = TimeFilteringExamples.objects.filter(date_start__range=[date_start_str, date_end_str]).filter(customer='blablah')

    print(df)

    context = {'name_get': name_get, 'date_start': date_start_get, 'date_end': date_end_get}
    return render(request, 'app_test_general/time_filter_answer.html', context)


def csv_load_save(request):
    # --> query (raw) database
    with connections['third_Db'].cursor() as cursor:
        cursor.execute("SELECT * FROM test_objects")
        row = cursor.fetchall()
    # --> get database-query into dataframe (pandas)
    df_db = pd.DataFrame(row, columns=[
        'id',
        'product',
        'price',
    ])

    list_df, list_id, list_products, list_prices = [], [], [], []

    if request.method == 'POST':
        # --> load csv-file by selecting
        file = request.FILES['document_csv']

        # --> convert csv-file into dataframe (pandas)
        df = pd.read_csv(file, sep=';')

        # --> catch first and last to elements for display in template (showing it worked!)
        list_id.append(df['id'].iloc[0])
        list_id.append(df['id'].iloc[1])
        list_id.append(df['id'].iloc[-1])
        list_id.append(df['id'].iloc[-2])

        list_products.append(df['product'].iloc[0])
        list_products.append(df['product'].iloc[1])
        list_products.append(df['product'].iloc[-2])
        list_products.append(df['product'].iloc[-1])

        list_prices.append(df['price'].iloc[0])
        list_prices.append(df['price'].iloc[1])
        list_prices.append(df['price'].iloc[-2])
        list_prices.append(df['price'].iloc[-1])

        # --> merge those items into list (for readability of <table> in template)
        x = 0
        while x < len(list_id):
            temp = [list_id[x], list_products[x], list_prices[x]]
            list_df.append(temp)
            x += 1

        # --> merge dataframes (database & csv-file) for comparison
        df_compared = pd.concat([df_db, df])

        # --> filter for unique values in column
        df_compared = df_compared.drop_duplicates(subset=['product'])

        # --> drop duplicates from filtered dataframe
        df_compared = pd.concat([df_compared, df_db]).drop_duplicates(keep=False)

        # --> keeping the columns that are necessary
        df_compared = df_compared[['id', 'product', 'price']]

        # # --> create engine with sqlalchemy (package)
        engine = create_engine('postgresql+psycopg2://postgres:2NzxmFa2sePy@localhost/DEMO_Load_Csv')
        df_compared.to_sql(
            name='test_objects',
            con=engine,
            index=False,
            # if_exists='replace'
            if_exists='append'
        )

    context = {'list_df': list_df}
    return render(request, 'app_test_general/csv_load_and_save.html', context)
