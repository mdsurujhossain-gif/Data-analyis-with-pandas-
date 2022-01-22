import pandas as pd
import openpyxl
import justpy as jp
import os
import pandas
from openpyxl import load_workbook
from datetime import datetime 
import matplotlib.pyplot as plt
from pytz import utc

df = pandas.read_excel(io='kpi.xlsx',
                    engine='openpyxl',
                    sheet_name='Daily_KPI',
                    usecols='D,F,H',nrows=1000,

                    parse_dates=['Date'])
                    # we can user skiprows= 3 to skip first three rows.
                    
df = df[df['Date'] != '30 Dates']
df = df[df['Date'] != '31 Dates']

df['Date'] = pandas.to_datetime(df.Date, format='%Y-%m-%d %H:%M:%S')
df['Date'] = df['Date'].dt.strftime('%Y-%m-%d')

day_wise = df.groupby(['Date','KPI Name2']).sum().unstack()



charts_def =  """
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average rating of courses by course by month'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Course units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of course reviews",classes="text-center text-h1 q-pt-md")
    p1 = jp.QDiv(a=wp,text="These grpahs represent course reviews")
    hc = jp.HighCharts(a=wp,options=charts_def)
    hc.options.title.text = "Average Rating by course by month"
    hc.options.xAxis.categories = list(day_wise.index)

    hc_data = [{"name":v1[1],"data":[v2 for v2 in day_wise[v1]]} for v1 in day_wise.columns]
    hc.options.series =hc_data


    return wp

jp.justpy(app)