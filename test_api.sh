#!/bin/bash
base_url="https://bdg-bankapp.herokuapp.com"
username="test"
password="pass#123"

echo "Token obtain API:"
time resp=`curl -sS -X POST $base_url'/api/auth-token/' -H 'Content-Type: application/json' \
-d '{"username": "'$username'","password": "'$password'"}'`
echo $resp


echo -e "\nFind Branch By IFSC:"
time resp=`curl -sS -X GET $base_url'/api/bank/ifsc/?ifsc=BDBL0001001' \
-H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE1\
NjM5OTY3OTUsImVtYWlsIjoidGVzdEBleGFtcGxlLmNvbSIsIm9yaWdfaWF0IjoxNTYzNTY0Nzk1fQ.ypdurAlT5fUHs7TWO2kv8cfsrcgV\
yw2Q4-WW1yJBNaQ' \-H 'Content-Type: application/x-www-form-urlencoded'`

echo $resp

echo -e "\nFind Branch By City & Bank name:"
time resp=`curl -sS -X GET $base_url'/api/branch/?bank=BANDHAN%20BANK%20LIMITED&city=KOLKATA&limit=20&offset=7' \
-H 'Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo5LCJ1c2VybmFtZSI6InRlc3QiLCJleHAiOjE1NjM\
5OTY3OTUsImVtYWlsIjoidGVzdEBleGFtcGxlLmNvbSIsIm9yaWdfaWF0IjoxNTYzNTY0Nzk1fQ.ypdurAlT5fUHs7TWO2kv8cfsrcgVyw2Q4-WW1yJBNaQ'`

echo $resp