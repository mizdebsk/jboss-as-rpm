%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

%global cachedir %{_var}/cache/%{name}
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global logdir %{_var}/log/%{name}
%global confdir %{_sysconfdir}/%{name}

%global jbuid 185

%global modules connector controller-client controller deployment-repository deployment-scanner domain-management ee ejb3 embedded jmx logging naming network platform-mbean process-controller protocol remoting security server threads transactions web weld

Name:             jboss-as
Version:          7.1.0
Release:          1%{?dist}
Summary:          JBoss Application Server 7
Group:            System Environment/Daemons
License:          LGPLv2+ and ASL 2.0
URL:              http://www.jboss.org/jbossas

# git clone git://github.com/jbossas/jboss-as.git
# cd jboss-as && git checkout 7.1.0.Final && git checkout-index -f -a --prefix=jboss-as-7.1.0.Final/
# find jboss-as-7.1.0.Final/ -name '*.jar' -type f -delete
# tar -cJf jboss-as-7.1.0.Final-CLEAN.tar.xz jboss-as-7.1.0.Final
Source0:          jboss-as-%{namedversion}-CLEAN.tar.xz
# Systemd service file
Source1:          jboss-as.service
# Systemd jboss-as launch file
Source2:          jboss-as-systemd.sh

Patch0:           0001-Disable-checkstyle.patch
Patch1:           0002-Fix-initd-script.patch
Patch2:           0003-Build-additional-modules.patch
# Modifications here are purely temporary until we solve issues in the Right Way (tm)
Patch3:           0004-Ugly-patch-nuff-said.patch
Patch4:           0005-Adding-javax.transaction-to-the-minimal-build.patch
Patch5:           0006-adding-javax.validation-to-build.xml.patch
Patch6:           0007-Only-copy-schemas-and-create-client-all-jar-on-norma.patch
Patch7:           0008-Make-the-dependency-on-dom4j-optional.patch
Patch8:           0009-AS7-3724-DO-NOT-UPSTREAM-an-ugly-patch-to-remove-IIO.patch
Patch9:           0010-adding-org.jboss.metadata-to-minimal-build.patch
Patch10:          0011-adding-org.jboss.ejb3-module-to-minimal-build.patch
Patch11:          0012-adding-org.jboss.as.logging.patch
Patch12:          0013-Removing-logging-module-from-the-normal-profile-as-i.patch
Patch13:          0014-making-the-dependency-in-javax.xml.ws.api-optional-i.patch
Patch14:          0015-adding-org.hibernate.validator.patch
Patch15:          0016-adding-org.jboss.remote-naming-to-minimal-build.patch
Patch16:          0017-Enable-org.jboss.as.transactions-module.patch
Patch17:          0018-Removing-use-of-HornetqJournalEnvironmentBean-in-Arj.patch
Patch18:          0019-adding-org.jboss.jboss-transaction-spi-to-minimal-bu.patch
Patch19:          0020-adding-jts-modules-to-minimal-build.patch
Patch20:          0021-adding-org.omg.api-to-minimal-build.patch
Patch21:          0022-Enable-org.jboss.as.security-module.patch
Patch22:          0023-Enable-part-of-org.jboss.as.clustering-module-infini.patch
Patch23:          0024-Removing-some-banned-deps-as-in-Fedora-those-are-jus.patch
Patch24:          0025-Add-jgroups-module.patch
Patch25:          0026-Add-infinispan-modules.patch
Patch26:          0027-Added-jboss-jacc-api-module.patch
Patch27:          0028-Added-javax.servlet.api-module.patch
Patch28:          0029-Added-org.jboss.security.negotiation-module.patch
Patch29:          0030-Added-org.picketbox-module.patch
Patch30:          0031-Added-sun.jdk-module.patch
Patch31:          0032-Added-jboss-as-connector-AS7-module.patch
Patch32:          0033-Added-jboss-as-web-jboss-as-clustering-api-jboss-as-.patch
Patch33:          0034-Added-net.jcip-org.jboss.ironjacamar-javax.resource..patch
Patch34:          0035-Make-some-modules-optional.patch
Patch35:          0036-Added-jboss-as-ejb3-jboss-as-weld-jboss-as-jpa-modul.patch
Patch36:          0037-Exludes-cleanup.patch
Patch37:          0038-Added-additional-modules-required-on-runtime.patch
Patch38:          0039-Enabled-rest-of-clustering-submodules.patch
Patch39:          0040-Fixed-remoting-jmx-gid-reverting-rmi-changes-adding-.patch
Patch40:          0041-AS7-3921-Upgrade-to-Remoting-JMX-1.0.2-including-swi.patch

BuildArch:        noarch

# Please keep alphabetically
BuildRequires:    ant-apache-bsf
BuildRequires:    apache-commons-logging
BuildRequires:    apache-commons-collections
BuildRequires:    apache-james-project
BuildRequires:    atinject
BuildRequires:    bean-validation-api >= 1.0.0-4
BuildRequires:    bsf >= 2.4.0-10
BuildRequires:    cal10n
BuildRequires:    cdi-api
BuildRequires:    dom4j
# TODO: ecj dependency tree is big and ugly...
BuildRequires:    ecj
BuildRequires:    geronimo-annotation
BuildRequires:    guava
BuildRequires:    h2
BuildRequires:    hibernate-jpa-2.0-api >= 1.0.1-5
BuildRequires:    hibernate-validator >= 4.2.0
BuildRequires:    infinispan >= 5.1.2-1
BuildRequires:    ironjacamar >= 1.0.9-3
BuildRequires:    jandex >= 1.0.3-3
BuildRequires:    java-devel >= 1:1.7.0
BuildRequires:    javamail
BuildRequires:    javassist
BuildRequires:    jgroups
BuildRequires:    jboss-annotations-1.1-api
BuildRequires:    jboss-classfilewriter
BuildRequires:    jboss-common-core >= 2.2.18-5
BuildRequires:    jboss-connector-1.6-api >= 1.0.1
BuildRequires:    jboss-dmr >= 1.1.1-3
BuildRequires:    jboss-ejb-3.1-api >= 1.0.2
BuildRequires:    jboss-ejb3-ext-api >= 2.0.0-2
BuildRequires:    jboss-ejb-client
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-httpserver >= 1.0.0-1
BuildRequires:    jboss-iiop-client
BuildRequires:    jboss-invocation >= 1.1.1-1
BuildRequires:    jboss-interceptor >= 2.0.0-1
BuildRequires:    jboss-interceptors-1.1-api >= 1.0.1
BuildRequires:    jboss-jacc-1.4-api >= 1.0.2
BuildRequires:    jboss-jad-1.2-api >= 1.0.1
BuildRequires:    jboss-jaxb-2.2-api
BuildRequires:    jboss-jaxrpc-1.1-api >= 1.0.1
BuildRequires:    jboss-jaspi-1.0-api >= 1.0.1
BuildRequires:    jboss-jms-1.1-api >= 1.0.1
BuildRequires:    jboss-jts
BuildRequires:    jboss-jsf-2.1-api
BuildRequires:    jboss-jsp-2.2-api
BuildRequires:    jboss-jstl-1.2-api >= 1.0.3
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging >= 3.1.0-2
BuildRequires:    jboss-logging-tools >= 1.0.0-1
BuildRequires:    jboss-logmanager >= 1.2.2-1
BuildRequires:    jboss-logmanager-log4j >= 1.0.0-3
BuildRequires:    jboss-marshalling >= 1.3.9-2
BuildRequires:    jboss-metadata >= 7.0.1-1
BuildRequires:    jboss-modules >= 1.1.1-2
BuildRequires:    jboss-msc >= 1.0.2
BuildRequires:    jboss-negotiation >= 2.2.0-3.SP1
BuildRequires:    jboss-remoting >= 3.2.2-2
BuildRequires:    jboss-remoting-jmx
BuildRequires:    jboss-remote-naming >= 1.0.1
BuildRequires:    jboss-rmi-1.0-api
BuildRequires:    jboss-sasl >= 1.0.0-2
BuildRequires:    jboss-saaj-1.3-api
BuildRequires:    jboss-servlet-3.0-api >= 1.0.0-1
BuildRequires:    jboss-stdio >= 1.0.1-3
BuildRequires:    jboss-specs-parent
BuildRequires:    jboss-threads >= 2.0.0-4
BuildRequires:    jboss-transaction-1.1-api >= 1.0.1
BuildRequires:    jboss-transaction-spi
BuildRequires:    jboss-web >= 7.0.10-1
BuildRequires:    jboss-vfs >= 3.1.0-1
BuildRequires:    jbossws-api
BuildRequires:    jcip-annotations
BuildRequires:    jline
BuildRequires:    joda-time
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    mojarra
BuildRequires:    picketbox
BuildRequires:    picketbox-commons
BuildRequires:    rhq-plugin-annotations
BuildRequires:    slf4j
BuildRequires:    slf4j-jboss-logmanager
BuildRequires:    staxmapper >= 1.1.0-2
BuildRequires:    systemd-units
BuildRequires:    weld-api >= 1.1-3
BuildRequires:    weld-core
BuildRequires:    weld-parent
BuildRequires:    xalan-j2
BuildRequires:    xerces-j2
BuildRequires:    xnio >= 3.0.1-2

Requires:         atinject
Requires:         apache-commons-logging
Requires:         apache-commons-collections
Requires:         bean-validation-api >= 1.0.0-4
Requires:         cal10n
Requires:         cdi-api
Requires:         dom4j
# TODO: ecj dependency tree is big and ugly...
Requires:         ecj
Requires:         guava
Requires:         geronimo-annotation
Requires:         h2
Requires:         hibernate-jpa-2.0-api >= 1.0.1-5
Requires:         hibernate-validator >= 4.2.0
Requires:         infinispan >= 5.1.2-1
Requires:         ironjacamar >= 1.0.9-3
Requires:         jandex >= 1.0.3-3
Requires:         java
Requires:         javamail
Requires:         javassist
Requires:         jboss-annotations-1.1-api
Requires:         jboss-classfilewriter
Requires:         jboss-common-core >= 2.2.18-5
Requires:         jboss-connector-1.6-api >= 1.0.1
Requires:         jboss-dmr >= 1.1.1-3
Requires:         jboss-ejb-3.1-api >= 1.0.2
Requires:         jboss-ejb3-ext-api >= 2.0.0-2
Requires:         jboss-ejb-client
Requires:         jboss-el-2.2-api
Requires:         jboss-httpserver >= 1.0.0-1
Requires:         jboss-iiop-client
Requires:         jboss-interceptor >= 2.0.0-1
Requires:         jboss-interceptors-1.1-api >= 1.0.1
Requires:         jboss-invocation >= 1.1.1-1
Requires:         jboss-jacc-1.4-api >= 1.0.2
Requires:         jboss-jad-1.2-api >= 1.0.1
Requires:         jboss-jaxb-2.2-api
Requires:         jboss-jaxrpc-1.1-api >= 1.0.1
Requires:         jboss-jaspi-1.0-api >= 1.0.1
Requires:         jboss-jms-1.1-api >= 1.0.1
Requires:         jboss-jsf-2.1-api
Requires:         jboss-jsp-2.2-api
Requires:         jboss-jstl-1.2-api >= 1.0.3
Requires:         jboss-jts
Requires:         jboss-logging >= 3.1.0-2
Requires:         jboss-logging-tools >= 1.0.0-1
Requires:         jboss-logmanager >= 1.2.2-1
Requires:         jboss-logmanager-log4j >= 1.0.0-3
Requires:         jboss-marshalling >= 1.3.9-2
Requires:         jboss-metadata >= 7.0.1-1
Requires:         jboss-modules >= 1.1.1-2
Requires:         jboss-msc >= 1.0.2
Requires:         jboss-negotiation >= 2.2.0-3.SP1
Requires:         jboss-remoting >= 3.2.2-2
Requires:         jboss-remoting-jmx
Requires:         jboss-remote-naming >= 1.0.1
Requires:         jboss-rmi-1.0-api
Requires:         jboss-sasl >= 1.0.0-2
Requires:         jboss-saaj-1.3-api
Requires:         jboss-servlet-3.0-api >= 1.0.0-1
Requires:         jboss-stdio >= 1.0.1-3
Requires:         jboss-threads >= 2.0.0-4
Requires:         jboss-transaction-1.1-api >= 1.0.1
Requires:         jboss-transaction-spi
Requires:         jboss-web >= 7.0.10-1
Requires:         jboss-vfs >= 3.1.0-1
Requires:         jbossws-api
Requires:         jcip-annotations
Requires:         jgroups
Requires:         jline
Requires:         joda-time
Requires:         jpackage-utils
Requires:         mojarra
Requires:         picketbox
Requires:         picketbox-commons
Requires:         rhq-plugin-annotations
Requires:         slf4j
Requires:         slf4j-jboss-logmanager
Requires:         staxmapper >= 1.1.0-2
Requires:         weld-api >= 1.1-3
Requires:         weld-core
Requires:         xalan-j2
Requires:         xerces-j2
Requires:         xnio >= 3.0.1-2
Requires(pre):    shadow-utils

%description
JBoss Application Server 7 is the latest release in a series of JBoss
Application Server offerings. JBoss Application Server 7, is a fast,
powerful, implementation of the Java Enterprise Edition 6 specification.
The state-of-the-art architecture built on the Modular Service Container
enables services on-demand when your application requires them.

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-as-%{namedversion}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1

%build
# We don't have packaged all test dependencies (jboss-test for example)
mvn-rpmbuild -Dmaven.test.skip=true -Dminimalistic -e install javadoc:aggregate

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{homedir}
install -d -m 755 $RPM_BUILD_ROOT%{confdir}
install -d -m 770 $RPM_BUILD_ROOT%{cachedir}/auth
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_unitdir}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}

for mode in standalone domain; do
  install -d -m 755 $RPM_BUILD_ROOT%{homedir}/${mode}
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}/data
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}/tmp
  install -d -m 775 $RPM_BUILD_ROOT%{logdir}/${mode}
done

# build-config is not installed in the resulting package, but required to build it
# ee-deployment is a special case, it should be a submodule of ee, but it isn't...
for m in %{modules} build-config ee-deployment; do
  # JAR
  cp -a ${m}/target/jboss-as-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  cp -a ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# Definition of submodules
multimodules="domain-http clustering jpa"
# If a submodule contains hyphen in the name, just skip it, e.g. domain-http => domainhttp
modules_clustering="api common impl jgroups infinispan registry service web-spi web-infinispan ejb3-infinispan"
modules_jpa="util spi"
modules_domainhttp="interface error-context"

for m in ${multimodules}; do

  eval submodules=\$"modules_${m//-/}"

  for sm in $submodules; do
    # JAR
    cp -a ${m}/${sm}/target/jboss-as-${m}-${sm}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}-${sm}.jar
    # POM
    cp -a ${m}/${sm}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}-${sm}.pom
    # DEPMAP
    %add_maven_depmap JPP.%{name}-%{name}-${m}-${sm}.pom %{name}/%{name}-${m}-${sm}.jar
  done
done

# Exceptions START

# JAR
cp -a jpa/core/target/jboss-as-jpa-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-jpa.jar
# POM
cp -a jpa/core/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-jpa.pom
# DEPMAP
%add_maven_depmap JPP.%{name}-%{name}-jpa.pom %{name}/%{name}-jpa.jar

# Exceptions END

# Parent POM
cp -a pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# Depmap fo parent POM
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# Apidocs
cp -a target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

pushd build/target/jboss-as-%{namedversion}
  # We don't need Windows files
  find bin/ -type f -name "*.bat" -delete

  # Install systemd files
  mv bin/init.d/jboss-as.conf $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}
  cp %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
  cp %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}

  rm -rf bin/init.d

  # standalone
  mv standalone/configuration $RPM_BUILD_ROOT%{confdir}/standalone
  mv standalone/deployments $RPM_BUILD_ROOT%{cachedir}/standalone
  # enable standalone-minimalistic.xml
  mv docs/examples/configs/standalone-minimalistic.xml $RPM_BUILD_ROOT%{confdir}/standalone/

  # domain
  mv domain/configuration $RPM_BUILD_ROOT%{confdir}/domain

  # Remove all jars from modules directory - we need to symlink them
  # TODO temporary with verbose, use -delete afterwards
  find . -type f -name "*.jar" -exec rm -rvf {} \;

  # TMP - investigate
  rm -rf bin/client

  mv copyright.txt README.txt LICENSE.txt welcome-content docs bin appclient modules $RPM_BUILD_ROOT%{homedir}
popd

pushd $RPM_BUILD_ROOT%{homedir}

  # Standalone
  ln -s %{cachedir}/standalone/deployments standalone/deployments
  ln -s %{confdir}/standalone standalone/configuration

  # Domain
  ln -s %{confdir}/domain domain/configuration

  # Symlink jboss-modules
  ln -s $(build-classpath jboss-modules) jboss-modules.jar
  
  # Symlinks to log dirs
  ln -s %{logdir}/standalone standalone/log
  ln -s %{logdir}/domain domain/log

  # temp dir
  ln -s %{cachedir}/standalone/tmp standalone/tmp
  ln -s %{cachedir}/domain/tmp domain/tmp

  # data dir
  ln -s %{cachedir}/standalone/data standalone/data
  ln -s %{cachedir}/domain/data domain/data

  # auth dir
  ln -s %{cachedir}/auth auth
  
  # Create symlinks to jars
  pushd modules
    # JBoss AS modules
    # Symlinks all main AS7 modules + some addtiional modules that have different naming scheme
    for m in %{modules} domain-http-error-context domain-http-interface; do
      ln -s %{_javadir}/jboss-as/jboss-as-${m}.jar org/jboss/as/${m}/main/jboss-as-${m}-%{namedversion}.jar
    done

    for m in ${multimodules}; do
      eval submodules=\$"modules_${m//-/}"

      for sm in $submodules; do
        if [ -d "org/jboss/as/${m}/${sm}/main/" ]; then
          ln -s %{_javadir}/jboss-as/jboss-as-${m}-${sm}.jar org/jboss/as/${m}/${sm}/main/jboss-as-${m}-${sm}-%{namedversion}.jar
        else
          echo "SKIPPING symlinking 'jboss-as-${m}-${sm}.jar'. This may be a special case handled elsewhere."
        fi
      done
    done

    # And don't forget this module which should be a submodule...
    ln -s %{_javadir}/jboss-as/jboss-as-ee-deployment.jar org/jboss/as/ee/deployment/main/jboss-as-ee-deployment-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-clustering-web-spi.jar org/jboss/as/clustering/web/spi/main/jboss-as-clustering-web-spi-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-clustering-web-infinispan.jar org/jboss/as/clustering/web/infinispan/main/jboss-as-clustering-web-infinispan-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-clustering-ejb3-infinispan.jar org/jboss/as/clustering/ejb3/infinispan/main/jboss-as-clustering-ejb3-infinispan-%{namedversion}.jar

    # And some other expcetions...
    ln -s %{_javadir}/jboss-as/jboss-as-jpa.jar org/jboss/as/jpa/main/jboss-as-jpa-%{namedversion}.jar

    # Please keep alphabetic by jar name
    ln -s $(build-classpath apache-commons-collections) org/apache/commons/collections/main/commons-collections.jar
    ln -s $(build-classpath atinject) javax/inject/api/main/atinject.jar
    ln -s $(build-classpath cal10n/cal10n-api) ch/qos/cal10n/main/cal10n-api.jar
    ln -s $(build-classpath cdi-api) javax/enterprise/api/main/cdi-api.jar
    ln -s $(build-classpath ecj) org/jboss/as/web/main/ecj.jar
    ln -s $(build-classpath guava) com/google/guava/main/guava.jar
    ln -s $(build-classpath geronimo-validation) javax/validation/api/main/geronimo-validation.jar
    ln -s $(build-classpath hibernate-validator) org/hibernate/validator/main/hibernate-validator.jar
    ln -s $(build-classpath hibernate-jpa-2.0-api) javax/persistence/api/main/hibernate-jpa-2.0-api.jar

    ln -s $(build-classpath infinispan/infinispan-cachestore-jdbc) org/infinispan/cachestore/jdbc/main/infinispan-cachestore-jdbc.jar
    ln -s $(build-classpath infinispan/infinispan-cachestore-remote) org/infinispan/cachestore/remote/main/infinispan-cachestore-remote.jar
    ln -s $(build-classpath infinispan/infinispan-client-hotrod) org/infinispan/client/hotrod/main/infinispan-client-hotrod.jar
    ln -s $(build-classpath infinispan/infinispan-core) org/infinispan/main/infinispan-core.jar

    ln -s $(build-classpath ironjacamar/ironjacamar-common-api) org/jboss/ironjacamar/api/main/ironjacamar-common-api.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-common-spi) org/jboss/ironjacamar/api/main/ironjacamar-common-spi.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-core-api) org/jboss/ironjacamar/api/main/ironjacamar-core-api.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-common-impl) org/jboss/ironjacamar/impl/main/ironjacamar-common-impl.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-core-impl) org/jboss/ironjacamar/impl/main/ironjacamar-core-impl.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-deployers-common) org/jboss/ironjacamar/impl/main/ironjacamar-deployers-common.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-validator) org/jboss/ironjacamar/impl/main/ironjacamar-validator.jar
    ln -s $(build-classpath ironjacamar/ironjacamar-jdbc) org/jboss/ironjacamar/jdbcadapters/main/ironjacamar-jdbc.jar

    ln -s $(build-classpath javamail/mail) javax/mail/api/main/mail.jar
    ln -s $(build-classpath javassist) org/javassist/main/javassist.jar
    ln -s $(build-classpath jcip-annotations) net/jcip/main/jcip-annotations.jar
    ln -s $(build-classpath jandex) org/jboss/jandex/main/jandex.jar
    ln -s $(build-classpath jboss-annotations-1.1-api) javax/annotation/api/main/jboss-annotations-1.1-api.jar
    ln -s $(build-classpath jboss-classfilewriter) org/jboss/classfilewriter/main/jboss-classfilewriter.jar
    ln -s $(build-classpath jboss-common-core) org/jboss/common-core/main/jboss-common-core.jar
    ln -s $(build-classpath jboss-connector-1.6-api) javax/resource/api/main/jboss-connector-1.6-api.jar
    ln -s $(build-classpath jboss-dmr) org/jboss/dmr/main/jboss-dmr.jar
    ln -s $(build-classpath jboss-ejb-3.1-api) javax/ejb/api/main/jboss-ejb-3.1-api.jar
    ln -s $(build-classpath jboss-ejb3-ext-api) org/jboss/ejb3/main/jboss-ejb3-ext-api.jar
    ln -s $(build-classpath jboss-ejb-client) org/jboss/ejb-client/main/jboss-ejb-client.jar
    ln -s $(build-classpath jboss-el-2.2-api) javax/el/api/main/jboss-el-2.2-api.jar
    ln -s $(build-classpath jboss-httpserver) org/jboss/com/sun/httpserver/main/jboss-httpserver.jar
    ln -s $(build-classpath jboss-iiop-client) org/jboss/iiop-client/main/jboss-iiop-client.jar
    ln -s $(build-classpath jboss-interceptor-core) org/jboss/interceptor/main/jboss-interceptor-core.jar
    ln -s $(build-classpath jboss-interceptor-spi) org/jboss/interceptor/spi/main/jboss-interceptor-spi.jar
    ln -s $(build-classpath jboss-interceptors-1.1-api) javax/interceptor/api/main/jboss-interceptors-1.1-api.jar
    ln -s $(build-classpath jboss-invocation) org/jboss/invocation/main/jboss-invocation.jar
    ln -s $(build-classpath jboss-jacc-1.4-api) javax/security/jacc/api/main/jboss-jacc-1.4-api.jar
    ln -s $(build-classpath jboss-jad-1.2-api) javax/enterprise/deploy/api/main/jboss-jad-1.2-api.jar
    ln -s $(build-classpath jboss-jaxb-2.2-api) javax/xml/bind/api/main/jboss-jaxb-2.2-api.jar
    ln -s $(build-classpath jboss-jaxrpc-1.1-api) javax/xml/rpc/api/main/jboss-jaxrpc-1.1-api.jar
    ln -s $(build-classpath jboss-jaspi-1.0-api) javax/security/auth/message/api/main/jboss-jaspi-1.0-api.jar
    ln -s $(build-classpath jboss-jms-1.1-api) javax/jms/api/main/jboss-jms-1.1-api.jar
    ln -s $(build-classpath jboss-jsf-2.1-api) javax/faces/api/main/jboss-jsf-2.1-api.jar
    ln -s $(build-classpath jboss-jsp-2.2-api) javax/servlet/jsp/api/main/jboss-jsp-2.2-api.jar
    ln -s $(build-classpath jboss-jstl-1.2-api) javax/servlet/jstl/api/main/jboss-jstl-1.2-api.jar
    ln -s $(build-classpath jboss-jts/jbossjta) org/jboss/jts/main/jbossjta.jar
    ln -s $(build-classpath jboss-jts/jbossjta-integration) org/jboss/jts/integration/main/jbossjta-integration.jar
    ln -s $(build-classpath log4j) org/apache/log4j/main/log4j.jar
    ln -s $(build-classpath jboss-logging) org/jboss/logging/main/jboss-logging.jar
    ln -s $(build-classpath jboss-logmanager) org/jboss/logmanager/main/jboss-logmanager.jar
    ln -s $(build-classpath jboss-logmanager-log4j) org/jboss/logmanager/log4j/main/jboss-logmanager-log4j.jar
    ln -s $(build-classpath jboss-marshalling) org/jboss/marshalling/main/jboss-marshalling.jar
    ln -s $(build-classpath jboss-marshalling-river) org/jboss/marshalling/river/main/jboss-marshalling-river.jar
    ln -s $(build-classpath jboss-metadata/jboss-metadata-appclient) org/jboss/metadata/main/jboss-metadata-appclient.jar
    ln -s $(build-classpath jboss-metadata/jboss-metadata-common) org/jboss/metadata/main/jboss-metadata-common.jar
    ln -s $(build-classpath jboss-metadata/jboss-metadata-ear) org/jboss/metadata/main/jboss-metadata-ear.jar
    ln -s $(build-classpath jboss-metadata/jboss-metadata-ejb) org/jboss/metadata/main/jboss-metadata-ejb.jar
    ln -s $(build-classpath jboss-metadata/jboss-metadata-web) org/jboss/metadata/main/jboss-metadata-web.jar
    ln -s $(build-classpath jboss-msc) org/jboss/msc/main/jboss-msc.jar
    ln -s $(build-classpath jboss-remoting) org/jboss/remoting3/main/jboss-remoting.jar
    ln -s $(build-classpath jboss-remote-naming) org/jboss/remote-naming/main/jboss-remote-naming.jar
    ln -s $(build-classpath jboss-remoting-jmx) org/jboss/remoting3/remoting-jmx/main/jboss-remoting-jmx.jar
    ln -s $(build-classpath jboss-rmi-1.0-api) javax/rmi/api/main/jboss-rmi-1.0-api.jar
    ln -s $(build-classpath jboss-saaj-1.3-api) javax/xml/soap/api/main/jboss-saaj-1.3-api.jar
    ln -s $(build-classpath jboss-sasl) org/jboss/sasl/main/jboss-sasl.jar

    ln -s $(build-classpath jboss-negotiation/jboss-negotiation-common) org/jboss/security/negotiation/main/jboss-negotiation-common.jar
    ln -s $(build-classpath jboss-negotiation/jboss-negotiation-extras) org/jboss/security/negotiation/main/jboss-negotiation-extras.jar
    ln -s $(build-classpath jboss-negotiation/jboss-negotiation-net) org/jboss/security/negotiation/main/jboss-negotiation-net.jar
    ln -s $(build-classpath jboss-negotiation/jboss-negotiation-ntlm) org/jboss/security/negotiation/main/jboss-negotiation-ntlm.jar
    ln -s $(build-classpath jboss-negotiation/jboss-negotiation-spnego) org/jboss/security/negotiation/main/jboss-negotiation-spnego.jar

    ln -s $(build-classpath jboss-servlet-3.0-api) javax/servlet/api/main/jboss-servlet-3.0-api.jar
    ln -s $(build-classpath jboss-stdio) org/jboss/stdio/main/jboss-stdio.jar
    ln -s $(build-classpath jboss-threads) org/jboss/threads/main/jboss-threads.jar
    ln -s $(build-classpath jboss-transaction-1.1-api) ./javax/transaction/api/main/jboss-transaction-1.1-api.jar
    ln -s $(build-classpath jboss-transaction-spi) org/jboss/jboss-transaction-spi/main/jboss-transaction-spi.jar
    ln -s $(build-classpath jboss-vfs) org/jboss/vfs/main/jboss-vfs.jar
    ln -s $(build-classpath jboss-web) org/jboss/as/web/main/jboss-web.jar
    ln -s $(build-classpath jgroups) org/jgroups/main/jgroups.jar
    ln -s $(build-classpath joda-time) org/joda/time/main/joda-time.jar
    ln -s $(build-classpath mojarra/jsf-impl) com/sun/jsf-impl/main/jsf-impl.jar
    ln -s $(build-classpath picketbox/picketbox) org/picketbox/main/picketbox.jar
    ln -s $(build-classpath picketbox/infinispan) org/picketbox/main/infinispan.jar
    ln -s $(build-classpath picketbox-commons) org/picketbox/main/picketbox-commons.jar
    ln -s $(build-classpath slf4j/api) org/slf4j/main/api.jar
    ln -s $(build-classpath slf4j/ext) org/slf4j/ext/main/ext.jar
    ln -s $(build-classpath slf4j/jcl-over-slf4j) org/slf4j/jcl-over-slf4j/main/jcl-over-slf4j.jar
    ln -s $(build-classpath slf4j-jboss-logmanager) org/slf4j/impl/main/slf4j-jboss-logmanager.jar
    ln -s $(build-classpath staxmapper) org/jboss/staxmapper/main/staxmapper.jar
    ln -s $(build-classpath weld-api/weld-api) org/jboss/weld/api/main/weld-api.jar
    ln -s $(build-classpath weld-api/weld-spi) org/jboss/weld/spi/main/weld-spi.jar
    ln -s $(build-classpath weld-core) org/jboss/weld/core/main/weld-core.jar
    ln -s $(build-classpath xalan-j2) org/apache/xalan/main/xalan-j2.jar
    ln -s $(build-classpath xalan-j2-serializer) org/apache/xalan/main/xalan-j2-serializer.jar
    ln -s $(build-classpath xerces-j2) org/apache/xerces/main/xerces-j2.jar
    ln -s $(build-classpath xnio-api) org/jboss/xnio/main/xnio-api.jar
    ln -s $(build-classpath xnio-nio) org/jboss/xnio/nio/main/xnio-nio.jar
  popd
popd

%pre
# Add jboss-as user and group
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -c "JBoss AS" -u %{jbuid} -g %{name} -s /bin/nologin -r -d %{homedir} %{name}

%files
%defattr(0664,root,jboss-as,0755)
%{homedir}/appclient
%{bindir}/*.conf
%attr(0755,root,root) %{bindir}/*.sh
%attr(0755,root,root) %{_bindir}/%{name}
%dir %{homedir}/bin
%{homedir}/auth
%{homedir}/domain
%{homedir}/standalone
%{homedir}/modules
%{homedir}/welcome-content
%{homedir}/jboss-modules.jar
%{cachedir}/standalone/deployments/README.txt
%attr(0775,root,jboss-as) %dir %{cachedir}/standalone/data
%attr(0775,root,jboss-as) %dir %{cachedir}/standalone/tmp
%attr(0775,root,jboss-as) %dir %{cachedir}/domain/data
%attr(0775,root,jboss-as) %dir %{cachedir}/domain/tmp
%attr(0700,jboss-as,jboss-as) %dir %{cachedir}/auth
%attr(0770,root,jboss-as) %dir %{logdir}/standalone
%attr(0770,root,jboss-as) %dir %{logdir}/domain
%attr(0775,root,jboss-as) %dir %{confdir}/standalone
%attr(0775,root,jboss-as) %dir %{confdir}/domain
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.xml
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.xml
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_unitdir}/%{name}.service
%doc %{homedir}/docs
%doc %{homedir}/copyright.txt
%doc %{homedir}/LICENSE.txt
%doc %{homedir}/README.txt
%doc README.md
%{_mavenpomdir}/*
%{_mavendepmapfragdir}/*
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
* Mon Apr 02 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.0-1
- Initial packaging

