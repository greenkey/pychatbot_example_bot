__version__ = "0.2"

from eddie.bot import Bot, command
import eddie


class ExampleBot(Bot):

    def default_response(self, in_message):
        return self.help()

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

    @command
    def what(self):
        text = """
            eddie is a library to let you create bot in seconds.
            You can find further information here: 
            http://github.com/greenkey/eddie
        """
        return text

    @command
    def help(self):
        text = """
            Currently I'm not very smart, I'm just programmed with a set of commands:
        """
        text += '\n'.join([self.command_prepend + cmd for cmd in self.command_names])
        return text
