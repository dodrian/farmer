from web3 import Web3
import logging


logging.basicConfig(format='%(asctime)s:%(message)s', level=logging.INFO)

CHAIN_ID=137
RPC_URL="https://rpc-mainnet.matic.network"
w3 = Web3(Web3.HTTPProvider(RPC_URL))


