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

def hash_object_id(hash_data):
    data=hash_data
    set_hash_id=''
    object_id = hashlib.md5()
    if "duration_sec" and "duration_nsec" in hash_data:
        del hash_data["duration_sec"]
        del hash_data["duration_nsec"]
        hash_data['actions'] = hash_data['actions']['OUTPUT']
        hash_data['dl_dst'] = hash_data['match']['dl_dst']
        hash_data['dl_src'] = hash_data['match']['dl_src']
        hash_data['in_port'] = hash_data['match']['in_port']
    if 'match' in hash_data:
        del hash_data["match"]
    for key, value in hash_data.items():
        # set_hash_id = set_hash_id + str(v)
        if type(value) is not int:
            object_id.update(value.encode('utf-8'))
        else:

            object_id.update(str(value).encode("utf-8"))
    return (str(object_id.hexdigest()))
