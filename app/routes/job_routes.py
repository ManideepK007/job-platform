from flask import Blueprint, request, jsonify
from app.models.job import Job

job_bp = Blueprint("jobs", __name__)

@job_bp.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{"title": j.title} for j in jobs])
@job_bp.route("/jobs/filter")
def filter_jobs():
    location = request.args.get("location")
    jobs = Job.query.filter_by(location=location).all()
    return jsonify([j.title for j in jobs])