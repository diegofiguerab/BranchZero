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

def assign_missing_ids():
    # Collect IDs from existing applications
    ids = []

    for job in jobs:
        if "id" in job:
            ids.append(job["id"])

    # Find the next available ID
    if not ids:
        new_id = 1
    else:
        new_id = max(ids) + 1

    # Assign unique IDs to applications missing one
    for job in jobs:
        if "id" not in job:
            job["id"] = new_id
            new_id += 1

    # Save updated applications to jobs.json
    save_jobs()

assign_missing_ids()

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
        assign_missing_ids()
        return redirect(url_for("internships"))

    return render_template("internships.html", jobs=jobs)