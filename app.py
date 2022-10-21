# app.py

from flask import Flask, render_template

max_avail = 100
report_name = "Device availability"
devices = [
    {"name": "M-MLAPT-FBN01", "avail": 99},
    {"name": "M-PRAPT-FBN01", "avail": 99},
    {"name": "M-CBAPT-FBN01", "avail": 95},
    {"name": "M-CBHUME-FBN01", "avail": 80},
]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html", title=" my love <3")

@app.route("/results")
def results():
    context = {
        "title" : "Device availability",
        "devices": devices,
        "report_name": report_name,
        "max_avail" : max_avail
    }
    return render_template("results.html", **context)

if __name__ == "__main__":
    app.run(host="enauto.homelab.com", debug=True)
    
