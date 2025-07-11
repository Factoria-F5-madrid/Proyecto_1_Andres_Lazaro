from core import Taximetro
from logger import get_logger

logger = get_logger(__name__)

def taximetro():
    print('Bienvenido al taxímetro con Python de F5')

    stop_rate = 0.02
    move_rate = 0.05
    choice = input('¿Deseas configurar los precios manualmente? (s/n): ').strip().lower()

    if choice == 's':
        logger.info("Usuario elige configurar tarifas manualmente")
        while True:
            try:
                stop_rate = float(input('Ingrese el precio por segundo detenido (ej. 0.02): '))
                move_rate = float(input('Ingrese el precio por segundo en movimiento (ej. 0.05): '))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
                logger.warning("Entrada no válida al configurar tarifas")
    else:
        print(f'Usando tarifas predeterminadas: detenido = ${stop_rate}/s, en movimiento = ${move_rate}/s')
        logger.info("Usando tarifas por defecto")

    taxi = Taximetro(stop_rate, move_rate)
    logger.debug("Instancia de Taximetro creada")

    print('\nComandos: start, stop, move, finish, exit')

    while True:
        command = input('> ').strip().lower()
        logger.debug(f"Comando recibido: {command}")

        if command == 'start':
            if taxi.trip_active:
                print('Error: El viaje ya ha iniciado.')
                logger.warning("Intento de iniciar viaje ya activo")
                continue
            taxi.start_trip()
            print('El viaje ha comenzado.')
            logger.info("Viaje iniciado")

        elif command in ('stop', 'move'):
            if not taxi.trip_active:
                print('Error: El viaje no ha iniciado.')
                logger.warning(f"Intento de cambiar a '{command}' sin viaje activo")
                continue
            new_state = 'stop' if command == 'stop' else 'moving'
            taxi.change_state(new_state)
            print(f'El estado cambió a: {new_state}')
            logger.info(f"Estado cambiado a: {new_state}")

        elif command == 'finish':
            if not taxi.trip_active:
                print('Error: No hay un viaje en curso.')
                logger.warning("Intento de finalizar un viaje no iniciado")
                continue
            summary = taxi.stop_trip()
            stop_time = summary["stop_time"]
            moving_time = summary["moving_time"]
            total_fare = summary["fare"]
            print(f'Tiempo detenido: {stop_time:.1f} segundos')
            print(f'Tiempo en movimiento: {moving_time:.1f} segundos')
            print(f'Total a pagar: ${total_fare:.2f}')

        elif command == 'exit':
            print('Hasta luego, amigo.')
            logger.info("Aplicación finalizada por el usuario")
            break

        else:
            print('Comando no reconocido. Usa: start, stop, move, finish, exit.')
            logger.warning(f"Comando no reconocido: {command}")

if __name__ == '__main__':
    taximetro()
