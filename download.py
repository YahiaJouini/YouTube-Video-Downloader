from pytube import YouTube
from flask import Flask,url_for,render_template,redirect,request
import pytube
app=Flask(__name__,template_folder='templates')
@app.route("/")
@app.route("/home")
def home_page():
    return render_template('download-page.html',title="Download Page")
@app.route('/status', methods=['POST'])
def status():
    if request.method == "POST" and request.form['url']!="":
        url = request.form['url']
        print(url)
        try:
            Download(url)
            return render_template('success.html',results='Successfully downloaded!')
        except:
            return render_template('success.html',title="status",results='An error has occurred!')
    else:
        return redirect(url_for("home_page"))
def Download(link):
    yt = YouTube(link)
    yt = yt.streams.get_highest_resolution().download()

if __name__=="__main__":
    app.run(debug=True)