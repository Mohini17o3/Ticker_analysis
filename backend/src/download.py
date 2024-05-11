import os
from sec_edgar_downloader import Downloader

filings_directory = os.path.join(os.path.dirname(__file__) , 'filings')

dl= Downloader("SEC Filings", "upretimohini@gmail.com" ,filings_directory)

dl.get("10-K" , "MSFT" ,after="1993-01-01", before="2023-01-01")
dl.get("10-K" , "AAPL" ,after="1993-01-01", before="2023-01-01")