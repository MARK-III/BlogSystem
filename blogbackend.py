import markdown
import codecs
import re
import os

def generate_essay():

    working_path = os.getcwd()
    md_path = os.path.join(working_path, 'md')
    html_path = os.path.join(working_path, 'html')
    md_list = os.listdir(md_path)

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
