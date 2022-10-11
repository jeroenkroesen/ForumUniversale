#!/bin/bash
cd ~/02-local/dev/artumis
source env/bin/activate
cd src
export FLASK_APP=artumis
export FLASK_ENV=development
flask run
