from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from tracker.models import Purchase

from tracker.extras import sterile_HTML, sterile_dictionary, run_bash, ViewTemplateExport, name_string, query

'''
def shop_dash(request, seller='artemii')
def encode_page(request, username="example")
def decode_page(request)
def site_report(request)
'''

def shop_qr(request, seller='artemii'):
    meta = request.META # extract meta information from request
    # (this is a dictionary)

    log = open('log.txt', 'a+')
    print(timezone.now(), file=log)
    print('link: ' + meta['REQUEST_URI'], file=log)
    print(meta['PATH_INFO'], '+?',  meta['QUERY_STRING'], file=log)
    # which is the same as meta['REQUEST_URI']
    for key in request.GET.keys():
        # request.GET is a QueryDict, note 'vars' and 'dir'
        print(key, ': ', request.GET[key], file=log)
    print('end log entry', file=log)
    log.close()

    # check validity
    if all(key in request.GET.keys() for key in ['type', 'price']):
        # make an entry in a db
        product = request.GET
        Purchase.objects.create(type=product['type'], price=product['price'], seller=seller)
        return render(request, 'tracker/shop_qr.html', {
                'seller': seller,
                'type': product['type'],
                'price': product['price'],
            })
    else:
        return HttpResponse("Error, check the valididy of the product link")


def shop_dash(request, seller='artemii'):
    from collections import OrderedDict
    from tracker.forms import PurchaseForm

    if request.method == 'POST':
        # could be done this way without validation
        # type = request.POST.get('type')
        form_response = PurchaseForm(request.POST)
        if form_response.is_valid():
            type = form_response.cleaned_data['type']
            price = form_response.cleaned_data['price']
            Purchase.objects.create(type=type, price=price, seller=seller)
            # parameters are sent to db, redirecting to this page
            # method will be POST, form will not be resubmitted on page refresh
            # e.g. an http GET after a POST
            return HttpResponseRedirect(reverse('shop_dash', args=[seller]))
            # reverse will return shop/sellername
        else:
            return HttpResponse("<h3>Error, the form is not valid. Please doublecheck the entry.</h3>")
    else: # meaning request.method is GET
        # render a page
        form = PurchaseForm()

        from collections import OrderedDict
        table_dict = OrderedDict()

        from mysite.settings import TIME_ZONE
        timezone.activate(TIME_ZONE) # ('Europe/Kiev')
        # time in db should always be in UTC format
        # convert it to local time right before output

        for purchase in Purchase.objects.raw('SELECT * FROM tracker_purchase ORDER BY time DESC'):
            purchase_dict = {
                'type': purchase.type,
                'price': str(purchase.price), # because JSON has only strings, the same with id
                'time': timezone.localtime(purchase.time).strftime("%H:%M"),
                'seller': name_string(purchase.seller), # uppercase first letter, lovercase the rest
            }
            # table_dict[str(purchase.id)] = purchase_dict
            table_dict[str(purchase.id)] = purchase_dict  # JSON should contain only strings, id is int

        table_list = ViewTemplateExport(table_dict, init_type='dictionary', compose_type='list') # will be a list string


        test = OrderedDict()

        i = 0
        for purchase in Purchase.objects.raw(query['group by type price']):
            purchase_dict = {
                'type': purchase.type,
                'price': str(purchase.price), # because JSON has only strings, the same with id
                # 'time': timezone.localtime(purchase.time).strftime("%H:%M"),
                # 'seller': purchase.seller,
                'groupsize': purchase.groupsize
            }
            # table_dict[str(purchase.id)] = purchase_dict
            test[str(i)] = purchase_dict  # JSON should contain only strings, id is int
            i += 1

        test = ViewTemplateExport(test, init_type='dictionary', compose_type='JSON') # will be a list string

        return render(request, 'tracker/shop_dash.html', {
                'table': table_list.compose(),
                'form': form,
                'seller': name_string(seller),
                'test': test.compose(),
            })

def encode_page(request, username="example"):
    from tracker.forms import EncodeForm

    method = request.method
    form = EncodeForm()
    if request.method == 'POST':
        form = EncodeForm(request.POST)
        message = form.data['message']
        try:
            number = int(message)
            from tracker.extras import my_encode
            crypto = my_encode(number)
            message = "Encoded number" + str(crypto)
        except:
            message = "Must be int"
    elif request.method == 'GET':
        message = 'Create a message'
    return render(request, 'tracker/encode_page.html', {
            'method' :method,
            'message': message,
            'form': form,
        })


def decode_page(request):
    method = request.method
    form = EncodeForm()
    if request.method == 'POST':
        form = EncodeForm(request.POST)
        message = form.data['message']
        try:
            number = int(message)
            from tracker.extras import my_encode
            crypto = my_encode(number)
            message = "Encoded number" + str(crypto)
        except:
            message = "Must be int"
    elif request.method == 'GET':
        message = 'Create a message'
    return render(request, 'tracker/encode_page.html', {
            'method' :method,
            'message': message,
            'form': form,
        })

def site_report(request):
    ''' view'''
    from os import getcwd, path

    # request test
    request_general, request_detailed = request_info(request) # tupple, general and detailed information about request

    # db test
    try:
        from tracker.models import Bookmark
        bookmarks = Bookmark.objects.order_by('created_date')
    except:
        bookmarks = "No bookmarks"

    # django test
    from django.conf import settings
    static_root, static_url = settings.STATIC_ROOT, settings.STATIC_URL
    settings_static = ViewTemplateExport( {
        "Static Root": static_root,
        "Static URL": static_url,
    }, init_type="dictionary", compose_type="JSON")

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

    # views.py show

    with open('tracker/views.py', 'r') as f:
        views_py = f.read()

    return render(request, 'tracker/site_report.html', {
        'bookmarks': bookmarks,
        'request_general': request_general,
        'request_detailed': request_detailed.compose(),
        'settings_static': settings_static.compose(),
        'md': md.compose(),
        'bash_resp': bash_resp,
        'cwd': cwd,
        'views_py': views_py,
    })

def request_info(request):
     # general info: <WSGIRequest: POST '/bookmarks'>
     general_info = sterile_HTML(str(request))
     # detailed info: will be a dictionary passed to template as JSON string
     detailed_info = ViewTemplateExport(vars(request), init_type='dictionary', compose_type='JSON') # will be a json string
     return general_info, detailed_info

def unicode_test(request):
    return HttpResponse("Текст українською, English txt")
