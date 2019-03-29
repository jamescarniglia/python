#!/opt/local/bin/python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('database_host',  type=str, nargs='?', default="localhost", help='Hostname or IP of the database, defaults to localhost')
parser.add_argument('database_user',  type=str, nargs='?', default="postgres", help='User to connect to the database, defaults to postgres')
parser.add_argument('database_password',  type=str, nargs='?', default="", help='Password to use, defaults to a blank string')
parser.add_argument('database',  type=str, nargs='?', default="postgres", help='Database to connect to, defaults to postgres')

args = parser.parse_args()
#print(args.database_host)
#print(args.database_user)
