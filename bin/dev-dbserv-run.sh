#!/bin/bash
cd ~/02-local/dev/learning/database_server_test/vagrant-ubuntu
vagrant up
ssh -L 3306:localhost:3306 vagrant@192.168.56.5
