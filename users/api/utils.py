import threading
from mail_templated import EmailMessage


class EmailThread(threading.Thread):
    def __init__(self, email: EmailMessage):
        threading.Thread.__init__(self)
        self.email = email

    def run(self):
        self.email.send()
