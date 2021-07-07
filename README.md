# farmer

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
