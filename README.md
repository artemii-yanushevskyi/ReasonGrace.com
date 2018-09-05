# Tracker
## Overview
*This project is currently under development.*
## Techical
#### Evironment
static path in format ```/static/=/path/to/static_folder/```. For instance ```css``` files are in static folder.
#### Version Control
```
git add --all .                                                                                                                      
git commit -m "Changed static path, added static file (css) and added README"                                                        
git push -u origin master
```

#### Bash

```.bash_profile```:

```
alias ..="cd .."                                                                                                                            
alias ....="cd ../.."                                                                                                                       
alias tracker="cd ~/site/mysite/tracker"                                                                                                    
alias site="cd ~/site/mysite"
```

#### Install JSONField

```fabulous@ssh4:~/site/env/bin$ pip install psycopg2```

```python manage.py makemigrations tracker```

*Do not forget to add a default value*



## To do

You can’t use a JSONField from django.contrib.postgres with an Sqlite3 database. You need to either set up a PostgreSQL database and update 
your DATABASES setting, or use a different field in your model. 


 #### Reset Migrations While Keeping DBs                                                                                                   
> ```                                                                                                                                       
python manage.py migrate --fake tracker zero
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate```

> Now I can commit from iPhone using CodeHub.