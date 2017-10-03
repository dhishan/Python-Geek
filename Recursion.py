from xml.dom.minidom import parseString, Document

xml_p = '<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/" s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><s:Body><u:GetGenericPortMappingEntryResponse xmlns:u="urn:schemas-upnp-org:service:WANIPConnection:1"><NewRemoteHost></NewRemoteHost><NewExternalPort>27707</NewExternalPort><NewProtocol>UDP</NewProtocol><NewInternalPort>27707</NewInternalPort><NewInternalClient>192.168.0.26</NewInternalClient><NewEnabled>1</NewEnabled><NewPortMappingDescription>Skype UDP at 192.168.0.26:27707 (3632)</NewPortMappingDescription><NewLeaseDuration>0</NewLeaseDuration></u:GetGenericPortMappingEntryResponse></s:Body></s:Envelope>'


def get_node_of(xml_node,tag):
	if not xml_node.hasChildNodes():
		return None
	if tag in xml_node.firstChild.tagName:
		return xml_node.firstChild
	for elem in xml_node.childNodes:
		node = get_node_of(elem,tag)
	if xml_node.nextSibling and not node:
		node = get_node_of(xml_node.nextSibling,tag)
	return node

get_node_of.cnt = 5

val = get_node_of(parseString(xml_p).childNodes[0],'GetGenericPortMappingEntryResponse')
# val = get_node_of(xml_p,'GetGenericPortMappingEntryResponse')
