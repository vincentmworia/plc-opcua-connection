from opcua import  *
from time import sleep


def establish_opc_conn():
    url = "opc.tcp://192.168.1.1:4840"
    client_conn = Client(url)

    while True:
        try:
            client_conn.connect()
            break
        except: 
            print('Reconnecting after 5 secs...')
            sleep(5)

    client_conn.get_root_node()  
    return client_conn



def read_input_value(client_fn, node_id):
    client_node = Client.get_node(client_fn, node_id)  # get node
    client_node_value = client_node.get_value()  # read node value
    return client_node_value


def write_value_bool(node_id, value, client_fn):
    client_node = client_fn.get_node(node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(
        client_node_value, ua.VariantType.Boolean))
    client_node.set_value(client_node_dv)


def write_value_int(node_id, value, client_fn):
    client_node = Client.get_node(client_fn, node_id)  # get node
    client_node_value = value
    client_node_dv = ua.DataValue(ua.Variant(
        client_node_value, ua.VariantType.Int16))
    client_node.set_value(client_node_dv)


plc_client_1 = establish_opc_conn()
i = 0
while True:
    write_value_int('ns=3;s="python_data"."workpiece_position"', i, plc_client_1)
    i+=1
    sleep(1)
    print(i)
    if(i==300):
        break
