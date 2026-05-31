# Maquina 3 (Client 2) - executar antes do client1
# Uso: SERVER_HOST=<ip-servidor> CLIENT1_HOST=<ip-client1> python run_client2.py
import pickle                  #-
from client   import Client    #-
from dbclient import DBClient  #-
from constRPC import *         #-

if __name__ == '__main__':                   #-
  c2   = Client(PORTC2)                      # cria client; escuta na porta #-
  print(f'Client2 waiting on port {PORTC2}') #-
  data = c2.recvAny()                        # bloqueia ate receber o stub #-
  dbC2 = pickle.loads(data)                  # desserializa a referencia remota #-
  dbC2.appendData('Client 2')               # usa o stub para acessar lista no servidor #-
  print(dbC2.getValue())                     #-
  c2.sendTo(HOSTS, PORTS, [STOP])           # sinaliza servidor para parar #-
