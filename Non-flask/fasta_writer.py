from Bio import SeqIO


def fasta_writer(seqio_object):
    """Converteert een seqio object naar een fasta file
    :param seqio_object: sequi object met alle sequenties en headers uit een
    csv
    :return: geen
    """
    try:
        with open('rv_seqs.fasta', 'w') as handle:
            SeqIO.write(seqio_object.values(), handle, 'fasta')
    except ValueError:
        print('Onverwachte value')
    except ModuleNotFoundError:
        print("De benodigde module is niet gevonden")


if __name__ == '__main__':
    seqio_dict = SeqIO.to_dict(SeqIO.parse('rv_seqs.csv', 'tab'))
    fasta_writer(seqio_dict)
