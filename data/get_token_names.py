from web3 import Web3
import json
import csv
import requests
from util import decode_abi_string


ARCHIVE_NODE_URL = 'http://localhost:8545'
data_file = '/data/latest-data/uniswapv2_top_tokens.csv'
outfilename = 'token_names.csv'


def get_token_symbol( token_addr):
    data = {}
    data['jsonrpc'] = '2.0'
    data['method'] = 'eth_call'
    function_selector = "0x95d89b41000000000000000000000000"
    calldata = function_selector
    data["params"] = [{"to": token_addr, "data":calldata}, "latest"]
    # now = datetime.now()
    data['id'] = 1
    r = requests.post(ARCHIVE_NODE_URL, json=data)
    response = json.loads(r.content)
    if 'result' not in response:
        # print(response)
        return  ''
    return decode_abi_string(response["result"])

fout = open(outfilename, 'w')
fout.write('token_address,token_symbol\n')
seen = set()
with open(data_file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(spamreader)
    for row in spamreader:
        # print(row)
        token_address = Web3.toChecksumAddress(row[1])
        if int(token_address, 16) == 0 or token_address in seen :
            continue
        seen.add(token_address)
        token_symbol = get_token_symbol(token_address)
        fout.write('{},{}\n'.format(token_address.lower(),token_symbol))
