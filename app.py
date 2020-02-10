from flask import Flask, render_template
import os
import random
import pandas as pd
import psycopg2

app = Flask(__name__)

connection=psycopg2.connect(host='flask.cbhu7ev8prgh.us-east-1.rds.amazonaws.com',
                            port=5432,
                            user='postgres',
                            password='postgres',
                            database='flask')

cursor=connection.cursor()

sql="""select * from passengers"""

demo=pd.read_sql(sql,con=connection)

# list of cat images
image = "https://dalu-my.sharepoint.com/:i:/r/personal/bl977277_dal_ca/Documents/docker.png?csf=1&e=CeXcwR"


@app.route("/")
def index():
    url = image
    name = demo.name[0]
    age = demo.age[0]
    return render_template("index.html", url=url,name=name,age=age)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
