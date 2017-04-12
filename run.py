#!/usr/bin/env python3

import os
import logging

from pychatbot.endpoints import HttpEndpoint, TelegramEndpoint
from example_bot import ExampleBot


logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":

    bot = ExampleBot()

    bot.add_endpoint(HttpEndpoint(
        port=int(os.environ['PORT'])
    ))

    bot.add_endpoint(TelegramEndpoint(
        token=os.environ['BOT_TG_TOKEN']
    ))

    bot.run()

    logging.info("Serving...")
