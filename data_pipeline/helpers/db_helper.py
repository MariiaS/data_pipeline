from sqlalchemy import create_engine, inspect

db_name = 'database'
db_user = 'username'
db_pass = 'secure_password'
db_host = 'db'
db_port = '5432'

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_user, db_pass, db_host, db_port, db_name)
db = create_engine(db_string)
inspector = inspect(db)


def add_data_to_table_from_df(user_df, game_name):
    table_name = game_name+'users'
    if inspector.has_table(table_name):
        print("The table already exists, adding new rows")
        user_df.to_sql("temporary_table", con=db)
        db.execute(
            "INSERT INTO " + table_name + "(SELECT * FROM temporary_table WHERE first_name NOT IN (SELECT first_name "
                                          "FROM " + table_name + ") AND last_name NOT IN (SELECT last_name FROM " +
            table_name + "))")
        drop_table("temporary_table")
    else:
        user_df.to_sql(table_name, con=db)


def drop_table(table_name):
    db.execute("DROP TABLE " + table_name)


def print_last_five_raws(table_name):
    result = db.execute("SELECT * FROM " + table_name + " LIMIT 5")
    for row in result:
        print(row)


def get_table_columns(game_name):
    table_name = game_name + 'users'
    return inspector.get_columns(table_name)
