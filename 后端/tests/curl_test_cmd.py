"""
    curl optins
    ~~~~~~~~~~~~~~~~~~~~~~~
-X	specify HTTP request method e.g. POST
-H	specify request headers e.g. "Content-type: application/json"
-d	specify request data e.g. '{"message":"Hello Data"}'
--data-binary	specify binary request data e.g. @file.bin
-i	shows the response headers
-u	specify username and password e.g. "admin:secret"
-v	enables verbose mode which outputs info such as request and response headers and errors
"""

"""
curl -X POST -d {'sCode':'2014211674','pwd':'2014211674'} http://127.0.0.1:5000/login
curl -H "Content-type: application/json" -X POST  -d '{'sCode':'2014211674','pwd':'2014211674'}' http://127.0.0.1:5000/login

curl -X GET http://127.0.0.1:5000/info
curl -i -H 'content-type: application/json' -X POST -d '{\"sCode\":\"2014211674\",\"pwd\":\"2014211674\"}' http://127.0.0.1:5000/login
"""
