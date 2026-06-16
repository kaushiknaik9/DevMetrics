from app.extensions import db
from datetime import datetime


class ReportStatus:
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class Report(db.Model):
    __tablename__ = "reports"

    id = db.Column(db.Integer, primary_key=True)

    tenant_id = db.Column(
        db.Integer, db.ForeignKey("tenants.id"), nullable=False, index=True
    )

    title = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), nullable=False, default=ReportStatus.PENDING)

    file_url = db.Column(db.String(500))

    error_msg = db.Column(db.Text)

    period_start = db.Column(db.DateTime)
    period_end = db.Column(db.DateTime)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    completed_at = db.Column(db.DateTime)

    tenant = db.relationship("Tenant", back_populates="report")

    def __repr__(self):
        return f"<Report: {self.title}, Status: {self.status}>"
