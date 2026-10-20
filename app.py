from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

def load_jobs():
    try:
        with open("jobs.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

jobs = load_jobs()

def save_jobs():
    with open("jobs.json", "w") as file:
        json.dump(jobs, file)

@app.route("/")
def home():
    return render_template("index.html")

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
        save_jobs()
        return redirect(url_for("internships"))

    return render_template("internships.html", jobs=jobs)


