import os
import psutil
from tabulate import tabulate

def Procesos():
    processes = []

    for proc in psutil.process_iter(['pid', 'nombre', 'create_time']):
        try:
            pinfo = proc.info
            processes.append({
                'pid': pinfo['pid'],
                'nombre': pinfo['nombre'],
                'create_time': pinfo['create_time']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return sorted(processes, key=lambda x: x['create_time'])

def sjf_planificador():
    procesos_en_ejecucion = Procesos()

    # Ordenar por tiempo de creación (corto a largo)
    procesos_en_ejecucion.sort(key=lambda x: x['create_time'])

    print("Procesos en ejecución (SJF):")
    print(tabulate(procesos_en_ejecucion, headers="keys", tablefmt="fancy_grid"))

if __nombre__ == "__main__":
    try:
        while True:
            os.system('clear')  # Limpiar la consola (Linux)
            sjf_planificador()
            time.sleep(1)  # Actualizar cada segundo
    except KeyboardInterrupt:
        print("\nVisualización terminada.")

