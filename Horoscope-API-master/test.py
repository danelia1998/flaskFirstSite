from flask import Flask, redirect, url_for, request, jsonify, render_template
from pyhoroscope import Horoscope as horo
app = Flask('Horoscope')
sunsigns = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
           "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces"]
timeframe = ["todays", "weekly", "yearly", "monthly"]

@app.route('/success/<name>')
def success(name):
    each = []
    for sunsign in sunsigns:
        if sunsign == name:
            for j in timeframe:
                result = eval("horo.get_" + j + "_horoscope(sunsign)")

        else:
            continue
    res = result['horoscope']
    return render_template('random_int.html', res=result['horoscope'])

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(host='localhost', port=5000)



