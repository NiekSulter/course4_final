import ssl
from Bio import Entrez
import mysql.connector
from blast import uid_gen


def taxonomy(organism):
    """Functie om per organisme de taxonomie op te vragen vanuit de entrez db
    :param organism: organisme
    :return: string met de taxonomie
    """
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        Entrez.email = "nieksulter1999@gmail.com"
        Entrez.api_key = "07e85849007ec973ed58aee0cf95ae2f4409"
        handle = Entrez.esearch(db="taxonomy",
                                term=organism.replace("(", " ")
                                .replace(")", " ")
                                .replace(":", " "))
        result = Entrez.read(handle)
        idlist = result["IdList"]
        Entrez.email = "nieksulter1999@gmail.com"
        fetch = Entrez.efetch(db="taxonomy", id=idlist, rettype="gb",
                              retmode="xml")
        taxonomy_result = Entrez.read(fetch)
        taxonomy_result = (taxonomy_result[0]['Lineage'])
        print(taxonomy_result)
        return taxonomy_result
    except:
        print('---------------ERROR---------------')
        pass


def organism_grabber():
    """Functie om de unieke organismen uit de protein_seq tabel te halen
    :return: lijst met unieke organismen
    """
    try:
        conn = mysql.connector.connect(host='opusflights.com',
                                       user='course4',
                                       password='course4',
                                       db='course4.3_test')
        cursor = conn.cursor()
        cursor.execute(
            "select distinct organism_name from protein_seq "
            "where organism_name is not null;")
        org_list = []
        x = 1
        for i in cursor:
            org_list.append(i[0])
            print(i[0])
            print(x)
            x += 1
        conn.close()
        return org_list
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


def tax_insert(tax, org):
    """Functie om de taxonomie resultaten te inserten in de database
    :param tax: string met taxonomie
    :param org: bijbehorende organisme
    :return: geen
    """
    try:
        conn = mysql.connector.connect(host='opusflights.com',
                                       user='course4',
                                       password='course4',
                                       db='course4.3_test')
        cursor = conn.cursor()
        SQL = "insert into taxonomy(tax_id, lineage, organism) values(%s, %s, %s)"
        uid = uid_gen()
        values = str(uid), str(tax), str(org)
        cursor.execute(SQL, values)
        conn.commit()
        conn.close()
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


def tax_id_insert():
    """Functie om foreign keys in de protein_seq tabel te plaatsen waar de
    organisme naam overeen komt met de taxonomy tabel.
    :return: geen
    """
    conn = mysql.connector.connect(host='opusflights.com',
                                   user='course4',
                                   password='course4',
                                   db='course4.3_test')
    cursor = conn.cursor()
    o_list = []
    cursor.execute('select organism_name from protein_seq')
    for i in cursor:
        o_list.append(i[0])
    print(o_list)
    try:
        for i in o_list:
            SQL = "update protein_seq set taxonomy_tax_id = " \
                  "(select tax_id from taxonomy where organism like \'{}\') " \
                  "where organism_name like \'{}\';".format(
                i, i)
            cursor.execute(SQL)
            conn.commit()
    except:
        print('PASS!')
        pass
    conn.close()
