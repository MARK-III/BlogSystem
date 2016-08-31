# coding:utf-8
import codecs
import re
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from blog import *
from config import *


class Index:

    def __init__(self):

        self.working_path = os.path.join(Config().working_path, 'Blog')

    def to_html(self):

        html_path = os.path.join(self.working_path, 'html')
        html_list = os.listdir(html_path)
        html_list.sort(reverse=True)
        index_file = os.path.join(self.working_path, 'html', 'index.html')
        index_output = codecs.open(index_file, mode='w', encoding='utf-8')
        
        # Write head
        index_output.write('<head>\n')
        index_output.write('<link rel="stylesheet" type="text/css" href=/css/' + Config().css_index + '>\n')
        index_output.write('<link rel="shortcut icon" href=/css/' + Config().icon + '>\n')
        index_output.write('<title>' + Config().blog_name + '</title>\n')
	index_output.write('</head>\n')
	
        # Write navi
	index_output.write('<ul>\n')
  	index_output.write('<li><a href=' + Config().public_url + '>' + Config().blog_name  + '</a></li>\n')
	index_output.write('<ul style="float:right;list-style-tpye:none;">\n')
    	#index_output.write('<li><a href="library">Library</a></li>\n')
	index_output.write('<li><a href="https://github.com/xjq">Projects</a></li>\n')
    	index_output.write('<li><a href="blog/2015_12_25_blog_architecture.html">About</a></li>\n')
 	index_output.write('</ul>\n')
	index_output.write('</ul>\n')

        # Write article list
        for html_name in html_list:
            if (html_name != 'index.html') & (html_name.find('html') > 0):
	    #  if re.match(r'[0-9][0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9].*', name) is not None:
		myarticle = article.Article(html_name.replace('html','md'))
		essay_name = myarticle.essay_name
                index_output.write('<a href="' + 'blog/' + html_name + '">' + essay_name + '</a>\n')
                index_output.write('<br></br>\n')
        
        index_output.close()
