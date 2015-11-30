# Django-CMS-Learning

# Ignore vagrant and implement equivalent ubuntu in case you use ubuntu

This uses Gale's Unchained framework for use with Django CMS.
###Daily Commands
####1. Login to your Vagrant machine
	
	vagrant ssh
	
###2. If logging in did not work you need to start your Vagrant machine:
	
	vagrant up
	
###3. Login to the virtualenv
	
	workon avalon
	cd avalon
	
###4. Run pip

	pip install -r requirements.txt

###5. Migrate the database

	python manage.py migrate

###Vagrant Installation Instructions
####1. Github access to Hain-Avalon


####2. Install vagrant 

	https://www.vagrantup.com/downloads.html


####3. Install VirtualBox

	https://www.virtualbox.org/wiki/Downloads


####4. Fork the Git repo

####5. Clone repo:
	
	git clone https://github.com/<user>/Hain-Avalon.git
	


####6. Open your project directory
   
      cd <git hub directory>
      

####7. Start vagrant

	vagrant up


####8. Login to vagrant

	vagrant ssh


####9. Login to database console


	sudo su postgres
	psql

####10. Create database:

	create role haineb with login superuser password 'haineb';
	create database haineb with owner haineb;

####11. Exit postgres console

	\q
	exit


####12. Make a virtual environment

	mkvirtualenv avalon

####13. work on virtual environment

	workon avalon
	cd avalon


####14. Run pip

	pip install -r requirements.txt

	
####15. Migrate the database

	python manage.py migrate


####16. Create a superuser to access the CMS admin console:

	python manage.py createsuperuser

Select admin for the user name and password
You can leave the email field blank

####17. Start the Django server:

	python manage.py runserver 0.0.0.0:8000


####18. Open the site in your browser:

	localhost:8000






###Installation Instructions

####1. System Setup


a) The development and deployment of this project is to be done on:

	- Ubuntu 14.04LTS


b) The following system libraries are dependancies to several other libraries/frameworks we use, you can install them by running the following on a command-line:

```
$ sudo apt-get install libffi-dev libssl-dev libxml2-dev libxslt1-dev libreadline6 libreadline6-dev python-dev python-setuptools

```

c) We use the 'Pillow' library for image manipulation, although the 
library itself will be installed via requirements.txt later on, these dependancies are essential for its successful compilation/installation:

```
$ sudo apt-get install libtiff5-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk libjpeg8-dev zlib1g-dev libjpeg-dev libfreetype6 libfreetype6-dev zlib1g-dev pngquant
```

d) Fork and Clone this repository to a directory on your local machine. 

```
git clone https://github.com/<YOUR-GITHUB-USERNAME>/Hain-Avalon.git
```

######CSS/Styling Related

e) We use Less for CSS, and are using Gulp for its compilation, it also watches the less files for changes if you ask it to. 

So first, we'll install NPM followed by Gulp, at the project's root directory:

```
$ sudo apt-get install npm
$ sudo ln -s /usr/bin/nodejs /usr/bin/node
$ sudo npm install -g gulp
$ sudo npm install gulp
$ sudo npm install gulp-less gulp-minify-css gulp-rename gulp-plumber
```

Once installed, then you can just say:

```
$ gulp
```
This will compile all the less files to a single 'apps.css' in the 'static/css' folder.

But, for continuous CSS development, on a seperate terminal run:

```
$ gulp watch
```
This will run a gulp process that keeps watching the less files and run compilation, on change of less files. You can change the less file and on Save of any '.less' file you'll see that the 'apps.less' has been compiled.

Also, as a practice, please ensure to check-in the latest generated CSS.



####2. Database Setup

Note: For dev, we are currently using SQLite.

The following command will install PostgreSQL on Ubuntu 14.04LTS:

```
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
```

a) Change the default postgres user creds:

```
sudo passwd postgres
SET A NEW PASSWORD - gale

su postgres
ENTER YOUR PASSWORD

psql
alter user postgres password 'gale';

\q
exit
```

b) Create an application DB User:

```
sudo adduser hainavalon
enter password as hainavalon

su postgres
psql
CREATE USER hainavalon WITH PASSWORD 'hainavalon';

CREATE DATABASE hainavalon;

GRANT ALL PRIVILEGES ON DATABASE hainavalon to hainavalon;
```

####3. ElasticSearch Setup

Note: This section is needed if you are planning to access/dev on the 'Search' page.

a) Make sure Java is installed, pref: Open JDK 7

```
$ java -version
```

If its not installed:

```
$ sudo apt-get install openjdk-7-jre-headless
```
If the installed version of Open JDK is < "1.7.0_79":

```
sudo apt-get install --only-upgrade openjdk-7-jdk
```

Once installed/upgraded; verify the version is  “1.7.0_79” (or higher).


b) Install ElasticSearch:

```
wget -qO - https://packages.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

echo "deb http://packages.elastic.co/elasticsearch/1.7/debian stable main" | sudo tee -a /etc/apt/sources.list.d/elasticsearch-1.7.list

sudo apt-get update && sudo apt-get install elasticsearch 1.7.2
sudo update-rc.d elasticsearch defaults 95 10

sudo /etc/init.d/elasticsearch start
```

c) Once your database models are populated, for e.g., you add relevant products and articles lets say, then to have them indexed and show up in search results just run the following command:

```
python manage.py rebuild_index --noinput
```


####4. Dev Setup

###### 1. Once your repo is cloned, create a virtual environment.

a) Install pip, virtualenv and wrapper if its not already installed.

```
$ sudo apt-get install python-pip
$ sudo pip install virtualenv
$ sudo pip install virtualenvwrapper
```

The follwing is needed to get the virtualwrapper going:

1st, ensure you're installing with sudo:

```
sudo pip install virtualenvwrapper
```

2nd, append the following lines to your .bashrc file (with nano ~/.bashrc):

```
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
```

Save the file and exit.

3rd, reload your profile

```
$ source ~/.bashrc
```

b) Create a virtualenv for this project,

```
$ mkvirtualenv avalon
```
This will create and activate a virtual environment named 'avalon'.

c) To deactivate:

```
$ deactivate

```

d) To activate again:

```
$ workon avalon
```

###### 2. Install necessary Python libraries.


a) To run this project you need to install all the python dependencies and libraries.

```
$ pip install -r requirements.txt
```

###### 3. Running the project.

a) Make migrations and Migrate DB,

```
$ python manage.py makemigrations
$ python manage.py migrate
```

b) Create a superuser

```
$ python manage.py createsuperuser
```
Enter username/password as dev/dev and you can leave the email empty. (its optional)


c) Once all the requirements are installed, you can simply run:

```
$ python manage.py runserver
```

or, for debug to see logs on crash

```
$ python manage.py runserver_plus
```


or for shell to debug with ipdb

```
$ python manage.py shell
```

d) For adding plug-ins, all available plugins will be available in the placeholder sections. 

e) To add App Hooks, add a normal page, then in the "Advanced Settings", under the App Hooks section select the desired App hook e.g: "Avalon Products Hook". For products you'll need to login to admin using creds created in step 'b', and add necessary Categories, Sub-Categories and Products.
