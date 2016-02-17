from random import choice
from re import sub


def busy(bot, event, *args):

    verbs = [
        'absorbing', 'adjusting', 'allocating', 'compiling',
        'compressing', 'deallocating', 'decoding', 'decompliling',
        'decompressing', 'decrypting', 'demultiplexing', 'disabling',
        'enabling', 'encoding', 'encrypting', 'factoring',
        'generating', 'indexing', 'initializing', 'mapping',
        'multiplexing', 'parsing', 'prioritizing', 'reordering',
        'resolving', 'reticulating', 'routing', 'sorting',
        'transcoding', 'upgrading', 'unravelling'
    ]

    adjectives = [
        'active', 'associative', 'bi-directional', 'corrupt',
        'complex', 'cybernetic', 'dank', 'deterministic',
        'duplicate', 'dynamic', 'ethereal', 'euclidean',
        'finite', 'high-level', 'infinite', 'inverse',
        'linked', 'low-level', 'multi-dimensional', 'negative',
        'non-euclidean', 'positive', 'prallel', 'quantifiable',
        'random', 'sentient', 'static', 'sub-zero', 'tertiary',
        'unlinked', 'unusual', 'well-documented', 'vectorized',
        ''  # Intentionally blank
    ]

    nouns = [
        'algorithms', 'archives', 'arrays', 'caches', 'coprocesses',
        'cores', 'datasets', 'fields', 'frames',
        'functions', 'datastores', 'lists', 'matrices',
        'objects', 'procedures', 'processes', 'queues',
        'receptacles', 'repositories', 'sectors', 'segments',
        'sequences', 'splines', 'states', 'structures',
        'tables', 'threads'
    ]

    message = '{} {} {}'.format(
        choice(verbs),
        choice(adjectives),
        choice(nouns)
    )

    bot.send_message(event.conv, sub(' +', ' ', message))
