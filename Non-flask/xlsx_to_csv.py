import pandas as pd


def convert(ip_fn, ip_col, ip_ofn):
    """Converteert een xlsx file naar een tab seperated csv
    :param ip_fn: Naam van het bestand
    :param ip_col: De relevante kolommen
    :param ip_ofn: De output filename
    :return:
     """
    try:
        df = pd.read_excel(ip_fn, index_col=None, header=None, usecols=ip_col)
        df.to_csv(ip_ofn, sep='\t', index=False, header=False)
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


if __name__ == '__main__':
    ip_fn = input('input filename: ')
    ip_col = input('input cols: ')
    ip_ofn = input('input output filename: ')
    convert(ip_fn, ip_col, ip_ofn)
