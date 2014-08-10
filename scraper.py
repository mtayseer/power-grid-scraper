import urllib, datetime, os

def fetch():
    # Instead of doing all the parsing later, I get the status from Mosab's site & store it
    url = 'http://power-grid-status.mos3abof.com/status'
    output = datetime.datetime.now().strftime('egyptera.%Y-%m-%d-%H-%M-%S.json')
    output = os.path.join(os.path.dirname(__file__), output)
    content = urllib.urlretrieve(url, output)

if __name__ == '__main__':
    fetch()