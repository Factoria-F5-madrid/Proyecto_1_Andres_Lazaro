import time

class Taximetro:
    def __init__(self, stop_rate=0.02, move_rate=0.05):
        self.trip_active = False
        self.state = None
        self.stop_time = 0.0
        self.moving_time = 0.0
        self.state_start_time = None
        self.stop_rate = stop_rate
        self.move_rate = move_rate
        self.start_time = None

    def start_trip(self):
        if not self.trip_active:
            self.trip_active = True
            self.state = "stop"
            now = time.time()
            self.state_start_time = now
            self.start_time = now

    def change_state(self, new_state):
        if not self.trip_active or new_state not in ["stop", "moving"]:
            return

        now = time.time()
        duration = now - self.state_start_time

        if self.state == "moving":
            self.moving_time += duration
        elif self.state == "stop":
            self.stop_time += duration

        self.state = new_state
        self.state_start_time = now

    def stop_trip(self):
        if not self.trip_active:
            return None

        now = time.time()
        duration = now - self.state_start_time

        if self.state == "moving":
            self.moving_time += duration
        elif self.state == "stop":
            self.stop_time += duration

        fare = self.stop_time * self.stop_rate + self.moving_time * self.move_rate

        # Guardar resumen antes de resetear
        summary = {
            "stop_time": self.stop_time,
            "moving_time": self.moving_time,
            "fare": fare
        }

        # Resetear estado
        self.trip_active = False
        self.state = None
        self.stop_time = 0.0
        self.moving_time = 0.0
        self.state_start_time = None
        self.start_time = None

        return summary

    def elapsed_in_state(self):
        if not self.trip_active or self.state_start_time is None:
            return 0
        return time.time() - self.state_start_time
