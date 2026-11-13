from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message):
        pass

class FileLogger(Logger):
    def log(self, message):
        print("Logging to file:", message)

class ConsoleLogger(Logger):
    def log(self, message):
        print("Logging to console:", message)

class LoggerFactory(ABC):
    @abstractmethod
    def createLogger(self):
        pass

    def logMessage(self, message):
        logger = self.createLogger()
        logger.log(message)

class FileLoggerFactory(LoggerFactory):
    def createLogger(self):
        return FileLogger()

class ConsoleLoggerFactory(LoggerFactory):
    def createLogger(self):
        return ConsoleLogger()

if __name__ == "__main__":
    file_factory = FileLoggerFactory()  
    console_factory = ConsoleLoggerFactory()

    file_factory.logMessage("Hello!")
    console_factory.logMessage("Hello!")