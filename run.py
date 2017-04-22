#!/usr/bin/env python3

import os
import logging

from eddie.endpoints import HttpEndpoint, TelegramEndpoint, TwitterEndpoint
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

    bot.add_endpoint(TwitterEndpoint(
        consumer_key=os.environ['BOT_TW_consumer_key'],
        consumer_secret=os.environ['BOT_TW_consumer_secret'],
        access_token=os.environ['BOT_TW_access_token'],
        access_token_secret=os.environ['BOT_TW_access_token_secret']
    ))

    bot.run()

    logging.info("Serving...")
