import xml.etree.ElementTree as ET
import re

f = open('admin.csv', 'w')

schools = ET.parse('C:\doc.kml')
root = schools.getroot()

for school in root.iter('{http://www.opengis.net/kml/2.2}Placemark'):
    name = school.findtext('{http://www.opengis.net/kml/2.2}name')
    name = '"' + name + '"'
    coordinates = ''
    for coord in school.iter('{http://www.opengis.net/kml/2.2}coordinates'):
        coordinates = coord.text
    coordinates = coordinates.replace(","," ")
    coordinates = re.sub(r'0\s',"0, ",coordinates)

    result = name + ',"SRID=4326;POLYGON((' + coordinates + '))",' + '"School Lot"' + "," + '"96"'
    print(result,file=f)

f.close()
