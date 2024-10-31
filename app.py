from flask import Flask
import logging
import time
import random


app = Flask(__name__)

#set up logging for the file
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    logger.info('Home page is accessed')    
    return "Welcome to the logging app!"

@app.route("/generate-log")
def generate_log():
    log_level = random.choice([logging.INFO, logging.WARNING, logging.ERROR])
    logger.log(log_level, f"Log level {log_level} generated at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    return "Log generated!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

