class DataPacketBuffer:

    def __init__(self, send_func):
        self.dest = -1
        self.x = -1
        self.y = -1
        self.inputs_received = 0
        self.send_func = send_func

    def receive_input(self, input_val):
        if self.inputs_received == 0:
            self.dest = input_val
        elif self.inputs_received == 1:
            self.x = input_val
        else:
            self.y = input_val
            self.send_func(self.dest, self.x, self.y)
            # print("Posting X=" + str(self.x) + " Y=" + str(self.y) + " to Node " + str(self.dest))

        self.inputs_received = (self.inputs_received + 1) % 3

