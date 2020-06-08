from flask import Flask, render_template, request
import Database
from blast import check_dna

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def display():
    return render_template("StartPagina.html")


@app.route("/Resultaten.html", methods=['POST', 'GET'])
def display_resultaten():
    if request.method == 'POST':
        filteren = request.form['filter']
        checkbox_p = ('protein_name' in request.form.keys())
        checkbox_s = ('stam' in request.form.keys())
        checkbox_f = ('Function' in request.form.keys())
        checkbox_o = ('Organisme' in request.form.keys())
        if filteren == "":
            list_all = Database.database()
        else:
            list_all = Database.database_filter(filteren, checkbox_p,
                                                checkbox_s,
                                                checkbox_f, checkbox_o)
        return render_template("Resultaten.html",
                               filter=filteren, list_all=list_all)
    else:
        return render_template("Resultaten.html")


@app.route("/blast.html", methods=['POST', 'GET'])
def o_blast():
    if request.method == 'POST':
        header = request.form['header']
        sequence = request.form['seq']
        remail = request.form['email']
        out, jid = check_dna(header, sequence, remail)
        if out == 1:
            status = "Blast completed"
        else:
            status = "An error occurred, blast aborted."
        return render_template('blast.html', status=status, jid=jid)
    else:
        return render_template('blast.html')


@app.route('/blastuser.html', methods=['POST', 'GET'])
def user_blast_results():
    if request.method == 'POST':
        jid = request.form['jid']
        header, sequence, list_all = Database.userblast(jid)
        return render_template('blastuser.html', header=header,
                               sequence=sequence, list_all=list_all)
    else:
        return render_template('blastuser.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
