# Pre-requisites
Run archive node, serving Ethereum HTTP JSON-RPC on port 8545

# Simulation Clients
`cd eth_clients/hardhat`
`bash launch_hardhats.sh`

`eth_clients/hardhat` directory has detailed instructions on managing sim clients

Sample optimization command:
`python3 optimize.py -t <test_transactions> -d <test_domain> -v`

If you want to run simulation standalone, sample command:
`python3 simulate_client.py -f <concrete_transactions>`

# Example files
concrete_transactions : `tests/optimised`
test_transactions : `tests/problem`
test_domain : `tests/multiple_tokens_domain`
