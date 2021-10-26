try:
    import datetime as dt
    from app import app
    from flask import render_template
except ImportError as eImp:
    print(f"The following import ERROR occurred: {eImp}")

# -------------Context processor-------------
@app.context_processor
def dateNow():
    return {
        "now": dt.datetime.utcnow()
    }

# -------------Endpoints-------------
@app.route("/")# Welcome HTML template
def index():
    return render_template("welcome.html", pageTitle= "Home")