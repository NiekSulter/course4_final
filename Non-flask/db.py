import mysql.connector
from Bio import SeqIO
import random
import string


def insert():
    """Functie om sequenties uit een fasta bestand in de database te zetten
    :return: geen
    """
    try:
        conn = mysql.connector.connect(host='opusflights.com',
                                       user='course4',
                                       password='course4',
                                       db='course4.3')

        cursor = conn.cursor()

        for record in SeqIO.parse('rv_seqs.fasta', 'fasta'):
            SQL = "insert into seq (seq_id,header, dna_seq, d_read) " \
                  "values (%s,%s, %s, %s)"
            uid = uid_gen()
            val = (uid, str(record.id), str(record.seq), 2)
            cursor.execute(SQL, val)

            conn.commit()
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


def uid_gen():
    """Functie om een uniek ID te genereren en te checken of deze al aanwezig
    is in de database
    :return: uid
    """
    try:
        t = True
        while t:
            uid = ''.join(
                random.choice(string.ascii_uppercase + string.digits) for _ in
                range(12))
            conn = mysql.connector.connect(host='opusflights.com',
                                           user='course4',
                                           password='course4',
                                           db='course4.3_test')
            cursor = conn.cursor()
            SQL = "select tax_id from taxonomy where tax_id like \'{}\'".format(
                uid)
            cursor.execute(SQL)
            uid_test = None
            for i in cursor:
                uid_test = i[0]
            if uid_test is not None:
                t = True
            else:
                t = False
            conn.close()
            return uid
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")
