# Parking App
App for car parking with IP rate-limitting. 
## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd car_parking-master/car_parking
    $ pip install -r requirements.txt
    ```
2. Set the maximum parking lot size in .env file

   ```bash
   ranger = [some_integer] 
   ```

3. Running app

   ```bash
   $ python manage.py runserver
   ```
4. Run the app in container using [Docker-compose](https://docs.docker.com/compose/install/).

   ```bash
   cd to the root directory
   $ docker-compose -f docker-compose.yml up -d --build
   ```      
   
5. Running test-cases

   ```bash
   $ pytest
   ```   
## Project Structure

### Backend 
```shell
car_parking/                               # All application code in this directory.
│
├─parking/─────┐-- __init__.py             # initializing file for Django module.
│              ├── asgi.py                 # standard interface between web servers, frameworks, and applications.    
│              ├── settings.py             # all settings for Django applications stored here.
│              ├── urls.py                 # all API end-points to be blended with views.
│              └─  wsgi.py                 # wsgi file for Django app        
├─- park/ ─────┐-- __init__.py             # initializing file for parking app.
│              ├── apps.py                 # All apps created are to be added here.
│              └─  views.py                # All views for the app is added here.
├─ tests/ ─────┐-- __init__.py             # initializing file for test module.
│              └─  test_parking.py         # contains all test cases for the parking app.
├─ .env                                    # Contains ranger variable for maximum slots in parking lot.
├─ requirements.txt                        # requirements file.
└─ manage.py                               # Main entry-point into the Django application.
```
## API Documentation 

### `Add car to parking slot` 

1. `POST /slots` 

```json
 application/json - { "car_number": "ka012395"}
```
##### `response`

```json
{"slot": "1", "car_number": "ka012395"}
    
```
2. `POST /unpark` 

```json
 application/json - { "slot": "1"}
```
##### `response`

```json
{"Success": "Car removed!"}
    
```
3. `GET /getslots?car_number=ka012395` 


##### `response`

```json
{"slot": "1","car_number": "ka012395"}
    
```
   `GET /getslots?slot=1` 


##### `response`

```json
{"slot": "1","car_number": "ka012395"}
    
```
##  Logic and Assumptions

1. **When a user comes for parking**
    - We first check if any slot is empty, if not appropriate error message is passed.
    - If slot is empty then we park the vehicle and returns the slot number.

2. **When a user wants to unpark the vehicle**   
    - We 1st check whether the slot given exists and if the given slot is empty, if not we pass the appropriate error message. 
    - If its a valid slot number with car parked then we remove the car parked in that slot.
    
3. **When user wants to get slot and car number by giving slot/car number**<br />
    ***If a user wants to search by car number***
    - We 1st check whether the given car number exists, if not we pass the appropriate error message.
    - If the car number is parked, we return car number with the slot where it is parked.
    - We have made two dictionary with key, value as car_number,slot_number and slot_number,car_number as search will be in O(n) as get results should always be faster.
    - Here search will be through dictionary car_to_slot which store key,value as car number, slot_number and thus search will be O(n).<br />
    ***If a user wants to search by slot***
    - We 1st check whether the slot given exists and if the given slot is empty, we pass the appropriate error message.
    - If its a valid slot number with car parked then we return car number with the slot where it is parked.
    - Here search will be through the dictionary 'slot_to_car' which store key,value as slot_number, car number and thus search will be O(n).
