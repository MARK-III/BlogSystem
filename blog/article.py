# coding:utf-8
import markdown
import codecs
import os
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
from blog import config


class Article:

    def __init__(self, name):

        self.working_path = os.getcwd()
	self.server_static_path = '/home/linaro/FlaskServer'
        self.md_name = name
        self.md_file = os.path.join(self.working_path, 'md', self.md_name)
        self.md_content = codecs.open(self.md_file, mode='r', encoding='utf-8').read()
	self.essay_name = self.md_content[1:self.md_content.find('\n')]

    def to_html(self):

        conf = config.Config()
        html_file = os.path.join(self.server_static_path, 'static', self.md_name.replace('md', 'html'))
        html_content = markdown.markdown(self.md_content)
        html_output = codecs.open(html_file, mode='w', encoding='utf-8', errors='xmlcharrefreplace')
        # Add head to article
	head = [
                '<head>\n',
                '<link rel="stylesheet" type="text/css" href=' + conf.public_url + conf.css_article + '/>\n',
                '<link rel="shortcut icon" href=' + conf.public_url + conf.icon + '>\n',
                '<title>' + self.essay_name + '</title>\n',
                '</head>\n'
        ]
        html_output.writelines(head)
        html_output.write(html_content)
        html_output.close()

