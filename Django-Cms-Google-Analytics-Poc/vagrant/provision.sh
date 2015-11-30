#!/bin/bash

#-------------------------------------------------------------
# Configuration
#-------------------------------------------------------------

PROJECT_NAME="DNN"
PROJECT_HOME="/vagrant"
USER_HOME="/home/vagrant"
OS_USER="vagrant"

DB_NAME="dnncms"
DB_USER="dnncms"
DB_PASS="dnncms"

ADMIN_USER="root"
ADMIN_PASS="root"
ADMIN_EMAIL="root@galepartners.com"

# Software Dependencies 
SOFTWARE_INSTALL=( 
    "expect"
    "git"
    "libcurl4-gnutls-dev"
    "libffi-dev"
    "libfreetype6-dev"
    "libgraphviz-dev"
    "libjpeg-dev"
    "libjpeg8-dev"
    "liblcms2-dev"
    "libmysqlclient-dev"
    "libpng12-dev"
    "libpng3"
    "libpq-dev"
    "librtmp-dev"
    "libssl-dev"
    "libtiff5-dev"
    "libwebp-dev"
    "libxml2-dev"
    "libxslt1-dev"
    "postgresql"
    "postgresql-contrib"
    "python-dev"
    "python-httplib2"
    "python-libxml2"
    "python-pygraphviz"
    "python-reportlab"
    "python-setuptools"
    "python-tk"
    "tcl8.6-dev"
    "tk8.6-dev"
)

SOFTWARE_BUILD_DEP=( 
    "psycopg2"
    "pillow"
)

BLDCYN='\e[1;36m' # Cyan

#-------------------------------------------------------------
# Install Software
#-------------------------------------------------------------

echo -e "${BLDCYN}[${PROJECT_NAME}] Updating VM"
DEBIAN_FRONTEND=noninteractive sudo apt-get -y update

echo -e "${BLDCYN}[${PROJECT_NAME}] Upgrading VM"
DEBIAN_FRONTEND=noninteractive sudo apt-get -y upgrade

echo -e "${BLDCYN}[${PROJECT_NAME}] OS Dependencies.."

for i in "${SOFTWARE_INSTALL[@]}"
do
   echo -e "${BLDCYN}[${PROJECT_NAME}] Installing [$i]"
   sudo apt-get -y install $i
done

for i in "${SOFTWARE_BUILD_DEP[@]}"
do
   echo -e "${BLDCYN}[${PROJECT_NAME}] Installing [$i]"
   sudo apt-get -y build-dep $i
done

#-------------------------------------------------------------
# Install VirtualEnv & Python Dependencies
#-------------------------------------------------------------

echo -e "${BLDCYN}[${PROJECT_NAME}] Installing and upgrading pip.."
sudo -H easy_install -U pip

echo -e "${BLDCYN}[${PROJECT_NAME}] Installing virtualenv.."
sudo -H pip install virtualenv

virtualenv ${USER_HOME}
source ${USER_HOME}/bin/activate

echo "source ${USER_HOME}/bin/activate" >> ${USER_HOME}/.bashrc
echo "cd ${PROJECT_HOME}" >> ${USER_HOME}/.bashrc

chown -R ${OS_USER}:${OS_USER} ${USER_HOME}

echo -e "${BLDCYN}[${PROJECT_NAME}] Installing required pip packages.."
pip install pyopenssl ndg-httpsclient pyasn1
pip install -r ${PROJECT_HOME}/requirements.txt
pip install djangocms-installer

#-------------------------------------------------------------
# Database
#-------------------------------------------------------------
echo -e "${BLDCYN}[${PROJECT_NAME}] Provisioning Database.."
expect ${PROJECT_HOME}/vagrant/config/set_db.exp $DB_NAME $DB_USER $DB_PASS $OS_USER

#-------------------------------------------------------------
# Django
#-------------------------------------------------------------
echo -e "${BLDCYN}[${PROJECT_NAME}] Creating project superuser"
expect ${PROJECT_HOME}/vagrant/config/set_admin.exp $OS_USER $PROJECT_NAME $PROJECT_HOME/app/ $ADMIN_USER $ADMIN_EMAIL $ADMIN_PASS

exit 0
