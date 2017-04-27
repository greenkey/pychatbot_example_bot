import eddie
import example_bot


def test_default_echoes():
    bot = example_bot.ExampleBot()

    assert example_bot.MSG_HELP in bot.process('hello!')


def test_welcome():
    bot = example_bot.ExampleBot()

    output = bot.process('/start')

    assert example_bot.MSG_WELCOME == output


def test_get_version():
    bot = example_bot.ExampleBot()

    output = bot.process('/version')

    assert example_bot.__version__ in output
    assert eddie.__version__ in output
