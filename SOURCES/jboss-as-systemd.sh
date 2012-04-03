#!/bin/sh

# Load Java configuration.
[ -r /etc/java/java.conf ] && . /etc/java/java.conf

export JAVA_HOME

# Load JBoss AS configuration.
if [ -z "$JBOSS_CONF" ]; then
  JBOSS_CONF="/etc/sysconfig/jboss-as"
fi

[ -r "$JBOSS_CONF" ] && . "${JBOSS_CONF}"

if [ -z "$JBOSS_HOME" ]; then
  JBOSS_HOME=/usr/share/jboss-as
fi

export JBOSS_HOME

if [ -z "$JBOSS_PIDFILE" ]; then
  JBOSS_PIDFILE=/var/run/jboss-as/jboss-as.pid
fi

if [ -z "$JBOSS_CONSOLE_LOG" ]; then
  JBOSS_CONSOLE_LOG=/var/log/jboss-as/console.log
fi

if [ -z "$JBOSS_CONFIG" ]; then
  JBOSS_CONFIG=standalone.xml
fi

JBOSS_SCRIPT=$JBOSS_HOME/bin/standalone.sh

# For SELinux we need to use 'runuser' not 'su'
if [ -x "/sbin/runuser" ]; then
  SU="/sbin/runuser -s /bin/sh"
else
  SU="/bin/su -s /bin/sh"
fi

start() {
  if [ -f $JBOSS_PIDFILE ]; then
    read ppid < $JBOSS_PIDFILE
    if [ `ps --pid $ppid 2> /dev/null | grep -c $ppid 2> /dev/null` -eq '1' ]; then
      failure
      echo
      return 1 
    else
      rm -f $JBOSS_PIDFILE
    fi
  fi
  mkdir -p $(dirname $JBOSS_CONSOLE_LOG)
  cat /dev/null > $JBOSS_CONSOLE_LOG

  mkdir -p $(dirname $JBOSS_PIDFILE)
  chown $JBOSS_USER $(dirname $JBOSS_PIDFILE) || true

  $SU - $JBOSS_USER -c "LAUNCH_JBOSS_IN_BACKGROUND=1 JBOSS_PIDFILE=$JBOSS_PIDFILE $JBOSS_SCRIPT -c $JBOSS_CONFIG" 2>&1 > $JBOSS_CONSOLE_LOG &
}

stop() {
  if [ -f $JBOSS_PIDFILE ]; then
    read kpid < $JBOSS_PIDFILE
    kill -15 $kpid
    rm -f $JBOSS_PIDFILE
  fi
}

case "$1" in
  start)
      start
      ;;
  stop)
      stop
      ;;
  restart)
      $0 stop
      $0 start
      ;;
  *)
      echo "Usage: $0 {start|stop|restart}"
      exit 1
      ;;
esac

