import mysql.connector


def database():
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="course4.3")
    cursor = conn.cursor()
    list_protein_name = []
    list_lineage = []
    list_description = []
    mysql_insert_query = """select protein_name, lineage, description 
    from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id limit 10"""
    cursor.execute(mysql_insert_query)
    for i in cursor:
        list_protein_name.append(i[0])
        list_lineage.append(i[1])
        list_description.append(i[2])
    cursor.close()
    conn.close()
    return list_protein_name, list_lineage, list_description


def database_filter(filter, checkbox_p, checkbox_s, checkbox_f):
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="course4.3")
    cursor = conn.cursor()
    list_protein_name = []
    list_lineage = []
    list_description = []
    if checkbox_p:
        if checkbox_s:
            if checkbox_f:  # p:True s:True f:True
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id 
                where protein_name like %s or lineage like %s or description like %s
                limit 10;"""
                query_input = (
                "%" + filter + "%", "%" + filter + "%", "%" + filter + "%")
            else:  # p:True s:True f:False
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                where protein_name like %s or lineage like %s
                limit 10;"""
                query_input = ("%" + filter + "%", "%" + filter + "%")
        else:
            if checkbox_f:  # p:True s:False f:True
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                where protein_name like %s or description like %s
                limit 10;"""
                query_input = ("%" + filter + "%", "%" + filter + "%")
            else:  # p:True s:False f:False
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id 
                where protein_name like %s
                limit 10;"""
                query_input = ("%" + filter + "%",)
    else:
        if checkbox_s:
            if checkbox_f:  # p:False s:True f:True
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                where lineage like %s or description like %s
                limit 10;"""
                query_input = ("%" + filter + "%", "%" + filter + "%")
            else:  # p:False s:True f:False
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                where lineage like %s
                limit 10;"""
                query_input = ("%" + filter + "%",)
        else:
            if checkbox_f:  # p:False s:False f:True
                mysql_insert_query = """select protein_name, lineage, description 
                from protein_seq join taxonomy t on protein_seq.taxonomy_tax_id = t.tax_id
                where description like %s
                limit 10;"""
                query_input = ("%" + filter + "%",)
    cursor.execute(mysql_insert_query, query_input)
    for i in cursor:
        list_protein_name.append(i[0])
        list_lineage.append(i[1])
        list_description.append(i[2])
    cursor.close()
    conn.close()
    return list_protein_name, list_lineage, list_description


if __name__ == "__main__":
    database()
