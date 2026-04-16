from flask import Blueprint, request, jsonify, render_template
from app.models.job import Job
from app.models.company import Company

job_bp = Blueprint("jobs", __name__)

@job_bp.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Welcome to the Job Platform API",
        "status": "Success",
        "available_endpoints": [
            "/jobs",
            "/jobs/filter",
            "/companies",
            "/skills"
        ]
    }), 200
@job_bp.route("/jobs", methods=["GET"])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{
        "id": j.id,
        "title": j.title,
        "company": j.company.name if j.company else "Unknown",
        } for j in jobs])
@job_bp.route("/jobs/filter")
def filter_jobs():
    location = request.args.get("location")
    if not location:
        return jsonify({"error": "Location parameter is required"}), 400
    jobs = Job.query.filter_by(location=location).all()
    return jsonify([{"title": j.title, "location": j.location} for j in jobs])