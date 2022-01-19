import justpy as jp
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pytz import utc
data = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
data['Month'] = data['Timestamp'].dt.strftime('%Y-%m')
monthly_average_course = data.groupby(['Month','Course Name'])['Rating'].count().unstack()


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
            text: 'Fruit units'
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
    hc.options.xAxis.categories = list(monthly_average_course.index)

    hc_data = [{"name":v1[1],"data":[v2 for v2 in monthly_average_course[v1]]} for v1 in monthly_average_course.columns]
    hc.options.series =hc_data


    return wp

jp.justpy(app)

