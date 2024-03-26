

import logging

# Define a custom format with bold text
log_format = '%(asctime)s %(levelname)s: \n%(message)s\n'

# Configure the logger with the custom format
logging.basicConfig(filename="/Users/juanreyesgarcia/Dev/Python/LLMs/LLMOps/logs/logging.log",
                    level=logging.INFO,
                    format=log_format)
