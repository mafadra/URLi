from urliclasses.genericusermessages import *

class output_manager:
    def __init__(self, output_argument):
        self.output_argument = output_argument

    def save_consult_in_output(self, consults):
        output_file_name = self.output_argument[0]
        output_file_type = output_file_name.split('.')[1]
        status_code_output_filter = list(map(str, self.output_argument[1:]))
        if output_file_type == 'txt':
            with open(output_file_name, 'w') as output_txt_file:
                if len(status_code_output_filter) > 0:
                    for consult in consults:
                        if consult['request_status_code'] in status_code_output_filter:
                            output_txt_file.write(f'{consult["request_datetime"]} - {consult["request_status_code"]} {consult["request_url"]}\n')

                else:
                    for consult in consults:
                        output_txt_file.write(f'{consult["request_datetime"]} - {consult["request_status_code"]} {consult["request_url"]}\n')

        elif output_file_type == 'json':
            import json
            with open(output_file_name, 'w') as output_json_file:
                json.dump(consults, output_json_file, indent=4)

    def output_file_type_is_supported(self, output_file_name: str, supported_output_file_types):
        output_file_type = output_file_name.split('.')[1]
        if output_file_type in supported_output_file_types:
            return True

        else:
            return False

    def file_exists_in_current_folder(self, file_to_verify):
        import os

        if os.path.isfile(file_to_verify):
            return True

        else:
            return False

class wordlist_manager:
    @staticmethod
    def read_wordlist_file(wordlist_file):
        wild_subdomains_wordlist = []
        with open(wordlist_file, 'r') as wordlist:
            for line in wordlist:
                wild_subdomains_wordlist.append(line.strip())
        return wild_subdomains_wordlist