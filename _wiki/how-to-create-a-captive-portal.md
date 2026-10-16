---
title: "How to create a captive portal"
layout: page
permalink: /how-to-create-a-captive-portal/
---

**Important information**
- These instructions are meant for the gateway routers, connected to the Internet and providing it to the rest of the mesh. It was not tested in networks with more than one exit.
- The captive portal system doesn't work when there is no access to the Internet

## Libremesh's DaybootRely version (1706)
1. Login to the router through ssh and update the software repositories:

`opkg update`

2. Now let’s install nodogsplash [nodogsplash](http://nodogsplash.readthedocs.io/en/latest/). This is a package for version 17 of LiMe.

`opkg install http://nuvem.tk/files/nodogsplash_0.9.2-1_mips_24kc.ipk`

3. Now we must edit the configuration file

`vi /etc/config/nodogsplash`

Change the following lines so that this is the final result:

Change "option enable" from 0 to 1

`option enable 1`

Uncomment (erase the hash symbol from the start) the following line:

`option config '/etc/nodogsplash/nodogsplash.conf'`

Erase all lines after this one.

4. Now save the file and exit the editor.

5. Create the file /etc/nodogsplash/nodogsplash.conf using the text below (modifying the IP and redirect page according to your network). You can find the ip to be used in the graphical interface (http://thisnode.info)under the menu menu network -> interfaces, LAN interface (IPV4) (without /16). The range are the first two numbers, follwed by .0.0/16. (for example, if the ip is 10.7.255.50, the range will be 10.7.0.0/16).

```

GatewayInterface br-lan
GatewayInterfaceExtra bmx+
GatewayInterfaceExtra2 anygw

FirewallRuleSet authenticated-users {
     FirewallRule allow to 0.0.0.0/0
}

FirewallRuleSet users-to-router {
 # Nodogsplash automatically allows tcp to GatewayPort,
 # at GatewayAddress, to serve the splash page.
 # However you may want to open up other ports, e.g.
 # 53 for DNS and 67 for DHCP if the router itself is
 # providing these services.
    FirewallRule allow udp port 53
    FirewallRule allow tcp port 53
    FirewallRule allow udp port 67
 # You may want to allow ssh, http, and https to the router
 # for administration from the GatewayInterface.  If not,
 # comment these out.
    FirewallRule allow tcp port 22
    FirewallRule allow tcp port 80
    FirewallRule allow tcp port 443
}
# end FirewallRuleSet users-to-router

FirewallRuleSet preauthenticated-users {
 # For preauthenticated users to resolve IP addresses in their initial
 # request not using the router itself as a DNS server,
 # you probably want to allow port 53 udp and tcp for DNS.
    FirewallRule allow tcp port 53
    FirewallRule allow udp port 53
 # For splash page content not hosted on the router, you
 # will want to allow port 80 tcp to the remote host here.
 # Doing so circumvents the usual capture and redirect of
 # any port 80 request to this remote host.
 # Note that the remote host's numerical IP address must be known
 # and used here.

     #change the IP for the address of the gateway router
     FirewallRule allow tcp port 80 to 10.7.122.55

}
# end FirewallRuleSet preauthenticated-users

EmptyRuleSetPolicy preauthenticated-users passthrough
EmptyRuleSetPolicy users-to-router passthrough

#change the IP for the address of the gateway router
GatewayName 10.7.122.55:80

#GatewayPort 80

MaxClients 500

ClientIdleTimeout 720

ClientForceTimeout 14400

#change the range for the ip range of your mesh network
GatewayIPRange 10.7.0.0/16

# BinVoucher "vale.sh"

# ForceVoucher yes

# EnablePreAuth yes
```

DON’T FORGET TO CHANGE THE Ips IN THE FILE ABOVE!

6. Go to the menu system -> startup and check if nodogsplash is ENABLED

7. Restart the router. When it is back on, the blocking of http pages should be working already.

8. Now let’s modify the FIREWALL so that https and other protocols/ports will also be blocked,

`vi /etc/config/firewall`

Comment out the following lines, including the hash symbol the beginning. It should look like this after editing.

```

#config forwarding
    #option src 'lan'
    #option dest 'wan'
```

Save the file and restart the firewall

```

/etc/init.d/firewall reload && /etc/init.d/firewall restart
```

Restart the router. Now the https pages should also be blocked.

## Voucher system configuration
1. Let’s connect through ssh, update repos and install the vale package.

```

opkg update && opkg install http://nuvem.tk/files/vale_0.1-1_mips_24kc.ipk
```

2. Now rename the splash html file. You can also customize this file to reflect your community info.

```

mv /etc/nodogsplash/htdocs/splash-vale.html /etc/nodogsplash/htdocs/splash.html
```

3. Restart nodogsplash
```

/etc/init.d/nodogsplash restart
```

4. Translate or adapt the messages in the file  /www/cgi-bin/vale

5. Add your VOUCHER codes in the files /etc/nodogsplash/vale/db.csv (you can use a [random code generator](http://generator.voucherify.io/#)).

You can see an example of the formatting here: [db.csv](https://github.com/coolabnet/lime-packages/blob/develop/packages/vale/files/etc/nodogsplash/vale/db.csv)

Each line must end with two commas, with no spaces, and begin with one comma. The columns will be used to annotate the date/time and MAC address of every voucher. To generate automatically the commas, use an empty column in the beginning and two in the end in your spreadsheet editor. Example:

```

reference,code,field1,field2
,6XvMcaLb,,
,cF6m7eXu,,
,nNqsSMCS,,
,GSYJPotH,,
,PecFaM8c,,
,Tx2GgNNX,,
,zEeTmcwu,,
,hBg5858g,,
,rmsgUqR2,,
```

6. Now copy it to your router:

```
 scp db.csv root@thisnode.info:/etc/nodogsplash/vale/
```

**References**

- [Tutorial da Nuvem](http://nuvem.tk/wiki/index.php/Fuma%C3%A7a_Data_Springs/Anexo_t%C3%A9cnico#Instala.C3.A7.C3.A3o_do_portal_de_controle_de_acesso)
- [Nodogsplash - Documentação](http://nodogsplash.readthedocs.io/en/latest/)
