from models.db import db
from sqlalchemy import Column, String, ForeignKey


class State(db.Model):
    __tablename__ = 'states'
    name = db.Column(db.String(255), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    transitions = db.relationship(
        "Transition", back_populates="from_state_name", foreign_keys="Transition.from_state")

    def as_dict(self):
        state_dict = {}
        for c in self.__table__.columns:
            try:
                state_dict[c.name] = getattr(self, c.name).isoformat()
            except AttributeError:
                state_dict[c.name] = getattr(self, c.name)
        return state_dict
