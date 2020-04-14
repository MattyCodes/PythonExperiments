from initializer import app, DEV_ENV, APP_ENV
from routes import *

# Run the server.
if __name__ == '__main__':
    app.run(debug =(APP_ENV is DEV_ENV))
