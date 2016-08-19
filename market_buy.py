# market buy 

import krakenex

# nouvelle classe API
k = krakenex.API()
# appel de la function load_key sur classe k
k.load_key('kraken.key')
# appel de la fonction query_private (pour passer un ordre AddOrder, sur la pair BTC/EUR, d'achat, au prix du marché, pour un montant de 0.01BTC)
k.query_private('AddOrder', {'pair': 'XXBTZEUR',
                             'type': 'buy',
                             'ordertype': 'market',
                             'volume': '0.01'})
