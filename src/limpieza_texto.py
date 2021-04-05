def columnas_mayus(df):
    columnas = list(df.columns)
    columnas_minus = [str(columna).upper() for columna in columnas]
    df.columns = columnas_minus
    return df.columns

def isnull(df):
    return df.isnull().sum().sort_values(ascending= False)

def coincidencia(patron, string):
    import re
    dni = re.search(patron, string)
    if dni is None:
        return 0
    return dni.group().lower()