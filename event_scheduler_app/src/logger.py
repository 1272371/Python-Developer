import logging
import sys
import logging
from logtail import LogtailHandler


token = "GWPMJdCq6n126Gpq8WdAhRjJ"

# Create and configure the logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Create a file handler and set the level to DEBUG
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a stream handler and set the level to INFO
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(logging.INFO)


better_stack_handler = LogtailHandler(source_token=token)

file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# Add the handlers to the logger
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)
logger.handlers = [stream_handler, file_handler,better_stack_handler]
