import PySimpleGUI as sg

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
        
        print('Exposure timing:',3.12,'-',3.625)
        print('------------------------',hex(312),'-',hex(362),"(resolution 10ns)")
    if event == 'reset':
        window['outlines'].update('')
        
        
    
    
    
window.close()