import re
import requests

url = 'https://www.google.com.au/search?hl=en&authuser=0&biw=1280&bih=628&tbm=isch&sa=1&ei=Lo2eWvHsGcGEtQWQmIeYBw&q=%E9%87%8D%E5%BA%86%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%A5%B3&oq=%E9%87%8D%E5%BA%86%E8%A1%97%E6%8B%8D%E7%BE%8E%E5%A5%B3&gs_l=psy-ab.3...7105.14494.0.14680.30.23.2.0.0.0.409.2902.2-8j0j2.10.0....0...1c.1j4.64.psy-ab..20.9.2133...0j0i13k1j0i13i30k1j0i30k1j0i13i5i30k1j0i67k1j0i8i30k1j0i12k1j0i12i24k1.0.Qk4YBVjOCrE'

html = requests.get(url).text
pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
i = 0
for each in pic_url:
    print each
    try:
        pic= requests.get(each, timeout=10)
    except requests.exceptions.ConnectionError:
        print "failed to download"
	continue
    string = 'pictures\\'+str(i) + '.jpg'
    fp = open(string,'wb')
    fp.write(pic.content)
    fp.close()
    i += 1
