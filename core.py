import time
from logger import get_logger

logger = get_logger(__name__)

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
            logger.info("Iniciando viaje")
            self.trip_active = True
            self.state = "stop"
            now = time.time()
            self.state_start_time = now
            self.start_time = now

    def change_state(self, new_state):
        if not self.trip_active or new_state not in ["stop", "moving"]:
            logger.warning(f"Intento de cambio inválido: viaje activo: {self.trip_active}, nuevo estado: {new_state}")
            return

        now = time.time()
        duration = now - self.state_start_time
        logger.debug(f"Cambiando estado de {self.state} a {new_state}. Duración anterior: {duration:.2f}s")

        if self.state == "moving":
            self.moving_time += duration
        elif self.state == "stop":
            self.stop_time += duration

        self.state = new_state
        self.state_start_time = now

    def stop_trip(self):
        if not self.trip_active:
            logger.warning("Intento de finalizar un viaje que no está activo")
            return None

        now = time.time()
        duration = now - self.state_start_time

        if self.state == "moving":
            self.moving_time += duration
        elif self.state == "stop":
            self.stop_time += duration

        fare = self.stop_time * self.stop_rate + self.moving_time * self.move_rate

        logger.info(
            f"Finalizando viaje. Detenido: {self.stop_time:.2f}s, "
            f"En movimiento: {self.moving_time:.2f}s, Tarifa: ${fare:.2f}"
        )

        summary = {
            "stop_time": self.stop_time,
            "moving_time": self.moving_time,
            "fare": fare
        }

        logger.debug(f"Resumen del viaje: {summary}")
        
        
        try:
            with open("historial.txt", "a", encoding="utf-8") as f:
                f.write(
                    f"{time.strftime('%Y-%m-%d %H:%M:%S')} - "
                    f"Detenido: {self.stop_time:.1f}s, "
                    f"En movimiento: {self.moving_time:.1f}s, "
                    f"Tarifa: ${fare:.2f}\n"
            )
            logger.info("Resumen guardado en historial.txt")
        except Exception as e:
            logger.error(f"Error al guardar el historial: {e}")

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
