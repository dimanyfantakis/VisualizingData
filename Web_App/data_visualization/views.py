from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from .forms import ChooseMeasurement, ChooseCountry
import logging

logger = logging.getLogger(__name__)
cursor = connection.cursor()


def home(request):
    return render(request, 'data_visualization/home.html')


def info(request):
    cursor.execute('SELECT C_Name from Countries')
    query_countries = cursor.fetchall()
    cursor.execute('SELECT Year from Years')
    query_years = cursor.fetchall()
    cursor.execute('SELECT * from Measurements')
    query_measurements = cursor.description
    query_measurements2 = []
    for i in range(len(query_measurements)):
        query_measurements2.append(query_measurements[i][:-6])
    t = ()
    query_measurements2 = query_measurements2[2:-1]
    for i in range(len(query_measurements2)):
        t2 = ()
        a = query_measurements2[i][0].replace('_', ' ')
        t2 += tuple([a])
        t += t2
    return render(request, 'data_visualization/info.html', {'Query1': query_countries, 'Query2': query_years,
                                                            'Query3': t})


def line_graph(request):
    if request.method == "POST":
        form_country = ChooseCountry(request.POST)
        form_measurement = ChooseMeasurement(request.POST)
        if form_country.is_valid() and form_measurement.is_valid():
            c_name = form_country.cleaned_data['name_country']
            m_name_t = form_measurement.cleaned_data['name_measurement']
            m_name = '_'.join(m_name_t.split(' '))
            label = m_name_t + ' in ' + c_name
            c_name += '\r'
            query = 'SELECT C_ID FROM Countries WHERE C_Name = %s;', [c_name]
            cursor.execute('SELECT ' + m_name + ' FROM Measurements WHERE Countries_C_ID in %s;', [query])
            query_measurement = cursor.fetchall()
            cursor.execute('SELECT Year FROM Years')
            query_years = cursor.fetchall

            return render(request, 'data_visualization/line_chart.html', {'Query': query_measurement,
                                                                          'Query2': query_years, 'Label': label})
    else:
        form_country = ChooseCountry()
        form_measurement = ChooseMeasurement()
    return render(request, 'data_visualization/form_line.html', {
        "form_country": form_country, "form_measurement": form_measurement
    })


def bar_graph(request):
    if request.method == "POST":
        form_country = ChooseCountry(request.POST)
        form_measurement = ChooseMeasurement(request.POST)
        if form_country.is_valid() and form_measurement.is_valid():
            c_name = form_country.cleaned_data['name_country']
            m_name_t = form_measurement.cleaned_data['name_measurement']
            m_name = '_'.join(m_name_t.split(' '))
            label = m_name_t + ' in ' + c_name
            c_name += '\r'
            query = 'SELECT C_ID FROM Countries WHERE C_Name = %s;', [c_name]
            cursor.execute('SELECT ' + m_name + ' FROM Measurements WHERE Countries_C_ID in %s;', [query])
            query_measurement = cursor.fetchall()
            cursor.execute('SELECT Year FROM Years')
            query_years = cursor.fetchall
            return render(request, 'data_visualization/bar_chart.html', {'Query': query_measurement,
                                                                         'Query2': query_years, 'Label': label})
    else:
        form_country = ChooseCountry()
        form_measurement = ChooseMeasurement()
    return render(request, 'data_visualization/form_bar.html', {
        "form_country": form_country, "form_measurement": form_measurement
    })


def scatter_graph(request):
    return render(request, 'data_visualization/scatter_chart.html')
