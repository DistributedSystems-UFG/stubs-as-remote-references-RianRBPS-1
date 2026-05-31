# Maquina 2 (Client 1) - executar por ultimo
# Uso: SERVER_HOST=<ip-servidor> CLIENT2_HOST=<ip-client2> python run_client1.py
from time     import sleep     #-
from client   import Client    #-
from dbclient import DBClient  #-
from constRPC import *         #-

if __name__ == '__main__':              #-
  c1   = Client(PORTC1)                # cria client #-
  dbC1 = DBClient(HOSTS, PORTS)       # cria stub apontando para o servidor #-
  dbC1.create()                        # cria lista no servidor #-
  dbC1.appendData('Client 1')         # adiciona dado #-
  print(f'Stub created (listID={dbC1.listID}), sending to Client2...') #-
  sleep(2)                             # aguarda client2 estar pronto #-
  c1.sendTo(HOSTC2, PORTC2, dbC1)    # passa a referencia remota para client2 #-
