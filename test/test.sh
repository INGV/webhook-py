# OK. Only the query string is printed
curl -X POST  -H "Content-Type: application/json"  http://localhost:8088/api/whook?pippo=1

# OK. Query string and json are printed
curl -X POST  -H "Content-Type: application/json"  http://localhost:8088/api/whook?pippo=1 -d '{"pippo": 1}'

# OK. Query string and json are printed
curl -X POST   http://localhost:8088/api/whook?pippo=1 -d '{"pippo": 1}'

# OK. Query string and json are printed
curl -X POST  -H "Content-Type: application/json"  http://localhost:8088/api/whook?pippo=1 -d '{"pippo": 1}'

# OK. Forms data are printed
curl -X POST  -d "param1=value1&param2=value2" -H "Content-Type: application/x-www-form-urlencoded" http://localhost:8088/api/whook

# OK. Query string and forms data are printed
curl -X POST  -d "param1=value1&param2=value2" -H "Content-Type: application/x-www-form-urlencoded" http://localhost:8088/api/whook?foo=bar&pippo=1

# OK. Query string and forms data are printed. Content-Type: application/x-www-form-urlencoded is implied
curl -X POST  -d "param1=value1&param2=value2"  http://localhost:8088/api/whook?foo=bar&pippo=1

# NOT-OK. Since Content-Type: application/x-www-form-urlencoded is implied, the data are supposed to be urlencoded, NOT josn
curl -X POST  -d '{"pippo': 1}  http://localhost:8088/api/whook?foo=bar&pippo=1