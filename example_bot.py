__version__ = "0.2"

from eddie.eddie.bot import Bot, command
import eddie.eddie as eddie


MSG_WELCOME = """
Hi, I'm Eddie-The-Bot, the bot that uses eddie library!
Type /help for a list of commands available
"""
MSG_WHAT = """
eddie is a library to let you create bot in seconds.
You can find further information here:
http://github.com/greenkey/eddie
"""
MSG_HELP = """
Currently I'm not very smart, I'm just programmed with a set of commands:
"""


class ExampleBot(Bot):

    def default_response(self, in_message):
        return self.help()

    @command
    def start(self):
        return MSG_WELCOME

    @command
    def version(self):
        my_version = "ExampleBot v%s" % __version__
        lib_version = "eddie v%s" % eddie.__version__
        return "\n".join([my_version, lib_version])

    @command
    def what(self):
        return MSG_WHAT

    @command
    def help(self):
        text = MSG_HELP
        text += '\n'.join([
            self.command_prepend + cmd
            for cmd in self.command_names
        ])
        return text
