# Código de https://imasters.com.br/back-end/utilizando-a-api-watchdog-em-python

import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from compile import compile_file
 
class ManipuladorDeEventos(FileSystemEventHandler):
    def catch_all_handler(self, event):
        pass
 
    def on_modified(self, event):
        if not event.is_directory:
            print(event.src_path + " modificado.")
            if len(event.src_path.split('.')) == 1:
                compile_file(event.src_path)
        self.catch_all_handler(event)
 
eventos = ManipuladorDeEventos()
observador = Observer()
observador.schedule(eventos, "notes", recursive=True)
observador.start()
 
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observador.unschedule(eventos)
    observador.stop()
observador.join()
