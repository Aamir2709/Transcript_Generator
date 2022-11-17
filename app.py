from flask import Flask,request,render_template
import utils
app = Flask(__name__,template_folder='template')
from flask_cors import CORS,cross_origin


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate',methods=['POST'])
def generate():
    utube_link = str(request.form.get('email'))
    result = utils.link(utube_link)
    return render_template("index.html",result=result)

@app.route('/summarizer')
def summarizer():
    return render_template("summerizer.html")

@app.route('/get_summarized',methods=['POST'])
def generate_summarizer():
    utube_link = str(request.form.get('email'))
    summary = utils.summarizer(utube_link)
    return render_template("summerizer.html",result=summary)




if __name__=="__main__":
    app.run(debug=True)
