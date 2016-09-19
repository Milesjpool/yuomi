#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
TARG="/var/www/yuomi"

echo "Setting up yuomi in /var/www..."
if [ ! -L $TARG ]; then
  ln -s $DIR/yuomi_website/ $TARG
fi

echo "Setup complete"
