import markdown
import codecs
import re
import os
import html

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

html_list = os.listdir(html_path)

index_name = 'index.html'
index_path = os.path.join(html_path, index_name)
index = codecs.open(index_path, mode='w', encoding='utf-8')
public_ip = '150.236.158.45'
public_url = 'http://' + public_ip + '/'
blog_name = "XJQ's Blog"
index.write('<h1>' + blog_name + '</h1>\n')
for html_name in html_list:
    if (html_name != 'index.html'):
        index.write('<a href="' + public_url + html_name + '">' + html_name + '</a>\n')
index.close()
