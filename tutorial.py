import PySimpleGUI as sg
import Calculatetaglens

sg.theme('DarkTeal7')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('TagFreq(Hz):',size=(15,1)),sg.Input(size=(20,1),key='freq'),sg.Text('Diopter(Dptr):',size=(15,1)),sg.Input(size=(20,1),key='dptr')],
            [sg.Text('ExposureTime(us):',size=(15,1)), sg.InputText(size=(20,1),key='Extime'),sg.Text('MaxDptr(|Dptr|):',size=(15,1)),sg.Input(size=(20,1),key='maxdptr')],
            [sg.Button('OK',key='cal'), sg.Button('リセット',key='reset')],
            [sg.Output(size=(50,20),key='outlines')]
        ]

# ウィンドウの生成
window = sg.Window('TagParameterFinder', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    if event == 'cal':
        window['outlines'].update('')
        freq = float(values['freq'])
        dptr = float(values['dptr'])
        maxdptr = float(values['maxdptr'])
        exposuretime = float(values['Extime'])
        
        time = Calculatetaglens.exposuretiming(freq,dptr,maxdptr)
        t1 = [time[0]*10**6,time[0]*10**6+exposuretime]
        t2 = [time[1]*10**6,time[1]*10**6+exposuretime]
        
        t1hex = [round(time[0]/(10*10**-9)),round((time[0]+exposuretime/(10**6))/(10*10**-9))]
        t2hex = [round(time[1]/(10*10**-9)),round((time[1]+exposuretime/(10**6))/(10*10**-9))]
        
        print(f'Exposure timing(1):{t1[0]:.4f}us -- {t1[1]:.4f}us')
        print(f'-------------------{t1hex[0]:x} -- {t1hex[1]:x}')
        print(f'Exposure timing(2):{t2[0]:.4f}us -- {t2[1]:.4f}us')
        print(f'-------------------{t2hex[0]:.x} -- {t2hex[1]:.x}')
        print('------------------------',hex(312),'-',hex(362),"(resolution 10ns)")
    if event == 'reset':
        window['outlines'].update('')
        
        
    
    
    
window.close()