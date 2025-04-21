import configparser
import os


parser = configparser.ConfigParser()

parser.read(os.path.join(os.path.dirname(__file__), 'Z:\cours_quatrième_année\PersonalCourse\DataEngineerProjectKafkaZookeeper\config\config.local'))

YOUTUBE_API_KEY = parser.get('youtube', 'API_KEY')
PLAYLIST_ID = parser.get('youtube','PLAYLIST_ID')