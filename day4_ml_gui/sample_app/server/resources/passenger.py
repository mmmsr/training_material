from flask import request
from flask_restful import Resource
from model import db, Passenger, PassengerSchema

passengers_schema = PassengerSchema(many=True)
passenger_schema = PassengerSchema()

class PassengerResource(Resource):
	def get(self):
		passengers = Passenger.query.all()
		passengers = passengers_schema.dump(passengers).data
		return {'status': 'success', 'passengers': passengers}, 200


	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			   return {'message': 'No input data provided'}, 400

		passenger = Passenger(
			first_name=json_data['first_name'],
			last_name=json_data['last_name'],
			pclass=json_data['pclass'],
			age=json_data['age'],
			sex=json_data['sex'],
			fare=json_data['fare'],
			family_size=json_data['family_size'],
			embarked=json_data['embarked']
		)

		db.session.add(passenger)
		db.session.commit()

		result = passenger_schema.dump(passenger).data

		return { "status": 'success', 'result': result }, 201


	def delete(self):
		json_data = request.get_json(force=True)
		if not json_data:
			   return {'message': 'No input data provided'}, 400
		# Validate and deserialize input
		data, errors = passenger_schema.load(json_data)
		if errors:
			return errors, 422
		passenger = Passenger.query.filter_by(id=data['id']).delete()
		db.session.commit()

		result = passenger_schema.dump(passenger).data

		return { "status": 'success', 'data': result}, 204
