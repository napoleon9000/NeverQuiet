from defination.definations import Status


class Session:
    def __init__(self, user_id):
        self.user_id = user_id
        self.status = Status([0, 0])

    def update_status(self, status: Status):
        self.status = status
