#!/bin/bash

# default command
COMMAND="poetry export --without-hashes -f requirements.txt -o requirements.txt"

# check for the --with argument
if [[ "$1" == "--with" && -n "$2" ]]; then
  COMMAND+=" --with $2"
fi

# run the constructed command
eval $COMMAND
