from pychatbot.bot import Bot, command


class ExampleBot(Bot):

    def default_response(self, in_message):
        return in_message

    @command
    def start(self):
        return "Welcome to ExampleBot, the bot that uses pychatbot library!"
