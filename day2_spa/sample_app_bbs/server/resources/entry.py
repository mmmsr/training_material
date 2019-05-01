from flask import request
from flask_restful import Resource
from model import db, Entry, EntrySchema

entries_schema = EntrySchema(many=True)
entry_schema = EntrySchema()

class EntryResource(Resource):
	def get(self):
		entries = Entry.query.all()
		entries = entries_schema.dump(entries).data
		return {'status': 'success', 'entries': entries}, 200


	def post(self):
		json_data = request.get_json(force=True)
		if not json_data:
			   return {'message': 'No input data provided'}, 400
		# Validate and deserialize input
		data, errors = entry_schema.load(json_data)
		if errors:
			print('errors:', errors)
			return errors, 422
		entry = Entry(
			title=json_data['title'],
			body=json_data['body'],
			posted_by=json_data['posted_by']
		)

		db.session.add(entry)
		db.session.commit()

		result = entry_schema.dump(entry).data

		return { "status": 'success', 'data': result }, 201


	def put(self):
		json_data = request.get_json(force=True)
		if not json_data:
			   return {'message': 'No input data provided'}, 400
		# Validate and deserialize input
		data, errors = entry_schema.load(json_data)
		if errors:
			return errors, 422
		entry = Entry.query.filter_by(id=data['id']).first()
		if not entry:
			return {'message': 'Category does not exist'}, 400
		entry.name = data['name']
		db.session.commit()

		result = entry_schema.dump(entry).data

		return { "status": 'success', 'data': result }, 204


	def delete(self):
		json_data = request.get_json(force=True)
		if not json_data:
			   return {'message': 'No input data provided'}, 400
		# Validate and deserialize input
		data, errors = entry_schema.load(json_data)
		if errors:
			return errors, 422
		entry = Entry.query.filter_by(id=data['id']).delete()
		db.session.commit()

		result = entry_schema.dump(entry).data

		return { "status": 'success', 'data': result}, 204
