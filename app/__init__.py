from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # ✅ Config
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost/jobdb"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # ✅ Init extensions
    db.init_app(app)

    # ✅ Import models (INSIDE function to avoid circular import)
    from app.models.company import Company
    from app.models.job import Job
    from app.models.skill import Skill
    from app.models.job_skill import job_skills
    # from app.models.user import User
    # ✅ Import routes
    from app.routes.job_routes import job_bp
    from app.routes.company_routes import company_bp
    from app.routes.skill_routes import skill_bp

    # ✅ Register routes
    app.register_blueprint(job_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(skill_bp)

    return app