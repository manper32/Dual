from sikuli.Sikuli import *
import org.sikuli.script.SikulixForJython
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pwd = os.path.join(BASE_DIR, r"images")

ICSIconIN = Pattern(os.path.join(pwd, "ICSIcon.png")).similar(0.90)
ICSIconOUT = Pattern(os.path.join(pwd,"ICSIconOUT.png")).similar(0.93)
Search = Pattern(os.path.join(pwd, "Search.png")).targetOffset(17,0)
Add = os.path.join(pwd, "Add.png")
Window = os.path.join(pwd, "Window.png")
error = os.path.join(pwd, "BadSearch.png")
value = Pattern(os.path.join(pwd, "value.png")).targetOffset(64,-6).similar(0.80)
delete = Pattern(os.path.join(pwd, "delete.png")).similar(0.80)
address = os.path.join(pwd, "address.png")
address_button = os.path.join(pwd, "address_button.png")
sistem_warning = os.path.join(pwd, "sistem_warning.png")
close_button = os.path.join(pwd, "1653412003237.png")

def PopularTipification(debtor, action, efect, contact, reason, phone, description, t1, t2 ,t3 ,t4):
    if exists(ICSIconOUT):
        click(ICSIconOUT)
    doubleClick(Search)
    paste(debtor)
    type(Key.ENTER)
    while True:
        if exists(Pattern(Add).similar(0.80)):
            type(Key.ENTER)
            for i in range(8):
                if i == 0 and action != 'null':
                    type(action[:int(float(t1))]+Key.TAB)
                elif i == 1 and efect != 'null':
                    type(efect[:int(float(t2))]+Key.TAB)
                elif i == 2  and contact != 'null':
                    type(contact[:int(float(t3))]+Key.TAB)
                elif i == 3 and reason != 'null':
                    type(reason[:int(float(t4))]+Key.TAB)
                elif i == 4 and phone != 'null':
                    type(phone[:4]+Key.TAB)
                elif i == 6 or i == 4 and phone == 'null':
                    type(Key.DOWN+Key.TAB)
                elif i == 7:
                    paste(description)
                else:
                    type(Key.TAB)
            break
        elif exists(error):
            break
    if os.environ['PHONE'] != 'null' or os.environ['ADDRESS'] != 'null' or os.environ['EMAIL'] != 'null':
        Demographics()
    if os.environ['VALUE'] != 'null' and os.environ['MULTI'] == 'False':
        Commitment()
    # if os.environ['PHONE'] == 'null' and os.environ['ADDRESS'] == 'null' and os.environ['EMAIL'] == 'null' and os.environ['VALUE'] == 'null':
    #     type(Key.ENTER)

def Commitment():
    if not exists(Pattern(Add).similar(0.80)):
        click(Add)
    else:
        type(Key.ENTER)
    click(value)
    click(delete)
    paste(os.environ['VALUE'])
    for i in range(6):
        type(Key.TAB)
        if i == 3:
            paste(os.environ['DATE'])
    if exists(sistem_warning):
        type(Key.TAB+Key.ENTER)
    click(Pattern(close_button).targetOffset(0,-70))
    click(Pattern(close_button).targetOffset(0,5))
        # type('a', KeyModifier.CTRL)
    # type(Key.ENTER)
    # click(Pattern(close_button).targetOffset(0,15))
                
def Demographics():
    objects = ['PHONE', 'ADDRESS', 'EMAIL']
    for i in objects:
        if os.environ[i] != 'null':
            if not exists(address_button):
                click(Pattern(address).similar(0.58))
            if i == 'PHONE':
                click(Pattern(address_button).targetOffset(0,32))
                for j in range(6):
                    type(Key.TAB)
                    if j == 0:
                        paste("{:0.0f}".format(float(os.environ['PHONE'])))
                paste('57')
            if i == 'ADDRESS' or i == 'EMAIL':
                click(Pattern(address_button).targetOffset(0,-32))
                for j in range(4):
                    if j == 0:
                        paste(os.environ[i])
                        type(Key.TAB)
                    if j == 1 and i == 'EMAIL':
                        type('e')
                    # if j == 2 and i == 'ADDRESS':
                    #     type(os.environ['CITY'])
                    else:
                        type(Key.TAB)
    # click(Pattern(address_button).targetOffset(-100,65))

PopularTipification(
    os.environ['DEBTOR'],
    os.environ['r1'],
    os.environ['r2'],
    os.environ['r3'],
    os.environ['r4'],
    os.environ['CALL_PHONE'],
    os.environ['DESCRIPTION'],
    os.environ['t1'],
    os.environ['t2'],
    os.environ['t3'],
    os.environ['t4'])
