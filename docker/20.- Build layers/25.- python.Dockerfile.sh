#!/bin/bash
set -e


# Upgrade system
PACKAGES=()
PACKAGES+=(ServiceDiscovery)

# Install all
pip3 install ${PACKAGES[@]}
