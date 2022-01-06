import justpy as jp
from justpy import justpy
import pandas
from datetime import datetime
import matplotlib.pyplot as plt
from pytz import utc
data = pandas.read_csv('reviews.csv',parse_dates=['Timestamp'])
share = data.groupby(['Course Name'])["Rating"].count()



charts_def = """
 {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Course reviews parcentage'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of Course Review",classes = "text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp,text="These graphs represent course review analysis")
    
    hc = jp.HighCharts(a=wp,options=charts_def)
    hc_data = [{"name":v1,"y":v2} for v1,v2 in zip(share.index,share[1])]
    hc.options.series[0].data=hc_data
    
    return wp

jp.justpy(app)
