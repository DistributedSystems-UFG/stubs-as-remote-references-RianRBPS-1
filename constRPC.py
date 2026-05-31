import os

OK       = '1'
ADD      = '2'
APPEND   = '3'
GETVALUE = '4'
CREATE   = '5'
STOP     = '6'
HOSTS    = os.environ.get('SERVER_HOST',  '')   # IP da maquina do servidor
PORTS    = 50004
PORTC1   = 50053
PORTC2   = 50054
HOSTC1   = os.environ.get('CLIENT1_HOST', '')   # IP da maquina do client1
HOSTC2   = os.environ.get('CLIENT2_HOST', '')   # IP da maquina do client2
