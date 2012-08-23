# Hi!

This is the [JBoss Application Server](http://www.jboss.org/jbossas/) RPM spec repository used to create RPM in [Fedora](https://fedoraproject.org).

## Repositories

There are two places where the JBoss AS spec file (and other files required to build the package) is stored:

1. [Fedora's Git repository](http://pkgs.fedoraproject.org/cgit/jboss-as.git/)
2. [GitHub](https://github.com/fedora-jboss-as/jboss-as-rpm)

## Workflow

The [GitHub repostitory](https://github.com/fedora-jboss-as/jboss-as-rpm) is a **mirror** created for the convenience of the packagers. The actual work is done on that mirror, then the commits are merged with the Fedora repository.

Please note that only `master` branch from Fedora Git repo is mirrored. This branch represents the current state of the **next** (unreleased) Fedora version. Other branches representing released Fedora versions (f16, f17...) are skipped. The `master` branch from Fedora is represented as `fedora_master` on GitHub. There may be some other branches, but these are temporary.

### How to genererate patches?

JBoss AS needs some patches to work in Fedora. Some of them are related to still missing dependencies some of them are bug fixes.

The **customized** source code used to compile JBoss AS is located in the [jboss-as repository on GitHub](https://github.com/fedora-jboss-as/jboss-as) repository. To generate patches from it, please use following command:

    git format-patch --no-numbered --no-signature 7.1.1.Final..HEAD


