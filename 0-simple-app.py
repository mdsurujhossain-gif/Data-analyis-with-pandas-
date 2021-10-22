import justpy as jp
from pandas.core.dtypes.common import classes


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp,text="Analysis of course reviews",classes="text-h3 text-center q-pt-md")
    p1 = jp.QDiv(a=wp,text="These grpahs represent course reviews ")

    
    return wp

jp.justpy(app) 