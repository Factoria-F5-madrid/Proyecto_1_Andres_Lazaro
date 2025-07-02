
import time

def calculate_fare(seconds_stopped, seconds_moving, stop_rate, move_rate):
    fare = seconds_stopped * stop_rate + seconds_moving * move_rate
    return fare

def taximeter():
      # Preguntar si usar tarifas por defecto o personalizadas
    stop_rate = 0.02
    move_rate = 0.05
    print('Bienvenido al taxímetro con Python de F5')
    print('\n¿Deseas configurar los precios manualmente o usar los predeterminados?')
    choice = input('Escribe "s" para configurar manualmente o "n" para usar predeterminados: ').strip().lower()

    if choice == 's':
        while True:
            try:
                stop_rate = float(input('Ingrese el precio por segundo detenido (ej. 0.02): '))
                move_rate = float(input('Ingrese el precio por segundo en movimiento (ej. 0.05): '))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    else:
        print(f'Se usarán las tarifas predeterminadas: detenido = ${stop_rate}/s, en movimiento = ${move_rate}/s')

    print('\nComandos disponibles: start, stop, move, finish, exit')

    trip_active = False
    start_time = 0
    stop_time = 0
    moving_time = 0
    state = None
    state_start_time = 0

    while True:
        command = input('> ').strip().lower()
        
        if command == 'start':
            if trip_active: 
                print('Error: El viaje ya ha iniciado.')
                continue
            trip_active = True
            start_time = time.time()
            stop_time = 0
            moving_time = 0
            state = 'stop'
            state_start_time = time.time()
            print('El viaje ha comenzado.')
        
        elif command in ('stop', 'move'):
            if not trip_active:
                print('Error: El viaje no ha iniciado.')
                continue
            duration = time.time() - state_start_time
            if state == 'stop':
                stop_time += duration
            elif state == 'moving':
                moving_time += duration
            
            state = 'stop' if command == 'stop' else 'moving'
            state_start_time = time.time()
            print(f'El estado cambió a: {state}')
        
        elif command == 'finish':
            if not trip_active:
                print('Error: No hay un viaje en curso.')
                continue
            duration = time.time() - state_start_time
            if state == 'stop':
                stop_time += duration
            elif state == 'moving':
                moving_time += duration

            total_fare = calculate_fare(stop_time, moving_time, stop_rate, move_rate)
            print(f'Tiempo detenido: {stop_time:.1f} segundos')
            print(f'Tiempo en movimiento: {moving_time:.1f} segundos')
            print(f'Total a pagar: ${total_fare:.2f}')
            trip_active = False
            state = None
        
        elif command == 'exit':
            print('Hasta luego, amigo.')
            break
        else:
            print('Comando no reconocido. Usa: start, stop, move, finish, exit.')

if __name__ == '__main__':
    taximeter()

