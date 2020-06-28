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
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmN2UwM2Y4OTgxNzQwMDEzZDgzZTA4IiwiYXVkIjoiaHR0cHM6Ly9naXRodWIuY29tL0RlZWtzaGFQcmFiaGFrYXIvQ29mZmVlU2hvcCIsImlhdCI6MTU5MzM3MTcyMSwiZXhwIjoxNTkzMzc4OTIxLCJhenAiOiIwUno3b1lMOWp3b1pIMFN4eFFMWDZncktSMkVGU1ZEeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.27lpyAlLdAkIsjRGJTG8LWLmWdIBYPULtj7i32Aw3c_LTcmctBcFG3H57ZX62lh2rltzov87trHkpVzlTa7WZlsLPcpnV8QKcxJO1umZ1R6d3lTndllnXOiNgg5BA-TaOJAS7ZI-NOk4n1g7Fqx-MkI_TabavltCrWO0coqQ1nhAIPLA38ePR8qCp0JwXFajour_fNZpQGYD9PPaLTo5g1sCFuWGq6mwAhZI5qxPAuCdURlesm1NctjpG-Xc7HQszsHzMVyvdMODCJxMvBVkMdx42yXiTCieulAthF4p1XUN9cbhgIuyATJ4e05mnApx0q_9tT2EHBCLMITD-TewYA

```

### Barista account
```
email: latte@gmail.com
password: apple123*
```
#### Token
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Im5aaUxsbEpDVk1sSjVpLWM2TGtBQSJ9.eyJpc3MiOiJodHRwczovL2RlZWRldi5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVmN2RmZTRlODI0YTUwMDE5MjA3ODVkIiwiYXVkIjoiaHR0cHM6Ly9naXRodWIuY29tL0RlZWtzaGFQcmFiaGFrYXIvQ29mZmVlU2hvcCIsImlhdCI6MTU5MzM3MTc5MiwiZXhwIjoxNTkzMzc4OTkyLCJhenAiOiIwUno3b1lMOWp3b1pIMFN4eFFMWDZncktSMkVGU1ZEeSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.cPNaHZJe3HzotBlUrX1lCF8AUjc9ppS818emA5-NFqZ_oVbUR_iA8oj49yk6u-4MFY0XP9cxEm4YMY2e6HqLET5STD4aBkM0WVEBFBPSJMlVJxs10FHmJPiA4g3W7PVG6BlTR6eKMqPr0t5qPoqO8fp-k_21yyqnPlUGkAnFoEAofUt1bqifsrdKmD6ICFXE_eglGtnPdTxZ5HdrHnySATZ3-IpPUOtkD6Yj48bKHeHTWfapV2WcljbFBAVka8KO2R9Mq_IF16DALw9SkdG2glk8DrXn3K0cx_PBdnxVCU1ldsIyYlIRzErNdmi2E0Haf3_Q6-w0eyfhysFouj63XA

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
