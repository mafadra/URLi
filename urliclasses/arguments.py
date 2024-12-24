class arguments:
    def __init__(self, parser):
        self.parser = parser

        self.required_group = self.parser.add_argument_group('required_arguments')
        self.required_group.add_argument('-d', '--domain', dest='domain', type=str, required=True, help='argument to the domain | ex.: -d or --domain domain.com')
        self.required_group.add_argument('-sc', '--subdomain-consult', dest='subdomain_consult', action='store_true', required=True, help='argument to subdomain consult | ex.: -sc or --subdomain-consult')

        self.parser.add_argument('-o', '--output', dest='output', type=str, required=False, nargs='+', help='argument to output | ex.: -o outputfile.txt or --output outputfile.txt (only txt and json format supported)')
        self.parser.add_argument('-s', '--status-code', dest='status_code', type=int, required=False, nargs='+', help='argument to filter status code | ex.: -s or --status-code 200 404 500 (you can use one or more status code)')

    @property
    def args(self):
        return self.parser.parse_args()
