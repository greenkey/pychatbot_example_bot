#!/usr/bin/env python3

import os

from endpoints.http import HttpEndpoint
from endpoints.telegram import TelegramEndpoint
import telegram.ext


if __name__ == "__main__":
    from example_bot import ExampleBot

    bot = ExampleBot()

    bot.add_endpoint(HttpEndpoint())

    bot.add_endpoint(TelegramEndpoint(
        token=os.environ['BOT_TG_TOKEN']
    ))

    bot.run()

    print("Serving...")
