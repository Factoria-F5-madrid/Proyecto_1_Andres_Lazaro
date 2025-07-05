from core import Taximeter

def taximeter():
    print('Bienvenido al taxímetro con Python de F5')
    
    # Preguntar si quiere configurar tarifas manuales
    stop_rate = 0.02
    move_rate = 0.05
    choice = input('¿Deseas configurar los precios manualmente? (s/n): ').strip().lower()

    if choice == 's':
        while True:
            try:
                stop_rate = float(input('Ingrese el precio por segundo detenido (ej. 0.02): '))
                move_rate = float(input('Ingrese el precio por segundo en movimiento (ej. 0.05): '))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    else:
        print(f'Usando tarifas predeterminadas: detenido = ${stop_rate}/s, en movimiento = ${move_rate}/s')

    taxi = Taximeter(stop_rate, move_rate)

    print('\nComandos: start, stop, move, finish, exit')

    while True:
        command = input('> ').strip().lower()

        if command == 'start':
            if taxi.trip_active:
                print('Error: El viaje ya ha iniciado.')
                continue
            taxi.start()
            print('El viaje ha comenzado.')
        
        elif command in ('stop', 'move'):
            if not taxi.trip_active:
                print('Error: El viaje no ha iniciado.')
                continue
            new_state = 'stop' if command == 'stop' else 'moving'
            taxi.change_state(new_state)
            print(f'El estado cambió a: {new_state}')
        
        elif command == 'finish':
            if not taxi.trip_active:
                print('Error: No hay un viaje en curso.')
                continue
            total_fare = taxi.finish()
            stop_time, moving_time, _ = taxi.get_summary()
            print(f'Tiempo detenido: {stop_time:.1f} segundos')
            print(f'Tiempo en movimiento: {moving_time:.1f} segundos')
            print(f'Total a pagar: ${total_fare:.2f}')
        
        elif command == 'exit':
            print('Hasta luego, amigo.')
            break
        
        else:
            print('Comando no reconocido. Usa: start, stop, move, finish, exit.')

if __name__ == '__main__':
    taximeter()
