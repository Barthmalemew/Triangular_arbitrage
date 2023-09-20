import PySimpleGUI as psg
import time
from turtle import *
import turtle
import krakenex

k = krakenex.API()

pair=[['XXBTZUSD', 'XETHZUSD', 'XETHXXBT'], ['XXBTZUSD', 'EOSUSD', 'EOSXBT'], ['XXBTZUSD', 'XXLMZUSD', 'XXLMXXBT'], ['XXBTZUSD', 'BCHUSD', 'BCHXBT'], ['XXBTZUSD', 'DASHUSD', 'DASHXBT'], ['XXBTZUSD', 'GNOUSD', 'GNOXBT'], ['XXBTZUSD', 'XETCZUSD', 'XETCXXBT'], ['XXBTZUSD', 'XREPZUSD', 'XREPXXBT'], ['XXBTZEUR', 'XETHZEUR', 'XETHXXBT'], ['XXBTZEUR', 'EOSEUR', 'EOSXBT'], ['XXBTZEUR', 'XXLMZEUR', 'XXLMXXBT'], ['XXBTZEUR', 'BCHEUR', 'BCHXBT'], ['XXBTZEUR', 'DASHEUR', 'DASHXBT'], ['XXBTZEUR', 'GNOEUR', 'GNOXBT'], ['XXBTZEUR', 'XETCZEUR', 'XETCXXBT'], ['XXBTZEUR', 'XREPZEUR', 'XREPXXBT']]

def k_trading_pair(a1):
    a_1 = k.query_public('Ticker', {"pair": a1[0]})
    a_2 = k.query_public('Ticker', {"pair": a1[1]})
    a_3 = k.query_public('Ticker', {"pair": a1[2]})

    return [a_1["result"], a_2["result"], a_3["result"]]

def calc_arb(a1,a2,a3):
    way1 = (1 * float(a1["b"][0]) * float(a3["b"][0]) / float(a2["a"][0]))
    way2 = (1 * float(a2["b"][0] / float(a3["a"][0]) / float(a1["a"][0])))

    return [way1-1,way2-1]


psg.theme('DarkAmber')   
# All the stuff inside your window. This is the PSG magic code compactor...

startingvalue = ''

layout=[[psg.Text('Base Currency', size=(20, 1),font='Lucido', justification='left')],
        [psg.Combo(['BTC', 'LTC', 'ETH'],default_value='BTC',key='Currency')],
        [psg.Text('Starting Amount', size=(20, 1),key= 'Starting', font='Lucido', justification='left'), psg.InputText(startingvalue)],
        [psg.Canvas(size=(100, 100), key= '-canvas-')],
        [psg.OK(), psg.Cancel()]]
# Create the Window
window = psg.Window('Triangular Arbitrage', layout)

canvas = window['-canvas-'].TKCanvas
first= ""
second = "" 
third = ""

    
# Event Loop to process "events"
while True:             
    event, values = window.read()
    for x in pair:
        first = x[0]
        second = x[1]
        third = x[2]

        turtle.bgcolor("dim gray")
        turtle.pencolor("#ffa500")
        turtle.right(120)
        turtle.forward(200)
        turtle.write(first)
        turtle.right(120)
        turtle.forward(200)
        turtle.write(second)
        turtle.right(120)
        turtle.forward(200)
        
        turtle.write(third)    
        turtle.right(120)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.write("Profit: $5")
        
        time.sleep(2)
        
        turtle.Screen().reset()

    if event in (psg.WIN_CLOSED, 'Cancel'):
        break


window.close()

