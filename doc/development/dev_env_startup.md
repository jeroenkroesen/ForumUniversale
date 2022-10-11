# Starting up the dev environment

## Set directories
```bash
appdir=~/02-local/dev/ForumUniversale
vagrantdir=~/02-local/dev/learning/database_server_test/vagrant-ubuntu
sassdir=~/02-local/dev/ForumUniversale/src/sass
cssdir=~/02-local/dev/ForumUniversale/src/app/static/css
```

## database server
```bash
cd $vagrantdir
vagrant up
ssh -L 3306:localhost:3306 vagrant@192.168.56.5
```
vagrant default password is: `vagrant`

## SASS compile
This is dev compile only. Enable minifying for production build.
```bash
sass --watch $sassdir:$cssdir
```

## Flask dev server
```bash
cd $appdir
source env/bin/activate
cd src
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

Flask will be at [http://localhost:5000](http://localhost:5000)
