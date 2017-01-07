from flask import Flask, url_for, render_template

from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/present")
def present():
    return render_template('present.html')

if __name__ == "__main__":
    app.run(debug=True)


# def render_sidebar_template(tmpl_name, **kwargs):
#     (var1, var2, var3) = generate_sidebar_data()
#     return render_template(tmpl_name, var1=var1, var2=var2, var3=var3, **kwargs)
