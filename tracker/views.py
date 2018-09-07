from django.shortcuts import render
from django.utils import timezone 
from tracker.models import Post
from django.http import HttpResponse
                                                                                                                                            
def tracker_data(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'tracker/tracker_data.html', {'posts': posts})

def dynamic_update(request):
    html = "<h1>dynamic update</h1> <code>def dynamic_update(request):</code>"
    return HttpResponse(html)

class ViewTemplateExport:
    def __init__(self, content, init_type='text', compose_type='html'):
        self.content = content # usually dictionary
        self.init_type = init_type
        self.compose_type = compose_type

    def compose(self):
        ''' prepare the object for export to template'''
        if type(self.content) == type({}) and self.init_type=='dictionary' and self.compose_type=='JSON':
            import json
            dictionary = self.content.copy() # absolutely necessary to make a copy,
            # so that changes in dictionary will not affect self.content.
            
            # How to see inside variable "dictionary" if I don't know how to print?
            # raise Exception(dictionary, type(dictionary))
            dictionary_str = sterile_dictionary(dictionary)

            json_string = json.dumps(dictionary_str)
            return_string = json_string
        elif self.init_type == "md" and self.compose_type=="jsvar":
            # use \n instead of \\n to make an actual new line, as opposed to a symbol "\n", in final html
            return_string = self.content.replace("\n", "\\n") + "\\n###### md to jsvar"
        else:
            # meaning input type is ..
            return_string = self.content
        return return_string

def sterile_HTML(html):
    import cgi
    sterile_bin = cgi.escape(html).encode('ascii', 'xmlcharrefreplace') # will be a binary string
    sterile = sterile_bin.decode() # now that's a string
    return sterile
    
def sterile_dictionary(dic):
    ''' converts a dictionary to a dictionary of strings'''
    for key, value in dic.items():
        if type(key) is not str:
            raise Exception("A key type has to be str, but", key, "is not a string")
            
        if type(value) is str:
            pass # the desired case
        elif type(value) is dict:
            dict_value = sterile_dictionary(value) # recurcive call
            dic[key] = dict_value
        else:
            # converting to str, for 
            # 'uwsgi.version': b'2.0.17.1' and
            # 'wsgi.errors': <_io.TextIOWrapper name=2 mode='w' encoding='UTF-8'>,
            dic[key] = str(value)
    return dic
            
def request_info(request):
    # general info: <WSGIRequest: POST '/bookmarks'>
    general_info = sterile_HTML(str(request))
    # detailed info: will be a dictionary passed to template as JSON string
    detailed_info = ViewTemplateExport(vars(request), init_type='dictionary', compose_type='JSON') # will be a json string
    return general_info, detailed_info

def site_report(request):
    ''' view'''
    from os import getcwd, path

    # request test
    request_general, request_detailed = request_info(request) # tupple, general and detailed information about request

    # db test
    from tracker.models import Bookmark
    bookmarks = Bookmark.objects.order_by('created_date')

    # django test
    from django.conf import settings
    static_root, static_url = settings.STATIC_ROOT, settings.STATIC_URL
    settings_static = ViewTemplateExport(
        "Static **root**```" + static_root + "```\nStatic **URL** ```" + static_url + "```.\n",
        init_type="md", compose_type="jsvar")

    # md test
    md_file_url = path.join(settings.STATIC_ROOT, 'private/test.md')
    md_info = "**complete** URL of the ```test.md``` on the server: ```" + md_file_url + "```.\\n### Context of test.md\n"
    # there is a bug "```.\n### Con..." works as expected, while "```.\n ### Con..." doesn't (ignores \n)
    with open(md_file_url) as f: 
        md_file_text = f.read()                          
    md = ViewTemplateExport(md_info + md_file_text,
        init_type="md", compose_type="jsvar")
  
    # bash test
    bash_query = "ls -al"
    bash_resp = run_bash(bash_query)

    # env test
    cwd = getcwd()

    return render(request, 'tracker/site_report.html', {
        'bookmarks': bookmarks, 
        'request_general': request_general, 'request_detailed': request_detailed.compose(),
        'settings_static': settings_static.compose(),
        'md': md.compose(),
        'bash_resp': bash_resp,
        'cwd': cwd,
    }) 

def bookmarks_display(request):
    ''' view'''
    from tracker.models import Bookmark
    
    if request.method == 'POST': 
        # If the form has been submitted... 
        import cgi
        html = ""
        html += str(dir(request))
        html += "<br><br>"
        html += str(vars(request))
        request_html_sterile = cgi.escape(request.__str__()).encode('ascii', 'xmlcharrefreplace') # will be a binary string
        request_html_sterile_str = request_html_sterile.decode()
        html += "<br><br>"
        html += "Request<br>: " + request_html_sterile_str
        # do your things with the posted data
        return HttpResponse(html) 
    else: 
        # form not posted : show the form.
        bookmarks = Bookmark.objects.order_by('created_date')
        html_notes = ""
        notes = ""
        md_notes = ""
        import os
              
        from django.conf import settings
        md_notes += "**import STATIC_ROOT _from_ settings: ```" + settings.STATIC_ROOT + "```**\\n"
        url = os.path.join(settings.STATIC_ROOT, 'private/test.md')
        md_notes += "#Full URL of the test.md: ```" + url + "```.\\n context of test.md:\\n" 
        with open(url) as f:
            md_text = f.read()
        md_text_flatline = md_text.replace("\n", "\\n")
        md_notes += '\\n\\n' + md_text_flatline 
        # use \n instead of \\n to make an actual new line, as opposed to a symbol "\n", in final html
        html_notes += os.getcwd() + "<br>\n"
        html_notes += "<br>\n".join(os.listdir("/home/fabulous/site")) 
        
        bash_query = """curl https://api.github.com/markdown/raw -X "POST" -H "Content-Type: text/plain" -d 
            "**ctrlf** __adf__" """
        bash = run_bash(bash_query)
        html_notes += bash.replace("\n", "<br>\n")
        notes += bash_query
        return render(request, 'tracker/bookmarks_display.html', {'bookmarks': bookmarks, 'request': request,
            'notes': notes, 'html_notes': html_notes,
            'md_notes': md_notes,
            })


def run_bash(bashCommand="ls -al"):
        # allows to run only one command at a time; & and && are unavailable
        # for scripts insert "./testbash.sh", better "sh test.sh" or "bash test.sh"
        import subprocess
        # Directory /home/fabulous == ~
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE, cwd="/home/fabulous/site/mysite/Blueprint")
        output, error = process.communicate() 
        response = "Output:\n{}\n\nError:\n{}\n\n".format(output, error) 
        # response_bin_convert = map(hex,output)
        # response_bin = "Output:\n{}\n\nError:\n{}\n\n".format(" ".join(char for char in response_bin_convert), error)    
        return response

