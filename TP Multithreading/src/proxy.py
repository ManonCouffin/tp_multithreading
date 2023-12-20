from http.server import BaseHTTPRequestHandler, HTTPServer
from manager import QueueClient

class Proxy(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.client = QueueClient()
        super().__init__(*args, **kwargs)

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Récupère une tâche de la file de tâches
        task = self.client.tasks.get()
        # Ajoute le résultat à la file de résultats
        self.client.results.put((task.identifier, task.time))

        # Envoie la représentation JSON du résultat
        self.wfile.write(bytes(task.to_json(), "utf-8"))

def run(server_class=HTTPServer, handler_class=Proxy):
    server_address = ("", 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == "__main__":
    run()
