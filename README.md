# CodenamesPictures
It's a game Codenames with AI generated images and players can choose any ideas for this images e.g. Twin Peaks and the pool of the pictures will be with things/persons from Twin Peaks.

# Before to start the `main.py`
## Alembic instructions
We need to start our Alembic migrations by command (if we didn't do this before):
```
alembic init migrations
```

After creating migrations we need to set the URL database and change the lines in settings:
- Go to the file `alembic.ini` and change the line 64 with `sqlalchemy.url=` to the database where we will make migrations;
- Then we need in `migrations/env.py`, import the Base model and change the lines:
```
from myapp import mymodel
target_metadata = Base
```

### Alembic commands
- Every time when we need to create a migrations to our database:
```
alembic revision -m "comment"
```
- Then we need to go to a new file with migration and upgrade the table;
- To apply the changes:
```
alembic upgrade heads
```
