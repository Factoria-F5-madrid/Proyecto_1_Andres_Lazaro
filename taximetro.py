import time 

def calculate_fare(seconds_stopped,seconds_moving):
    fare = seconds_stopped * 0.02 + seconds_moving * 0.05
    return fare

def taximeter():
    print('bienvenido al taximetro con python de F5')
    print(' comandos: Start,Stop,Move,finish,exit')
    trip_active = False
    start_time = 0
    stop_time = 0
    moving_time = 0 
    state = None
    state_start_time = 0
    while True:
        # Get the current state of the taximeter
        command = input('> ').strip().lower()
        if command == 'start':
            if trip_active: 
                print('error: El viaje ha iniciado ')
                continue
            trip_active = True
            start_time = time.time()
            stop_time = 0
            moving_time = 0
            state = 'stop'
            state_start_time = time.time()
            print('El tiempo ha iniciado ')
        elif command  in ('stop,move '):
            if not trip_active:
                print('error: El viaje no ha iniciado ')
                continue
            duration = time.time() - state_start_time
            if state ==  'stop':
                stop_time += duration #suma el tiempo detenido      
            else :
                moving_time += duration # suma el tiempo en movimiento
            
            state = 'stop' if command == 'stop' else 'moving' # se define el movimiento en el operador ternario 
            state_start_time = time.time()
            print(f'el estado cambio a : {state}')
        elif command == 'finish':
            if not trip_active:
                print('error: El viaje ha terminado ')
                continue 
            duration = time.time() - state_start_time
            if state == 'stop':
                stop_time += duration #suma el tiempo detenido
            else: 
                moving_time += duration #suma el tiempo en movimiento 

            total_fare = calculate_fare(stop_time, moving_time)
            print(f'tiempo dentenido : {stop_time: .1f}')
            print(f'tiempo en movimiento : {moving_time: .1f}')
            print(f'total a pagar : {total_fare: .1f}')
            trip_active = False
            state = None
        elif command == 'exit':
            print('Hasta luego amigo')
            break


if __name__ == '__main__':
    taximeter()



# Falta de conexión con la API: revisar integración con frameworks como Streamlit, Flask o Django
# La lógica general está bien implementada y la aplicación funciona correctamente
# Evaluar si se pueden cumplir más requerimientos funcionales
# Requerimiento sugerido: añadir campo de precio en movimiento o en espera de forma manual
# Pendiente: montar el frontend para visualización y control de datos
