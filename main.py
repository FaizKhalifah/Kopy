from flask import Flask, render_template

app = Flask(__name__, template_folder="views")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/nama',methods=["Get"])
def nama():
    nama1 = "Ravi"
    nama2 = "Bagas"
    nama3 = "Zufar"
    listprodi = ["Teknik informatika", "teknik komputer", "teknologi informasi", "sistem informasi"]
    return render_template('nama.html', nama1 = nama1, nama2 = nama2, nama3=nama3, listprodi=listprodi)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)