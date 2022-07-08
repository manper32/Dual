import os

import pandas as pd
import psycopg2
import pyautogui
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pwd = os.path.join(BASE_DIR, r"images")

"""
Clase Dual de escritorio, utilizando PyAutoGUI
"""
class RobotICS():
    def __init__(self):
        self.debtor = os.environ['DEBTOR']
        self.action = os.environ['r1']
        self.efect = os.environ['r2']
        self.contact = os.environ['r3']
        self.reason = os.environ['r4']
        self.phone = os.environ['CALL_PHONE']
        self.description = os.environ['DESCRIPTION']
        self.t1 = os.environ['t1']
        self.t2 = os.environ['t2']
        self.t3 = os.environ['t3']
        self.t4 = os.environ['t4']

    def Controller(self):
        self.SelectICS()
        self.SearchDebtor()
        self.ManageDebtor()
    
    """
    Seleccionar ICS
    """
    def SelectICS(self):
        if pd.isnull(pyautogui.locateOnScreen(os.path.join(pwd, 'Search.png'), grayscale=True, confidence=0.7)):
            x, y = pyautogui.center(pyautogui.locateOnScreen(os.path.join(pwd, 'ICSIconOUT.png'), grayscale=True, confidence=0.7))
            pyautogui.click(x= x, y=y ,clicks=1)
    
    """
    Buscar deudor
    """
    def SearchDebtor(self):
        x, y = pyautogui.center(pyautogui.locateOnScreen(os.path.join(pwd, 'Search.png'), grayscale=True, confidence=0.7))
        pyautogui.click(x= x+17, y=y ,clicks=2)
        pyautogui.write(self.debtor)
        pyautogui.press('enter')
    
    """
    Gestionar deudor
    """
    def ManageDebtor(self):
        start = 0
        end = 0
        step = 800
        while True:
            if not pd.isnull(pyautogui.locateOnScreen(os.path.join(pwd, 'Add.png'), grayscale=True, confidence=0.9)):
                if len(self.description) - end > step:
                    end = start + step
                else:
                    end = len(self.description)
                print(start, end)
                pyautogui.press('enter')
                for i in range(8):
                    if i == 0:
                        pyautogui.write(self.action[:int(float(self.t1))])
                        pyautogui.press('tab')
                    elif i == 1:
                        pyautogui.write(self.efect[:int(float(self.t2))])
                        pyautogui.press('tab')
                    elif i == 2:
                        pyautogui.write(self.contact[:int(float(self.t3))])
                        pyautogui.press('tab')
                    elif i == 3:
                        pyautogui.write(self.reason[:int(float(self.t4))])
                        pyautogui.press('tab')
                    elif i == 4 and self.phone != 'null':
                        pyautogui.write(self.phone[:4])
                        pyautogui.press('tab')
                    elif i == 6 or i == 4 and self.phone == 'null':
                        pyautogui.press('down')
                        pyautogui.press('tab')
                    elif i == 7:
                        pyautogui.write(self.description[start:end])
                    else:
                        pyautogui.press('tab')
                start = end + 1
                if end < len(self.description):
                    pyautogui.press('enter')
                    self.SearchDebtor()
                else:
                    break
            elif not pd.isnull(pyautogui.locateOnScreen(os.path.join(pwd, 'BadSearch.png'), grayscale=True, confidence=0.9)):
                break
        
        if os.environ['PHONE'] != 'null' or os.environ['ADDRESS'] != 'null' or os.environ['EMAIL'] != 'null':
            self.Demographics()
        if os.environ['VALUE'] != 'null' and os.environ['MULTI'] == 'False':
            self.Commitment()
        if os.environ['PHONE'] == 'null' and os.environ['ADDRESS'] == 'null' and os.environ['EMAIL'] == 'null' and os.environ['VALUE'] == 'null':
            pyautogui.press('enter')

    """
    Proceso adicional compromiso
    """
    def Commitment(self):
        if pd.isnull(pyautogui.locateOnScreen(os.path.join(pwd, 'Add.png'), grayscale=True, confidence=0.9)):
            x, y = pyautogui.center(pyautogui.locateOnScreen(os.path.join(pwd, 'Add.png'), grayscale=True, confidence=0.7))
            pyautogui.click(x= x, y=y ,clicks=1)
            pyautogui.press('enter')
        else:
            pyautogui.press('enter')
        
        time.sleep(1)
        x, y = pyautogui.locateCenterOnScreen(os.path.join(pwd, 'value.png'), grayscale=True, confidence=0.8)
        pyautogui.click(x= x+64, y=y-6 ,clicks=1)
        x, y = pyautogui.locateCenterOnScreen(os.path.join(pwd, 'delete.png'), grayscale=True, confidence=0.8)
        pyautogui.click(x= x, y=y ,clicks=1)
        pyautogui.write(os.environ['VALUE'])
        for i in range(6):
            pyautogui.press('tab')
            if i == 3:
                pyautogui.write(os.environ['DATE'])
        if not pd.isnull(pyautogui.locateOnScreen(os.path.join(pwd, 'sistem_warning.png'), grayscale=True, confidence=0.8)):
            pyautogui.press('tab')
            pyautogui.press('enter')
        x, y = pyautogui.locateCenterOnScreen(os.path.join(pwd, '1653412003237.png'), grayscale=True, confidence=0.8)
        pyautogui.click(x= x, y=y-70 ,clicks=1)
        pyautogui.click(x= x, y=y+5 ,clicks=1)

    """
    Proceso Adidcional demograficos
    """
    def Demographics(self):
        objects = ['PHONE', 'ADDRESS', 'EMAIL']
        for i in objects:
            if os.environ[i] != 'null':
                if pd.isnull(pyautogui.locateOnScreen(os.path.join(pwd, 'address_button.png'), grayscale=True, confidence=0.8)):
                    x, y = pyautogui.locateCenterOnScreen(os.path.join(pwd, 'address.png'), grayscale=True, confidence=0.8)
                    pyautogui.click(x= x, y=y ,clicks=1)
                if i == 'PHONE':
                    x, y = pyautogui.locateCenterOnScreen(os.path.join(pwd, 'address.png'), grayscale=True, confidence=0.8)
                    pyautogui.click(x= x, y=y+32 ,clicks=1)
                    for j in range(6):
                        pyautogui.press('tab')
                        if j == 0:
                            pyautogui.write("{:0.0f}".format(float(os.environ['PHONE'])))
                    pyautogui.write('57')
                if i == 'ADDRESS' or i == 'EMAIL':
                    time.sleep(0.1)
                    x, y = pyautogui.locateCenterOnScreen(os.path.join(pwd, 'address_button.png'), grayscale=True, confidence=0.8)
                    pyautogui.click(x= x, y=y-32 ,clicks=1)
                    for j in range(4):
                        if j == 0:
                            pyautogui.write(os.environ[i])
                            pyautogui.press('tab')
                        if j == 1 and i == 'EMAIL':
                            pyautogui.write('e')
                        else:
                            pyautogui.press('tab')
