from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'form'

@app.route('/')
def index():
      return 'Go to /survey to fill out a quick survey about yourself'

#--------------------------------------------------------------------------
@app.route('/survey')
def survey():
    return render_template("index.html")

@app.route('/result/success')
def dashboard():
    return render_template('success.html', name=session['s_name'], language=session['s_languages'], comment=session['s_comment'])

#---------------------------------------------------------------------------
@app.route('/result', methods=["POST"])
def submit():
    print(request.form)
    session['s_name']= request.form['name']
    session['s_locations']= request.form['locations']
    session['s_languages']= request.form['language']
    session['s_comment']= request.form['comment']
    return redirect('/result/success')

if __name__ == '__main__':
  app.run(debug=True)