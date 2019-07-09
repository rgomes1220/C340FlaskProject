import pymysql.cursors
import yaml
import os

# change working directory of this file to be able to
# use relative filepaths (for config/database.yml) correctly
abspath = os.path.abspath(__file__)
dirname = os.path.dirname(abspath)
os.chdir(dirname)



# Read in the configuration file
config = {}
with open("config/database.yml", 'r') as stream:
    try:
        config = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)

config = config.get('database')
# Create a connection to MySQL

def connectMySql():
    connection = pymysql.connect(host=config['host'],
                             user=config['user'],
                             password=str(config['password']),
                             db=config['db'],
                             charset=config['charset'],
                             cursorclass=pymysql.cursors.DictCursor)
    return connection
