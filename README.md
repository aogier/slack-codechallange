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
---
host: localhost
actions:
  - meta:
      description:
      dependencies:
    name: test
    action_name:
      test1:
        paramA: 'paramA'
        paramB: 'paramB'
...
```


#### Full example:
```
---
host: localhost
actions:
  - name: install_index_php
    meta:
     dependencies: ['install_apache2']
     description: 'Copying index.php to apache document root'
    action_name:
      copy:
        source: 'data/index.php'
        destination: '/var/www/html'
  - name: 'install_apache2'
    meta:
      description: 'Install apache'
    action_name:
      install_package:
        packagename: 'apache2'
        cmd_after: 'rm -f /var/www/html/index.html'
  - name: install_php5
    meta:
      description: 'Install php'
      dependecies: ['install_apache2']
    action_name:
      install_package:
        packagename: 'php5 libapache2-mod-php5'
...
```
### Test

`cd test && python parser_test.py`