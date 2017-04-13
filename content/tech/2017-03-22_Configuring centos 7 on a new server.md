Title: Configuring Centos 7 server
Modified: 2017-03-22 19:00
Tags: linux, docker
Summary: Just bought an HP DL360 Gen 6 server, 12 cores and 24GB RAM.  This is the documentation of getting this server up and running, including Installing Centos 7 server and a number of core services

# SATA Drives

The server came with a single HP 146GB 10K SAS drive.  No redundancy, and not really much storage.  I read up about the P410i RAID controller which the documentation says will allow the use of SATA drives.  So I bought two 2TB Seagate Barracuda drives.  I put them into some spare drive caddies and plugged them into the server.  Shortly afterwards the server started to sound like a jet engine.  It would appear this is a common problem with non HP drives not reporting the temperature in the "HP way" (Or at all maybe), so the server is assuming the worst and spinning the fans up to keep the "Overheating" drives cool.

This has been documented on a number of forums, and [this link](http://dascomputerconsultants.com/HPCompaqServerDrives.htm) has some data about some drives that are reported to work and some that are reported not to work.  Looks like I can add another Seagate drive to the list of problem drives.

# docker

Following the guide on [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-centos-7), which despite the errors during the install line not running as root, actually worked...  Follow the guide :-)

# Unifi Controller

Decided to try a new [Docker Unify container](https://hub.docker.com/r/linuxserver/unifi/)

~~~ Shell
sudo docker pull linuxserver/unifi

sudo mkdir -p /docker/unifi

sudo docker create \
  --name=unifi \
  -v /docker/unifi:/config \
  -p 8080:8080 \
  -p 8081:8081 \
  -p 8443:8443 \
  -p 8843:8843 \
  -p 8880:8880 \
  linuxserver/unifi

 sudo docker run unifi

# firewall

Centos uses firewalld as its firewall.  It is a little more complex than ufw, but again the [DigitalOcean Firewalld page](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-7) is great.
 ~~~

 I changed the zone for the network interfaces, by adding:

 ~~~ Shell

 ZONE=Home

 ~~~

 To the main interface and a similar one to the second network interface configuration.  These files are located at:

 ~~~ Shell

 /etc/sysconfig/network-scripts/ifcfg-enp2s0f0
 /etc/sysconfig/network-scripts/ifcfg-enp2s0f1

 ~~~

 I then had to [open the firewall](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-using-firewalld-on-centos-7), by defining a service to cover all of the ports needed for the Unifi controller, and saving it `/etc/firewalld/services/unifi.xml`.

 ~~~ xml

 <?xml version="1.0" encoding="utf-8"?>
<service>
  <short>Unifi</short>
  <description>Ports needed by the Unifi controller</description>
  <port protocol="tcp" port="8080"/>
  <port protocol="tcp" port="8081"/>
  <port protocol="tcp" port="8443"/>
  <port protocol="tcp" port="8843"/>
  <port protocol="tcp" port="8880"/>
</service>

~~~
