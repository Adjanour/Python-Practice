def generate_sql_from_description(table_desc):
    """
    Generates a SQL CREATE TABLE statement from a table description.

    Args:
        table_desc (dict): A dictionary describing the table structure.
            Example:
            {
                "table_name": "customers",
                "columns": [
                    {"name": "customer_id", "type": "integer", "primary_key": True},
                    {"name": "first_name", "type": "string", "max_length": 50},
                    {"name": "last_name", "type": "string", "max_length": 50},
                    {"name": "email", "type": "string",  "max_length": 100, "unique": True}
                ]
            }

    Returns:
        str: The generated SQL CREATE TABLE statement.
    """

    data_type_mapping = {
        "integer": "INT",
        "string": "VARCHAR", 
        "decimal":"DECIMAL",
        "date":"DATE",
        "datetime":"DATETIME",
        "bool":"BOOLEAN",
        "text":"TEXT"
    }

    sql = f"CREATE TABLE {table_desc['table_name']} (\n"

    for column in table_desc['columns']:
        sql += f"  {column['name']} {data_type_mapping[column['type']]}"
        if "max_length" in column:
            sql += f"({column['max_length']})"
        if column.get("primary_key"):
            sql += " PRIMARY KEY"
        if column.get("not_null"):
            sql += " NOT NULL"
        if column.get("unique"):
            sql += " UNIQUE"
        sql += ",\n"

    sql = sql[:-2]  # Remove last comma and newline
    sql += "\n);"
    return sql


# Example Usage
table_description = {
    "table_name": "products",
    "columns": [
        {"name": "product_id", "type": "integer", "primary_key": True,"not_null":True},
        {"name": "name", "type": "string", "max_length": 100},
        {"name": "price", "type": "decimal"},
        {"name": "description", "type": "text"},
        {"name": "created_on", "type": "datetime"},
        {"name": "is_active", "type": "bool"},
        {"name": "category", "type": "string", "max_length": 50, "not_null": True},
        {"name": "brand", "type": "string", "max_length": 50, "not_null": True},
        {"name": "created_by", "type": "integer", "not_null": True},
        {"name": "updated_by", "type": "integer", "not_null": True},
        {"name": "created_at", "type": "datetime", "not_null": True},
        {"name": "updated_at", "type": "datetime", "not_null": True},
    ]
}

create_table_sql = generate_sql_from_description(table_description)
print(create_table_sql)
