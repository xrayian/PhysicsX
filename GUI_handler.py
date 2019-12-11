import PySimpleGUI as sg
from support import Velocity, Distance, Time, Acceleration
from os import getlogin
from re import sub

error_count = 0
def parse_data(string, default = None, zero = 0):
    global error_count
    if string == "":
        return default
    else:
        try:
            return float(string)
        except:
            if error_count == 0:
                error_count += 1
                sg.popup_error('Do not enter anything other than numbers in these fields',title='Warning')
            print("[Parse_Error]: `"+ string + "` is not a valid number")

sg.set_options(element_padding=(5,5),icon="images/icon.ico",)
sg.change_look_and_feel('blueMono')
layout = [
    [sg.Text('Initial Velocity'), sg.InputText(focus=True,key='ivelocity'), sg.InputCombo(('m/s','km/h'),default_value='m/s',readonly=True,disabled=True) ],
    [sg.Text('Final Velocity '),  sg.InputText(key='velocity'), sg.InputCombo(('m/s','km/h'),default_value='m/s',readonly=True,disabled=True) ],
    [sg.Text('Acceleration  '),   sg.InputText(key='acceleration',disabled=True), sg.InputCombo(('m/s²','km/h²'),default_value='m/s²',readonly=True,disabled=True) ],
    [sg.Text('Elapsed Time'),     sg.InputText(key='time'),sg.InputCombo(('seconds','hours'),default_value='seconds',readonly=True,disabled=True),],
    [sg.Text('Distance       '),  sg.InputText(key='distance'),sg.InputCombo(('meters','kilometers'),default_value='meters',readonly=True,disabled=True),],
    [sg.Text('Determine      '),  sg.Radio('Acceleration',0,default=True,key='is_acceleration',enable_events='True'), sg.Radio('Velocity',0,key='is_velocity',enable_events='True'), sg.Radio('Time',0,key='is_time',enable_events='True'), sg.Radio('Distance',0,key='is_distance',enable_events='True'), ], 
    [sg.Output(size=(88, 10),key='log',font=("Segoe UI Bold",10),text_color='#221255')],
    [sg.Text('Acceleration Rate:',key="output",size=(50,1),font=('Segoe UI Bold',10))],
    [sg.Button(button_text='Calculate'),sg.Button(button_text='Clear'),
    sg.Button(button_text='Help'),
    sg.Button(button_text='Exit')]
]

window = sg.Window('PhysicsX', layout)

while True:
    event, values = window.read()
    
    if values['is_acceleration'] is True:

        window.find('acceleration').update("",disabled = True)
        window.find('output').update('Acceleration Rate:')
        window.find('velocity').update(disabled = False)
        window.find('distance').update(disabled = False)
        window.find('time').update(disabled = False)

    elif values['is_velocity'] is True:

        window.find('acceleration').update(disabled = False)
        window.find('output').update('Final Velocity:')
        window.find('velocity').update("",disabled = True)
        window.find('distance').update(disabled = False)
        window.find('time').update(disabled = False)

    elif values['is_distance'] is True:
        
        window.find('acceleration').update(disabled = False)
        window.find('velocity').update(disabled = False)
        window.find('distance').update("",disabled = True)
        window.find('output').update('Distance:')
        window.find('time').update(disabled = False)

    elif values['is_time'] is True:
        
        window.find('acceleration').update(disabled = False)
        window.find('velocity').update(disabled = False)
        window.find('distance').update(disabled = False)
        window.find('time').update("",disabled = True)
        window.find('output').update('Elapsed Time:')

    if event in (None, 'Exit', 'Cancel'):
        break
    
    if event == 'Calculate':
        initial_velocity =  parse_data(values['ivelocity'],default=0)
        final_velocity =  parse_data(values['velocity'])
        time =  parse_data(values['time'])
        distance =  parse_data(values['distance'])
        acceleration =  parse_data(values['acceleration'])
        if values['is_acceleration'] is True:
            result = Acceleration(initial_velocity= initial_velocity, final_velocity= final_velocity, time=time,distance=distance)
            ans = result.calculate()
            
            if ans is not None:
                answer_digit_only = sub(r"[^0123456789\.-]","",ans)
                
                if answer_digit_only != "":
                    window.find('output').update(f'Acceleration Rate: {answer_digit_only} meters/second²')
                    print(f"[Calculated_Result]: {ans}")
                else:
                    print (ans)

        elif values['is_velocity'] is True:
            result = Velocity(initial_velocity= initial_velocity, acceleration=acceleration, time=time,distance=distance)
            ans = result.calculate()
            if ans is not None:
                answer_digit_only = sub(r"[^0123456789\.-]","",ans)
                if answer_digit_only != "":
                    window.find('output').update(f'Final Velocity: {answer_digit_only} meters/second')
                    print(f"[Calculated_Result]: {ans}")
                else:
                    print(ans)

        elif values['is_time'] is True:
            result = Time(initial_velocity= initial_velocity, final_velocity= final_velocity, acceleration=acceleration,distance=distance)
            ans = result.calculate()
            if ans is not None:
                answer_digit_only = sub(r"[^0123456789\.-]","",ans)
                if answer_digit_only != "":

                    window.find('output').update(f'Elapsed Time: {answer_digit_only} seconds')
                    print(f"[Calculated_Result]: {ans}")
                
                else:
                    print(ans)

        elif values['is_distance'] is True:
            result = Distance(initial_velocity= initial_velocity, final_velocity= final_velocity, time=time,acceleration=acceleration)
            ans = result.calculate()
            if ans is not None:
                answer_digit_only = sub(r"[^0123456789\.-]","",ans)
                if answer_digit_only != "":

                    window.find('output').update(f'Distance: {answer_digit_only} meters')
                    print(f"[Calculated_Result]: {ans}")
                
                else:
                    print(ans)
                
        else:
            sg.PopupError('No Operation Selected',title='Critical Error')
    if event == 'Clear':
        window.find('ivelocity').update('')
        window.find('velocity').update('')
        window.find('distance').update('')
        window.find('time').update('')
        window.find('acceleration').update('')
        window.find('log').update('')
    if event == 'Debug':
        for i in values:
            print(f"values[{i}]--> {values[i]}")

    if event == "Help":
        user = getlogin()
        msg = (f'Hello {user}\n\nTo Calculate The Value Of A Property Just Click On The Dot Next To It\nIf You Don\'t Have A Value For Something: Leave It Blank!\n')
        sg.popup(msg,title="Help",background_color='#000000',text_color='#FFFFFF')

window.close()
