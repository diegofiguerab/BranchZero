from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

jobs = [ 
    {
    "company": "Google",
    "position": "Software Engineer Intern",
    "status": "Applied" 
    },
    {
    "company": "Microsoft",
    "position": "Software Engineer Intern",
    "status": "Interested"
    }
]

@app.route("/internships", methods=["GET", "POST"])
def internships():
    if request.method == "POST":
        company = request.form["company"]
        position = request.form["position"]
        status = request.form["status"]

        new_job = {
            "company": company,
            "position": position,
            "status": status
        }

        jobs.append(new_job)
        return redirect(url_for("internships"))

    return render_template("internships.html", jobs=jobs)


