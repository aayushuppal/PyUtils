import urllib.request
from urllib.error import HTTPError
from time import time

def getData(**kwargs):
    ts = time()

    args = kwargs['args']

    try:
        content = urllib.request.urlopen(args['get_url']).read()
    except HTTPError:
        content = None

    args['output']['content']    = content
    args['output']['time_taken'] = time() - ts

    print('getData for=\"{}\" takes time={}s'.format( args['get_url']
                                                , args['output']['time_taken']))
