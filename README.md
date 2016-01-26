Kipa
====

Kipa- / Tupa2-ohjelmisto, jota käytetään partiotaitokilpailujen tuloslaskentaan. 

## Starting the server
create new virtualenv with:
```
virtualenv kipa-virtualenv
```
Go in, and activate
```
cd kipa-virtualenv
source bin/activate
```
Clone this project inside current folder with 'git clone'

Next we need to install some dependencies
Inside project folder, run
```
pip install -r requirements.txt
```

Finally start server with
```
python manage.py runserver 0.0.0.0:8000
```

Vanhat sivustot:

* https://sites.google.com/site/kisapalvelukipa/
* http://sourceforge.net/projects/tupa2/
