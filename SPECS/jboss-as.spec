%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

%global cachedir %{_var}/cache/%{name}
%global homedir %{_datadir}/%{name}
%global bindir %{homedir}/bin
%global logdir %{_var}/log/%{name}
%global confdir %{_sysconfdir}/%{name}

%global jbuid 92

%global modules controller-client controller deployment-repository domain-management ee embedded jmx logging naming network platform-mbean process-controller protocol remoting security server transactions
%global modules_clustering common infinispan jgroups

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

BuildArch:        noarch

# Please keep alphabetically
BuildRequires:    ant-apache-bsf
BuildRequires:    apache-james-project
BuildRequires:    bean-validation-api
BuildRequires:    bsf >= 2.4.0-10
BuildRequires:    dom4j
BuildRequires:    geronimo-annotation
BuildRequires:    h2
BuildRequires:    hibernate-validator >= 4.2.0
BuildRequires:    infinispan >= 5.1.1-1
BuildRequires:    jandex >= 1.0.3
BuildRequires:    java-devel
BuildRequires:    jgroups
BuildRequires:    jboss-annotations-1.1-api
BuildRequires:    jboss-connector-1.6-api
BuildRequires:    jboss-dmr >= 1.1.1-1
BuildRequires:    jboss-ejb-3.1-api
BuildRequires:    jboss-httpserver >= 1.0.0-0.3.Beta3
BuildRequires:    jboss-invocation
BuildRequires:    jboss-interceptor >= 2.0.0-1
BuildRequires:    jboss-interceptors-1.1-api
BuildRequires:    jboss-jad-1.2-api
BuildRequires:    jboss-jts
BuildRequires:    jboss-parent
BuildRequires:    jboss-logging >= 3.1.0-0.1.CR1
BuildRequires:    jboss-logging-tools >= 1.0.0-1
BuildRequires:    jboss-logmanager-log4j >= 1.0.0
BuildRequires:    jboss-marshalling >= 1.3.4
BuildRequires:    jboss-metadata >= 7.0.0-1
BuildRequires:    jboss-modules >= 1.1.1-1
BuildRequires:    jboss-msc >= 1.0.1
BuildRequires:    jboss-negotiation
BuildRequires:    jboss-remoting >= 3.2.2
BuildRequires:    jboss-remoting-jmx
BuildRequires:    jboss-remote-naming >= 1.0.1
BuildRequires:    jboss-sasl >= 1.0.0-0.1.Beta9
BuildRequires:    jboss-stdio >= 1.0.1
BuildRequires:    jboss-specs-parent
BuildRequires:    jboss-threads >= 2.0.0
BuildRequires:    jboss-transaction-1.1-api
BuildRequires:    jboss-transaction-spi
BuildRequires:    jboss-vfs >= 3.1.0-0.1.CR1
BuildRequires:    jbossws-api
BuildRequires:    jline
BuildRequires:    jpackage-utils
BuildRequires:    maven
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-checkstyle-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    picketbox
BuildRequires:    picketbox-commons
BuildRequires:    rhq-plugin-annotations
BuildRequires:    staxmapper >= 1.1.0
BuildRequires:    xnio >= 3.0.0-0.2.CR5

Requires:         bean-validation-api
Requires:         dom4j
Requires:         geronimo-annotation
Requires:         h2
Requires:         hibernate-validator >= 4.2.0
Requires:         infinispan >= 5.1.1-1
Requires:         jandex >= 1.0.3
Requires:         java
Requires:         jboss-annotations-1.1-api
Requires:         jboss-connector-1.6-api
Requires:         jboss-dmr >= 1.1.1-1
Requires:         jboss-ejb-3.1-api
Requires:         jboss-httpserver >= 1.0.0-0.3.Beta3
Requires:         jboss-interceptor >= 2.0.0-1
Requires:         jboss-interceptors-1.1-api
Requires:         jboss-invocation
Requires:         jboss-jts
Requires:         jboss-logging >= 3.1.0-0.1.CR1
Requires:         jboss-logging-tools >= 1.0.0-1
Requires:         jboss-jad-1.2-api
Requires:         jboss-logmanager-log4j >= 1.0.0
Requires:         jboss-marshalling >= 1.3.4
Requires:         jboss-metadata >= 7.0.0-1
Requires:         jboss-modules >= 1.1.0-0.1.CR4
Requires:         jboss-msc >= 1.0.1
Requires:         jboss-negotiation
Requires:         jboss-remoting >= 3.2.2
Requires:         jboss-remoting-jmx
Requires:         jboss-remote-naming >= 1.0.1
Requires:         jboss-sasl >= 1.0.0-0.1.Beta9
Requires:         jboss-stdio >= 1.0.1
Requires:         jboss-threads >= 2.0.0
Requires:         jboss-transaction-1.1-api
Requires:         jboss-transaction-spi
Requires:         jboss-vfs >= 3.1.0-0.1.CR1
Requires:         jbossws-api
Requires:         jgroups
Requires:         jline
Requires:         jpackage-utils
Requires:         picketbox
Requires:         picketbox-commons
Requires:         rhq-plugin-annotations
Requires:         staxmapper >= 1.1.0
Requires:         xnio >= 3.0.0-0.2.CR5
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

%build
# We don't have packaged all test dependencies (jboss-test for example)
mvn-rpmbuild -Dmaven.test.skip=true -Dminimalistic -e install javadoc:aggregate

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/init.d
install -d -m 755 $RPM_BUILD_ROOT%{homedir}
install -d -m 755 $RPM_BUILD_ROOT%{confdir}
install -d -m 770 $RPM_BUILD_ROOT%{cachedir}/auth
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}

for mode in standalone domain; do
  install -d -m 755 $RPM_BUILD_ROOT%{homedir}/${mode}
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}/data
  install -d -m 755 $RPM_BUILD_ROOT%{cachedir}/${mode}/tmp
  install -d -m 775 $RPM_BUILD_ROOT%{logdir}/${mode}
done

for m in %{modules} build-config ee-deployment threads; do
  # JAR
  cp -a ${m}/target/jboss-as-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-${m}.jar
  # POM
  cp -a ${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-${m}.pom %{name}/%{name}-${m}.jar
done

# TODO simplify this!

# Special case domain-http submodules
for m in interface error-context; do
  # JAR
  cp -a domain-http/${m}/target/jboss-as-domain-http-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-domain-http-${m}.jar
  # POM
  cp -a domain-http/${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-domain-http-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-domain-http-${m}.pom %{name}/%{name}-domain-http-${m}.jar
done

# Clustering submodules
for m in %{modules_clustering}; do
  # JAR
  cp -a clustering/${m}/target/jboss-as-clustering-${m}-%{namedversion}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/%{name}-clustering-${m}.jar
  # POM
  cp -a clustering/${m}/pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-clustering-${m}.pom
  # DEPMAP
  %add_maven_depmap JPP.%{name}-%{name}-clustering-${m}.pom %{name}/%{name}-clustering-${m}.jar
done

# Parent POM
cp -a pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-parent.pom

# Depmap fo parent POM
%add_maven_depmap JPP.%{name}-%{name}-parent.pom

# Apidocs
cp -a target/site/apidocs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

pushd build/target/jboss-as-%{namedversion}
  # We don't need Windows files
  find bin/ -type f -name "*.bat" -delete

  # init.d
  mv bin/init.d/jboss-as.conf $RPM_BUILD_ROOT%{confdir}
  mv bin/init.d/jboss-as-standalone.sh $RPM_BUILD_ROOT%{_sysconfdir}/init.d/%{name}
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
  ln -s $(build-classpath jboss/jboss-modules) jboss-modules.jar
  
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

    # Please keep alphabetic by jar name

    ln -s $(build-classpath geronimo-validation) javax/validation/api/main/geronimo-validation.jar
    ln -s $(build-classpath hibernate-validator) org/hibernate/validator/main/hibernate-validator.jar

    ln -s $(build-classpath infinispan/cachestore-jdbc) org/infinispan/cachestore/jdbc/main/cachestore-jdbc.jar
    ln -s $(build-classpath infinispan/cachestore-remote) org/infinispan/cachestore/remote/main/cachestore-remote.jar
    ln -s $(build-classpath infinispan/client-hotrod) org/infinispan/client/hotrod/main/client-hotrod.jar
    ln -s $(build-classpath infinispan/core) org/infinispan/main/core.jar

    ln -s $(build-classpath jboss/jandex) org/jboss/jandex/main/jandex.jar
    ln -s $(build-classpath jboss/jboss-annotations-1.1-api) javax/annotation/api/main/jboss-annotations-1.1-api.jar
    ln -s $(build-classpath jboss/jboss-common-core) org/jboss/common-core/main/jboss-common-core.jar
    ln -s $(build-classpath jboss/jboss-dmr) org/jboss/dmr/main/jboss-dmr.jar
    ln -s $(build-classpath jboss/jboss-ejb3-ext-api) org/jboss/ejb3/main/jboss-ejb3-ext-api.jar
    ln -s $(build-classpath jboss/jboss-httpserver) org/jboss/com/sun/httpserver/main/jboss-httpserver.jar
    ln -s $(build-classpath jboss/jboss-interceptors-1.1-api) javax/interceptor/api/main/jboss-interceptors-1.1-api.jar
    ln -s $(build-classpath jboss/jboss-invocation) org/jboss/invocation/main/jboss-invocation.jar
    ln -s $(build-classpath jboss/jboss-jacc-1.4-api) javax/security/jacc/api/main/jboss-jacc-1.4-api.jar
    ln -s $(build-classpath jboss-jts/jbossjta) org/jboss/jts/main/jbossjta.jar
    ln -s $(build-classpath jboss-jts/jbossjta-integration) org/jboss/jts/integration/main/jbossjta-integration.jar
    ln -s $(build-classpath log4j) org/apache/log4j/main/log4j.jar
    ln -s $(build-classpath jboss/jboss-logging) org/jboss/logging/main/jboss-logging.jar
    ln -s $(build-classpath jboss/jboss-logmanager) org/jboss/logmanager/main/jboss-logmanager.jar
    ln -s $(build-classpath jboss/jboss-logmanager-log4j) org/jboss/logmanager/log4j/main/jboss-logmanager-log4j.jar
    ln -s $(build-classpath jboss/jboss-marshalling) org/jboss/marshalling/main/jboss-marshalling.jar
    ln -s $(build-classpath jboss/jboss-marshalling-river) org/jboss/marshalling/river/main/jboss-marshalling-river.jar
    ln -s $(build-classpath jboss/jboss-metadata-appclient) org/jboss/metadata/main/jboss-metadata-appclient.jar
    ln -s $(build-classpath jboss/jboss-metadata-common) org/jboss/metadata/main/jboss-metadata-common.jar
    ln -s $(build-classpath jboss/jboss-metadata-ear) org/jboss/metadata/main/jboss-metadata-ear.jar
    ln -s $(build-classpath jboss/jboss-metadata-ejb) org/jboss/metadata/main/jboss-metadata-ejb.jar
    ln -s $(build-classpath jboss/jboss-metadata-web) org/jboss/metadata/main/jboss-metadata-web.jar
    ln -s $(build-classpath jboss/jboss-msc) org/jboss/msc/main/jboss-msc.jar
    ln -s $(build-classpath jboss/jboss-remoting) org/jboss/remoting3/main/jboss-remoting.jar
    ln -s $(build-classpath jboss-remote-naming) org/jboss/remote-naming/main/jboss-remote-naming.jar
    ln -s $(build-classpath jboss-remoting-jmx) org/jboss/remoting3/remoting-jmx/main/jboss-remoting-jmx.jar
    ln -s $(build-classpath jboss/jboss-sasl) org/jboss/sasl/main/jboss-sasl.jar
    ln -s $(build-classpath jboss/jboss-servlet-3.0-api) javax/servlet/api/main/jboss-servlet-3.0-api.jar
    ln -s $(build-classpath jboss/jboss-stdio) org/jboss/stdio/main/jboss-stdio.jar
    ln -s $(build-classpath jboss/jboss-threads) org/jboss/threads/main/jboss-threads.jar
    ln -s $(build-classpath jboss/jboss-transaction-1.1-api) ./javax/transaction/api/main/jboss-transaction-1.1-api.jar
    ln -s $(build-classpath jboss-transaction-spi) org/jboss/jboss-transaction-spi/main/jboss-transaction-spi.jar
    ln -s $(build-classpath jboss/jboss-vfs) org/jboss/vfs/main/jboss-vfs.jar
    ln -s $(build-classpath jgroups) org/jgroups/main/jgroups.jar
    ln -s $(build-classpath jboss/staxmapper) org/jboss/staxmapper/main/staxmapper.jar
    ln -s $(build-classpath jboss/xnio-api) org/jboss/xnio/main/xnio-api.jar
    ln -s $(build-classpath jboss/xnio-nio) org/jboss/xnio/nio/main/xnio-nio.jar

    # JBoss AS modules (without build-config)
    for m in %{modules} threads domain-http-error-context; do
      ln -s %{_javadir}/jboss-as/jboss-as-${m}.jar org/jboss/as/${m}/main/jboss-as-${m}-%{namedversion}.jar
    done

    # JBoss AS clustering submodules
    for m in %{modules_clustering}; do
      ln -s %{_javadir}/jboss-as/jboss-as-clustering-${m}.jar org/jboss/as/clustering/${m}/main/jboss-as-clustering-${m}-%{namedversion}.jar
    done

    # special case naming
    ln -s %{_javadir}/jboss-as/jboss-as-domain-http-interface.jar org/jboss/as/domain-http-interface/main/jboss-as-domain-http-interface-%{namedversion}.jar
    ln -s %{_javadir}/jboss-as/jboss-as-ee-deployment.jar org/jboss/as/ee/deployment/main/jboss-as-ee-deployment-%{namedversion}.jar
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
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/%{name}.conf
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/standalone/*.xml
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.properties
%attr(0664,jboss-as,jboss-as) %config(noreplace) %{confdir}/domain/*.xml
%attr(0755,root,root) %config(noreplace) %{_sysconfdir}/init.d/%{name}
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
* Thu Feb 16 2012 Carlo de Wolf <cdewolf@redhat.com> 7.1.0-1
- Package 7.1.0.Final

* Mon Jan 09 2012 Marek Goldmann <mgoldman@redhat.com> 7.1.0-0.1.CR1b
- Initial packaging

