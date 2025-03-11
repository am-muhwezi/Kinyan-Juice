from flask import Flask
from app import create_app
from app.config.config import Config_dict


app=create_app()

if __name__=="__main__":
    app.run()
