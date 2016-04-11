# coding:utf-8
import codecs
import re
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from blog import config
from blog import article


class Index:

    def __init__(self):

        self.working_path = os.getcwd()
	self.server_static_path = '/home/linaro/FlaskServer'

    def to_html(self):

        conf = config.Config()
        html_path = os.path.join(self.server_static_path, 'static')
        html_list = os.listdir(html_path)
        html_list.sort(reverse=True)
        index_file = os.path.join(self.server_static_path, 'static', 'index.html')
        index_output = codecs.open(index_file, mode='w', encoding='utf-8')
        # Write head
        index_output.write('<head>\n')
        index_output.write('<link rel="stylesheet" type="text/css" href=' + conf.css_index + '/>\n')
        index_output.write('<link rel="shortcut icon" href=' + conf.icon + '>\n')
        index_output.write('<title>' + conf.blog_name + '</title>\n')
	index_output.write('</head>\n')
	# Write navi
	index_output.write('<ul>\n')
  	index_output.write('<li><a href=' + conf.public_url + '>' + conf.blog_name  + '</a></li>\n')
	index_output.write('<ul style="float:right;list-style-tpye:none;">\n')
    	index_output.write('<li><a href="https://github.com/xjq">Projects</a></li>\n')
    	index_output.write('<li><a href="2015_12_25_blog_architecture.html">About</a></li>\n')
 	index_output.write('</ul>\n')
	index_output.write('</ul>\n')
        # Write h1
        #index_output.write('<h1>' + conf.blog_name + '</h1>\n')
        # Write article list
        for html_name in html_list:
            if (html_name != 'index.html') & (html_name.find('html') > 0):
	    #  if re.match(r'[0-9][0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9].*', name) is not None:
		myarticle = article.Article(html_name.replace('html','md'))
		essay_name = myarticle.essay_name
                index_output.write('<a href="' + html_name + '">' + essay_name + '</a>\n')
                index_output.write('<br></br>\n')
        index_output.close()
