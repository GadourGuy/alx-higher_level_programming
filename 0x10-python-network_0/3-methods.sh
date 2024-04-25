#!/bin/bash
# displaies available requests.
curl -sLI "$1"  | grep "Allow" | cut -d " " -f 2-
