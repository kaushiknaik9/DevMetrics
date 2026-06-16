from app.extensions import db
from datetime import datetime


class RoleEnum:
    SUPER_ADMIN = "super_admin"
    ORG_ADMIN = "org_admin"
    DEVELOPER = "developer"
    # only three roles and now you cant store anything other than this if you do then you have attribute error so wrong data is not saved


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    tenant_id = db.Column(
        db.Integer, db.ForeignKey("tenants.id"), nullable=False, index=True
    )

    email = db.Column(db.String(255), unique=True, nullable=False)

    password_hash = db.Column(db.String(255), nullable=False)

    full_name = db.Column(db.String(120), nullable=False)

    role = db.Column(db.String(20), nullable=False, default=RoleEnum.DEVELOPER)

    is_active = db.Column(db.Boolean, default=True, nullable=False)

    is_email_verified = db.Column(db.Boolean, default=False, nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    tenant = db.relationship("Tenant", back_populates="users")

    metrics = db.relationship(
        "Metric", back_populates="user", cascade="all, delete-orphan", lazy="dynamic"
    )

    __table_args__ = (db.Index("ix_users_tenant_email", "tenant_id", "email"),)

    def __repr__(self):
        return f"<User {self.email}>"
