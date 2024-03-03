from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message):
        # Abstract method to log a message
        raise NotImplementedError("Subclasses must implement log method.")


class LoggingSystem:
    def __init__(self, logger: Logger):
        # Initialize LoggingSystem object with a logger
        self.logger = logger

    def do_something(self):
        # Do something and log it
        self.logger.log("Did something...")


class CustomLogger(Logger):
    def log(self, message):
        # Custom logging implementation
        print("Custom logging:", message)


class TestLogger(Logger):
    def log(self, message):
        # Test logging implementation
        print("Test logging:", message)


def main():
    # Example usage
    custom_logger = CustomLogger()
    logging_system = LoggingSystem(custom_logger)
    logging_system.do_something()

    test_logger = TestLogger()
    test_logging_system = LoggingSystem(test_logger)
    test_logging_system.do_something()


if __name__ == "__main__":
    main()