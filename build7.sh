#!/usr/bin/env bash
set -ex  ## we like things verbose

## install some helpers
sudo yum install -y rpmdevtools rpm-devel

## setup our build path
rpmdev-setuptree

## link the specs
ln -sf /tmp/build/SPECS/*.spec $HOME/rpmbuild/SPECS/

## link the sources
find /tmp/build/SOURCES \( -type f -o -type l \) -exec ln -sf {} $HOME/rpmbuild/SOURCES/ \;

## download sources
for spec in $HOME/rpmbuild/SPECS/*.spec; do
    spectool -g -R $spec
done

## build packages
rpmbuild -ba $HOME/rpmbuild/SPECS/*.spec

## copy built files out of the vagrant/docker environment
## skip if you are doing this manually
if [ -f /.dockerenv ] || [ -f /.doing_the_vagrant ]; then
    sudo mkdir -p /tmp/build/artifacts/7
    sudo cp -rf $HOME/rpmbuild/RPMS $HOME/rpmbuild/SRPMS /tmp/build/artifacts/7
fi
