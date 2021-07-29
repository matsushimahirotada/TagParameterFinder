import PySimpleGUI as sg
import sys
import os
import Calculatetaglens

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

sg.theme('DarkTeal7')

layout = [  [sg.Text('TagFreq(Hz):',size=(15,1)),sg.Input(size=(20,1),key='freq'),sg.Text('Diopter(Dptr):',size=(15,1)),sg.Input(size=(20,1),key='dptr')],
            [sg.Text('ExposureTime(ns):',size=(15,1)), sg.InputText(size=(20,1),key='Extime'),sg.Text('MaxDptr(|Dptr|):',size=(15,1)),sg.Input(size=(20,1),key='maxdptr')],
            [sg.Button('OK',key='cal'), sg.Button('reset',key='reset')],
            [sg.Output(size=(50,20),key='outlines')]
        ]

window = sg.Window('TagParameterFinder', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'cal':
        window['outlines'].update('')
        try:
            freq = float(values['freq'])
            dptr = float(values['dptr'])
            maxdptr = abs(float(values['maxdptr']))
            exposuretime = float(values['Extime'])
        except ValueError:
            sg.PopupCancel('There is non-numeric data!',title='Error')
        else:
            time = Calculatetaglens.exposuretiming(freq,dptr,maxdptr)
            t1 = [time[0]*10**6,time[0]*10**6+exposuretime/1000]
            t2 = [time[1]*10**6,time[1]*10**6+exposuretime/1000]
            t1hex = [round(time[0]/(10*10**-9)),round((time[0]+exposuretime/(10**9))/(10*10**-9))]
            t2hex = [round(time[1]/(10*10**-9)),round((time[1]+exposuretime/(10**9))/(10*10**-9))]
            
            print(f'Exposure timing(1):{t1[0]:.4f}us -- {t1[1]:.4f}us')
            print(f'--------Hex-------------      0x{t1hex[0]:x} -- 0x{t1hex[1]:x}',sep='----')
            print(f'Exposure timing(2):{t2[0]:.4f}us -- {t2[1]:.4f}us')
            print(f'--------Hex-------------      0x{t2hex[0]:x} -- 0x{t2hex[1]:x}',sep='----')
            
    if event == 'reset':
        window['outlines'].update('')
    
    
window.close()