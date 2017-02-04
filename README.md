# Mgmt

### History
There are only two problem in computer science:


1. Invalidate caches
2. Name things
3. Being off by one error

I dont want to care about caches today so I decided to copy the name for this application from [mgmt](https://github.com/purpleidea/mgmt)

The host configuration syntax is mostly copied from ansible (or maybe because is yaml I think I copied it from ansible.. fairly sure somebody else before them and me got the idea)
### Feature

### Usage
`mgmt -h` gives you a complete list of options.

By default the only things you would need for is to specify a **--host-config \<filename>** to tell mgmt what action perform on the server.

Depending the kind of installation that you went for (global or local) you might want to adjust the **--host-config-directory** variable.

### Requirements
In order to use mgmt you need on your system Python3. Despite using some Python3 specific feature (inspect.signature) in general there is no reason to not switch to Python3 if possible.

So far the only external requirements is pyyaml and jinja2.

Either run `pip install -r requirements.txt` or use the package provided by your distribution (on *Debian / Ubunty* system `apt-get install python-yaml python-jinja2` should be enough)

