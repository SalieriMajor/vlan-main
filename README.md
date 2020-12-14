## Running the project 

You will need:
- postgres installed. 
- Python installed in your system. 

### Setting up Postgres


First, we will need to create a postgres database. We first enter the postgres console by entering the following console

```bash
psql -U postgres
```
Then enter the postgres user password. IF you have pgadCREATEmin, you can enter into the postgres database directly without entering this. 

We then run the following to create our database, user and password:
```postgresql
CREATE DATABASE netinfo;
\c netinfo
CREATE USER netinfo_user WITH PASSWORD 'netinfo_password';
GRANT ALL PRIVILEGES ON DATABASE netinfo TO netinfo_user;
GRANT ALL ON SCHEMA public to netinfo_user;
GRANT ALL ON ALL TABLES IN SCHEMA public to netinfo_user;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to netinfo_user;
```

### Setting up our python environment

If you're on python3 run:
```shell script
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# run the migration
flask db upgrade
```

Your database should now have the relevant tables
Now, alter the .env file DEVICE_ADDRESS, DEVICE_USERNAME and DEVICE_PASSWORD to be those of your Cisco device. 

If you run 
```shell script
flask run
```

It should run the server. Open your browser and go to http://127.0.0.1:5000. Click <i>synchronize</i> and if the credentials entered in the .env file are correct, you should see all the vlans on the device with their details on that page. 

You shhould also be able to delete and add new vlans. 

