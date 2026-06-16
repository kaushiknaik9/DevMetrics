from app.extensions import db
from datetime import datetime


class MetricTypes:
    COMMIT = "commit"
    PULL_REQUEST = "pull_request"
    CODE_REVIEW = "code_review"
    BUG_FIX = "bug_fix"


class Metric(db.Model):
    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)

    tenant_id = db.Column(
        db.Integer, db.ForeignKey("tenants.id"), nullable=False, index=True
    )

    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False, index=True
    )

    metric_type = db.Column(db.String(30), nullable=False)

    value = db.Column(db.Integer, nullable=False, default=1)

    description = db.Column(db.String)

    recorded_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship("User", back_populates="metrics")
    tenant = db.relationship("Tenant", back_populates="metrics")

    __table_args__ = (
        db.Index("ix_metrics_tenant_recorded", "tenant_id", "recorded_at"),
        db.Index("ix_metrics_tenant_user", "tenant_id", "user_id"),
    )

    def __repr__(self):
        return f"<Metric {self.metric_type}, user={self.user_id}>"
