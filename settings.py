from web3 import Web3, exceptions
from web3.middleware import construct_sign_and_send_raw_middleware
import logging
import secrets


logging.basicConfig(format='%(asctime)s: %(levelname)s %(message)s', level=logging.INFO)

CHAIN_ID=137
RPC_URL="https://rpc-mainnet.matic.network"
w3 = Web3(Web3.HTTPProvider(RPC_URL))
w3.middleware_onion.add(construct_sign_and_send_raw_middleware(secrets.PRIVATE_KEY))
w3.eth.default_account = secrets.MY_ADDRESS


