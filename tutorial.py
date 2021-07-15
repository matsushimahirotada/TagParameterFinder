import PySimpleGUI as sg

sg.theme('DarkTeal7')   # デザインテーマの設定

# ウィンドウに配置するコンポーネント
layout = [  [sg.Text('TagFreq(Hz):',size=(15,1)),sg.Input(size=(20,1)),sg.Text('Diopter(Dptr):',size=(15,1)),sg.Input(size=(20,1))],
            [sg.Text('ExposureTime(us):',size=(15,1)), sg.InputText(size=(20,1)),sg.Text('MaxDptr(|Dptr|):',size=(15,1)),sg.Input(size=(20,1))],
            [sg.Button('OK'), sg.Button('キャンセル')] ]

# ウィンドウの生成
window = sg.Window('TagParameterFinder', layout)

# イベントループ
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'キャンセル':
        break
    elif event == 'OK':
        print('あなたが入力した値： ', values[0])

window.close()