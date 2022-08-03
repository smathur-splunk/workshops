1. Download snmpd
```bash
sudo apt update
sudo apt install snmpd
sudo nano /etc/snmp/snmpd.conf
```

2. Inside `snmpd.conf`, change the line `agentaddress  127.0.0.1,[::1]` to `agentAddress udp:161,udp6:[::1]:161` and on a new line, add `rocommunity public`. Save these changes to the file. See example [here](https://gist.githubusercontent.com/smathur-splunk/4660aab9c9aed7bac8bc95c20ec6afb4/raw/10ac402b17da5603abf2b8b19a4582599cda0a23/snmpd.conf).

3. Restart snmpd and check the status
```bash
sudo service snmpd restart
sudo service snmpd status
```

At this point, the agent has been set up to send data to SC4SNMP. Now on to setting up SC4SNMP itself!