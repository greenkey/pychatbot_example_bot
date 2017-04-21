__version__ = "0.2"

from pychatbot.bot import Bot, command
import pychatbot


class ExampleBot(Bot):

    def default_response(self, in_message):
        return in_message

    @command
    def start(self):
        return "Welcome to ExampleBot, the bot that uses pychatbot library!"

    @command
    def version(self):
        my_version = "ExampleBot v%s" % __version__
        lib_version = "pychatbot v%s" % pychatbot.__version__
        return "\n".join([my_version, lib_version])
