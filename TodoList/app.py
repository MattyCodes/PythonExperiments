from initializer import app, DEV_ENV, APP_ENV
from routes import *

# Run the server.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=(APP_ENV is DEV_ENV))
