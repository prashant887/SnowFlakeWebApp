from flask import Flask, render_template, request
import pandas as pd
from SnowFlakeConnection import sfConnect

app = Flask('my website')


@app.route("/")
def homepage():
    cur.execute('SELECT * FROM COLORS')
    rows = pd.DataFrame(cur.fetchall(), columns=["Color UID", "Color Name"])
    dfhtml = rows.to_html()
    return render_template('index.html', dfhtml=dfhtml)


@app.route("/submit")
def submit():
    return render_template('submit.html')


@app.route("/thanks", methods=["POST"])
def thanks():
    color = request.form.get("cname")
    name = request.form.get("uname")
    sql = '''insert into colors 
select max(color_uid) + 1 ,'{}' from COLORS'''.format(color.upper())
    cur.execute(sql)
    return render_template('thanks.html', colorname=color, username=name)


@app.route("/coolcharts")
def coolcharts():
    sql = '''select COLOR_NAME,count(*) from colors
group by COLOR_NAME order by 2 desc;'''
    cur.execute(sql)
    rows = pd.DataFrame(cur.fetchall(), columns=["color", "votes"])
    # rows.to_csv('data_charts.csv', index=False)
    charJson = rows.to_json( orient='records')
    dfhtml = rows.to_html()
    return render_template('coolcharts.html',charJson=charJson)


cnx = sfConnect()

cur = cnx.cursor()

app.run(host='0.0.0.0',port=9090, debug=True)
