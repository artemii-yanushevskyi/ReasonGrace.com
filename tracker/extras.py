def my_encode(n):
    return (n*34 + 71)//541

class ViewTemplateExport:
    def __init__(self, content, init_type='text', compose_type='html'):
        self.content = content # usually dictionary
        self.init_type = init_type
        self.compose_type = compose_type

    def compose(self):
        ''' prepare the object for export to template'''
        from collections import OrderedDict
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
