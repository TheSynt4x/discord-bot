import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(message)s',
    handlers=[
        logging.FileHandler(
            "logs/%s.log" % datetime.today().strftime('%Y-%m-%d'),),
        logging.StreamHandler(),
    ],
)

logger = logging
