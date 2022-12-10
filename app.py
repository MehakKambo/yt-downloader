from flask import Flask, render_template, request, session
from pytube import YouTube

app = Flask(__name__)
app.config['SECRET_KEY'] = "Your key"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        session['link'] = request.form.get('url')
        try:
            url = YouTube(session['link'])
            url.check_availability()
        except:
            return render_template("error.html")
        return render_template("download.html", url = url)
    return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)