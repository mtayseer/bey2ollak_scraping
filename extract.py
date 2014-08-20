import sys
import json
from lxml.html import fromstring

# lang: 0 => Arabic, 1 => Francozeft
# city: 0 => Cairo, 1 => Alexandria
# road status:
#   -1: no data
#    1: best
#    5: worst

def translate_status(status):
    if status == 'images/blank-statues-44.png':
        return -1
    else:
        return int(status.replace('images/level_icon_', '').replace('.png', ''))

def main():
    url = 'http://www.bey2ollak.com/Traffic?action=getTraffic&target=4&city=0&lang=1'
    doc = fromstring(open(sys.argv[1]).read())
    elements = doc.cssselect('.block-item_nokia')[1:]

    road_status = dict(
                        (elt.cssselect('.col-1 label.green a')[0].text.strip(u'\xa0'),
                         translate_status(elt.cssselect('.col-2 img')[0].attrib['src']))
                        for elt in elements)

    output_file_name = sys.argv[1].replace('.html', '.json')
    with open(output_file_name, 'w') as output:
        json.dump(road_status, output, sort_keys=True, indent=4)
    print output_file_name

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Usage:\n\t {} <input_file.html>'.format(__file__)
        sys.exit()
    main()
