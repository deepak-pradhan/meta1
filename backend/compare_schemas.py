import sys
import json
from tinydb import TinyDB, Query

DB_PATH = 'TinyDB_schema_store.json'
schema_db = TinyDB(DB_PATH)

def get_schema(name):
    Schema = Query()
    return schema_db.search(Schema.name == name)[0]['data']['tables']

def compare_schemas(schema1_name, schema2_name):
    schema1 = get_schema(schema1_name)
    schema2 = get_schema(schema2_name)
    
    differences = {}
    
    for table1 in schema1:
        table2 = next((t for t in schema2 if t['name'] == table1['name']), None)
        if table2:
            table_diff = compare_tables(table1, table2)
            if table_diff:
                differences[table1['name']] = table_diff
        else:
            differences[table1['name']] = [{"name": col['name'], "status": "removed"} for col in table1['columns']]
    
    for table2 in schema2:
        if not any(t['name'] == table2['name'] for t in schema1):
            differences[table2['name']] = [{"name": col['name'], "status": "added"} for col in table2['columns']]
    
    return differences

def compare_tables(table1, table2):
    table_diff = []
    columns1 = {col['name']: col for col in table1['columns']}
    columns2 = {col['name']: col for col in table2['columns']}
    
    for col_name in set(columns1.keys()) | set(columns2.keys()):
        if col_name not in columns1:
            table_diff.append({"name": col_name, "status": "added"})
        elif col_name not in columns2:
            table_diff.append({"name": col_name, "status": "removed"})
        elif columns1[col_name] != columns2[col_name]:
            table_diff.append({"name": col_name, "status": "modified"})
    
    return table_diff

if __name__ == "__main__":
    schema1_name = sys.argv[1]
    schema2_name = sys.argv[2]
    result = compare_schemas(schema1_name, schema2_name)
    print(json.dumps(result))