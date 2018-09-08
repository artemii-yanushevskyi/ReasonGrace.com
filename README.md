# Tracker
## Overview
*This project is currently under development.*
## Techical
#### Evironment
static path in format ```/static/=/path/to/static_folder/```. For instance ```css``` files are in static folder.
#### Version Control

```bash
git add --all .                                                                                                                      
git commit -m "Changed static path, added static file (css) and added README"                                                        
git push -u origin master
```

#### Bash ```.bash_profile```


```bash
alias ..="cd .."                                                                                                                            
alias ....="cd ../.."                                                                                                                       
alias tracker="cd ~/site/mysite/tracker"                                                                                                    
alias site="cd ~/site/mysite"
```

#### Install JSONField

```bash
fabulous@ssh4:~/site/env/bin$ pip install psycopg2
```

```bash
python manage.py makemigrations tracker
```

*Do not forget to add a default value*


## To do

You can’t use a JSONField from django.contrib.postgres with an Sqlite3 database. You need to either set up a PostgreSQL database and update
your DATABASES setting, or use a different field in your model.


## Development process

#### Reset Migrations While Keeping DBs                                                                                                   
```bash                                                                                                                                       
python manage.py migrate --fake tracker zero
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete
python manage.py makemigrations
python manage.py showmigrations
python manage.py migrate
```

> Atom code editor with sftp support is the best option I know for remote editing.

> Now I can edit files and commit changes from iPhone via CodeHub.

## Resources
#### Recursive table
Tables nested in each other:
[bl.ocks.org](http://bl.ocks.org/nautat/raw/4085017/ bl.ocks.org)


[The Hitchhiker’s Guide to d3.js](https://medium.com/@enjalot/the-hitchhikers-guide-to-d3-js-a8552174733a Medium)

