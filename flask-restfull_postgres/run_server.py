from app import app, api
from endpoints import add_urls

if __name__ == "__main__":
    add_urls(api)
    app.run()