# Maquina 1 (Servidor) - executar primeiro
# Uso: python run_server.py
from server   import Server   #-
from constRPC import PORTS    #-

if __name__ == '__main__':    #-
  server = Server(PORTS)      #-
  print(f'Server listening on port {PORTS}') #-
  server.run()                #-
