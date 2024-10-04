import xml.etree.ElementTree as ET 
tree = ET.parse('chuong2\\bai2.3.xml') 
root = tree.getroot()
name = root.find('name')
print(name.text)
staff = root.find("staff")
print(staff.attrib['id'])
