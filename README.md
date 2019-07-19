# Fyle Banks Search API 

## Installation and run

Create virtualenv (Python3.6)
```bash
$ python3.6 -m venv myvenv
```
Activate virtualenv using
```bash
source myvenv/bin/activate
```
Clone this repo
```bash
git clone https://github.com/b4isty/fyle-coding-test.git
```
Install dependencies
```bash
pip install -r requirements.txt
```
Go to the project directory and run migrations files  using this command
```bash
python manage.py migrate
```

To run this project
```bash
python manage.py runserver
```

To run tests
```bash
python manage.py test
```
# Documentation of Banks Search API 

To create a user request to the signup API at https://bdg-bankapp.herokuapp.com/api/signup/
Sample payload
```bash
{
    "username": "test",
    "email": "test@example.com",
    "password": "testpass"
}
```
Or using curl
```bash
curl -X POST -H 'Accept:application/json;' -d username=test -d email=test@example.com -d password=pass#123 https://bdg-bankapp.herokuapp.com/api/signup/

```

To login navigate to https://bdg-bankapp.herokuapp.com/api/auth-token/ api 
Sample payload
```bash
{
    "username": "test",
    "password": "testpass"
}

```
Or using curl
```bash
curl -X POST -H 'Accept:application/json;' -d username=test -d password=testpass https://bdg-bankapp.herokuapp.com/api/auth-token/

```

It will return a token. Use that token in header to authenticate the user on other APIs

To verify and refresh token navigate to https://bdg-bankapp.herokuapp.com/api/verify-token/ and 
https://bdg-bankapp.herokuapp.com/api/refresh-token/ accordingly with below payload

```bash
{
    "token": "your token"
}
```
Or using curl for verify and refresh token

```bash
curl -X POST -H 'Accept:application/json;' -d token="your token" https://bdg-bankapp.herokuapp.com/api/verify-token/

curl -X POST -H 'Accept:application/json;' -d token="your token" https://bdg-bankapp.herokuapp.com/api/refresh-token/
```


To get bank details by ifsc
```bash
curl -X GET -H 'Authorization: JWT your token' 'https://bdg-bankapp.herokuapp.com/api/bank/ifsc/?ifsc=BDBL0001001'

```

To get branch details by bank and city
```bash
curl -X GET -H 'Authorization: JWT your token' 'https://bdg-bankapp.herokuapp.com/api/branch/?bank=BANDHAN%20BANK%20LIMITED&city=KOLKATA&limit=20&offset=10'

```

CURL script location

```bash
<Project directory>/test_api.sh

```
To run CURL script
```bash
bash test_api.sh

```




