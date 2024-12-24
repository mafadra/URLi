from urliclasses.timeclasses import *
from termcolor import colored

class text_colors:
    @staticmethod
    def red_text(text):
        return colored(text, 'red')

    def green_text(text):
        return colored(text, 'green')

    def yellow_text(text):
        return colored(text, 'yellow')

    def blue_text(text):
        return colored(text, 'blue')

    def cyan_text(text):
        return colored(text, 'cyan')

    def magenta_text(text):
        return colored(text, 'magenta')

class urli_secondary_messages:
    @staticmethod
    class status_messages:
        @staticmethod
        def error_message(message):
            print(text_colors.red_text(f'[-] {message}'))
        
        def sucess_message(message):
            print(text_colors.green_text(f'[-] {message}'))
        
        def normal_message(message):
            print(f'[-] {message}')

    class especial_messages:
        @staticmethod
        def wildcard_subdomain(request_dict: dict):
            if request_dict['request_status_code'] == 200:
                urli_secondary_messages.status_codes_messages.ok_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]} | WILDCARD SUBDOMAIN')

            elif request_dict['request_status_code'] == 404:
                urli_secondary_messages.status_codes_messages.not_found_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]} | WILDCARD SUBDOMAIN')

            elif request_dict['request_status_code'] == 'RQE':
                urli_secondary_messages.status_codes_messages.request_error_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]} | WILDCARD SUBDOMAIN')
            
            else:
                urli_secondary_messages.status_codes_messages.other_status_code_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]} | WILDCARD SUBDOMAIN')

        def subdomain_in_wildcard_subdomain(request_dict: dict):
            if request_dict['request_status_code'] == 200:
                urli_secondary_messages.status_codes_messages.ok_message(f'> {request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')

            elif request_dict['request_status_code'] == 404:
                urli_secondary_messages.status_codes_messages.not_found_message(f'> {request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')

            elif request_dict['request_status_code'] == 'RQE':
                urli_secondary_messages.status_codes_messages.request_error_message(f'> {request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')
            
            else:
                urli_secondary_messages.status_codes_messages.other_status_code_message(f'> {request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')

    class status_codes_messages:
        @staticmethod
        def ok_message(message):
            print(text_colors.green_text(f'[-] {message}'))
        
        def not_found_message(message):
            print(text_colors.yellow_text(f'[-] {message}'))

        def request_error_message(message):
            print(text_colors.red_text(f'[-] {message}'))

        def other_status_code_message(message):
            print(text_colors.cyan_text(f'[-] {message}'))
    
class urli_principal_messages:
    @staticmethod
    def initial_urli_message(domain):
        print(text_colors.cyan_text(f'[-] Domain: {domain} | working on it, wait a little'))

    def header_message(items_list_size, timeout, consult_type, domain):
        estimated_hours, estimated_minutes, estimated_seconds = handle_time.estimated_time_urli_consult(items_list_size, timeout)
        current_time = handle_time.current_time('%d/%m/%Y %H:%M:%S')
        print(text_colors.magenta_text(f'[-] Estimated time: {estimated_hours} hours, {estimated_minutes} minutes, {estimated_seconds} seconds | {items_list_size} {consult_type} to check'))
        print(text_colors.blue_text(f'[-] Finding {consult_type} on https://{domain} at {current_time}'))

    def footer_message(consult_time_in_seconds, items_list_size, consult_type, domain):
        consult_hours, consult_minutes, consult_seconds = handle_time.convert_seconds_to_hms(consult_time_in_seconds)
        print(text_colors.blue_text(f'[-] {items_list_size} {consult_type} checked on https://{domain}'))
        print(text_colors.magenta_text(f'[-] Consult total time: {consult_hours} hours, {consult_minutes} minutes, {consult_seconds} seconds'))

    def urli_banner():
        print(text_colors.yellow_text(r'''
 _   _ ____  _     _ 
| | | |  _ \| |   (_)
| | | | |_) | |   | |
| |_| |  _ <| |___| |
 \___/|_| \_\_____|_|v1.0
'''))
        