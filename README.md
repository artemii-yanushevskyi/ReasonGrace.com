# Tracker
## Overview

This project is made for educational purposes.
It has all the basic common elements of IT development

* Programing, Python
* Data Analysis, separate repository [here](https://github.com/artemii-yanushevskyi/Interviews-preparation)
* Databases, SQLite
* Backend, Django
* Frontend


## Techical
#### Evironment
static path in format ```/static/=/path/to/static_folder/```. For instance ```css``` files are in static folder.
#### Version Control

```bash
git add --all .                                                                                                                      
git commit -m "Changed static path, added static file (css) and added README"                                                        
git push -u origin master
```

#### Bash

Shell color palette, alias and shortcuts have been moved to a separate repository [Terminal](https://github.com/artemii-yanushevskyi/Terminal).

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

### Django

[Django Girls Tutorials](https://tutorial.djangogirls.org/en/), good tutorial to get started.
