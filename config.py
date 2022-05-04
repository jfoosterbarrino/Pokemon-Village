import os

class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")
    REGISTERED_USERS={
        'kevinb@codingtemple.com':{"name":"Kevin","password":"abc123"},
        'jalenfooster@gmail.com':{"name":"Jalen","password":"Coconut25"},
        'treybarrino@gmail.com':{"name":"Trey", "password":"Jalen9150"}
    }