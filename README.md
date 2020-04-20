# Mysql_crud_web_api

## Requirements:

Mysql installed
python3.6 or up
flask installed (if not installed, use command: pip install flask)
flask_mysqldb installed (if not installed, use command: pip install flask_mysqldb)

## Running the app:

open app.py in editor and enter the database details(user,password,host,database name) and save.
Now go to the app directory and run the command: "python app.py"
python or python3 as per the envirenment variable set for python3 in your computer

By default server will be running on localhost with port 5000
ie. "http://127.0.0.1:5000/"


## Usage with examples:

### Get all the data in database:
Hit this api "/api/v1.0/get_data"

### Store:
This will store the given data into database

"http://127.0.0.1:5000/api/v1.0/store_data"

data body:(parameters)

```{
	"date": "2020-12-15",
	"id": "1232",
	"item": "bike",
	"name": "someone",
	"price": 32000
}```


### Update:
This will replace the row with given sr.no by given data

"http://127.0.0.1:5000/api/v1.0/update_row"

data_body:(parameters)

```{
    "date": "2020-12-15",
    "id": "1222",
    "item": "module",
    "name": "someoneelse",
    "price": 4200,
    "sr": "1"
}```


### Delete:
This will delete the row with given sr.no

"http://127.0.0.1:5000/api/v1.0/delete_row"

data_body:(parameters)

```{
	"sr" : "1"
}```

## License:

This project is licensed under the MIT License - see the LICENSE.md file for details