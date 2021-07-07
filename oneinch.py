import requests
from settings import w3, logging, CHAIN_ID
from secrets import MY_ADDRESS
from web3 import Web3


ONEINCH_API= "https://api.1inch.exchange/v3.0/%s/" % CHAIN_ID



def quote(from_token, to_token, amount):
	URL = ONEINCH_API + 'quote'
	query = { 
		'fromTokenAddress': from_token.address,
		'toTokenAddress': to_token.address,
		'amount': amount
	}
	logging.debug("Getting quote: %s", query)
	r = requests.get(URL, query)
	if not r.ok:
		r.raise_for_status()
	response = int(r.json()['toTokenAmount'])
	logging.info("Quoted exchange rate at %s", response)
	return response

def swap(from_token, to_token, amount, gas=2, slippage=5):
	URL = ONEINCH_API + 'swap'
	query = { 
		'fromTokenAddress': from_token.address,
		'toTokenAddress': to_token.address,
		'amount': amount,  
		'fromAddress': MY_ADDRESS,
		'slippage': slippage
	}
	r = requests.get(URL, query)
	raw_tx = r.json()['tx']
	raw_tx['value']=int(raw_tx['value'])
	raw_tx['to']=Web3.toChecksumAddress(raw_tx['to'])
	raw_tx['gasPrice']=w3.toWei(gas, 'gwei')
	logging.debug(raw_tx)

	return w3.eth.wait_for_transaction_receipt(w3.eth.send_transaction(raw_tx), poll_latency=1)

def hr_quote(from_token, to_token):
	amount = quote(from_token, to_token, 10 ** from_token.decimals)
	return to_token.hr_amount(amount)


