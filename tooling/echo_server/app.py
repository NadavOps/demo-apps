import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import environ

PORT = environ.get('PORT', 8080)

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        message_parts = [
                'CLIENT VALUES:',
                'client_address=%s (%s)' % (self.client_address,
                                            self.address_string()),
                'command=%s' % self.command,
                'path=%s' % self.path,
                'real path=%s' % parsed_path.path,
                'query=%s' % parsed_path.query,
                'request_version=%s' % self.request_version,
                '',
                'SERVER VALUES:',
                'server_version=%s' % self.server_version,
                'sys_version=%s' % self.sys_version,
                'protocol_version=%s' % self.protocol_version,
                '',
                'HEADERS RECEIVED:',
                ]
        for name, value in sorted(self.headers.items()):
            if name.lower() == "cookie":
                try:
                    message_parts.append(f'{name}:')
                    cookie_value_as_array = value.rstrip().split("; ")
                    for item in cookie_value_as_array:
                        cookie_key = item.split("=")[0]
                        cookie_value = item.split("=")[1]
                        message_parts.append(f'  {cookie_key}: {cookie_value}')
                except Exception as e:
                    print(f"ERROR: cookie header was not recived as opinionated expected, defaulting to regular output. Exception is: {e}")
                    message_parts.append('%s: %s' % (name, value.rstrip()))
            else:
                message_parts.append('%s: %s' % (name, value.rstrip()))
        message_parts.append('')
        message = '\r\n'.join(message_parts)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))
        return

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', int(PORT)), GetHandler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
