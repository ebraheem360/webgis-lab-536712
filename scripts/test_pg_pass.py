import psycopg

passwords = [
    "postgres",
    "admin",
    "password",
    "root",
    "1234",
    "12345",
    "123456",
    "12345678",
    "123456789",
    "nust",
    "igis",
    "webgis",
    "ebraheem",
    "ibrahim",
    "ebraheem360",
    "536712",
    "gis123",
    "nust123",
    "Postgres",
    "Admin",
    "Password",
    "Nust123",
    "Ibrahim123",
    "PostgreSQL",
    "postgis",
]

for p in passwords:
    try:
        conn = psycopg.connect(
            host="localhost",
            port=5432,
            user="postgres",
            password=p,
            dbname="webgis",
            connect_timeout=2
        )
        print(f"SUCCESS! Password is: '{p}'")
        conn.close()
        break
    except Exception as e:
        pass
else:
    print("None of the common passwords matched.")
