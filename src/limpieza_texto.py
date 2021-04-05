def columnas_mayus(df):
    """
    Return the columns in capital letters
    """
    columnas = list(df.columns)
    columnas_minus = [str(columna).upper() for columna in columnas]
    df.columns = columnas_minus
    return df.columns

def isnull(df):
    """
    Check null numbers and sort them.
    """
    return df.isnull().sum().sort_values(ascending= False)

def coincidencia(patron, string):
    """
    Search regex pattern and return it in lowercase .
    patron:
        regex pattern
    Returns:
        pattern group lowercase
    """
    import re
    dni = re.search(patron, string)
    if dni is None:
        return 0
    return dni.group().lower()