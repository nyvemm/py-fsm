import os
from models.db import db
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from flask import Flask, jsonify, request
from sqlalchemy import Column, Integer, String, ForeignKey

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
engine = create_engine(os.getenv("DATABASE_URL"))

db.init_app(app)


class State(db.Model):
    __tablename__ = 'states'
    name = db.Column(db.String(255), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    transitions = db.relationship(
        "Transition", back_populates="from_state_name", foreign_keys="Transition.from_state")


class Transition(db.Model):
    __tablename__ = 'transitions'
    name = Column(String(255), primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False,
                           server_default=db.func.now())
    from_state = Column(String(255), ForeignKey('states.name'))
    from_state_name = db.relationship("State", foreign_keys=[from_state])
    to_state = Column(String(255), ForeignKey('states.name'))
    to_state_name = db.relationship("State", foreign_keys=[to_state])


@ app.route('/add_state', methods=['POST'])
def add_state():
    if 'state_name' not in request.json:
        return jsonify({'message': 'State name is required'}), 400

    state_name = request.json['state_name']

    existing_state = State.query.filter_by(name=state_name).first()

    if existing_state:
        return jsonify({'message': 'State already exists'}), 400

    new_state = State(name=state_name)

    db.session.add(new_state)
    db.session.commit()

    return jsonify({'message': 'State added successfully'}), 201


@app.route('/get_states', methods=['GET'])
def get_states():
    states = State.query.all()
    states_list = {}
    for state in states:
        transitions_list = []
        if state.transitions:
            for transition in state.transitions:
                transitions_list.append(
                    {'name': transition.name, 'to_state': transition.to_state,
                        'created_at': transition.created_at})
        states_list[state.name] = {
            'created_at': state.created_at, 'transitions': transitions_list}
    return jsonify(states_list), 200


@ app.route('/add_transition', methods=['POST'])
def add_transition():
    if 'transition_name' not in request.json or 'from_state' not in request.json or 'to_state' not in request.json:
        return jsonify({'message': 'Transition name, from state, and to state are required'}), 400
    transition_name = request.json['transition_name']
    from_state = request.json['from_state']
    to_state = request.json['to_state']

    existing_transition = Transition.query.filter_by(
        name=transition_name).first()

    if existing_transition:
        return jsonify({'message': 'Transition already exists'}), 400

    from_state_exist = State.query.filter_by(name=from_state).first()
    if not from_state_exist:
        return jsonify({'message': 'From state does not exist'}), 400

    to_state_exist = State.query.filter_by(name=to_state).first()
    if not to_state_exist:
        return jsonify({'message': 'To state does not exist'}), 400

    new_transition = Transition(
        name=transition_name, from_state=from_state, to_state=to_state)

    db.session.add(new_transition)
    db.session.commit()

    return jsonify({'message': 'Transition added successfully'}), 201


@ app.route('/get_transitions', methods=['GET'])
def get_transitions():
    transitions = Transition.query.all()
    transitions_obj = {}
    for transition in transitions:
        transitions_obj[transition.name] = {
            'from_state': transition.from_state_name.name, 'to_state': transition.to_state_name.name, 'created_at': transition.created_at}
    return jsonify(transitions_obj), 200


if __name__ == '__main__':
    app.run()
