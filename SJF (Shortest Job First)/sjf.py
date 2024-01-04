import os
import psutil
from tabulate import tabulate

def get_running_processes():
    processes = []

    for proc in psutil.process_iter(['pid', 'name', 'create_time']):
        try:
            pinfo = proc.info
            processes.append({
                'pid': pinfo['pid'],
                'name': pinfo['name'],
                'create_time': pinfo['create_time']
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return sorted(processes, key=lambda x: x['create_time'])

def sjf_scheduler():
    running_processes = get_running_processes()

    # Ordenar por tiempo de creación (corto a largo)
    running_processes.sort(key=lambda x: x['create_time'])

    print("Procesos en ejecución (SJF):")
    print(tabulate(running_processes, headers="keys", tablefmt="fancy_grid"))

if __name__ == "__main__":
    try:
        while True:
            os.system('clear')  # Limpiar la consola (Linux)
            sjf_scheduler()
            time.sleep(1)  # Actualizar cada segundo
    except KeyboardInterrupt:
        print("\nVisualización terminada.")
