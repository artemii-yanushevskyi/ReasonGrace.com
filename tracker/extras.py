# -*- coding: utf-8 -*-
from collections import OrderedDict

def name_string(name):
    ''' uppercase first letter, lovercase the rest
    full unicode support
    Usage:
    # -*- coding: utf-8 -*- is required
    print(name_string('НфВАФвІЇЇФАІЧУВСКАС КИТ?ЮБЄЖДЛЇХЗЩШГыаываФываФывафыВапавыППЫАВПЫВАР326492387!@#$%^&*к4Me'))
    '''
    return name.decode('utf-8').upper()[0] + name.decode('utf-8').lower()[1:]

def my_encode(n):
    return (n*34 + 71)//541

class ViewTemplateExport:
    def __init__(self, content, init_type='text', compose_type='html'):
        self.content = content # usually dictionary
        self.init_type = init_type
        self.compose_type = compose_type

    def compose(self):
        ''' prepare the object for export to template'''
        if type(self.content) is dict or type(self.content) is OrderedDict and self.init_type=='dictionary' and self.compose_type=='JSON':
            import json
            dictionary = self.content.copy() # absolutely necessary to make a copy,
            # so that changes in dictionary will not affect self.content.

            # How to see inside variable "dictionary" if I don't know how to print?
            # raise Exception(dictionary, type(dictionary))
            dictionary_str = sterile_dictionary(dictionary)
            if type(self.content) is OrderedDict:
                json_string = json.dumps(dictionary_str, sort_keys=False, indent=4)
            elif type(self.content) is dict:
                json_string = json.dumps(dictionary_str, sort_keys=True, indent=4)
            # json_string = json_string.replace("\n", "\\n")
            return_string = json_string
        elif type(self.content) is dict or type(self.content) is OrderedDict and self.init_type=='dictionary' and self.compose_type=='list':
            dictionary = self.content.copy() # absolutely necessary to make a copy,
            # so that changes in dictionary will not affect self.content.

            dictionary_sterile = sterile_dictionary(self.content)
            return_string = str(dictionary_to_listdict(dictionary_sterile))

        elif self.init_type == "md" and self.compose_type=="jsvar":
            # use \n instead of \\n to make an actual new line, as opposed to a symbol "\n", in final html
            return_string = self.content.replace("\n", "\\n") + "\\n###### md to jsvar"
        else:
            # meaning input type is ..
            return_string = self.content
        return return_string

def dictionary_to_listdict(dictionary):
    if is_dictionary(dictionary):
        return_list = []
        for key, value in dictionary.items():
            list = [key] + [dictionary_to_listdict(value)]
            return_list.append(list)
        return return_list
    else:
        return dictionary

def sterile_HTML(html):
    import cgi
    sterile_bin = cgi.escape(html).encode('ascii', 'xmlcharrefreplace') # will be a binary string
    sterile = sterile_bin.decode() # now that's a string
    return sterile

def sterile_dictionary(dictionary):
    ''' converts a dictionary to a dictionary of strings'''
    for key, value in dictionary.items():
        if type(key) is not str:
            raise Exception("A key type has to be str, but", key, "is not a string")

        if type(value) is str:
            pass # the desired case
        elif type(value) is dict:
            dict_value = sterile_dictionary(value) # recurcive call
            dictionary[key] = dict_value
        else:
            dictionary[key] = str(value)
    return dictionary

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

def is_dictionary(obj):
    return True if type(obj) is OrderedDict or type(obj) is dict else False


query = {
    'list new first':
        'SELECT * FROM tracker_purchase ORDER BY time DESC',
    'group by type price':
        'SELECT id, type, price, count(*) as groupsize FROM tracker_purchase GROUP BY type, price',
    }
