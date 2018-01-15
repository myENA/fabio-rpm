# RPM Spec for Fabio

# Building

The RPMs may be built with [Docker](#with-docker), [Vagrant](#with-vagrant), or [manual](#manual).

Whatever way you choose you will need to do a few basic things first.

```bash
git clone https://github.com/myENA/fabio-rpm  ## check out this code
cd fabio-rpm                                  ## uhh... you should know
mkdir -p artifacts                            ## prep the artifacts location
```

## With Docker

```bash
docker build -t ena/fabio-rpm .                                ## build the image
docker run -v $PWD/artifacts:/tmp/artifacts -it ena/fabio-rpm  ## run the image and build the RPMs
```

## With Vagrant

```bash
vagrant up                         ## provision and build the RPMs
```

## Manual

```bash
cat build.sh     ## read the script
```

## Result

Five RPMs will be copied to the `artifacts` folder:
1. `fabio-<version>-<release>.rpm`          - The binary and systemd service definition (required)
2. `fabio-config-<version>-<release>.rpm`   - Example agent configuration (recommended)

# Running

1. Install the RPM(s) that you need
2. Review and edit (if needed) `/etc/sysconfig/fabio` and `/etc/fabio/fabio.properties` (config package)
3. Start the service and tail the logs: `systemctl start fabio.service` and `journalctl -f --no-pager -u fabio`
4. Optionally start on reboot with: `systemctl enable fabio.service`

# Further reading

See the [fabiolb.net](https://fabiolb.net) website.
