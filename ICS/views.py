import ctypes
import datetime as dt
import os
import shlex
import subprocess
import time as tm
from time import time

import pandas as pd
import psycopg2
from django.conf import settings
from django.core import management
from django.core.management.commands import loaddata
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from ICS.serializers import DualDeskSerializer

"""
implementacion con Selenium
"""
@method_decorator(csrf_exempt,name='dispatch')
class ICSdualWeb(APIView):
  def post(self,request):
    initial = time()
    
    options = Options()
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.get('https://ics-mobile.mibanco.com.co:8443/')
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()

    user_name = driver.find_element_by_id('j_id_f:username')
    user_password = driver.find_element_by_name('fscpassword_j_id_f:password')
    submit = driver.find_element_by_name('j_id_f:BtnLogin')
    
    user_name.send_keys('prv_oscar_ortiz')
    user_password.send_keys('ICS6789*')
    submit.send_keys(Keys.RETURN)

    return Response({'Time': str(dt.timedelta(seconds=time() - initial))},status=status.HTTP_200_OK)


"""
Clase Dual de escritorio, utilizando Jython y python
"""
class ICSdualDesk(APIView):
    def ExecuteSikuli(self, data):
        if data.telefono == '':
            data.update({'telefono': 'null'})
        initial = time()
        indicator = data.indicador
        os.environ['SIKULI_EXE'] =os.path.join(settings.BASE_DIR, r'ICS\templates\sikulixide-2.0.5.jar')
        os.environ['SIKULI_SCRIPT'] = os.path.join(settings.BASE_DIR, r'ICS\templates\sikuli\NoContact.py')
        os.environ['DEBTOR'] = data.deudor_id
        os.environ['R1'] = data.r1
        os.environ['R2'] = data.r2
        os.environ['R3'] = data.r3
        os.environ['R4'] = data.r4
        os.environ['T1'] = str(data.t1)
        os.environ['T2'] = str(data.t2)
        os.environ['T3'] = str(data.t3)
        os.environ['T4'] = str(data.t4)
        os.environ['CALL_PHONE'] = data.telefono
        os.environ['DESCRIPTION'] = data.descripcion
        if data[['n1', 'n2', 'n3', 'n4']].any():
            os.environ['VALUE'] = str(int(data.valor))
            os.environ['DATE'] = dt.datetime.strftime(data.fecha_pago, '%d/%m/%Y')
        else:
            os.environ['VALUE'] = 'null'
            os.environ['DATE'] = 'null'
            
        for i in ['phone', 'address', 'city', 'email']:
            if not pd.isna(data[i]):
                os.environ[i.upper()] = str(data[i])
            else:
                os.environ[i.upper()] = 'null'

        command = "java -cp %SIKULI_EXE% org.python.util.jython %SIKULI_SCRIPT%"
        print(subprocess.Popen(
            shlex.split(command),
            shell=True,
            stdout=subprocess.PIPE).stdout.read().decode())
        print(dt.timedelta(seconds=time() - initial))
        if os.environ['MULTI'] == 'True':
            ctypes.windll.user32.MessageBoxW(0, "Gestion con multiples obligaciones", "Advertencia", 0)

    def post(self,request):
        initial = time()

        serializer = DualDeskSerializer(data=request.data)
        if serializer.is_valid():

            with open(os.path.join(settings.BASE_DIR, 'ICS/templates/query1.sql'), 'r') as file:
                query = file.read()
            data = pd.read_sql(query.format(request.data.get('user')), psycopg2.connect(**settings.PSQL_MAIN))
            commit_fields = [column for column in data.columns if len(column) == 2 and column.find('n') == 0]
            amount = data.groupby(by=['gestion_fecha'], as_index=True, sort=False).count()['n1']
            if amount.shape[0]<1:
                return Response(status=status.HTTP_204_NO_CONTENT)
            print(data)
            if data.loc[0, commit_fields].any() and amount[0] > 1:
                os.environ['MULTI'] = 'True'
            else:
                os.environ['MULTI'] = 'False'
            print(os.environ['MULTI'])

            self.ExecuteSikuli(data.loc[0].copy())

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({'Time': str(dt.timedelta(seconds=time() - initial))},status=status.HTTP_200_OK)
