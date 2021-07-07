# farmer

Python code for interacting with common Polygon tokens, 1inch, and more...

## Installation and running

Setup the environment with `pipenv install`.

Load the environment with `pipenv shell` or `pipenv run python3`

## Protecting your private key

It's recommended to install [secret-stopper](https://github.com/dodrian/secret-stopper) to prevent you from accidently commiting your private key (or doxxing your public address).  This will replace any pre or post commits you may have already installed

```
curl https://raw.githubusercontent.com/dodrian/secret-stopper/master/post-commit > .git/hooks/post-commit
curl https://raw.githubusercontent.com/dodrian/secret-stopper/master/pre-commit > .git/hooks/pre-commit
chmod u+x .git/hooks/*-commit
```

## Usage

### Tokens

Common Polygon are defined in the `tokens` module.

Lookup token balance and helper methods:

```
>>> tokens.USDC.balanceOf(MY_ADDRESS)
179050000
>>> tokens.USDC.hr_balanceOf(MY_ADDRESS)
179.05
>>> tokens.WETH.to_wei(1.2)
1200000000000000000
>>> tokens.WETH.hr_amount(_)
1.2
```

The same can be done for MATIC (native currency):

```
>>> tokens.MATIC.hr_balanceOf(MY_ADDRESS)
30.394
```

Aave tokens are also provided:
```
>>> tokens.aave.USDC.balanceOf(MY_ADDRESS)
0

```

### 1inch

Support is provided for getting quotes and making swaps via [1inch](https://app.1inch.io):

```
>>> oneinch.quote(tokens.WETH, tokens.USDC, 1000000000000000000)
2339289225
>>> oneinch.hr_quote(tokens.WETH, tokens.USDC)
2338.046491
>>> oneinch.swap(tokens.MATIC, tokens.WETH, tokens.MATIC.to_wei(1.5)) 
[...]
```
Swaps will block execution until the transaction is confirmed, or raise an exception if too much time passes.