class SyntaxException(Exception):
    def __init__(self, message, errors):
        self.message=message
        self.errors = errors

    def __str__(self):
        return self.message + "\nLine : " + str(self.errors[0]) +\
            ", Column : " + str(self.errors[1]) +\
            "\nReport: (" + self.errors[2] + ")"

class SyntaxErrorListener():
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise SyntaxException("Syntax Error", (line, column, msg))

    def reportAmbiguity(self, *args, **kwargs):
        pass

    def reportContextSensitivity(self, *args, **kwargs):
        pass

    def reportAttemptingFullContext(self, *args, **kwargs):
        pass
