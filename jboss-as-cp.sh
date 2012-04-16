#/bin/sh

usage()
{
cat << EOF
usage: $0 options

Makes possible to run JBoss AS in different directory by creating the structure and copying required configuration files.

OPTIONS:
   -h      Show this message
   -c      JBoss AS configuration xml file (see \$JBOSS_HOME/docs/examples/configs/), default: standalone-web.xml
   -l      Location where the directory structure should be created (required)
EOF
}

STANDALONE_XML="standalone-web.xml"

while getopts “hcl:” OPTION
do
     case $OPTION in
         h)
             usage
             exit 1
             ;;
         c)
             STANDALONE_XML=$OPTARG
             ;;
         l)
             LOCATION=$OPTARG
             ;;
         ?)
             usage
             exit
             ;;
     esac
done

if [[ -z $LOCATION ]]
then
     usage
     exit 1
fi

if [ "x$JBOSS_HOME" = "x" ]; then
   JBOSS_HOME="/usr/share/jboss-as"
fi

mkdir -p ${LOCATION}/{data,deployments,log,tmp,configuration}

cp $JBOSS_HOME/docs/examples/configs/$STANDALONE_XML ${LOCATION}/configuration/
cp $JBOSS_HOME/docs/examples/properties/logging.properties ${LOCATION}/configuration/
cp $JBOSS_HOME/docs/examples/properties/mgmt-users.properties ${LOCATION}/configuration/

# Make sure the mgmt-users.properties file has correct permissions!
chmod 600 ${LOCATION}/configuration/mgmt-users.properties

echo -e "Directory ${LOCATION} ws prepared to launch JBoss AS!\n\nYou can now boot your server: JBOSS_BASE_DIR=${LOCATION} ${JBOSS_HOME}/bin/standalone.sh -c ${STANDALONE_XML}"

