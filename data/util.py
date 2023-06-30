def decode_abi_string(hex_string):
    try:
        offset = int(hex_string[:66], 16)
        length = int(hex_string[2+offset*2:2+offset*2+64], 16)
        ret = bytes.fromhex(hex_string[2+offset*2+64: 2+offset*2+64+2*length]).decode('utf-8')
        return ret
    except:
        try:
            return bytes.fromhex(hex_string[2:].strip('0')).decode('utf-8')
        except:
            return ''