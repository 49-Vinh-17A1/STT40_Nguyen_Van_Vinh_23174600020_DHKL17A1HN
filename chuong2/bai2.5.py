import xml.etree.ElementTree as ET 
import xml.dom.minidom
tree = ET.parse('chuong2\\bai2.3.xml')
doc = xml.dom.minidom.parse("chuong2\\bai2.3.xml") 
root = tree.getroot()
name = root.find('name')
print(name.text)
nhanvien = root.find("staff")
print(nhanvien.attrib['id'])

staff = doc.getElementsByTagName("staff")
print("%d staff:" % staff.length)
for id in staff:
    print(id.getAttribute("id"))