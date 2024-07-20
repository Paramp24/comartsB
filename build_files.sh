echo "BUILD START"

# create a virtual environment named 'venv' if it doesn't already exist
python3 -m venv env

echo "Venv Built now activating"

# activate the virtual environment
source env/bin/activate

echo "Venv Activated"
echo "now download packages"

# install all deps in the venv
pip install -r requirements.txt

echo "now packages download"

# collect static files using the Python interpreter from venv
python manage.py collectstatic --noinput

echo "BUILD END"

# [optional] Start the application here 
# python manage.py runserver