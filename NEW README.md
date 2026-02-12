# RFD-TOOL

RFD tool

## Cd into django-adminlte-master

```
cd django-adminlte-master
```

## Commands to run

### Activate Venv

```
python -m venv venv
.\\venv\\Scripts\\Activate.ps1
```

### Fallback for build in windows

```
python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py makemigrations
python manage.py migrate
```

### Runnning the server

```
python manage.py runserver
```

## Git Commands
### At Start of the day - To Downloads latest changes.
```
git pull 
```

### At Middle of the day - To Shows what is modified.
```
git status 
```

###  Before Commiting - To Stages all changes.
```
git add . 
```

### After finishing a task - To Saves a version.
(enter msg regarding commit in "......")
```
git commit -m "......" 
```

### End of the day - To Uploads to GitHub.
```
git push
```
