# Code Challenge Template
# Technology used
- Django
- Django Rest Framework
- SQLite for database

# Problem Solving Approach
Problem solving approach is attached as .docx along with this repo.
.docx file also contains screenshots of work done.

<br>

# Structure
- wx_data --> Weather data Provided 
- yld_data --> Yield data Provided
- src --> Source Code Provided
- answers --> output.log Generated


# Steps to run the program

- Create and run the virtual environment using commands: <br>
  pip install virtualenv <br>
  virtualenv env<br> <br> To activate virtual environment :<br>
  env/Scripts/activate (in Windows) <br>
  source env/bin/activate (in Linux and Mac)

- Navigate to "src/coding_test/" directory using command cd in terminal
- Install all the requirements using command <br> 
  pip install -r "requirements.txt"
- Migrate the models: <br>
  python manage.py makemigrations <br>
  python manage.py makemigrations app <br>
  python manage.py migrate
- Create superuser <br>
  python manage.py createsuperuser <br>
- Run the python server using command: <br>
  python manage.py runserver <br>
- Ingesting the data:<br>
  Run shell in another terminal using command: <br>python manage.py shell <br> <br>
  Run following commands:<br>
  from app.helper import get_weather_data_by_ingestion, get_yield_data_by_ingestion, get_statistics_information<br>
  get_weather_data_by_ingestion()<br>
  get_yield_data_by_ingestion()<br>
  get_statistics_information()

- Now all the data is uploaded, and it can be seen by accessing admin panel by visiting localhost: <br>
  http://127.0.0.1:8000/admin/login/?next=/admin/

- And other functionalities can be accessed through these API links: <br>
http://127.0.0.1:8000/api/weather<br>
http://127.0.0.1:8000/api/yield <br>
http://127.0.0.1:8000/api/weather/stats/

- With query params it can also be accessed such as : <br>
  http://127.0.0.1:8000/api/weather/?date=20100111

<br><br>
- To run the unittest you can run the command: <br>
  python manage.py test
