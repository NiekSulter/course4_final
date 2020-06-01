import Database
from flask import Flask, render_template, request, url_for

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
        if filteren == "":
            list_protein_name, list_lineage, list_description = Database.database()
        else:
            list_protein_name, list_lineage, list_description = Database.database_filter(filteren, checkbox_p, checkbox_s,
                                            checkbox_f)
        length = list(range(len(list_protein_name)))
        return render_template("Resultaten.html", filter=filteren,
                               length=length,
                               list_protein_name=list_protein_name,
                               list_lineage=list_lineage,
                               list_description=list_description)
    else:
        return render_template("Resultaten.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0')
