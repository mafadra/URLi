from urliclasses.genericusermessages import *
import requests as r

class handle_requests:
    @staticmethod
    def url_is_up(url_to_check):
        try:
            subdomain_font_request = r.get(url_to_check)

        except r.exceptions.RequestException:
            return False, 'request error'

        else:
            if subdomain_font_request.status_code == 200:
                return True, subdomain_font_request.status_code
            else:
                return False, subdomain_font_request.status_code
    
    def request_subdomain_and_return_response_dict(url_to_request, request_headers, request_timeout):
        try:
            response = r.get(url_to_request, headers=request_headers, timeout=request_timeout)

        except r.exceptions.RequestException:
            return {
                'request_url': url_to_request,
                'request_status_code': 'RQE',
                'request_reason': 'request error',
                'request_datetime': handle_time.current_time('%Y-%m-%d %H:%M:%S')
            }
            
        else:
            return {
                'request_url': url_to_request,
                'request_status_code': response.status_code,
                'request_reason': response.reason,
                'request_datetime': handle_time.current_time('%Y-%m-%d %H:%M:%S')
            }

    def check_status_codes_and_show_results(request_dict):
        if request_dict['request_status_code'] == 200:
            urli_secondary_messages.status_codes_messages.ok_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')

        elif request_dict['request_status_code'] == 404:
            urli_secondary_messages.status_codes_messages.not_found_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')

        elif request_dict['request_status_code'] == 'RQE':
            urli_secondary_messages.status_codes_messages.request_error_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')
        
        else:
            urli_secondary_messages.status_codes_messages.other_status_code_message(f'{request_dict["request_datetime"]} | {request_dict["request_status_code"]} {request_dict["request_url"]} - {request_dict["request_reason"]}')
