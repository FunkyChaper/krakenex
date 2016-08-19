# market buy 

import krakenex

k = krakenex.API()
k.load_key('kraken.key')

k.query_private('AddOrder', {'pair': 'XXBTZEUR',
                             'type': 'buy',
                             'ordertype': 'market',
                             'volume': '0.01'})