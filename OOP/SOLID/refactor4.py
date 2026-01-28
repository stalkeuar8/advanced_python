class FileLogger:
    def log(self, message):
        with open("log.txt", "a") as f:
            f.write(f"LOG: {message}\n")

class App:
    def __init__(self, logger: FileLogger):
        self.logger = logger

    def do_work(self):
        self.logger.log(self=self.logger, message="Work started")
        self.logger.log(self=self.logger, message="Work finished")

app = App(FileLogger)
app.do_work()