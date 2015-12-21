import codecs
import os

def generate_index():

    public_ip = '150.236.158.45'
    public_port = '10090'
    public_url = 'http://' + public_ip + ':' + public_port + '/'

    working_path = os.getcwd()
    html_path = os.path.join(working_path, 'html')
    html_list = os.listdir(html_path)

    index_name = 'index.html'
    index_path = os.path.join(html_path, index_name)
    index = codecs.open(index_path, mode='w', encoding='utf-8')

    blog_name = "XJQ's Blog"
    index.write('<h1>' + blog_name + '</h1>\n')

    for html_name in html_list:
        if (html_name != 'index.html'):
            index.write('<a href="' + public_url + html_name + '">' + html_name + '</a>\n')
            index.write('<br></br>\n')
    index.close()
