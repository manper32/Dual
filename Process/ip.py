import psycopg2
import socket
import os
import pandas as pd

"""
Clase para obtener ip del cliente actual(asesor) y procesar gestiones
"""
class GetIp():
    def __init__(self):
        self.IP = self.ip()

    def ip(self):
        hostname=socket.gethostname()
        IP=socket.gethostbyname(hostname)
        return IP
    
    def upload(self):
        self.MainFolder()
        PSQL_MAIN = {
            'host': os.environ.get('PSQL_MAIN_HOST').replace("'",''),
            'port': os.environ.get('PSQL_MAIN_PORT').replace("'",''),
            'user': os.environ.get('PSQL_MAIN_USER').replace("'",''),
            'password': os.environ.get('PSQL_MAIN_PSW').replace("'",''),
            'database': os.environ.get('PSQL_MAIN_DB').replace("'",''),
        }
        user = str()
        while type(user) == str:
            try:
                user = int(input('Introduzca su usuario WiseR por favor: '))
            except:
                print('El usuario solo contiene caracteres numéricos')

        with open(os.path.join(os.environ['BASE_DIR'], r'Process\Query\exists.sql'), 'r') as file:
            query = file.read()
        if pd.read_sql(query.format(user), psycopg2.connect(**PSQL_MAIN)).empty:
            with open(os.path.join(os.environ['BASE_DIR'], r'Process\Query\insert.sql'), 'r') as file:
                query = file.read()
            connection = psycopg2.connect(**PSQL_MAIN)
            cursor = connection.cursor()
            cursor.execute(query.format((user, self.IP)))
        else:
            with open(os.path.join(os.environ['BASE_DIR'], r'Process\Query\update.sql'), 'r') as file:
                query = file.read()
            connection = psycopg2.connect(**PSQL_MAIN)
            cursor = connection.cursor()
            cursor.execute(query.format(user, self.IP))
        connection.commit()
        cursor.close()
        connection.close()
    
    def MainFolder(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        os.environ['BASE_DIR'] = BASE_DIR


if __name__ == '__main__':
    GetIp().upload()
