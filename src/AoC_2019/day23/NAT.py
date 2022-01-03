class NAT:

    def __init__(self, computers):
        self.computers = computers
        self.last_x = -1
        self.last_y = -1

    def receive_packet(self, x, y):
        self.last_x = x
        self.last_y = y

    def monitor(self):
        while True:
            idle = True
            for comp in self.computers:
                if comp.has_packets():
                    idle = False
                    break

            if idle and self.last_x > 0 and self.last_y > 0:
                print([self.last_x, self.last_y])
                self.computers[0].post_inputs([self.last_x, self.last_y])
                self.last_y = -1
                self.last_x = -1
