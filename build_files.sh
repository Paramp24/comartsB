source env/bin/activate

pip install -r requirements.txt 
python3.11 manage.py collectstatic
