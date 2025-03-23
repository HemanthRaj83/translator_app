from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route("/", methods=["GET", "POST"])
def translate():
    translated_text = ""
    if request.method == "POST":
        text = request.form.get("text")
        dest_lang = request.form.get("language")
        if text and dest_lang:
            translated = translator.translate(text, dest=dest_lang)
            translated_text = translated.text
    return render_template("index.html", translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)
