%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

%global cachedir %{_var}/cache/%{name}
%global libdir %{_var}/lib/%{name}
%global rundir %{_var}/run/%{name}
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global logdir %{_var}/log/%{name}
%global confdir %{_sysconfdir}/%{name}

%global jbuid 185

# Enabled modules:
%global modules appclient cli cmp configadmin connector controller-client controller deployment-repository deployment-scanner domain-management ee ejb3 embedded host-controller jacorb jaxr jaxrs jmx jsr77 logging management-client-content mail messaging modcluster naming network platform-mbean pojo process-controller protocol remoting sar security server threads transactions web weld xts

# Additional modules enabled, but not listed above because of different structure:
# arquillian domain-http clustering jpa osgi jdr webservices

Name:             jboss-as
Version:          7.1.1
Release:          16%{?dist}
Summary:          JBoss Application Server
Group:            System Environment/Daemons
License:          LGPLv2 and ASL 2.0
URL:              http://www.jboss.org/jbossas

# git clone git://github.com/jbossas/jboss-as.git
# cd jboss-as && git checkout 7.1.1.Final && git checkout-index -f -a --prefix=jboss-as-7.1.1.Final/
# find jboss-as-7.1.1.Final/ -name '*.jar' -type f -delete
# tar -cJf jboss-as-7.1.1.Final-CLEAN.tar.xz jboss-as-7.1.1.Final
Source0:          jboss-as-%{namedversion}-CLEAN.tar.xz

# Makes possible to run JBoss AS in different directory by creating the structure and copying required configuration files
Source1:          jboss-as-cp.sh

Patch0:           0001-fedora-Disable-checkstyle.patch
Patch1:           0002-fedora-Added-standalone-web.xml-example-configuratio.patch
Patch2:           0003-Add-systemd-files-re-arrange-directory-with-init-scr.patch
Patch3:           0004-Fix-JBOSS_HOME-when-jboss-cli.sh-is-executed-through.patch
Patch4:           0005-AS7-3800-JBOSS_BASE_DIR-is-checked-in-standalone.sh-.patch
Patch5:           0006-fedora-Remove-activation-module.patch
Patch6:           0007-Use-properties-in-add-user-AS7-module.patch
Patch7:           0008-added-support-for-overriding-the-user-and-roles-prop.patch
Patch8:           0009-AS7-4536-add-user.sh-mangles-permissions-of-mgmt-use.patch
Patch9:           0010-AS7-4286-Fix-JavaCC-grammars-for-version-5.patch
Patch10:          0011-fedora-Remove-jasper-jdt-requirement-it-was-replaced.patch
Patch11:          0012-Removed-unused-import-in-modcluster-module.patch
Patch12:          0013-fedora-Remove-org.osgi.enterprise-dependency.patch
Patch13:          0014-fedora-Drop-some-enforcer-exclusions-these-are-alias.patch
Patch14:          0015-fedora-Remove-jbossweb-native-dependency.-We-ll-have.patch
Patch15:          0016-fedora-Disable-checkstyle-in-testsuite-too.patch
Patch16:          0017-fedora-Disable-testsuites.patch
Patch17:          0018-fedora-Make-AS7-work-with-jython-2.2.1.patch
Patch18:          0019-fedora-Add-jtype-dependency-to-hibernate-validator-t.patch
Patch19:          0020-Add-org.apache.openjpa-module.-This-allows-to-use-th.patch
Patch20:          0021-fedora-Add-org.hibernate.3-module.patch
Patch21:          0022-fedora-Add-org.osgi-org.osgi.compendium-dependency-s.patch
Patch22:          0023-JBWS-3446-Add-methods-for-creating-a-test-https-conn.patch
Patch23:          0024-Modified-AS7-4890-upgrade-to-JBossWS-4.1.0.Beta1.patch
Patch24:          0025-fedora-Remove-javax.jws.api.-This-is-part-of-the-JDK.patch
Patch25:          0026-fedora-Missing-module-dependencies-in-mime4j-com.sun.patch
Patch26:          0027-fedora-Remove-still-unavailable-in-Fedora-dependenci.patch
Patch27:          0028-fedora-Do-not-extract-jbossweb-native-it-s-symlinked.patch

BuildArch:        noarch

# Please keep alphabetically
BuildRequires:    antlr
BuildRequires:    ant-apache-bsf
BuildRequires:    apache-commons-beanutils
BuildRequires:    apache-commons-cli
BuildRequires:    apache-commons-codec
BuildRequires:    apache-commons-collections
BuildRequires:    apache-commons-configuration
BuildRequires:    apache-commons-io
BuildRequires:    apache-commons-lang
BuildRequires:    apache-commons-logging
BuildRequires:    apache-commons-pool
BuildRequires:    apache-james-project
BuildRequires:    apache-juddi
BuildRequires:    apache-mime4j
BuildRequires:    apache-scout
BuildRequires:    arquillian-core
BuildRequires:    arquillian-osgi
BuildRequires:    atinject
BuildRequires:    bean-validation-api
BuildRequires:    bsf
BuildRequires:    cal10n
BuildRequires:    cdi-api
BuildRequires:    cssparser
BuildRequires:    cxf >= 2.6.3
BuildRequires:    cxf-api >= 2.6.3
BuildRequires:    cxf-common >= 2.6.3
BuildRequires:    cxf-rt >= 2.6.3
BuildRequires:    cxf-tools >= 2.6.3
BuildRequires:    dom4j
BuildRequires:    ecj
BuildRequires:    felix-configadmin
BuildRequires:    felix-osgi-core
BuildRequires:    felix-osgi-compendium
BuildRequires:    guava
BuildRequires:    h2
BuildRequires:    hibernate
BuildRequires:    hibernate-entitymanager
BuildRequires:    hibernate-infinispan
BuildRequires:    hibernate-envers
BuildRequires:    hibernate3 >= 3.6.10-7
BuildRequires:    hibernate3-entitymanager >= 3.6.10-7
BuildRequires:    hibernate3-infinispan >= 3.6.10-7
BuildRequires:    hibernate-commons-annotations
BuildRequires:    hibernate-jpa-2.0-api
BuildRequires:    hibernate-validator
BuildRequires:    hornetq
BuildRequires:    httpcomponents-client
BuildRequires:    httpcomponents-core
BuildRequires:    git
BuildRequires:    glassfish-jaxb
BuildRequires:    glassfish-saaj
BuildRequires:    gnu-getopt
BuildRequires:    istack-commons
BuildRequires:    infinispan
BuildRequires:    ironjacamar
BuildRequires:    jacorb
BuildRequires:    jackson
BuildRequires:    jandex
BuildRequires:    java-devel >= 1:1.7.0
BuildRequires:    javacc-maven-plugin
BuildRequires:    javamail
BuildRequires:    javassist
BuildRequires:    jaxen
BuildRequires:    jaxws-jboss-httpserver-httpspi
BuildRequires:    jettison
BuildRequires:    jgroups
BuildRequires:    jbosgi-deployment
BuildRequires:    jbosgi-framework
BuildRequires:    jbosgi-metadata
BuildRequires:    jbosgi-repository
BuildRequires:    jbosgi-resolver1
BuildRequires:    jbosgi-spi
BuildRequires:    jbosgi-vfs
BuildRequires:    jbosgi-parent
BuildRequires:    jboss-annotations-1.1-api
BuildRequires:    jboss-classfilewriter
BuildRequires:    jboss-common-core
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-dmr
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-ejb3-ext-api
BuildRequires:    jboss-ejb-client
BuildRequires:    jboss-el-2.2-api
BuildRequires:    jboss-httpserver
BuildRequires:    jboss-iiop-client
BuildRequires:    jboss-invocation
BuildRequires:    jboss-interceptor
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-j2eemgmt-1.1-api
BuildRequires:    jboss-jacc-1.4-api
BuildRequires:    jboss-jad-1.2-api
BuildRequires:    jboss-jaxb-2.2-api
BuildRequires:    jboss-jaxb-intros
BuildRequires:    jboss-jaxr-1.0-api
BuildRequires:    jboss-jaxrpc-1.1-api
BuildRequires:    jboss-jaxrs-1.1-api
BuildRequires:    jboss-jaxws-2.2-api
BuildRequires:    jboss-jaspi-1.0-api
BuildRequires:    jboss-jms-1.1-api
BuildRequires:    jboss-jts >= 4.16.2-10
BuildRequires:    jboss-jsf-2.1-api
BuildRequires:    jboss-jsp-2.2-api
BuildRequires:    jboss-jstl-1.2-api
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging
BuildRequires:    jboss-logging-tools
BuildRequires:    jboss-logmanager
BuildRequires:    jboss-logmanager-log4j
BuildRequires:    jboss-marshalling
BuildRequires:    jboss-metadata
BuildRequires:    jboss-modules
BuildRequires:    jboss-msc
BuildRequires:    jboss-negotiation
BuildRequires:    jboss-remoting
BuildRequires:    jboss-remoting-jmx
BuildRequires:    jboss-remote-naming
BuildRequires:    jboss-rmi-1.0-api >= 1.0.4-4
BuildRequires:    jboss-sasl
BuildRequires:    jboss-saaj-1.3-api
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jboss-stdio
BuildRequires:    jboss-specs-parent
BuildRequires:    jboss-threads
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-transaction-spi
BuildRequires:    jboss-web
BuildRequires:    jboss-web-native
BuildRequires:    jboss-vfs
BuildRequires:    jbossws-parent
BuildRequires:    jbossws-api
BuildRequires:    jbossws-common >= 2.0.4-3
BuildRequires:    jbossws-common-tools
BuildRequires:    jbossws-cxf >= 4.1.0
BuildRequires:    jbossws-spi >= 2.1.0
BuildRequires:    jbossws-native >= 4.1.0
BuildRequires:    jbossxb
BuildRequires:    jcip-annotations
BuildRequires:    jdom
BuildRequires:    jline
BuildRequires:    jul-to-slf4j-stub
BuildRequires:    joda-time
BuildRequires:    javapackages-tools >= 0.7.2-1
BuildRequires:    jpackage-utils
BuildRequires:    jtype
BuildRequires:    jython >= 2.2.1-9
BuildRequires:    maven-local
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-dependency-plugin
BuildRequires:    maven-help-plugin
BuildRequires:    maven-shade-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-ear-plugin
BuildRequires:    maven-eclipse-plugin
BuildRequires:    maven-ejb-plugin
BuildRequires:    xml-maven-plugin
BuildRequires:    mojarra
BuildRequires:    mod_cluster-java >= 1.2.1-2
BuildRequires:    neethi
BuildRequires:    nekohtml
BuildRequires:    netty
BuildRequires:    objectweb-asm
BuildRequires:    openjpa
BuildRequires:    opensaml-java
BuildRequires:    opensaml-java-openws
BuildRequires:    opensaml-java-xmltooling
BuildRequires:    opensaml-java-parent
BuildRequires:    picketbox
BuildRequires:    picketbox-commons
BuildRequires:    picketbox-xacml
BuildRequires:    resteasy >= 2.3.2-7
BuildRequires:    rhq-plugin-annotations
BuildRequires:    scannotation
BuildRequires:    sac
BuildRequires:    serp
BuildRequires:    shrinkwrap
BuildRequires:    shrinkwrap-resolver
BuildRequires:    slf4j
BuildRequires:    slf4j-jboss-logmanager
BuildRequires:    snakeyaml
BuildRequires:    staxmapper
BuildRequires:    stax2-api
BuildRequires:    systemd-units
BuildRequires:    velocity
BuildRequires:    weld-api
BuildRequires:    weld-core
BuildRequires:    weld-parent
BuildRequires:    woodstox-core
BuildRequires:    wsdl4j >= 1.6.2-5
BuildRequires:    wss4j >= 1.6.7
BuildRequires:    ws-xmlschema
BuildRequires:    xalan-j2
BuildRequires:    xerces-j2
BuildRequires:    xml-security
BuildRequires:    xml-commons-apis
BuildRequires:    xml-commons-resolver
BuildRequires:    xnio
BuildRequires:    xom

Requires:         antlr
Requires:         atinject
Requires:         apache-commons-beanutils
Requires:         apache-commons-cli
Requires:         apache-commons-codec
Requires:         apache-commons-collections
Requires:         apache-commons-configuration
Requires:         apache-commons-io
Requires:         apache-commons-lang
Requires:         apache-commons-logging
Requires:         apache-commons-pool
Requires:         apache-juddi
Requires:         apache-mime4j
Requires:         apache-scout
Requires:         apr
Requires:         arquillian-core
Requires:         arquillian-osgi
Requires:         bean-validation-api
Requires:         cal10n
Requires:         cdi-api
Requires:         cssparser
Requires:         cxf >= 2.6.3
Requires:         cxf-api >= 2.6.3
Requires:         cxf-common >= 2.6.3
Requires:         cxf-rt >= 2.6.3
Requires:         cxf-tools >= 2.6.3
Requires:         dom4j
Requires:         ecj
Requires:         felix-configadmin
Requires:         felix-osgi-core
Requires:         felix-osgi-compendium
Requires:         guava
Requires:         glassfish-jaxb
Requires:         glassfish-saaj
Requires:         gnu-getopt
Requires:         h2
Requires:         hibernate
Requires:         hibernate-entitymanager
Requires:         hibernate-infinispan
Requires:         hibernate-envers
Requires:         hibernate3 >= 3.6.10-7
Requires:         hibernate3-entitymanager >= 3.6.10-7
Requires:         hibernate3-infinispan >= 3.6.10-7
Requires:         hibernate-commons-annotations
Requires:         hibernate-jpa-2.0-api
Requires:         hibernate-validator
Requires:         hornetq
Requires:         httpcomponents-client
Requires:         httpcomponents-core
Requires:         istack-commons
Requires:         infinispan
Requires:         ironjacamar
Requires:         jacorb
Requires:         jackson
Requires:         jandex
Requires:         java >= 1:1.7.0
Requires:         javamail
Requires:         javassist
Requires:         jaxen
Requires:         jaxws-jboss-httpserver-httpspi
Requires:         jettison
Requires:         jbosgi-deployment
Requires:         jbosgi-framework
Requires:         jbosgi-metadata
Requires:         jbosgi-repository
Requires:         jbosgi-resolver1
Requires:         jbosgi-spi
Requires:         jbosgi-vfs
Requires:         jboss-annotations-1.1-api
Requires:         jboss-classfilewriter
Requires:         jboss-common-core
Requires:         jboss-connector-1.6-api
Requires:         jboss-dmr
Requires:         jboss-ejb-3.1-api
Requires:         jboss-ejb3-ext-api
Requires:         jboss-ejb-client
Requires:         jboss-el-2.2-api
Requires:         jboss-httpserver
Requires:         jboss-iiop-client
Requires:         jboss-interceptor
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-invocation
Requires:         jboss-j2eemgmt-1.1-api
Requires:         jboss-jacc-1.4-api
Requires:         jboss-jad-1.2-api
Requires:         jboss-jaxb-2.2-api
Requires:         jboss-jaxb-intros
Requires:         jboss-jaxr-1.0-api
Requires:         jboss-jaxrpc-1.1-api
Requires:         jboss-jaxrs-1.1-api
Requires:         jboss-jaxws-2.2-api
Requires:         jboss-jaspi-1.0-api
Requires:         jboss-jms-1.1-api
Requires:         jboss-jsf-2.1-api
Requires:         jboss-jsp-2.2-api
Requires:         jboss-jstl-1.2-api
Requires:         jboss-jts >= 4.16.2-10
Requires:         jboss-logging
Requires:         jboss-logging-tools
Requires:         jboss-logmanager
Requires:         jboss-logmanager-log4j
Requires:         jboss-marshalling
Requires:         jboss-metadata
Requires:         jboss-modules
Requires:         jboss-msc
Requires:         jboss-negotiation
Requires:         jboss-remoting
Requires:         jboss-remoting-jmx
Requires:         jboss-remote-naming
Requires:         jboss-rmi-1.0-api >= 1.0.4-4
Requires:         jboss-sasl
Requires:         jboss-saaj-1.3-api
Requires:         jboss-servlet-3.0-api
Requires:         jboss-stdio
Requires:         jboss-threads
Requires:         jboss-transaction-1.1-api
Requires:         jboss-transaction-spi
Requires:         jboss-web
Requires:         jboss-web-native
Requires:         jboss-vfs
Requires:         jbossws-api
Requires:         jbossws-common >= 2.0.4-3
Requires:         jbossws-common-tools
Requires:         jbossws-cxf >= 4.1.0
Requires:         jbossws-spi >= 2.1.0
Requires:         jbossws-native >= 4.1.0
Requires:         jbossxb
Requires:         jcip-annotations
Requires:         jdom
Requires:         jgroups
Requires:         jline
Requires:         jul-to-slf4j-stub
Requires:         joda-time
Requires:         javapackages-tools >= 0.7.2-1
Requires:         jpackage-utils
Requires:         jtype
Requires:         jython >= 2.2.1-9
Requires:         mojarra
Requires:         mod_cluster-java >= 1.2.1-2
Requires:         neethi
Requires:         nekohtml
Requires:         netty
Requires:         objectweb-asm
Requires:         openjpa
Requires:         openssl
Requires:         opensaml-java
Requires:         opensaml-java-openws
Requires:         opensaml-java-xmltooling
Requires:         picketbox
Requires:         picketbox-commons
Requires:         picketbox-xacml
Requires:         resteasy >= 2.3.2-7
Requires:         rhq-plugin-annotations
Requires:         scannotation
Requires:         sac
Requires:         serp
Requires:         shrinkwrap
Requires:         shrinkwrap-resolver
Requires:         slf4j
Requires:         slf4j-jboss-logmanager
Requires:         snakeyaml
Requires:         staxmapper
Requires:         stax2-api
Requires:         velocity
Requires:         weld-api
Requires:         weld-core
Requires:         woodstox-core
Requires:         wsdl4j >= 1.6.2-5
Requires:         wss4j >= 1.6.7
Requires:         ws-xmlschema
Requires:         xalan-j2
Requires:         xerces-j2
Requires:         xml-commons-apis
Requires:         xml-commons-resolver
Requires:         xml-security
Requires:         xnio
Requires:         xom
Requires(pre):    shadow-utils
Requires(post):   systemd-units
Requires(preun):  systemd-units
Requires(postun): systemd-units

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

git init
git config user.email "jboss-as-owner@fedoraproject.org"
git config user.name "JBoss AS package owner"
git add .
git commit -a -q -m "%{version} baseline."

git am %{patches}

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"
%pom_xpath_remove "pom:build/pom:extensions" build-config/pom.xml

%build
export MAVEN_OPTS="-Xms512m -Xmx1024m -XX:PermSize=128m -XX:MaxPermSize=384m"

# We don't have packaged all test dependencies (jboss-test for example)
mvn-rpmbuild -Dmaven.test.skip=true -e install javadoc:aggregate

%install

install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{homedir}
install -d -m 755 $RPM_BUILD_ROOT%{confdir}
install -d -m 755 $RPM_BUILD_ROOT%{rundir}
install -d -m 770 $RPM_BUILD_ROOT%{cachedir}/auth
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -d -m 755 $RPM_BUILD_ROOT%{_unitdir}
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}

for mode in standalone domain; do
  install -d -m 755 $RPM_BUILD_ROOT%{homedir}/${mode}
  install -d -m 775 $RPM_BUILD_ROOT%{libdir}/${mode}/data
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}
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
multimodules="arquillian domain-http clustering jpa osgi webservices"
# If a submodule contains hyphen in the name, just skip it, e.g. domain-http => domainhttp
modules_arquillian="common container-managed container-remote protocol-jmx testenricher-msc"
modules_clustering="api common impl jgroups infinispan registry service singleton web-spi web-infinispan ejb3-infinispan"
modules_jpa="util spi openjpa hibernate3 hibernate4"
modules_domainhttp="interface error-context"
modules_osgi="service configadmin"
modules_webservices="server-integration tests-integration"

for m in ${multimodules}; do
  # POM
  cp -a ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}-parent.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}-parent.pom

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

for m in jdr sos; do
  # JAR
  cp -a jdr/jboss-as-${m}/target/jboss-as-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  cp -a jdr/jboss-as-${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# POMs
cp -a jpa/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-jpa-parent.pom
cp -a jdr/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-jdr-parent.pom
cp -a spec-api/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-spec-api.pom

# Depmaps
%add_maven_depmap JPP.%{name}-%{name}-jpa-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-jdr-parent.pom
%add_maven_depmap JPP.%{name}-%{name}-spec-api.pom

# Exceptions END

# Parent POM
cp -a pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# Depmap for parent POM
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# Apidocs
cp -a target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

pushd build/target/jboss-as-%{namedversion}
  # We don't need Windows files
  find bin/ -type f -name "*.bat" -delete

  # Install systemd files
  mv bin/initscripts/systemd/jboss-as.conf $RPM_BUILD_ROOT%{confdir}/%{name}.conf
  mv bin/initscripts/systemd/jboss-as.service $RPM_BUILD_ROOT%{_unitdir}/%{name}.service

  # We don't need legacy init scripts
  rm -rf bin/initscripts

  # Prepare directory for properties files
  install -d -m 755 docs/examples/properties

  # Copy logging.properties and mgmt-users.properties so we can reuse it later in jboss-as-cp script
  cp standalone/configuration/logging.properties docs/examples/properties/
  cp standalone/configuration/mgmt-users.properties docs/examples/properties/
  # Lower a bit the permissions, so ordinary user can copy it. It's an example file!
  chmod 644 docs/examples/properties/mgmt-users.properties

  # standalone
  mv standalone/configuration $RPM_BUILD_ROOT%{confdir}/standalone
  mv standalone/deployments $RPM_BUILD_ROOT%{libdir}/standalone/deployments
  mv standalone/lib $RPM_BUILD_ROOT%{libdir}/standalone/lib
  mv standalone/tmp $RPM_BUILD_ROOT%{cachedir}/standalone/tmp

  # Install standalone-web.xml
  cp docs/examples/configs/standalone-web.xml $RPM_BUILD_ROOT%{confdir}/standalone/standalone-web.xml

  # domain
  mv domain/configuration $RPM_BUILD_ROOT%{confdir}/domain
  mv domain/tmp $RPM_BUILD_ROOT%{cachedir}/domain/tmp

  # Remove all jars from modules directory - we need to symlink them
  # TODO temporary with verbose, use -delete afterwards
  find . -type f -name "*.jar" -exec rm -rvf {} \;

  # TMP - investigate
  rm -rf bin/client

  mv copyright.txt README.txt LICENSE.txt welcome-content docs bin appclient modules $RPM_BUILD_ROOT%{homedir}
popd

chmod 775 $RPM_BUILD_ROOT%{libdir}/standalone/deployments

pushd $RPM_BUILD_ROOT%{homedir}

  # Standalone
  ln -s %{confdir}/standalone standalone/configuration
  ln -s %{libdir}/standalone/deployments standalone/deployments
  ln -s %{libdir}/standalone/data standalone/data
  ln -s %{libdir}/standalone/lib standalone/lib
  ln -s %{logdir}/standalone standalone/log
  ln -s %{cachedir}/standalone/tmp standalone/tmp

  # Domain
  ln -s %{confdir}/domain domain/configuration
  ln -s %{libdir}/domain/data domain/data
  ln -s %{logdir}/domain domain/log
  ln -s %{cachedir}/domain/tmp domain/tmp

  # Symlink jboss-modules
  ln -s $(build-classpath jboss-modules) jboss-modules.jar
  
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
    ln -s %{_javadir}/jboss-as/jboss-as-jpa-hibernate3.jar org/jboss/as/jpa/hibernate/3/jboss-as-jpa-hibernate3-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-jpa-hibernate4.jar org/jboss/as/jpa/hibernate/4/jboss-as-jpa-hibernate4-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-jdr.jar org/jboss/as/jdr/main/jboss-as-jdr-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-sos.jar org/jboss/as/jdr/main/jboss-as-sos-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-osgi-service.jar org/jboss/as/osgi/main/jboss-as-osgi-service-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-webservices-server-integration.jar org/jboss/as/webservices/main/jboss-as-webservices-server-integration-%{namedversion}.jar

    # Remove native libs that are shipped with the source distribution...
    rm -rf org/hornetq/main/lib/*

    # Prepare directories for native libs
    install -d -m 755 org/jboss/as/web/main/lib/linux-{x86_64,i686}
    install -d -m 755 org/hornetq/main/lib/linux-{x86_64,i686}

    # Please keep alphabetic by jar name

    for m in codec collections configuration io lang logging; do
      ln -s $(build-classpath apache-commons-${m}) org/apache/commons/${m}/main/commons-${m}.jar
    done

    for m in beanutils cli configuration pool; do
      ln -s $(build-classpath apache-commons-${m}) org/apache/commons/${m}/main/apache-commons-${m}.jar
    done

    ln -s $(build-classpath apache-juddi/juddi-client) org/apache/juddi/juddi-client/main/juddi-client.jar
    ln -s $(build-classpath apache-juddi/uddi-ws) org/apache/juddi/uddi-ws/main/uddi-ws.jar
    ln -s $(build-classpath apache-scout) org/apache/juddi/scout/main/scout.jar

    for m in core dom storage; do
      ln -s $(build-classpath apache-mime4j/${m}) org/apache/james/mime4j/main/${m}.jar
    done

    ln -s $(build-classpath antlr) org/antlr/main/antlr.jar
    # Make sure we don't specify the version suffix in the jar name for antlr
    # TODO report a bug and fix this properly
    sed -i "s|antlr.*\.jar|antlr\.jar|" org/antlr/main/module.xml

    ln -s $(build-classpath atinject) javax/inject/api/main/atinject.jar
    ln -s $(build-classpath cal10n/cal10n-api) ch/qos/cal10n/main/cal10n-api.jar
    ln -s $(build-classpath cdi-api) javax/enterprise/api/main/cdi-api.jar

    for m in api rt-bindings-coloc rt-bindings-object rt-bindings-soap \
             rt-bindings-xml rt-core rt-databinding-aegis rt-databinding-jaxb rt-frontend-jaxws \
             rt-frontend-simple rt-management rt-transports-http rt-transports-jms \
             rt-transports-local rt-ws-addr rt-ws-mex rt-ws-policy rt-ws-rm rt-ws-security \
             tools-common tools-java2ws tools-validator tools-wsdlto-core tools-wsdlto-databinding-jaxb \
             tools-wsdlto-frontend-jaxws services-sts-core; do
      ln -s $(build-classpath cxf/${m}) org/apache/cxf/impl/main/${m}.jar
    done

    ln -s $(build-classpath cxf/api) org/apache/cxf/main/api.jar

    for m in xjc-boolean xjc-dv xjc-ts; do
      ln -s $(build-classpath cxf-xjc-utils/cxf-${m}) org/apache/cxf/impl/main/cxf-${m}.jar
    done

    ln -s $(build-classpath cssparser) net/sourceforge/cssparser/main/cssparser.jar
    ln -s $(build-classpath dom4j) org/dom4j/main/dom4j.jar
    ln -s $(build-classpath ecj) org/jboss/as/web/main/ecj.jar
    ln -s $(build-classpath guava) com/google/guava/main/guava.jar
    ln -s $(build-classpath glassfish-jaxb/jaxb-impl) com/sun/xml/bind/main/jaxb-impl.jar
    ln -s $(build-classpath glassfish-jaxb/jaxb-xjc) com/sun/xml/bind/main/jaxb-xjc.jar
    ln -s $(build-classpath glassfish-saaj) com/sun/xml/messaging/saaj/main/glassfish-saaj.jar

    ln -s $(build-classpath gnu-getopt) gnu/getopt/main/gnu-getopt.jar
    # Make sure we don't specify the version suffix in the jar name for gnu-getopt
    # TODO report a bug and fix this properly
    sed -i "s|gnu-getopt.*\.jar|gnu-getopt\.jar|" gnu/getopt/main/module.xml

    ln -s $(build-classpath bean-validation-api) javax/validation/api/main/bean-validation-api.jar
    ln -s $(build-classpath h2) com/h2database/h2/main/h2.jar
    ln -s $(build-classpath hibernate-validator) org/hibernate/validator/main/hibernate-validator.jar
    ln -s $(build-classpath jtype) com/googlecode/jtype/main/jtype.jar
    ln -s $(build-classpath hibernate-jpa-2.0-api) javax/persistence/api/main/hibernate-jpa-2.0-api.jar

    ln -s $(build-classpath hibernate3/hibernate-core-3) org/hibernate/3/hibernate-core.jar
    ln -s $(build-classpath hibernate3/hibernate-entitymanager-3) org/hibernate/3/hibernate-entitymanager.jar
    ln -s $(build-classpath hibernate3/hibernate-infinispan-3) org/hibernate/3/hibernate-infinispan.jar
    ln -s $(build-classpath hibernate/hibernate-commons-annotations) org/hibernate/3/hibernate-commons-annotations.jar

    ln -s $(build-classpath hibernate/hibernate-core) org/hibernate/main/hibernate-core.jar
    ln -s $(build-classpath hibernate/hibernate-entitymanager) org/hibernate/main/hibernate-entitymanager.jar
    ln -s $(build-classpath hibernate/hibernate-infinispan) org/hibernate/main/hibernate-infinispan.jar
    ln -s $(build-classpath hibernate/hibernate-commons-annotations) org/hibernate/main/hibernate-commons-annotations.jar
    ln -s $(build-classpath hibernate/hibernate-envers) org/hibernate/envers/main/hibernate-envers.jar

    ln -s $(build-classpath hornetq/hornetq-core) org/hornetq/main/hornetq-core.jar
    ln -s $(build-classpath hornetq/hornetq-jms) org/hornetq/main/hornetq-jms.jar
    ln -s $(build-classpath hornetq/hornetq-ra) org/hornetq/ra/main/hornetq-ra.jar

    ln -s $(build-classpath httpcomponents/httpclient) org/apache/httpcomponents/main/httpclient.jar
    ln -s $(build-classpath httpcomponents/httpcore) org/apache/httpcomponents/main/httpcore.jar
    ln -s $(build-classpath httpcomponents/httpmime) org/apache/httpcomponents/main/httpmime.jar

    ln -s $(build-classpath istack-commons-runtime) com/sun/xml/bind/main/istack-commons-runtime.jar

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

    for m in jackson-core-asl jackson-jaxrs jackson-mapper-asl jackson-xc; do
      ln -s $(build-classpath jackson/${m}) org/codehaus/jackson/${m}/main/${m}.jar
    done

    ln -s $(build-classpath jacorb) org/jacorb/main/jacorb.jar
    ln -s $(build-classpath javamail/mail) javax/mail/api/main/mail.jar
    ln -s $(build-classpath javassist) org/javassist/main/javassist.jar
    ln -s $(build-classpath jaxen) org/jaxen/main/jaxen.jar
    ln -s $(build-classpath jaxws-jboss-httpserver-httpspi) org/jboss/ws/jaxws-jboss-httpserver-httpspi/main/jaxws-jboss-httpserver-httpspi.jar
    ln -s $(build-classpath jcip-annotations) net/jcip/main/jcip-annotations.jar
    ln -s $(build-classpath jandex) org/jboss/jandex/main/jandex.jar
    ln -s $(build-classpath jboss-jaxrs-1.1-api) javax/ws/rs/api/main/jaxrs-api.jar

    ln -s $(build-classpath jbosgi-deployment) org/jboss/osgi/framework/main/jbosgi-deployment.jar
    ln -s $(build-classpath jbosgi-framework-core) org/jboss/osgi/framework/main/jbosgi-framework-core.jar
    ln -s $(build-classpath jbosgi-metadata) org/jboss/osgi/metadata/main/jbosgi-metadata.jar
    ln -s $(build-classpath jbosgi-repository/jbosgi-repository-api) org/jboss/osgi/repository/main/jbosgi-repository-api.jar
    ln -s $(build-classpath jbosgi-repository/jbosgi-repository-core) org/jboss/osgi/repository/main/jbosgi-repository-core.jar
    ln -s $(build-classpath jbosgi-resolver1/jbosgi-resolver1-spi) org/jboss/osgi/framework/main/jbosgi-resolver1-spi.jar
    ln -s $(build-classpath jbosgi-resolver1/jbosgi-resolver1-api) org/jboss/osgi/framework/main/jbosgi-resolver1-api.jar
    ln -s $(build-classpath jbosgi-resolver1/jbosgi-resolver1-felix) org/jboss/osgi/framework/main/jbosgi-resolver1-felix.jar
    ln -s $(build-classpath jbosgi-spi) org/jboss/osgi/spi/main/jbosgi-spi.jar
    ln -s $(build-classpath jbosgi-vfs-vfs) org/jboss/osgi/vfs/main/jbosgi-vfs-vfs.jar
    ln -s $(build-classpath jbosgi-vfs-vfs30) org/jboss/osgi/vfs/main/jbosgi-vfs-vfs30.jar

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
    ln -s $(build-classpath jboss-j2eemgmt-1.1-api) javax/management/j2ee/api/main/jboss-j2eemgmt-1.1-api.jar
    ln -s $(build-classpath jboss-jacc-1.4-api) javax/security/jacc/api/main/jboss-jacc-1.4-api.jar
    ln -s $(build-classpath jboss-jad-1.2-api) javax/enterprise/deploy/api/main/jboss-jad-1.2-api.jar
    ln -s $(build-classpath jboss-jaxb-2.2-api) javax/xml/bind/api/main/jboss-jaxb-2.2-api.jar
    ln -s $(build-classpath jboss-jaxb-intros) org/jboss/jaxbintros/main/jboss-jaxb-intros.jar
    ln -s $(build-classpath jboss-jaxr-1.0-api) javax/xml/registry/api/main/jboss-jaxr-1.0-api.jar
    ln -s $(build-classpath jboss-jaxrpc-1.1-api) javax/xml/rpc/api/main/jboss-jaxrpc-1.1-api.jar
    ln -s $(build-classpath jboss-jaxrs-1.1-api) javax/ws/rs/api/main/jboss-jaxrs-1.1-api.jar
    ln -s $(build-classpath jboss-jaxws-2.2-api) javax/xml/ws/api/main/jboss-jaxws-2.2-api.jar
    ln -s $(build-classpath jboss-jaspi-1.0-api) javax/security/auth/message/api/main/jboss-jaspi-1.0-api.jar
    ln -s $(build-classpath jboss-jms-1.1-api) javax/jms/api/main/jboss-jms-1.1-api.jar
    ln -s $(build-classpath jboss-jsf-2.1-api) javax/faces/api/main/jboss-jsf-2.1-api.jar
    ln -s $(build-classpath jboss-jsp-2.2-api) javax/servlet/jsp/api/main/jboss-jsp-2.2-api.jar
    ln -s $(build-classpath jboss-jstl-1.2-api) javax/servlet/jstl/api/main/jboss-jstl-1.2-api.jar
    ln -s $(build-classpath jboss-jts/jbossjts) org/jboss/jts/main/jbossjts.jar
    ln -s $(build-classpath jboss-jts/jbossjts-integration) org/jboss/jts/integration/main/jbossjts-integration.jar
    ln -s $(build-classpath jboss-jts/jbossxts) org/jboss/xts/main/jbossxts.jar
    ln -s $(build-classpath jboss-jts/jbossxts-api) org/jboss/xts/main/jbossxts-api.jar
    ln -s $(build-classpath jboss-jts/jbosstxbridge) org/jboss/xts/main/jbosstxbridge.jar
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
    ln -s $(build-classpath jbossws-api) org/jboss/ws/api/main/jbossws-api.jar
    ln -s $(build-classpath jbossws-common) org/jboss/ws/common/main/jbossws-common.jar
    ln -s $(build-classpath jbossws-common-tools) org/jboss/ws/tools/common/main/jbossws-common-tools.jar
    ln -s $(build-classpath jbossws-spi) org/jboss/ws/spi/main/jbossws-spi.jar

    for m in jbossws-cxf-factories jbossws-cxf-transports-httpserver jbossws-cxf-server; do
      ln -s $(build-classpath jbossws-cxf/${m}) org/jboss/ws/cxf/${m}/main/${m}.jar
    done

    ln -s $(build-classpath jbossws-cxf/jbossws-cxf-client) org/jboss/ws/jaxws-client/main/jbossws-cxf-client.jar
    ln -s $(build-classpath jbossws-cxf/jbossws-cxf-resources-jboss711) org/jboss/as/webservices/main/jbossws-cxf-resources.jar

    ln -s $(build-classpath jbossws-native/jbossws-native-core) org/jboss/ws/native/jbossws-native-core/main/jbossws-native-core.jar
    ln -s $(build-classpath jbossws-native/jbossws-native-services) org/jboss/ws/native/jbossws-native-services/main/jbossws-native-services.jar

    ln -s $(build-classpath jbossxb) org/jboss/xb/main/jbossxb.jar
    ln -s $(build-classpath jdom) org/jdom/main/jdom.jar
    ln -s $(build-classpath jgroups) org/jgroups/main/jgroups.jar
    ln -s $(build-classpath jettison) org/codehaus/jettison/main/jettison.jar
    ln -s $(build-classpath jline) jline/main/jline.jar
    ln -s $(build-classpath jul-to-slf4j-stub) org/jboss/logging/jul-to-slf4j-stub/main/jul-to-slf4j-stub.jar
    ln -s $(build-classpath joda-time) org/joda/time/main/joda-time.jar
    ln -s $(build-classpath log4j) org/apache/log4j/main/log4j.jar
    ln -s $(build-classpath jython) org/python/jython/standalone/main/jython.jar
    ln -s $(build-classpath mojarra/jsf-impl) com/sun/jsf-impl/main/jsf-impl.jar

    for m in container-catalina container-jbossweb container-spi core; do
      ln -s $(build-classpath mod_cluster/${m}) org/jboss/as/modcluster/main/${m}.jar
    done

    # TODO remove this when netty >= 3.5.10-1 will be available
    ln -s $(build-classpath netty) org/jboss/netty/main/netty31.jar
    ln -s $(build-classpath netty) org/jboss/netty/main/netty.jar
    ln -s $(build-classpath neethi) org/apache/neethi/main/neethi.jar
    ln -s $(build-classpath nekohtml) net/sourceforge/nekohtml/main/nekohtml.jar
    ln -s $(build-classpath objectweb-asm/asm) asm/asm/main/asm.jar

    ln -s $(build-classpath openjpa/kernel) org/apache/openjpa/main/kernel.jar
    ln -s $(build-classpath openjpa/lib) org/apache/openjpa/main/lib.jar
    ln -s $(build-classpath openjpa/persistence) org/apache/openjpa/main/persistence.jar
    ln -s $(build-classpath openjpa/persistence-jdbc) org/apache/openjpa/main/persistence-jdbc.jar
    ln -s $(build-classpath openjpa/jdbc) org/apache/openjpa/main/jdbc.jar

    ln -s $(build-classpath opensaml-java) org/opensaml/main/opensaml-java.jar
    ln -s $(build-classpath opensaml-java-openws) org/opensaml/main/opensaml-java-openws.jar
    ln -s $(build-classpath opensaml-java-xmltooling) org/opensaml/main/opensaml-java-xmltooling.jar
    ln -s $(build-classpath felix/org.osgi.core) org/osgi/core/main/org.osgi.core.jar
    ln -s $(build-classpath felix/org.osgi.compendium) org/jboss/osgi/framework/main/org.osgi.compendium.jar
    ln -s $(build-classpath picketbox/picketbox) org/picketbox/main/picketbox.jar
    ln -s $(build-classpath picketbox/infinispan) org/picketbox/main/infinispan.jar
    ln -s $(build-classpath picketbox-commons) org/picketbox/main/picketbox-commons.jar
    ln -s $(build-classpath picketbox-xacml) org/jboss/security/xacml/main/picketbox-xacml.jar

    for m in atom-provider cdi jackson-provider jaxb-provider jaxrs jettison-provider jsapi multipart-provider yaml-provider; do
      ln -s $(build-classpath resteasy/resteasy-${m}) org/jboss/resteasy/resteasy-${m}/main/resteasy-${m}.jar
      # Jandex indexes
      ln -s $(build-classpath resteasy/resteasy-${m}-jandex) org/jboss/resteasy/resteasy-${m}/main/resteasy-${m}-jandex.jar
    done

    # RestEasy exception
    ln -s $(build-classpath resteasy/async-http-servlet-3.0) org/jboss/resteasy/resteasy-jaxrs/main/async-http-servlet-3.0.jar

    ln -s $(build-classpath sac) org/w3c/css/sac/main/sac.jar
    ln -s $(build-classpath scannotation) org/scannotation/scannotation/main/scannotation.jar
    ln -s $(build-classpath serp) net/sourceforge/serp/main/serp.jar

    ln -s $(build-classpath shrinkwrap/api) org/jboss/shrinkwrap/core/main/api.jar
    ln -s $(build-classpath shrinkwrap/spi) org/jboss/shrinkwrap/core/main/spi.jar
    ln -s $(build-classpath shrinkwrap/impl-base) org/jboss/shrinkwrap/core/main/impl-base.jar

    ln -s $(build-classpath slf4j/api) org/slf4j/main/api.jar
    ln -s $(build-classpath slf4j/api) org/slf4j/main/slf4j-api.jar
    ln -s $(build-classpath slf4j/ext) org/slf4j/ext/main/ext.jar
    ln -s $(build-classpath slf4j/ext) org/slf4j/ext/main/slf4j-ext.jar

    ln -s $(build-classpath slf4j/jcl-over-slf4j) org/slf4j/jcl-over-slf4j/main/jcl-over-slf4j.jar
    ln -s $(build-classpath slf4j-jboss-logmanager) org/slf4j/impl/main/slf4j-jboss-logmanager.jar
    ln -s $(build-classpath snakeyaml) org/yaml/snakeyaml/main/snakeyaml.jar
    ln -s $(build-classpath staxmapper) org/jboss/staxmapper/main/staxmapper.jar
    ln -s $(build-classpath stax2-api) org/codehaus/woodstox/main/stax2-api.jar
    ln -s $(build-classpath txw2) com/sun/xml/bind/main/txw2.jar
    ln -s $(build-classpath velocity) org/apache/velocity/main/velocity.jar
    ln -s $(build-classpath weld-api/weld-api) org/jboss/weld/api/main/weld-api.jar
    ln -s $(build-classpath weld-api/weld-spi) org/jboss/weld/spi/main/weld-spi.jar
    ln -s $(build-classpath weld-core) org/jboss/weld/core/main/weld-core.jar
    ln -s $(build-classpath woodstox-core-asl) org/codehaus/woodstox/main/woodstox-core-asl.jar
    ln -s $(build-classpath wsdl4j) javax/wsdl4j/api/main/wsdl4j.jar
    ln -s $(build-classpath wss4j) org/apache/ws/security/main/wss4j.jar
    ln -s $(build-classpath xalan-j2) org/apache/xalan/main/xalan-j2.jar
    ln -s $(build-classpath xalan-j2-serializer) org/apache/xalan/main/xalan-j2-serializer.jar
    ln -s $(build-classpath xerces-j2) org/apache/xerces/main/xerces-j2.jar
    ln -s $(build-classpath xml-security) org/apache/santuario/xmlsec/main/xml-security.jar
    ln -s $(build-classpath xmlschema-core) org/apache/ws/xmlschema/main/xmlschema-core.jar
    ln -s $(build-classpath xml-commons-apis) org/apache/xerces/main/xml-commons-apis.jar
    # TODO: remove this when xml-commons-resolver >= 1.2-11 will be available
    ln -s $(build-classpath xml-commons-resolver) org/apache/xml-resolver/main/xml-resolver-1.2.jar
    ln -s $(build-classpath xml-commons-resolver) org/apache/xml-resolver/main/xml-commons-resolver.jar
    ln -s $(build-classpath xnio-api) org/jboss/xnio/main/xnio-api.jar
    ln -s $(build-classpath xnio-nio) org/jboss/xnio/nio/main/xnio-nio.jar
    ln -s $(build-classpath xom) nu/xom/main/xom.jar
  popd
popd

pushd $RPM_BUILD_ROOT%{_bindir}
  # jboss-cli
  ln -s %{bindir}/jboss-cli.sh jboss-cli

  install -m 755 %{SOURCE1} jboss-as-cp
popd

%pre
# Add jboss-as user and group
getent group %{name} >/dev/null || groupadd -r %{name} -g %{jbuid}
getent passwd %{name} >/dev/null || \
    useradd -c "JBoss AS" -u %{jbuid} -g %{name} -s /bin/nologin -r -d %{homedir} %{name}
exit 0

%post
# AS7 relies on some arch specific binary modules, let's link them.
# We don't want to do this at build time because it should be still noarch package.
arch=`uname -m`

if [ "${arch}" = "x86_64" ]; then
  libdir="/usr/lib64"
else
  libdir="/usr/lib"
fi

pushd %{homedir}/modules/org/hornetq/main/lib/linux-${arch} > /dev/null
  ln -sf ${libdir}/libHornetQAIO.so.0 libHornetQAIO.so
popd > /dev/null

pushd %{homedir}/modules/org/jboss/as/web/main/lib/linux-${arch} > /dev/null
  ln -sf ${libdir}/libjbnative-1.so.0 libtcnative-1.so
  ln -sf ${libdir}/libapr-1.so.0 libapr-1.so
  ln -sf ${libdir}/libcrypto.so libcrypto.so
  ln -sf ${libdir}/libssl.so libssl.so
popd > /dev/null

# Systemd
%if 0%{?fedora} > 17

%systemd_post jboss-as.service

%else

if [ $1 -eq 1 ] ; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%endif

%preun
# Let's clean up the arch-specific symlinks
arch=`uname -m`

rm -rf %{homedir}/modules/org/jboss/as/web/main/lib/linux-${arch}/*
rm -rf %{homedir}/modules/org/hornetq/main/lib/linux-${arch}/*

# Systemd
%if 0%{?fedora} > 17

%systemd_preun jboss-as.service

%else

if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable jboss-as.service > /dev/null 2>&1 || :
    /bin/systemctl stop jboss-as.service > /dev/null 2>&1 || :
fi

%endif

%postun

# Systemd
%if 0%{?fedora} > 17

%systemd_postun_with_restart jboss-as.service

%else

/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart jboss-as.service >/dev/null 2>&1 || :
fi

%endif

%files
%{homedir}/appclient
%dir %{bindir}
%{bindir}/*.conf
%{bindir}/*.sh
%{bindir}/*.xml
%{_bindir}/*
%{homedir}/auth
%{homedir}/domain
%{homedir}/standalone
%{homedir}/modules
%{homedir}/welcome-content
%{homedir}/jboss-modules.jar
%attr(-,root,jboss-as) %{libdir}/standalone
%attr(-,root,jboss-as) %{libdir}/domain
%attr(0775,root,jboss-as) %dir %{rundir}
%attr(0775,root,jboss-as) %dir %{cachedir}/standalone/tmp
%attr(0775,root,jboss-as) %dir %{cachedir}/domain/tmp
%attr(0770,root,jboss-as) %dir %{logdir}/standalone
%attr(0770,root,jboss-as) %dir %{logdir}/domain
%attr(0775,root,jboss-as) %dir %{confdir}/standalone
%attr(0775,root,jboss-as) %dir %{confdir}/domain
%attr(0700,jboss-as,jboss-as) %dir %{cachedir}/auth
%attr(0600,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.xml
%attr(0600,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.xml
%config(noreplace) %{confdir}/%{name}.conf
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
%doc %{homedir}/LICENSE.txt

%changelog
* Tue Feb 19 2013 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-16
- Remove wagon extension

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 7.1.1-14
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Dec 04 2012 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-13
- Rebasing patches

* Wed Nov 28 2012 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-12
- Fixing many missing symlinks
- Make standalone.xml the default configuration instead standalone-web.xml
- Add an easy way to override the default bind address for systemd service

* Tue Nov 20 2012 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-11
- Add webservices support based on CXF 2.6.3
- The jackson modules don't have symlinks to .jar files, RHBZ#879008
- The jettison modules doesn't have symlinks to .jar, RHBZ#879009
- The mime4j module doesn't have symlinks to .jar files, RHBZ#879014
- The snakeyaml modules doesn't have symlinks to .jar, RHBZ#879017
- The com.sun.xml.bind needs to include the istack-commons-runtime.jar file, RHBZ#879020

* Tue Nov 06 2012 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-10
- Added Hibernate 4 (default persistence provider) support
- Preparations for webservice-related modules from CXF
- Use static GID, RHBZ#873897

* Tue Sep 18 2012 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-9
- Introduce new systemd-rpm macros in jboss-as spec file, RHBZ#856680
- Added org.jboss.as.xts module

* Thu Aug 30 2012 Marek Goldmann <mgoldman@redhat.com> - 7.1.1-8
- Added org.jboss.as.jpa.jacorb module

* Thu Aug 23 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.1-7
- Added org.jboss.as.jpa.openjpa module
- Added org.jboss.as.jpa.hibernate3 module
- Added jtype dependency to hibernate-validator to fix NoClassDefFoundError exception
- Regenerated patches with git format-patch --no-numbered --no-signature
- Added ExampleDS to the standalone-web.xml config

* Wed Aug 01 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.1-6
- /usr/bin conflict between jboss-as-7.1.1-4 and filesystem-3.1-1, RHBZ#839419
- Missing symlinks RHBZ#842997, RHBZ#842996
- Fixed BR
- Fixed empty version requirement for org.eclipse.jdt:core

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 04 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.1-4
- jboss-as-cp script is missing argument placeholder for c optarg, RHBZ#827571
- Create a startup script when creating a new user instance (jboss-as-cp), RHBZ#827588
- The user instance create script (jboss-as-cp) should allow a port offset to be specified, RHBZ#827589
- Added org.jboss.as.modcluster module
- Added org.jboss.as.jsr77 module
- Added org.jboss.as.arquillian module
- Added org.jboss.as.osgi module
- Added org.jboss.as.configadmin module
- Added org.jboss.as.spec-api module
- Add ExampleDS based on H2 database, RHBZ#81252

* Fri May 11 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.1-3
- Changed the way we apply patches at build time
- Added org.jboss.as.sar module
- Added org.jboss.as.host-controller module
- Added org.jboss.as.jaxr module
- Added org.jboss.as.messaging module

* Wed May 02 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.1-2
- Link to native  modules in post section to avoid arch-specific Requires

* Fri Apr 20 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.1-1
- Upstream release 7.1.1.Final
- Added jboss-as-cmp module
- Added jboss-as-mail module
- Added jboss-as-jaxrs module
- Added jboss-as-pojo module
- Spec file cleanup from versions

* Mon Apr 16 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.0-3
- Simplified systemd files
- Added jboss-as-cli module
- Make it possible to run as different user in different direcotry by changing JBOSS_BASE_DIR
- Fixed issues with using add-user.sh script
- Changed validation API jar to bean-validation
- Added jboss-as-cp script to be able to use JBoss AS from different dir as different user
- Removed activation AS7 module - it's already in JDK
- Make it possible to add a user also when JBoss AS is run from different directory

* Wed Apr 04 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.0-2
- Fixed rpmlint issues
- Fixed license
- Added LICENSE.txt file to javadoc subpackage
- Use standalone-web.xml config from docs as default

* Mon Apr 02 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.0-1
- Initial packaging

