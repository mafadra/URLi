from urliclasses.arguments import *
from urliclasses.file import *
from urliclasses.formatresults import *
from urliclasses.subdomainclasses import *
from urliclasses.genericusermessages import *
import argparse
import sys

arguments_class = arguments(argparse.ArgumentParser(description='--- URLi is a tool that list subdomains in a application | visit (link) to know more | version: v1.0.0 ---'))
domain_to_verify = arguments_class.args.domain
status_code_filter = arguments_class.args.status_code
output_file_arg = arguments_class.args.output

urli_principal_messages.urli_banner()
urli_principal_messages.initial_urli_message(domain_to_verify)

outpt_manager = output_manager(output_file_arg)

supported_output_file_types = ['txt', 'json']
target_domain_is_up, domain_status_code = handle_requests.url_is_up(f'https://{domain_to_verify}')

if target_domain_is_up == False:
    urli_secondary_messages.status_messages.error_message(f"Domain '{domain_to_verify}' is down")
    sys.exit()

if output_file_arg:
    output_file_name = output_file_arg[0]
    if outpt_manager.output_file_type_is_supported(output_file_name, supported_output_file_types) == False:
        output_file_type = output_file_name.split('.')[1]
        urli_secondary_messages.status_messages.error_message(f"'{output_file_type}' to output file is not supported. Try to use 'txt' or 'json' format")
        sys.exit()

    if outpt_manager.file_exists_in_current_folder(output_file_name) == True:
        urli_secondary_messages.status_messages.error_message(f"File '{output_file_name}' already exists in current folder. Try to use other name to output file")
        sys.exit()

sb_fonts = subdomain_fonts(domain_to_verify)
subdomains_results = sb_fonts.formatted_results_from_all_subdomains_fonts
sb = subdomain(subdomains_results, domain_to_verify)
subdomains = sb.show_subdomains_final_results(None, 5, status_code_filter)

if output_file_arg:
    outpt_manager.save_consult_in_output(subdomains)
