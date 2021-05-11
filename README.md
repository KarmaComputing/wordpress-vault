# Wordpress Vault - stop wordpress from getting hacked

## Why is this useful?

Wordpress core without plugins is pretty secure.
The plugin ecosystem sadly is not.

## How does this work?

By making the filesystem immutable, many common Wordpress
plugin hacks can be mitigated.

1. Automatically lock the Wordpress installation (making it immutable)
2. Unlock when updates are performed
3. Automate all the above

## I don't/can't do this myself, can I pay you to do it?

Yes. See [Secure Wordpress](https://secure-wordpress.karmacomputing.co.uk)

## Why not just fix the plugins?

Consumers of Wordpress, sometimes trying to save money from building a more robust solution- will instead assemble a WordPress website themselves by combining plugins. 

This creates a security nightmare, but the problem is real and, it's very hard to take the candy away when the economics work in this way.

### Install

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```
