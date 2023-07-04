import os
import codecs

os.system("pip install -r requirements")

# rm cache
os.system("python rm_cache.py")

# makemigrations
os.system("python manage.py makemigrations")

# migrate
os.system("python manage.py migrate")

# load data from json file
os.system("python manage.py loaddatautf8 data.json")

# runserver
os.system("python manage.py runserver")