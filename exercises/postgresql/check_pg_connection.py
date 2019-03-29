#!/opt/local/bin/python
#
# check_pg_connection.py
#
# Script is used to test if postgres is accepting connections.
#
#
import psycopg2
import argparse

parser = argparse.ArgumentParser(description='Used to test if postgres is accpeting connections')
parser.add_argument('database_host',  type=str, nargs='?', default="localhost", help='Hostname or IP of the database, defaults to localhost')
parser.add_argument('database_port',  type=str, nargs='?', default="5432", help='Port to use, defaults to 5432')
parser.add_argument('database',  type=str, nargs='?', default="postgres", help='Database to connect to, defaults to postgres')
parser.add_argument('database_user',  type=str, nargs='?', default="xxx", help='User to connect to the database, defaults to nagioscheck')
parser.add_argument('database_password',  type=str, nargs='?', default="xxx", help='Password to use, defaults to our default password')
args = parser.parse_args()

def db_connection(host, user, password, database, port):
    ''' connects to the slave and queries the xlog_receive_location, converts the value from hex to integer
    and places it in a global variable.
    '''
    try:
        conn_string = "host={0} dbname={1} user={2} password={3} port={4}".format(host,database,user,password,port)
        conn = psycopg2.connect(conn_string)
    except psycopg2.OperationalError as e:
        estr=str(e)
        if "Connection refused" in estr:
            print("CRITICAL: POSTGRES ON %s PORT %s NOT ACCEPTING CONNECTIONS"  % (host,port))
            exit(2)
        elif "authentication failed" in estr:
            print("UNKNOWN: POSTGRES ON %s PORT %s AUTHENTICATION FAILED"  % (host,port))
            exit(3)
        else:
            print("UNKNOWN: POSTGRES ON %s PORT %s RECEIVING UNKNOWN ERROR"  % (host,port))
            exit(3)
    cursor = conn.cursor()
    cursor.execute("select pg_backend_pid()")
    conn.close
    print("OK: POSTGRES ACCEPTING CONNECTIONS")


# Running of the functions.
db_connection(args.database_host, args.database_user, args.database_password, args.database, args.database_port)
