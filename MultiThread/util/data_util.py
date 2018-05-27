import urllib.request
from time import time

def getData(**kwargs):
    ts = time()

    args = kwargs['args']

    content = urllib.request.urlopen(args['get_url']).read()

    args['output']['content']    = content
    args['output']['time_taken'] = time() - ts

    print('getData for=\"{}\" takes={}s'.format( args['get_url']
                                                , args['output']['time_taken']))
