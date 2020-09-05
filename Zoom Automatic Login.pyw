import pyautogui,time,datetime,os
credentials={"6787682929":"rajan19","6148658883":"1212","8483186991":"004734"}
timel=["0950","1050","1150"]
def auto_join(i,p):
    pyautogui.hotkey("win","d")
    time.sleep(0.5)
    pyautogui.press("win")
    time.sleep(0.5)
    pyautogui.write(message="start zoom")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(x=956,y=573)
    time.sleep(0.5)
    pyautogui.click(x=1155,y=518)
    time.sleep(5)
    pyautogui.hotkey("win","up")
    time.sleep(0.5)
    pyautogui.click(x=717,y=57)
    time.sleep(0.5)
    pyautogui.click(x=774,y=425)
    time.sleep(1)
    pyautogui.write(message=i)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write(message=p)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(5)
    pyautogui.hotkey("win","up")
    time.sleep(0.5)
    pyautogui.hotkey("win","d")
no=3#int(input("Enter number of classes: "))
'''for x in range (no):
    mid=str(input("Enter ID: "))
    password=str(input("Enter Password: "))
    timer=str(input("Enter Time in the format [HHMM (24 HOUR CLOCK TIME)]: "))
    timel.append(timer)
    credentials[mid]=password'''
mid=list(credentials)
values=credentials.values()
password=list(values)
print(mid)
print(password)
print("Credentials Given by you: ",credentials)
print("Time of joining: ",timel)
for y in range (no):
    i=mid[y]
    p=password[y]
    timea=timel[y]
    today=datetime.date.today()
    dt=datetime.datetime.strptime(timea, "%H%M")
    when=datetime.datetime(*today.timetuple()[:3],
                           *dt.timetuple()[3:6])
    wait_time=(when-datetime.datetime.now()).total_seconds()
    if wait_time<0:
        print(f'Time {when} has already passed')
    else:
        print(f'Waiting {wait_time} seconds until {when}')
        time.sleep(wait_time)
        os.system("taskkill /IM Zoom.exe /T /F")
        auto_join(i,p)