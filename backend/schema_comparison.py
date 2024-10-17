from tinydb import TinyDB, Query
from sqlalchemy import MetaData, Table
import json

DB_PATH = 'TinyDB_schema_store.json'
schema_db = TinyDB(DB_PATH)

def compare_schemas(schema1_name, schema2_name):
    schema1 = get_schema(schema1_name)
    schema2 = get_schema(schema2_name)
    
    differences = {
        'added': [],
        'removed': [],
        'modified': []
    }
    
    # Compare tables
    compare_tables(schema1, schema2, differences)
    
    # Compare columns within tables
    compare_columns(schema1, schema2, differences)
    
    return differences

def get_schema(schema_name):
    Schema = Query()
    return schema_db.search(Schema.name == schema_name)[0]['data']

def compare_tables(schema1, schema2, differences):
    tables1 = set(table['name'] for table in schema1['tables'])
    tables2 = set(table['name'] for table in schema2['tables'])
    
    differences['added'].extend(list(tables2 - tables1))
    differences['removed'].extend(list(tables1 - tables2))

def compare_columns(schema1, schema2, differences):
    for table in schema1['tables']:
        if table['name'] in [t['name'] for t in schema2['tables']]:
            table2 = next(t for t in schema2['tables'] if t['name'] == table['name'])
            compare_table_columns(table, table2, differences)

def compare_table_columns(table1, table2, differences):
    columns1 = {col['name']: col for col in table1['columns']}
    columns2 = {col['name']: col for col in table2['columns']}
    
    for col_name, col in columns2.items():
        if col_name not in columns1:
            differences['added'].append(f"{table1['name']}.{col_name}")
        elif col != columns1[col_name]:
            differences['modified'].append(f"{table1['name']}.{col_name}")
    
    for col_name in columns1:
        if col_name not in columns2:
            differences['removed'].append(f"{table1['name']}.{col_name}")

# Add more helper functions as needed