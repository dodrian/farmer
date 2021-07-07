import requests
from settings import w3, logging, CHAIN_ID


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

def hr_quote(from_token, to_token):
	amount = quote(from_token, to_token, 10 ** from_token.decimals)
	hr = amount / (10 ** to_token.decimals)
	return hr

