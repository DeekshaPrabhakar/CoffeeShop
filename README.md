# Coffee Shop Full Stack

## Full Stack Nano - IAM Final Project
The application is a digitally enabled cafe for students at Udacity to order drinks, socialize, and study hard. The application:

1) Display graphics representing the ratios of ingredients in each drink.
2) Allow public users to view drink names and graphics.
3) Allow the shop baristas to see the recipe information.
4) Allow the shop managers to create new drinks and edit existing drinks.


## Auth0 account
```python
AUTH0_DOMAIN = 'deedev.auth0.com'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'https://github.com/DeekshaPrabhakar/CoffeeShop'
```

`The tokens may expire, so please use the login credentials below to generate a new JWT token`

### Manager account
```
email: mocha@gmail.com
password: apple123*
```
#### Token
```


```

### Barista account
```
email: latte@gmail.com
password: apple123*
```
#### Token
```


```

## Running the app
- Install dependencies with `pip install -r backend/requirements.txt`
- Set the FLASK_APP variable running `export FLASK_APP=api.py`
- Run the app with `flask run --reload`

## About the Stack

### Backend

The `./backend` directory contains a Flask server with a SQLAlchemy module Auth0 integration for authentication.

[View the README.md within ./backend for more details.](./backend/README.md)

### Frontend

The `./frontend` directory contains a complete Ionic frontend to consume the data from the Flask server.  

[View the README.md within ./frontend for more details.](./frontend/README.md)

## Resources
- [Starter Code](https://github.com/udacity/FSND/tree/master/projects/03_coffee_shop_full_stack/starter_code)
