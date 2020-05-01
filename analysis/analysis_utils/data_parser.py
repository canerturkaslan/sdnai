import hashlib
import ast
async def parse_array_object(data):
    a = data['actions']
    b = str(a)
    s = b.replace("[", "{")
    c = s.replace("']", "'}")
    d = c.replace(":", "':'")
    res = ast.literal_eval(d)
    data['actions'] = res
    return data

def hash_object_id(data):
    object_id = hashlib.blake2b(digest_size=12)
    if "duration_sec" and "duration_nsec" in data:
        if data['match'].__len__() is 0:
            del data["match"]
        else:
            data['dl_dest'] = data['match']['dl_dst']
            data['dl_source'] = data['match']['dl_src']
            data['in_port'] = data['match']['in_port']
            del data["match"]
        del data["duration_sec"]
        del data["duration_nsec"]
        data['actions'] = data['actions']['OUTPUT']

    for key, value in data.items():
        if type(value) is not int:
            object_id.update(value.encode('utf-8'))
        else:
            object_id.update(str(value).encode("utf-8"))
    return str(object_id.hexdigest())

def clean_port_data(desc_data,port_data):
    del desc_data['state']
    del desc_data['config']
    del desc_data['peer']
    del desc_data['advertised']
    del desc_data['supported']
    del desc_data['max_speed']
    del desc_data['port_no']
    port_data['name'] = desc_data['name']
    port_data['mac_addr'] = desc_data['hw_addr']
    port_data['curr'] = desc_data['curr']
    port_data['curr_speed'] = desc_data['curr_speed']
    return port_data