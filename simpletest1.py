import PySimpleGUI as psg
psg.theme('DarkAmber')

currency = ""
currencies = ('Euros', 'USD', 'Pounds')

layout = [  [psg.Text('Select the currency that you want to start with')],
            [psg.Listbox(currencies, size=(15, len(currencies)), key='-CURRENCY-', enable_events=True)],
            [psg.Text('Starting Amount'), psg.InputText()]]
            

window = psg.Window('Select a currency', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_ClOSEED:
        break
    if values['-CURRENCY-']:
        currency = '-CURRENCY-'
        psg.popup({values[currency][0]})
window.close()

