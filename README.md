# Raspberry Pi Humidity / Temperature control with Django Dashboard

## Requirements

- DHT22 Sensor
- Raspberry PI Zero W


## Python / Django setup

#### Create a virtualenv  
    python3 -m venv ~/.virtualenvs/pinkbird

#### Add Secret Key to environment
    echo 'export SECRET_KEY="unique to you"' >> ~/.virtualenvs/pinkbird/bin/activate

#### Source into virtualenv
    source ~/.virtualenvs/pinkbird/bin/activate

#### Install python requirements
    pip install -r requirements.txt  

#### Run migrations 
    ./manage.py migrate  

#### Start the Django Server
    ./manage.py runserver 0.0.0.0:80  

