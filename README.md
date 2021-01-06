# To Do List by Maxim Isakov

## Running it locally

```shell script
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
python todolist.py
```

## Running Tests

```shell script
pytest test.py
```

## API Spec

### Get the current list

**URL** : `http://localhost:8000/list/`

**Method** : `GET`

### Create item in list

**URL** : `http://localhost:8000/list/`

**Method** : `POST`

**Request Body**

```json
{
    "itemName": "Get Dressed",
    "priority": 1
}
```

### Delete item from list

**URL** : `http://localhost:8000/list/{item_priority}`

**Method** : `DELETE`

### Get the list of missing priorities

**URL** : `http://localhost:8000/missing-list/`

**Method** : `GET`