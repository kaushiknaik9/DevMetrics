from app.extensions import db
from datetime import datetime


class Tenant(db.Model):
    __tablename__ = "tenants"

    # if not mentioned class name becomes table name

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(120), nullable=False)

    slug = db.Column(db.String(80), unique=True, nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )
    # if utcnow() then this is created everytime class is created
    # but now utcnow then each time row is inserted it is created

    users = db.relationship(
        "User", back_populates="tenant", cascade="all, delete-orphan", lazy="dynamic"
    )

    reports = db.relationship(
        "Report", back_populates="tenant", cascade="all, delete-orphan", lazy="dynamic"
    )

    metrics = db.relationship(
        "Metric", back_populates="tenant", cascade="all, delete-orphan", lazy="dynamic"
    )

    def __repr__(self):
        return f"<Tenant {self.slug}>"
