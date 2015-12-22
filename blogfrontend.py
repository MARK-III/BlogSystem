#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import codecs
import os

def generate_index():

    public_ip = '192.168.0.93'
    public_url = 'http://' + public_ip + '/'

    working_path = os.getcwd()
    html_path = os.path.join(working_path, 'static')
    html_list = os.listdir(html_path)

    index_name = 'index.html'
    index_path = os.path.join(html_path, index_name)
    index = codecs.open(index_path, mode='w', encoding='utf-8')

    blog_name = "坐井观天"
    index.write('<h1>' + blog_name + '</h1>\n')

    for html_name in html_list:
        if (html_name != 'index.html'):
            index.write('<a href="' + public_url + 'blog/' + html_name + '">' + html_name + '</a>\n')
            index.write('<br></br>\n')
    index.close()
