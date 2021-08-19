# NOKIA OLT SSH WITH PYTHON

Simple script to connect with SSH to NOKIA / ALCATEL OLTs ISAN FX8, FX16

---
## Dependences python3 and netmiko
#### how to install dependences on Debian / Ubuntu
apt install python3<br>
apt install python3-pip<br>
apt install python3-netmiko<br>

#### Example running command "show equipament slot"

<pre>
./nokia-olt-ssh.py 
================================================================================
slot table
================================================================================
slot       |actual-type|enabled|error-status          |availability |restrt-cnt
-----------+-----------+-------+----------------------+-------------+-----------
nt-a        fant-f      yes     no-error               available     0         
nt-b        empty       no      no-error               not-installed 0         
lt:1/1/1    fglt-b      yes     no-error               available     0         
lt:1/1/2    fglt-b      yes     no-error               available     0         
lt:1/1/3    fglt-b      yes     no-error               available     0         
lt:1/1/4    fglt-b      yes     no-error               available     0         
lt:1/1/5    fglt-b      yes     no-error               available     0         
lt:1/1/6    fglt-b      yes     no-error               available     0         
lt:1/1/7    fglt-b      yes     no-error               available     0         
lt:1/1/8    fglt-b      yes     no-error               available     0         
lt:1/1/9    fglt-b      yes     no-error               available     0         
lt:1/1/10   empty       no      no-installation        not-installed 0         
lt:1/1/11   empty       no      no-installation        not-installed 0         
lt:1/1/12   empty       no      no-installation        not-installed 0         
lt:1/1/13   empty       no      no-installation        not-installed 0         
lt:1/1/14   empty       no      no-installation        not-installed 0         
lt:1/1/15   empty       no      no-installation        not-installed 0         
lt:1/1/16   empty       no      no-installation        not-installed 0         
vlt:1/1/63  empty       no      no-error               not-installed 0         
vlt:1/1/64  empty       no      no-error               not-installed 0         
--------------------------------------------------------------------------------
slot count : 20
================================================================================
</pre>
