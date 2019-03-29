#!/opt/local/bin/python
#
# Written with python 2.7.3
#
# checkPG91replicationlag.py
#
# This script is used to test the replication lag between two postgres database servers, one being master the other slave
# The script queries the xlog location of the master (logs sent) and the xlog received location (logs received by master).
# The output of these two values are hex values which are converted into bytes, the script finds the difference and then \
# compares it to the max allowed lag between the logs
#
# Todo: needs a lot of cleanup
#
# USAGE
# 	$0 master_database slave_database

# Run every 10 minutes. Requires python be installed with psycopg2 and sys modules
#
#
import psycopg2
import sys

# Check if two arguments were given to the script
if len(sys.argv) != 3:
	print("\nUSAGE", sys.argv[0], "master_database slave_database\n")
	exit(3)

# Define variables
dbmaster_host = sys.argv[1]
dbslave_host = sys.argv[2]
dbname = ""
dbuser = ""
dbpass = ""
# max_lag is the amount of allowable lag, in bytes, between master and slave.  Default is set to 300MB
max_lag = 314572800


def dbmaster(host):
       '''
	 This function connects to the master and queries the xlog_location, converts the value from hex to integer
	 and places it in a global variable.
        '''
	try:
		conn_string = "host={0} dbname={1} user={2} password={3}".format(host,dbname,dbuser,dbpass)
		conn = psycopg2.connect(conn_string)
	except psycopg2.OperationalError as e:
		print("Error", e)
		exit(3)
	cursor = conn.cursor()
	cursor.execute("select pg_current_xlog_location()")
	global dbmaster_num
	db_row = cursor.fetchone()
	db_hex  = db_row[0].translate(None, "/")
	dbmaster_num = int(db_hex, 16)
	conn.close

def dbslave(host):
	'''This function connects to the slave and queries the xlog_receive_location, converts the value from hex to integer
	 and places it in a global variable.
         '''
	try:
		conn_string = "host={0} dbname={1} user={2} password={3}".format(host,dbname,dbuser,dbpass)
		conn = psycopg2.connect(conn_string)
	except psycopg2.OperationalError as e:
		print("Error", e)
		exit(3)
	cursor = conn.cursor()
	cursor.execute("select pg_last_xlog_receive_location()")
	global dbslave_num
	db_row = cursor.fetchone()
	db_hex  = db_row[0].translate(None, "/")
	dbslave_num = int(db_hex, 16)
	conn.close

def db_replicate_lag(master,slave):
       '''
	Determines the lag between the slave and master and then tests it against the max_lag
        '''
	real_lag=int(slave)-int(master)
	if real_lag > max_lag:
		print("POSTGRES_LAG CRITICAL: LAG =", real_lag)
		exit(2)
	else:
		print("POSTGRES_LAG OK: LAG =", real_lag)
		exit(0)


dbmaster(dbmaster_host)
dbslave(dbslave_host)
db_replicate_lag(dbmaster_num,dbslave_num)
