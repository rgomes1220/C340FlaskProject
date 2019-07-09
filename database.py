import pymysql.cursors
import yaml

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
connection = pymysql.connect(host=config['host'],
                             user=config['user'],
                             password=str(config['password']),
                             db=config['db'],
                             charset=config['charset'],
                             cursorclass=pymysql.cursors.DictCursor)
