import time
import threading

class SignalState():

    def __init__(self, color, duration):
        self.color = color
        self.duration = duration

class Signal():
    def __init__(self, states):
        self.states = states

    def start(self, after_duration = 0):
        self.IsRunning = True
        while self.IsRunning:
            for item in self.states:
                if(self.IsRunning):
                    self.state = item.color
                    print(self.state)
                    time.sleep(item.duration)

    def stop(self):
        self.IsRunning = False
        print('signal stopped')


if __name__ == '__main__':
    sig = Signal([SignalState("red", 6),SignalState("yellow", 1), SignalState("green", 2)])
    t1 = threading.Thread(target=sig.start)
    t1.start()
    time.sleep(20)
    sig.stop()
    


