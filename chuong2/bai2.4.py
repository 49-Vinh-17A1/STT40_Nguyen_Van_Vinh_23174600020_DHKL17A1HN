import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("chuong2\\bai2.3.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)
    staff = doc.getElementsByTagName("staff")
    print("%d staff:" % staff.length)
    for id in staff:
        print(id.getAttribute("id"))
main()