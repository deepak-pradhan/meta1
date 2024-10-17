from tinydb import TinyDB
import json

DB_PATH = 'TinyDB_schema_store.json'
schema_db = TinyDB(DB_PATH)

schemas = schema_db.all()
print(json.dumps(schemas))