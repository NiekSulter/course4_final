import mysql.connector


def database():
    try:
        """Haalt de gegevens in de database op.
            :return: Een lijst met proteine naam, een lijst met de lineage,
            een lijst met de functie
            """
        conn = mysql.connector.connect(
            host="opusflights.com",
            user="course4",
            password="course4",
            db="course4.3_test")
        cursor = conn.cursor()
        mysql_insert_query = """select protein_name, organism_name, accession, 
        e_value, percent_identity, query_cover, lineage
        from protein_seq left outer join taxonomy t 
        on protein_seq.taxonomy_tax_id = t.tax_id"""
        cursor.execute(mysql_insert_query)
        list_all = []
        for i in cursor:
            # print(i)
            list_all.append(i)
        cursor.close()
        conn.close()
        for i in list_all:
            print(i[0])
        return list_all
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


def database_filter(filter, checkbox_p, checkbox_s, checkbox_f, checkbox_o):
    try:
        """Filtert in de database op het zoekwoord in kolommen die gevinkt
            waren op de Resultaten pagina.
            :param filter: Een string waarop gefilterd wordt
            :param checkbox_p: Een boolean of er wel of niet gefilterd wordt in
            de proteine naam
            :param checkbox_s: Een boolean of er wel of niet gefilterd wordt in
            de lineage
            :param checkbox_f: Een boolean of er wel of niet gefilterd wordt in
            de functie
            :param checkbox_o: Een boolean of er wel of niet gefilterd wordt in
            het organisme
            :return: Een lijst met proteine naam, een lijst met de lineage,
            een lijst met de functie
            """
        conn = mysql.connector.connect(
            host="opusflights.com",
            user="course4",
            password="course4",
            db="course4.3_test")
        cursor = conn.cursor()
        query_input = ''
        list_all = []
        if checkbox_p:
            if checkbox_s:
                if checkbox_f:
                    if checkbox_o:  # p:True s:True f:True o:True
                        mysql_insert_query = """select protein_name, 
                        organism_name, accession, e_value, percent_identity, 
                        query_cover, lineage 
                        from protein_seq join taxonomy t on 
                        protein_seq.taxonomy_tax_id = t.tax_id 
                        where protein_name like %s or lineage like %s or 
                        description like %s or organism_name like %s;"""
                        query_input = (
                        "%" + filter + "%", "%" + filter + "%", "%"
                        + filter + "%", "%" + filter + "%")
                    else:  # p:True s:True f:True o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id 
                        where protein_name like %s 
                        or lineage like %s or description like %s;"""
                        query_input = (
                        "%" + filter + "%", "%" + filter + "%", "%"
                        + filter + "%")
                else:
                    if checkbox_o:  # p:True s:True f:False o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where protein_name like %s or lineage 
                        like %s or organism_name like %s;"""
                        query_input = (
                            "%" + filter + "%", "%" + filter + "%",
                            "%" + filter + "%")
                    else:  # p:True s:True f:False o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where protein_name like %s or lineage like %s;"""
                        query_input = ("%" + filter + "%", "%" + filter + "%")
            else:
                if checkbox_f:
                    if checkbox_o:  # p:True s:False f:True o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where protein_name like %s or description 
                        like %s or organism_name like %s;"""
                        query_input = (
                            "%" + filter + "%", "%" + filter + "%",
                            "%" + filter + "%")
                    else:  # p:True s:False f:True o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where protein_name like %s or description like %s;"""
                        query_input = ("%" + filter + "%", "%" + filter + "%")
                else:
                    if checkbox_o:  # p:True s:False f:False o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id 
                        where protein_name like %s 
                        or organism_name like %s;"""
                        query_input = ("%" + filter + "%", "%" + filter + "%")
                    else:  # p:True s:False f:False o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id 
                        where protein_name like %s;"""
                        query_input = ("%" + filter + "%",)
        else:
            if checkbox_s:
                if checkbox_f:
                    if checkbox_o:  # p:False s:True f:True o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where lineage like %s or description 
                        like %s or organism_name like %s;"""
                        query_input = (
                            "%" + filter + "%", "%" + filter + "%",
                            "%" + filter + "%")
                    else:  # p:False s:True f:True o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where lineage like %s or description like %s;"""
                        query_input = ("%" + filter + "%", "%" + filter + "%")
                else:
                    if checkbox_o:  # p:False s:True f:False o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where lineage like %s or organism_name like %s;"""
                        query_input = ("%" + filter + "%", "%" + filter + "%")
                    else:  # p:False s:True f:False o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where lineage like %s;"""
                        query_input = ("%" + filter + "%",)
            else:
                if checkbox_f:
                    if checkbox_o:  # p:False s:False f:True o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where description like %s or organism_name like %s;"""
                        query_input = ("%" + filter + "%", "%" + filter + "%")
                    else:  # p:False s:False f:True o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id
                        where description like %s;"""
                    query_input = ("%" + filter + "%",)
                else:
                    if checkbox_o:  # p:False s:False f:False o:True
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                         from protein_seq join
                        taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                                            where organism_name like %s;"""
                        query_input = ("%" + filter + "%",)
                    else:  # All False p:False s:False f:False o:False
                        mysql_insert_query = """select protein_name, organism_name,
                         accession, e_value, percent_identity, query_cover, lineage 
                        from protein_seq join taxonomy t 
                        on protein_seq.taxonomy_tax_id = t.tax_id"""
        cursor.execute(mysql_insert_query, query_input)
        for i in cursor:
            list_all.append(i)
        cursor.close()
        conn.close()
        return list_all
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


def userblast(jid):
    """Ophalen van de userblast resultaten
    :param jid: uniek job id gegenereed tijdens de blast
    :return: header, sequentie en een lijst met de blast resultaten
    """
    header = ''
    sequence = ''
    list_all = []
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="user_blast")
    cursor = conn.cursor()
    cursor.execute(
        "select header, dna_seq from seq where job_id like \'{}\'".format(jid))
    for i in cursor:
        header = i[0]
        sequence = i[1]
    cursor.close()
    cursor2 = conn.cursor()
    if jid:
        cursor2.execute(
            "select protein_name, organism_name, accession, e_value, "
            "percent_identity, query_cover, job_job_id from protein_seq "
            "where job_job_id like \'{}\'".format(
                jid))
    else:
        cursor2.execute(
            "select protein_name, organism_name, accession, e_value, "
            "percent_identity, query_cover, job_job_id from protein_seq "
            "where job_job_id is not null")
    for i in cursor2:
        list_all.append(i)
    conn.close()
    return header, sequence, list_all


if __name__ == "__main__":
    database()
