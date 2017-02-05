# Mgmt

### History

The name of this tool has been taken from [mgmt](https://github.com/purpleidea/mgmt)

The host configuration syntax is mostly copied from ansible (or maybe because it's yaml I think I copied it from ansible)

### Usage
`mgmt -h` gives you a complete list of options.

By default the only things you would need for is to specify a **--host-config \<filename>** to tell mgmt what action perform on the server.

Depending the kind of installation that you went for (global or local) you might want to adjust the **--host-config-directory** variable.

### Requirements
In order to use **mgmt** you need on your system Python >=3.4.

So far the only external requirements is pyyaml and jinja2.

Either run `pip install -r requirements.txt` or use the package provided by your distribution (on *Debian / Ubunty* system `apt-get install python-yaml python-jinja2` should be enough)

For convenience on Debian/Ubuntu system a ``bootstrap.sh`` script has been added.

### File configuration
The configuration for a host is following the yaml syntax. What is really necessary is to define a group of ``actions`` (list). Every action requires at the least a container called ``name`` that list at least one action.

N.B. Actions have to be available in the operation_registry at parse time.
#### Action params:

action params are directly coupled to the function we want to call. Unnecessary action might be ignored.

##### Example:
Given the function

``func(paramA, paramB, paramC='something')``

The corrisponding necessary action definition should look like:

```
actions:
	- description: This is a very important action
	  name:
	    func:
		   paramA: "something"
		   paramB: "something"
```


#### Full example:
```
---
host: localhost
actions:
  - description: 'Copying index.php to apache document root'
    name:
      copy:
        source: '/tmp/index.php'
        destination: '/var/www/html'
  - description: 'Copying from Template(a) to B'
    name:
      copy_from_template:
        source: '/tmp/source_template'
        destination: '/tmp/destination_template'
        variables: {Host: localhost, Name: test}
        mode: '0123'
  - description: 'Install apache'
    name:
      install_package:
        packagename: 'apache2'
        cmd_after: 'rm /var/www/html/index.html'
  - description: 'Install php'
    name:
      install_package:
        packagename: 'php5 libapache2-mod-php5'
...
```

