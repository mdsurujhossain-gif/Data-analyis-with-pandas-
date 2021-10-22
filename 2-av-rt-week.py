import justpy as jp
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pytz import utc
data = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
data['Week'] = data['Timestamp'].dt.strftime('%Y-%U')
week_average = data.groupby(['Week']).mean()




charts_def = """{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Average Rating by Week'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Week'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: '',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of course reviews",classes="text-h3 text-center q-pt-md")
    p1 = jp.QDiv(a=wp,text="These grpahs represent course reviews ")
    hc = jp.HighCharts(a=wp,options=charts_def)
    hc.options.title.text = "Average Rating by Week"

    hc.options.xAxis.categories=list(week_average.index)
    hc.options.series[0].data=list(week_average["Rating"])


    return wp

jp.justpy(app)