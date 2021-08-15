from snowflake import connector


def sfConnect():
    cnx = connector.connect(account='jd98257.canada-central.azure',
                            user='prashant887', password='prashantL@887',
                            warehouse='COMPUTE_WH', database='DEMO_DB', schema='PUBLIC', role='ACCOUNTADMIN')
    return cnx
