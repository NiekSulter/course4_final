from Bio.Alphabet import IUPAC, DNAAlphabet
from Bio.Blast import NCBIWWW, NCBIXML
from Bio.Seq import Seq
import re
import mysql.connector
import random
import string
from automail import mail_notifier


def uid_gen(c):
    t = True
    while t:
        uid = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(c))
        conn = mysql.connector.connect(host='opusflights.com',
                                       user='course4',
                                       password='course4',
                                       db='user_blast')
        cursor = conn.cursor()
        SQL = "select job_id from seq where job_id like \'{}\'".format(uid)
        cursor.execute(SQL)
        uid_test = None
        for i in cursor:
            uid_test = i[0]
        if uid_test != None:
            t = True
        else:
            t = False
        conn.close()
        return uid

def check_dna(header, seq, remail):
    seq_d = Seq(seq, IUPAC.unambiguous_dna)
    if seq_d:
        uid = seq_insert(header, seq)
        bl(seq_d, uid, remail)
        return 1, uid
    else:
        print(seq_d)
        return 0


def bl(seq, job_id, remail):
    print('starting blast')
    result = NCBIWWW.qblast('blastx', 'nr', seq, hitlist_size=10)
    print('blast complete')
    parse_result(result, job_id, remail)


def parse_result(result, job_id, remail):
    blast_record = NCBIXML.read(result)
    for alignment in blast_record.alignments:
        # ID systeem -> hervormen naar uid systeem
        protein_id = uid_gen(11)

        # Acessiecode van gevonden eiwit
        accession = alignment.title.split("|")[1]

        # Organisme naam uit de desc halen d.m.v. een regex, if else statement om NoneTypes eruit te halen
        organism_regex = "(?<=\[).+?(?=])"
        organism1 = re.search(organism_regex, alignment.title)
        if organism1 is None:
            organism = 'geen titel'
        else:
            organism = organism1.group()

        # Description ophalen d.m.v. een regex, if else statement om NoneTypes eruit te halen
        description = alignment.title

        description_regex = "(?<=\|).+?(?=\[)"
        description1 = re.search(description_regex, alignment.title)
        if description1 is None:
            protein_name = 'geen naam gevonden'
        else:
            protein_name = description1.group().split('|')[1]

        # e-value ophalen
        e_value = alignment.hsps[0].expect

        # proteine sequentie ophalen
        protein_seq = alignment.hsps[0].sbjct

        # query cover berekenen
        al = alignment.hsps[0].align_length
        lenseq = 301
        query_cover = round((al / lenseq) * 100)

        # percent identity ophalen.
        percent_identity = round(alignment.hsps[0].identities / alignment.hsps[0].align_length * 100)

        conn = mysql.connector.connect(
            host="opusflights.com",
            user="course4",
            password="course4",
            db="user_blast")
        cursor = conn.cursor()
        SQL = "insert into protein_seq(protein_id, protein_seq, protein_name, organism_name, description, accession, e_value, percent_identity, query_cover, job_job_id) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = protein_id, protein_seq, protein_name, organism, description, accession, e_value, percent_identity, query_cover, job_id
        cursor.execute(SQL, values)
        conn.commit()
        conn.close()
    mail_notifier(remail, job_id)

def seq_insert(header, seq):
    conn = mysql.connector.connect(
        host="opusflights.com",
        user="course4",
        password="course4",
        db="user_blast")
    cursor = conn.cursor()
    SQL = "insert into seq(job_id, header, dna_seq, datum) values(%s, %s, %s, NOW())"
    uid = uid_gen(8)
    values = (uid, header, seq)
    cursor.execute(SQL, values)
    conn.commit()
    conn.close()
    return uid