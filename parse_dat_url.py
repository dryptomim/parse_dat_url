import sys
import re
from urllib.parse import parse_qs, urlsplit

SCHEME_REGEX = r'[a-z]+:\/\/'
VERSION_REGEX = r'^(dat:\/\/)?([^/]+)(\+[^/]+)(.*)$'

def parse_dat_url (string, qs = None):
    
    if re.match(SCHEME_REGEX,string) is None:
        string = 'dat://' + string
    
    parsed,version = None, None
    result = {}
    match = [s for s in re.findall(VERSION_REGEX,string)]
    if match:
        parsed = urlsplit((match[0][0] or '') + (match[0][1] or '') + (match[0][3] or ''))
        version = str(match[0][2])[1:]
    else:
        parsed = urlsplit(string)
    if parsed.query is not None:
       search = parsed.query
       query = parse_qs(parsed.query, qs)
    #print("SEARCH: " + str(search) + " QUERY: " + str(query))
    result['protocol'] = parsed.scheme + ':'
    result['slashes'] = True
    result['auth'] = None
    result['host'] =  parsed.netloc
    result['port'] = None
    result['hostname'] = parsed.netloc
    result['hash'] = None
    result['search'] = search
    result['query'] = query
    result['pathname'] =  parsed.path
    result['path'] =  parsed.path or ''
    result['href'] =  string
    result['version'] =  version        
    return result