from models.db import db
from sqlalchemy import Column, String, ForeignKey


class Transition(db.Model):
    __tablename__ = 'transitions'
    name = Column(String(255), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    from_state = Column(String(255), ForeignKey('states.name'))
    from_state_name = db.relationship("State", foreign_keys=[from_state])
    to_state = Column(String(255), ForeignKey('states.name'))
    to_state_name = db.relationship("State", foreign_keys=[to_state])

    def as_dict(self):
        transition_dict = {}
        for c in self.__table__.columns:
            try:
                transition_dict[c.name] = getattr(self, c.name).isoformat()
            except AttributeError:
                transition_dict[c.name] = getattr(self, c.name)
        return transition_dict
