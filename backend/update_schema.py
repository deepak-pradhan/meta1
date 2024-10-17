import sys
import json
from tinydb import TinyDB, Query

DB_PATH = 'TinyDB_schema_store.json'
schema_db = TinyDB(DB_PATH)

def update_schema(schema_data):
    Schema = Query()
    result = schema_db.update(schema_data, Schema.name == schema_data['name'])
    if result:
        return {'success': True, 'message': 'Schema updated successfully'}
    else:
        return {'success': False, 'message': 'Schema not found or no changes made'}

if __name__ == "__main__":
    schema_json = sys.argv[1]
    schema_data = json.loads(schema_json)
    result = update_schema(schema_data)
    print(json.dumps(result))