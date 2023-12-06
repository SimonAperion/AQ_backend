# from flask_security.models import fsqla_v3 as fsqla
from sqlalchemy.orm import relationship, backref
from sqlalchemy import MetaData, UniqueConstraint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from sqlalchemy import Boolean, Column, Integer, Date, String, ForeignKey

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# TODO: Delete Cascade usw...

metadata = MetaData(naming_convention=convention)
ma = Marshmallow()
db = SQLAlchemy(metadata=metadata)

# Schemas sind nicht schön aber es funktioniert
# Eventuell muss bei den migrations manuell die version angepasst werden


class BaseModel(db.Model):
    __abstract__ = True
    __table_args__ = {"schema": "aq"}


# Security
class RolesUsers(BaseModel):
    __tablename__ = "roles_users"
    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("aq.user.id"))
    role_id = Column(Integer(), ForeignKey("aq.role.id"))


class Role(BaseModel):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    # role_userer = relationship("User",secondary="aq.roles_users")


class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True)
    password = Column(String(255), nullable=False)
    roles = relationship(
        "Role", secondary="aq.roles_users", backref=backref("users", lazy="dynamic")
    )


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "name", "description")


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = ("id", "email", "username", "token", "roles")

    roles = fields.Nested(RoleSchema, many=True)


users_schema = UserSchema(many=True)
