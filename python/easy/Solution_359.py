# 359. Logger Rate Limiter

class Logger:
    def __init__(self):
        self.history = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if timestamp < self.history.get(message, 0):
            return False
        self.history[message] = timestamp + 10
        return True


logger = Logger()
logger.shouldPrintMessage(1, "foo")  # True
logger.shouldPrintMessage(2, "bar")  # True
logger.shouldPrintMessage(3, "foo")  # False
logger.shouldPrintMessage(15, "foo")  # True
