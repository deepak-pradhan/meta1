import sys
import json
from tinydb import TinyDB, Query

DB_PATH = 'TinyDB_schema_store.json'
schema_db = TinyDB(DB_PATH)

def get_schema(name):
    Schema = Query()
    return schema_db.search(Schema.name == name)[0]['data']

def compare_schemas(schema1_name, schema2_name):
    schema1 = get_schema(schema1_name)
    schema2 = get_schema(schema2_name)
    
    differences = {}
    
    for table_name in set(schema1.keys()) | set(schema2.keys()):
        table_diff = []
        table1 = schema1.get(table_name, {})
        table2 = schema2.get(table_name, {})
        
        for column_name in set(table1.keys()) | set(table2.keys()):
            if column_name not in table1:
                table_diff.append({"name": column_name, "status": "added"})
            elif column_name not in table2:
                table_diff.append({"name": column_name, "status": "removed"})
            elif table1[column_name] != table2[column_name]:
                table_diff.append({"name": column_name, "status": "modified"})
        
        if table_diff:
            differences[table_name] = table_diff
    
    return differences

if __name__ == "__main__":
    schema1_name = sys.argv[1]
    schema2_name = sys.argv[2]
    result = compare_schemas(schema1_name, schema2_name)
    print(json.dumps(result))