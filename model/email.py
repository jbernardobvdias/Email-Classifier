class Email:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

class EmailWLabel:
    def __init__(self, sender, content, label):
        self.sender = sender
        self.content = content
        self.label = label