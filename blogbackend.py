#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import markdown
import codecs
import re
import os

def generate_essay():

    working_path = os.getcwd()
    md_path = os.path.join(working_path, 'md')
    html_path = os.path.join(working_path, 'static')
    md_list = os.listdir(md_path)
    html_list = os.listdir(html_path)

    #Check if static folder exists, if not create it

    for html_name in html_list:
        html = os.path.join(html_path, html_name)
        os.remove(html)

    for md_name in md_list:

        if ( re.match(r'[0-9][0-9][0-9][0-9]_[0-9][0-9]_[0-9][0-9].*',md_name) != None ):

            html_name = str(md_name).replace('md','html')
            md = os.path.join(md_path, md_name)
            html = os.path.join(html_path, html_name)
            input_file = codecs.open(md, mode='r', encoding='utf-8')
            input = input_file.read()
            output = markdown.markdown(input)
            output_file = codecs.open(html, mode='w', encoding='utf-8', errors='xmlcharrefreplace')
            output_file.write(output)
