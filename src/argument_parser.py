import argparse


class ArgumentParser:
    def __init__(self):
        argument_parser = argparse.ArgumentParser()
        argument_parser.add_argument(
            "-d", "--debug", action="store_true", help="post a message to the debug channel"
        )
        argument_parser.add_argument(
            "-m", "--migrate", action="store_true", help="migrate mode"
        )
        self.arguments = argument_parser.parse_args()
