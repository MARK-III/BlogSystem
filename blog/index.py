# coding:utf-8
import codecs
import re
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from blog import config


class Index:

    def __init__(self):

        self.working_path = os.getcwd()

    def to_html(self):

        conf = config.Config()
        html_path = os.path.join(self.working_path, 'static')
        html_list = os.listdir(html_path)
        html_list.sort(reverse=True)
        index_file = os.path.join(self.working_path, 'static', 'index.html')
        index_output = codecs.open(index_file, mode='w', encoding='utf-8')
        # Write head
        index_output.write('<head>\n')
        index_output.write('<link rel="stylesheet" type="text/css" href=' + conf.public_url + conf.css_index + '/>\n')
        index_output.write('<link rel="shortcut icon" href=' + conf.public_url + conf.icon + '>\n')
        index_output.write('</head>\n')
        # Write h1
        index_output.write('<h1>' + conf.blog_name + '</h1>\n')
        # Write article list
        for html_name in html_list:
            if (html_name != 'index.html') & (html_name.find('html') > 0):
                html_file = open(os.path.join(html_path, html_name), mode='r')
                html_contents = html_file.readlines()
                essay_name = html_contents[5].replace('<h1>','').replace('</h1>\n','')
                html_file.close()
                index_output.write('<a href="' + conf.public_url + html_name + '">' + essay_name + '</a>\n')
                index_output.write('<br></br>\n')
        index_output.close()
