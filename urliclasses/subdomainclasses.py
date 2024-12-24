from urliclasses.file import *
from urliclasses.formatresults import *
from urliclasses.handlerequests import *
from urliclasses.genericusermessages import *
from urliclasses.timeclasses import *
import requests as r

class subdomain_fonts:
    def __init__(self, domain):
        self.domain = domain

    @property
    def subdomains_from_crtsh(self):
        crtsh_url = f'https://crt.sh/json?q={self.domain}'
        response = r.get(crtsh_url)
        crtsh_is_up, crtsh_status_code = handle_requests.url_is_up(crtsh_url)
        if crtsh_is_up == True:
            urli_secondary_messages.status_messages.normal_message(f'Finding subdomains on https://crt.sh - status code: {crtsh_status_code}')
            subdomains_from_crtsh = []
            response_crtsh_json = response.json()
            for entry in response_crtsh_json:
                entry['name_value'] = entry['name_value'].split('\n')
                for entry_name_value in entry['name_value']:
                    subdomains_from_crtsh.append(entry_name_value)

            return {
                'subdomains_from_crtsh': subdomains_from_crtsh,
                'crtsh_is_up': True
            }

        else:
            urli_secondary_messages.status_messages.error_message(f'Crtsh is down. Try to run URLi later - status code: {crtsh_status_code}')
            return {
                'subdomains_from_crtsh': [],
                'crtsh_is_up': False
            }

    @property
    def formatted_results_from_all_subdomains_fonts(self):
        all_results = format_result.sum_all_results_from_subdomain_fonts(self.subdomains_from_crtsh['subdomains_from_crtsh'])
        all_results = format_result.remove_duplicated_items(all_results)
        all_results = format_result.remove_specific_item_from_list(all_results, self.domain)
        return all_results

class subdomain:
    def __init__(self, subdomains_to_request, target_domain):
        self.subdomains_to_request = subdomains_to_request
        self.target_domain = target_domain
    
    def handle_wildcard_subdomain(self, wildcard_subdomain: str, request_headers, request_timeout, status_code_filter):
        wildcard_url = f'https://{wildcard_subdomain}'
        wildcard_subdomain_response_dict = handle_requests.request_subdomain_and_return_response_dict(wildcard_url, request_headers, request_timeout)
        urli_secondary_messages.especial_messages.wildcard_subdomain(wildcard_subdomain_response_dict)
        if wildcard_subdomain_response_dict['request_status_code'] == 200:
            for potencial_subdomain in wordlist_manager.read_wordlist_file('urliclasses/wildsubdomains.txt'):
                potencial_subdomain_url = f'https://{potencial_subdomain}.{wildcard_subdomain}'
                potencial_subdomain_response_dict = handle_requests.request_subdomain_and_return_response_dict(potencial_subdomain_url, request_headers, request_timeout)
                if status_code_filter:
                    if potencial_subdomain_response_dict['request_status_code'] in status_code_filter:
                        urli_secondary_messages.especial_messages.subdomain_in_wildcard_subdomain(potencial_subdomain_response_dict)
                        continue
                
                else:
                    urli_secondary_messages.especial_messages.subdomain_in_wildcard_subdomain(potencial_subdomain_response_dict)
                    continue
        else:
            return False

    def process_subdomains_responses(self, request_headers, request_timeout, status_code_filter: list):
        urli_consult_timer = timer()
        subdomains = []
        wildcard_subdomains = []
        with urli_consult_timer:
            for subdomain_to_request in self.subdomains_to_request:
                if '*.' in subdomain_to_request:
                    subdomain_to_request = subdomain_to_request.replace('*.', '')
                    wildcard_subdomains.append(subdomain_to_request)
                    continue
                
                subdomain_to_request_url = f'https://{subdomain_to_request}'
                response_dict = handle_requests.request_subdomain_and_return_response_dict(subdomain_to_request_url, request_headers, request_timeout)

                if status_code_filter:
                    if response_dict['request_status_code'] in status_code_filter:
                        if subdomain_to_request in wildcard_subdomains:
                            self.handle_wildcard_subdomain(subdomain_to_request, request_headers, request_timeout, status_code_filter)
                            continue
                        handle_requests.check_status_codes_and_show_results(response_dict)
                        subdomains.append(response_dict)

                else:
                    if subdomain_to_request in wildcard_subdomains:
                        self.handle_wildcard_subdomain(subdomain_to_request, request_headers, request_timeout, status_code_filter)
                        continue
                    handle_requests.check_status_codes_and_show_results(response_dict)
                    subdomains.append(response_dict)

        return urli_consult_timer.urli_execution_time_in_seconds, subdomains

    def show_subdomains_final_results(self, request_headers, request_timeout, status_code_filter: list):
        urli_principal_messages.header_message(len(self.subdomains_to_request), request_timeout, 'subdomains', self.target_domain)
        consult_total_time, subdomains = self.process_subdomains_responses(request_headers, request_timeout, status_code_filter)
        urli_principal_messages.footer_message(consult_total_time, len(self.subdomains_to_request), 'subdomains', self.target_domain)
        return subdomains