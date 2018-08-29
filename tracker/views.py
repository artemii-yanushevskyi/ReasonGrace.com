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

def bookmarks_display(request):
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
        
        from django.contrib.staticfiles.storage import staticfiles_storage
        url = staticfiles_storage.url('private/test.md')
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
