# README
In short:
Core of the logic behind the website can be found in the views.py.
If you want to add a page, you have to include it in the url_patterns in urls.py.
The html files in the templates folder can interact with the views.py file using:
{{}} notation for values from the context supplied by views.py
extra functions from side_functions.py
javascript forms and functions in the static/js folder

To run do:
python3 manage.py runserver  

Note when deploying to the azure VM:
Change the value of ALLOWED_HOST to the ip adress belonging to the VM
Change the value of DEBUG to False

How I deployed it now is by pulling the now_ok_sql branche from github through an ssh connection to the VM. In this git repository only the dump of the sqlite db is included, which has to be read first on the VM in order to make the website function properly. This can be done by connecting to a db, in this case development.sqlite by typing: "sqlite3 development.sqlite" in the terminal and then type: ".read scpl_no_text.sql". Where "scpl_no_text.sql" is the dump file. 