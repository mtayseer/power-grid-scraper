import urllib, datetime, os

def fetch():
    url = 'http://loadmeter.egyptera.org/ClockToolTip.aspx'
    output = datetime.datetime.now().strftime('egyptera.%Y-%m-%d-%H-%M-%S.html')
    output = os.path.join(os.path.dirname(__file__), output)
    content = urllib.urlretrieve(url, output)

if __name__ == '__main__':
    fetch()