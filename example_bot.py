__version__ = "0.2"

from eddie.bot import Bot, command
import eddie


class ExampleBot(Bot):

    def default_response(self, in_message):
        return in_message

    @command
    def start(self):
        return """
            Hi, I'm EddieBot, the bot that uses eddie library!

            Type /help
        """

    @command
    def version(self):
        my_version = "ExampleBot v%s" % __version__
        lib_version = "eddie v%s" % eddie.__version__
        return "\n".join([my_version, lib_version])
