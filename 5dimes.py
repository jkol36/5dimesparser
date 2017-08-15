import requests


#first query 5 dimes
#send form data to LoginVerify.asp
s = requests.Session()
def authenticate():
	request_mapper = {
		'1': {'url':'http://www.5dimes.eu/LoginVerify.Asp', 
			'headers': {
			    'Origin': 'http://www.5dimes.eu',
			    'Accept-Encoding': 'gzip, deflate',
			    'Accept-Language': 'en-US,en;q=0.8',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
			    'Content-Type': 'application/x-www-form-urlencoded',
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			    'Cache-Control': 'max-age=0',
			    'Referer': 'http://www.5dimes.eu/',
			    'Connection': 'keep-alive',
			},
			'cookies': {
		    'ASPSESSIONIDQSQRCADC': 'CLOFMIBANEAJKNCJLOCACEBM',
		    'ASPSESSIONIDAQRSDDAB': 'GMOJMIBANDNKJKBHMKNOCNOL',
		    '5DCustomer': 'ic35946',
		    '78935480-VID': '1219202351480350',
		    '78935480-SKEY': '6755025048354475359',
		    'HumanClickSiteContainerID_78935480': 'STANDALONE',
		    'ASPSESSIONIDQSBQCADD': 'DLMMMIBAIJJPPFILCLNHCKLE'
			},
			'data':'customerID=ic35946&password=Bettor123&goto=S&submit1=Login'
		},
		'2': {'url': 'http://www.5dimes.eu/LoginVerify2.Asp',
			'headers': {
		    'Origin': 'http://www.5dimes.eu',
		    'Accept-Encoding': 'gzip, deflate',
		    'Accept-Language': 'en-US,en;q=0.8',
		    'Upgrade-Insecure-Requests': '1',
		    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
		    'Content-Type': 'application/x-www-form-urlencoded',
		    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		    'Cache-Control': 'max-age=0',
		    'Referer': 'http://www.5dimes.eu/LoginVerify.Asp',
		    'Connection': 'keep-alive'
			},
			'cookies': {
			    'ASPSESSIONIDQSQRCADC': 'CLOFMIBANEAJKNCJLOCACEBM',
			    'ASPSESSIONIDAQRSDDAB': 'GMOJMIBANDNKJKBHMKNOCNOL',
			    '5DCustomer': 'ic35946',
			    '78935480-VID': '1219202351480350',
			    '78935480-SKEY': '6755025048354475359',
			    'HumanClickSiteContainerID_78935480': 'STANDALONE',
			    'ASPSESSIONIDQSBQCADD': 'DLMMMIBAIJJPPFILCLNHCKLE'
			},	

			'data': 'customerID=ic35946&password=Bettor123&goto=S&ioBB=0400R9HVeoYv1gsNf94lis1ztkb1RWgb4ZAt%2B9xxA32YhA%2F7t%2FXdl3yovcBEtpQUidHpL66jjezG%2FfXXnfra5uHnDwI%2BY73H2L2OdUsprl5Sq8nl3OCiMt8Ua81mEx5T4nMe2V8MP4h2JKRMHa4CePzc2Qz1gslwtNv6MLejutG4hxLRAWjwuaoD5SgO%2BUqpxb%2B%2BsZBfgyIR%2BXyE6hsi11FUlhkwfCqvl92YFoMYq0xp4y64xI1RTIYC8ouD71qCKcmZqa%2Bc5UMfdLNXqLz%2B1vlqUAr9dE2jcfl0wgroQBfpyuLBX2tqQuRw89ZA7Bf4iSOrVTw2C4oQ2p5KKlg2xwOLLtPtb5t32w%2BKigIYmGjEZZSZsEq6iTzfMHoP%2F7tyR4jyYtRAfcOg9jbPrUkHB8HIR7yGLvlRliwz898GnyP1mBxLEwrNkykUlAfOtP2LQF5swOGCmEaWeJamIif%2FiDuMCcLUB69g4E97xS9GTGQ%2FPXHr6cXXHZ4V1gkH%2BzgzCnlu2IdccHc397y%2FuWnmR53MjcYRY3uox5K7Yg8CuMOt5MLq4WCiHMbq2GjALu16znkKgpMf97%2B4%2BapLMrPrMVvJlvLE8xAy%2Fthn2bG0spfZB%2BdxKzY0c1nMArLlM2qhzPAJGVfyNMcvdtBAR27Zdi%2BvjqcgW2OSBx1tiK7pMCw9zdSiIoabLPGlRpxSY1DdVpEfj4CAIIdX%2FsP8HELp2Y6%2BcWUiZtnt5TG%2BDi8R6wVNV9r6qoxEqm2gQ71%2FY9e8eiB47caT1pbMLWo04sGPxWGvdUjXzk77ILZ%2FeUsQ7RNrLro1kTKIs1496YkpIh3A707lm2e25SQbo1PhMwGxYRYC00R70kxJPvuMTn3Cs8SNRaHmY1XpDGBtyWF8hRwW7Jsss29L0sFkQPnkjHloApNDPJIEFaG7TsuZ7u6UZrLMXNZ90c4daMxzNcOazUYYzBb5UsHozl%2BXYShmK7Ltd63OEQm68rvRvAGkcYv1IEAR88cFJGkaA%2BtmVfLCciltSYY5s4MRORiqGLNXVODf8eZox9UMy8j4SDVyQ8IeKP0QDx60rx43O43OFKivCA%2BbKa9FMwFk%2B4ow9GK05eRGD5irbYJnbndIx5YYMNTZUpKej4IeaZ4E2y9YwH6mAJ3ZTHu22dBsS3fnOJQ3hhuMSInGTfpnqGm%2BFh%2FCQvUypvL9OHrB05MsEQB3lVhTny7QKm0Bva3jH3nbRHFsVWEIaCzMHcO8ldW2m1EPRNmBDAZAU2huETNTvnNzP4as2WNIMWI0LYOMX%2FzzUhhTH6BeN7B%2BETiEuyx%2BfdZIO0PdhRirnrsUUA3pDXHzRR0J0Z3KrDBtdh49pTzw7czYXo3BTCX2hk%2FYqCTeRjyO%2B9xxA32YhA%2FyUYXQ91QqKBcWvEsMdd2%2BlZWzQe%2FQPJCa%2BSEM%2Bh%2BfhCakGVW650VyO%2BFuGA4WaPDl9%2Fy4h%2FVUMcQwdw8dkokWaDROmN1a%2FaedizKgcTSmkr1WxaVIZDonIi7SoUevORqKAhiYaMRllJmwSrqJPN8weg%2F%2Fu3JHiPJi1EB9w6D2Ns%2BtSQcHwchH8yTvxpRpME0%3D'

		},
		'3': {
			'url':'http://www.5dimes.eu/LoginViewComments.asp',
			'headers': {
			    'Accept-Encoding': 'gzip, deflate, sdch',
			    'Accept-Language': 'en-US,en;q=0.8',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			    'Referer': 'http://www.5dimes.eu/LoginVerify.Asp',
			    'Connection': 'keep-alive',
			    'Cache-Control': 'max-age=0'
			},
			'cookies': {
			    'ASPSESSIONIDQSQRCADC': 'CLOFMIBANEAJKNCJLOCACEBM',
			    'ASPSESSIONIDAQRSDDAB': 'GMOJMIBANDNKJKBHMKNOCNOL',
			    'ASPSESSIONIDQSBQCADD': 'DLMMMIBAIJJPPFILCLNHCKLE',
			    '78935480-VID': '1219202351480350',
			    '78935480-SKEY': '6755025048354475359',
			    'HumanClickSiteContainerID_78935480': 'STANDALONE',
			    '5DCustomer': 'ic35946'
			},

		},
		'4': {
			'url': 'http://www.5dimes.eu/WagerMenu.asp',
			'cookies': {
		    'ASPSESSIONIDQSQRCADC': 'CLOFMIBANEAJKNCJLOCACEBM',
		    'ASPSESSIONIDAQRSDDAB': 'GMOJMIBANDNKJKBHMKNOCNOL',
		    'ASPSESSIONIDQSBQCADD': 'DLMMMIBAIJJPPFILCLNHCKLE',
		    '78935480-VID': '1219202351480350',
		    '78935480-SKEY': '6755025048354475359',
		    'HumanClickSiteContainerID_78935480': 'STANDALONE',
		    '5DCustomer': 'ic35946'
			},

			'headers': {
			    'Origin': 'http://www.5dimes.eu',
			    'Accept-Encoding': 'gzip, deflate',
			    'Accept-Language': 'en-US,en;q=0.8',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
			    'Content-Type': 'application/x-www-form-urlencoded',
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			    'Cache-Control': 'max-age=0',
			    'Referer': 'http://www.5dimes.eu/LoginViewComments.asp',
			    'Connection': 'keep-alive'
			},
			'data': 'gotFlash=Y'

		},
		'5': {
			'url': 'http://www.5dimes.eu/bbSportSelection.asp',
			'headers': {
				'Accept-Encoding': 'gzip, deflate, sdch',
			    'Accept-Language': 'en-US,en;q=0.8',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			    'Referer': 'http://www.5dimes.eu/LoginViewComments.asp',
			    'Connection': 'keep-alive',
			    'Cache-Control': 'max-age=0'
    			},
    		'cookies': {
    			'ASPSESSIONIDQSQRCADC': 'CLOFMIBANEAJKNCJLOCACEBM',
			    'ASPSESSIONIDAQRSDDAB': 'GMOJMIBANDNKJKBHMKNOCNOL',
			    'ASPSESSIONIDQSBQCADD': 'DLMMMIBAIJJPPFILCLNHCKLE',
			    '78935480-VID': '1219202351480350',
			    '78935480-SKEY': '6755025048354475359',
			    'HumanClickSiteContainerID_78935480': 'STANDALONE',
			    '5DCustomer': 'ic35946'
			    }
			},
		'6': {
			'url': 'http://www.5dimes.eu/BbGameSelection.asp',
			'headers': {
				'Accept-Encoding': 'gzip, deflate, sdch',
			    'Accept-Language': 'en-US,en;q=0.8',
			    'Upgrade-Insecure-Requests': '1',
			    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
			    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			    'Referer': 'http://www.5dimes.eu/LoginViewComments.asp',
			    'Connection': 'keep-alive',
			    'Cache-Control': 'max-age=0'
			    },
			'cookies': {
				'ASPSESSIONIDQSQRCADC': 'CLOFMIBANEAJKNCJLOCACEBM',
			    'ASPSESSIONIDAQRSDDAB': 'GMOJMIBANDNKJKBHMKNOCNOL',
			    'ASPSESSIONIDQSBQCADD': 'DLMMMIBAIJJPPFILCLNHCKLE',
			    '78935480-VID': '1219202351480350',
			    '78935480-SKEY': '6755025048354475359',
			    'HumanClickSiteContainerID_78935480': 'STANDALONE',
			    '5DCustomer': 'ic35946'
			    },
			'data':'inetWagerNumber=0.28686135991562794&inetSportSelection=sport&Soccer_China=on&Soccer_England=on&Soccer_European+Cup=on&Soccer_France=on&Soccer_Germany=on&Soccer_International=on&Soccer_India=on&Soccer_Mexico=on&Soccer_Poland=on&Soccer_Romania=on&Soccer_Scotland=on&Soccer_Slovakia=on&Soccer_South+America=on&Soccer_Women+Intl=on&Soccer_Halftime=on&Soccer_Futures=on'

			}
		}




	s.post(request_mapper['1']['url'], headers=request_mapper['1']['headers'], cookies=request_mapper['1']['cookies'], data=request_mapper['1']['data']).text
	s.post(request_mapper['2']['url'], headers=request_mapper['2']['headers'], cookies=request_mapper['2']['cookies'], data=request_mapper['2']['data']).text
	s.get(request_mapper['3']['url'], headers=request_mapper['3']['headers'], cookies=request_mapper['3']['cookies']).text
	s.post(request_mapper['4']['url'], headers=request_mapper['4']['headers'], cookies=request_mapper['4']['cookies'], data=request_mapper['4']['data']).text
	s.get(request_mapper['5']['url'], headers=request_mapper['5']['headers'], cookies=request_mapper['5']['cookies']).text
	print s.post(request_mapper['6']['url'], headers=request_mapper['6']['headers'], cookies=request_mapper['6']['cookies'], data=request_mapper['6']['data']).text




authenticate()
