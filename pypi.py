import alp
import argparse
import xmlrpclib

def pypi_query(query, pip=False):
    client = xmlrpclib.ServerProxy('http://pypi.python.org/pypi')
    results = client.search({'name': query})
    items = []

    results.sort(key = lambda item: item['_pypi_ordering'], reverse=True)
    results = results[:30]

    for i, result in enumerate(results, start=1):
        subtitle = u'Version: {0} | {1}'.format(
            result.get('version'),
            result.get('summary'))

        arg = 'https://pypi.python.org/pypi/{0}/'.format(result.get('name'))
        if pip:
            arg = 'pip install {0}=={1}'.format(
                result.get('name'),
                result.get('version'))

        item = alp.Item(
            uid=str(i),
            arg=arg,
            valid=True,
            title=result.get('name'),
            subtitle=subtitle)
        items.append(item)

    alp.feedback(items)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--query',
        required=True,
        help='The term to query pypi')
    parser.add_argument(
        '--pip',
        action='store_true',
        help='Return pip install command instead of url')
    args = parser.parse_args()
    pypi_query(args.query, args.pip)
