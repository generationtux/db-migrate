#!/usr/bin/python
#
# PSUEDO
# - Run cloudmigrate [CSQL IP] [RDS HOSTNAME]
# - Connect to Google Cloud SQL
# - MySQL Dump of database
# - Store MySQL Dump File Locally
# - Connect to AWS RDS MySQL Instance
# - Load Dump File onto AWS RDS MySQL Instance
# - Test Connectivity

import argparse, gzip, os

def dump(hostname, username, database):
    # let user know what the is script is doing
    print "Dumping MySQL \033[91;1m%s\033[0m database on \033[91;1m%s\033[0m --> \033[91;1m%s.sql.gz\033[0m." % (database, hostname, database)
    mysqldump = "mysqldump -h%s -u%s -p --add-drop-database --databases %s | gzip -f > %s.sql.gz" % (hostname, username, database, database)
    os.system(mysqldump)
    return database

def load(hostname, username, database):
    # deflate gzipped sql file
    print "Deflating \033[91;1m%s.sql.gz\033[0m --> \033[32;1m%s.sql\033[0m" % (database, database)
    os.system("gunzip -v -f -q %s.sql.gz" % database)

    # restore the database on the new host
    print "Restoring MySQL %s database on %s." % (database, hostname)
    os.system("mysql -h%s -u%s -p < %s.sql" % (hostname, username, database))

    # remove old dump file
    print "Removing %s.sql dump file" % database
    os.system("rm -f %s.sql" % database)

def main():
    # building help menu
    usage = "usage: %prog [options] arg"
    parser = argparse.ArgumentParser(prog='dbmigrate', description="Migrate database from one host to another host")
    parser.add_argument('--src', metavar=('host/ip', 'username', 'database'), dest="src", nargs=3, type=str, help="Source database connection credentials.", required=True)
    parser.add_argument('--dest', metavar=('host/ip', 'username'), dest="destination", nargs=2, type=str, help="Destination database connection credentials. NOTE: Username must have database creation privileges", required=True)

    # get all the args
    args = parser.parse_args()

    # get source parameters
    src_host = args.src[0]
    src_user = args.src[1]
    database = args.src[2]

    # create dump file from source database
    dump(src_host, src_user, database)

    # if dumpfile exists then load
    # it into the destination database
    if os.path.exists(database + '.sql.gz'):
        dst_host = args.destination[0]
        dst_user = args.destination[1]
        load(dst_host, dst_user, database)


if __name__ == "__main__":
    main()
