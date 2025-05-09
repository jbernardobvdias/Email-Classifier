class Email:
    def __init__(self, sender, subject, content):
        self.sender = sender
        self.subject = subject
        self.content = content

class EmailWLabel:
    def __init__(self, sender, subject, content, label):
        self.sender = sender
        self.subject = subject
        self.content = content
        self.label = label