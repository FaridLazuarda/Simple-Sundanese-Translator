from flask import Flask, redirect, url_for, render_template, request
from translator import translate
app = Flask(__name__)

'''
File ini berisi fungsi untuk back-end dari website
'''

# route untuk home page/main page
@app.route("/", methods=["POST", "GET", "SWAP"])
def home():
    if request.method == "POST":
        # memasukkan input dari web ke variabel
        sent_input = request.form["inputText"]
        algo = request.form["algorithm"]
        lang = request.form["language"]

        # conditioning apabila teks masukan kosong 
        if(len(sent_input)>0): # jika tidak kosong maka jalankan fungsi
            translated = translate(sent_input, lang, algo)
            return render_template("index.html", inputText = sent_input, translatedText = translated )
        else: # jika kosong maka refresh page
            return render_template("index.html")
    else:
        return render_template("index.html", inputText = '', translatedText = '')

# route untuk about page
@app.route('/about')
def about():
    return render_template('about.html')

# route untuk guide page
@app.route('/guide')
def guide():
    return render_template('guide.html')

# akan menjalankan server sebagai program utama
if __name__ == "__main__":
    app.static_folder = 'static'
    app.run(debug=True)

