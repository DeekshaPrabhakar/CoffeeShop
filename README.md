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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmN2UwM2Y4OTgxNzQwMDEzZDgzZTA4IiwiYXVkIjoiaHR0cHM6Ly9naXRodWIuY29tL0RlZWtzaGFQcmFiaGFrYXIvQ29mZmVlU2hvcCIsImlhdCI6MTU5MzQwMzQ3NSwiZXhwIjoxNTkzNDg5ODc1LCJhenAiOiIwUno3b1lMOWp3b1pIMFN4eFFMWDZncktSMkVGU1ZEeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.SifgAoA5WGcj3BokvX7r8Ey27TBTWHEuIzLOv5w87_Gv3mNuu758VU1tSdC6F9ocxkEN2N0kJDnS0I6TDEnf4TA7iLXyrZsHMMTHXg9ei8xwmIH8WteesBFRVzijsbgUMoX1GdvuwltQUC45g8ybgK46Q9R7ldY928I9TBGU6eUl821tPYNktaYZmtwZlf-u0M-rEj7JJSnopyGZ0lTxSOd5l0T2RiSUC9C2sd1KuDk5jGX6jo1achBpQHUWF5fz72LSKEBIFzqOh4_rUWn1TVGc_RFnkzW7q_G53n_uMR4XUo9WamuoSMX-kcaWGuMAQwAI67lz0AJlrwA-wB6Lsg

```

### Barista account
```
email: latte@gmail.com
password: apple123*
```
#### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmN2RmZTRlODI0YTUwMDE5MjA3ODVkIiwiYXVkIjoiaHR0cHM6Ly9naXRodWIuY29tL0RlZWtzaGFQcmFiaGFrYXIvQ29mZmVlU2hvcCIsImlhdCI6MTU5MzQwMzUzNywiZXhwIjoxNTkzNDg5OTM3LCJhenAiOiIwUno3b1lMOWp3b1pIMFN4eFFMWDZncktSMkVGU1ZEeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.AAvnJHYP7Li0UCnxoICMGjt1Sdcdjj1oi2_NrzqVKNyTKvY1_vPJvjBmIvNSpJoKCumolDA5ZVeJ6duyVX-BEs9q4atKuW1xbV-QUGfH0hK7_Yd8Z4akGtNi_9JSBYcnLWO1uhOcJTtiugNxBBG6DEemcoHCixC5xPonc1eOknI0o3vfT9p8yN5GSEvykF150pu_TeLj76r88sb3nrc4V9cKdpk-sVZPJ3o3X_E3zwxnQgv5yD6NL2-eno_x8uAI3qyXsqIGta5aYgqU3-WAciisSRl5u_KJrNdd0PGfwu3OgkQqTGOqKbIJFNBkRrBhM1KRzhIEWbT7aJMGJus1eg

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
