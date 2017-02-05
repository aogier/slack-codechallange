#!/usr/bin/env bash

set -e

for package in "python3-jinja2 python3-yaml"; do
    sudo apt-get install -y $package
done


