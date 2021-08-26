from snowflake import connector
import os


def sfConnect():
    account = os.getenv('ACC')
    user = os.getenv('USER')
    password = os.getenv('PASSWD')
    warehouse = os.getenv('WH')
    database = os.getenv('DB')
    schema = os.getenv('SCHEMA')
    role = os.getenv('ROLE')

    # print("user = [{}] , password=[{}]".format(user,password))
    cnx = connector.connect(account=account.strip(),user=user.strip(), password=password.strip(),
                            warehouse=warehouse.strip(), database=database.strip(), schema=schema.strip(), role=role.strip())
    return cnx
