## Dependencias

    flask 
    flask-restplus
    flask-cors
    flask-login
    requests
    pymongo
## Backup & Restore DB

    mongodump --archive=test.20150715.archive --db test
    mongorestore --archive=test.20150715.archive --db test

## Uso
    primero correr el api
    segundo correr el testapp