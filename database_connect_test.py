import psycopg2

def postgres_test():

    try:
        conn = psycopg2.connect("dbname='pepernotendatabase' user='postgres' host='localhost' password='pwd' port='5433' connect_timeout=1 ")
        conn.close()
        return True

    except:
        return False
