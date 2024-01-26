
class UserInterface:
    def __init__(self, lineLength=130):
        self.lineLength = lineLength
        self.border = "<" + "-" * lineLength + ">"

    def textLoopBorder(self, text):
        def textLoop(text):
            words = text.split()
            lines = []
            currentLine = ""
            for word in words:
                if len(currentLine) + len(word) + 1 <= self.lineLength:
                    currentLine += word + " "
                else:
                    lines.append(currentLine.strip())
                    currentLine = word + " "
            if currentLine:
                lines.append(currentLine.strip())
            borderedLines = [f"|{line.center(self.lineLength)}|" for line in lines]
            return f"{self.border}\n{'\n'.join(borderedLines)}\n{self.border}"
        return textLoop(text)