import os
import xml.etree.ElementTree
#from bs4 import BeautifulSoup
import codecs


from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


root = xml.etree.ElementTree.parse('blog.xml').getroot()

#for child in root:
#    print(child.tag, child.attrib)


#entry = root.find('{http://www.w3.org/2005/Atom}entry')

#for child in entry:
#    print(child.tag, child.attrib)

count=0

outfile = codecs.open('blogout.txt', 'w', 'utf-8')

for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
    for type in entry.findall('{http://www.w3.org/2005/Atom}category'):
        print('!!!!', type.get('term'))
        if 'post' in type.get('term'):
            title = entry.find('{http://www.w3.org/2005/Atom}title')
            print(title.text)
            outfile.write(title.text)
            outfile.write('\r\n\r\n')
            content = strip_tags(entry.find('{http://www.w3.org/2005/Atom}content').text)
            print(content)
            outfile.write(content)
            outfile.write('\r\n\r\n')
            count = count + 1

print (str(count))

outfile.close()
