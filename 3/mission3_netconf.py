from ncclient import manager
import xmltodict, json
import netconf_credentials as c

def get_interfaces():
    filter = """
    <filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> <interface>
    <GigabitEthernet>
    <name/>
    <switchport>
    <access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch" />
    </switchport>
    </GigabitEthernet>
    </interface>
    </native>
    </filter>
    """
    with manager.connect(
            host=c.NETCONF_ADDRESS,port=c.NETCONF_PORT,
            username=c.NETCONF_USER,password=c.NETCONF_PW,
            hostkey_verify=False) as m:
        interfaces = m.get_config(source="running", filter=filter).data_xml

    interface_list = []
    interfaces = json.loads(json.dumps(xmltodict.parse(interfaces)))
    interfaces = interfaces["data"]["native"]["interface"]["GigabitEthernet"]

    for item in interfaces:
        #On the sandbox "IOS XE on Catalyst 9000 16.12 EFT Code" there are
        # two interfaces we do not want to change the VLAN info. We check
        # first if the interface is one of those, and if yes, we go to the
        # next item in our for loop with the key word "continue"

        if item["name"] == "0/0" or item["name"] == "1/0/1":
            continue
        try:
            vlan = item["switchport"]["access"]["vlan"]["vlan"]
        except KeyError:
            vlan = None
        interface_list.append({"name":item["name"], "vlan":vlan})

    return interface_list

def change_vlan(interface, vlan):
    config = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <GigabitEthernet>
    <name>{}</name>
    <switchport>
    <access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch">
    <vlan><vlan>{}</vlan></vlan>
    </access>
    </switchport>
    <description> Configured by NETCONF </description>
    </GigabitEthernet>
    </interface>
    </native>
    </config>
    """
    with manager.connect(
        host=c.NETCONF_ADDRESS,port=c.NETCONF_PORT,
        username=c.NETCONF_USER,password=c.NETCONF_PW,hostkey_verify=False) as m:

        response = m.edit_config(target="running", config=config.format(interface, vlan))

    return response
