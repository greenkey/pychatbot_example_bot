import eddie
import example_bot


def test_default_echoes():
    bot = example_bot.ExampleBot()

    assert 'hello!' == bot.process('hello!')


def test_welcome():
    bot = example_bot.ExampleBot()

    output = bot.process('/start')

    assert 'welcome' in output.lower()


def test_get_version():
    bot = example_bot.ExampleBot()

    output = bot.process('/version')

    assert example_bot.__version__ in output
    assert eddie.__version__ in output
