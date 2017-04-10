import pychatbot
import example_bot


def test_get_version():
    bot = example_bot.ExampleBot()

    output_version = bot.version()

    assert example_bot.__version__ in output_version
    assert pychatbot.__version__ in output_version
