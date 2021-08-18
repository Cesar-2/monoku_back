import pandas as pd
from datetime import datetime
# fwrite = open('prueba.txt', 'w')


def load_data(Cancion, Artista, Instrumento, Label, BandasSimilares):
    data = pd.read_csv("prueba_back_monoku_2021_datos.csv")
    df = pd.DataFrame(data)
    df = pd.read_csv('prueba_back_monoku_2021_datos.csv')
    df = df.to_dict('records')
    for i in df:
        datos_cancion = {
            'fecha': datetime.strptime(i['FECHA'], '%Y-%m-%d %H:%M:%S'),
            'id_externo': i['ID_EXTERNO'],
            'nombre': i['NOMBRE'],
            'album': i['ALBUM'],
            'banda': i['BANDA'],
            'duracion': i['DURACION'],
            'genero': i['GENERO'],
            'subgenero': i['SUBGENERO']
        }

        cancion = Cancion.objects.create(**datos_cancion)

        datos_artista = {
            'nombre': i['ARTISTA'],
            'cancion': cancion
        }
        Artista.objects.create(**datos_artista)
        for banda_similar in i['BANDAS_SIMILARES'].split(';'):
            datos_bandas_similares = {
                'nombre': banda_similar,
                'cancion': cancion
            }
            BandasSimilares.objects.create(**datos_bandas_similares)
        for instrumento in i['INSTRUMENTOS'].split(';'):
            datos_instrumento = {
                'nombre': instrumento,
                'cancion': cancion
            }
            Instrumento.objects.create(**datos_instrumento)
        for label in i['LABELS'].split(';'):
            datos_label = {
                'nombre': label,
                'cancion': cancion
            }
            Label.objects.create(**datos_label)
