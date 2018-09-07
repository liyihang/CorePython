import re
from urllib import request


class Spider():
    url = "https://www.panda.tv/cate/lol"
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>'
    number_pattern = '<span class="video-number">([\s\S]*?)</span>'

    def __fetch_content(self):
        res = request.urlopen(Spider.url)
        htmls = res.read()
        htmls = str(htmls, encoding='utf8')
        return htmls

    def __analyisis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        infos = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            info = {'name': name, 'number': number}
            infos.append(info)
        return infos

    def __refine(self, infos):
        lam = lambda info: {
            'name': info['name'][0].strip(),
            'number': info['number'][0]
        }
        return map(lam, infos)

    def __sort(self, infos):
        infos = sorted(infos,key=self.__sort_seed)
        return infos

    def __sort_seed(self,infos):
        return infos['number']


    def __show(self, inofs):
        for info in inofs:
            print(info['name'] + '--------' + info['number'])

    def go(self):
        htmls = self.__fetch_content()
        infos = self.__analyisis(htmls)
        infos = list(self.__refine(infos))
        infos = self.__sort(infos)
        self.__show(infos)



spider = Spider()
spider.go()
