# SC4SNMP Complete Setup

![SC4SNMP architecture diagram](https://i.imgur.com/BrnrxK5.png)

### Port Requirements
- SNMP agent: UDP `161` (polling), `162` (traps)
- SC4SNMP host: UDP `161` (polling)

### SC4SNMP Host Requirements
- 4 cores
- 8GB memory
- 50GB storage

On AWS, the `t2.xlarge` EC2 instance type meets these requirements.