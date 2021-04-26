import requests
from bs4 import BeautifulSoup
import requests

TOKEN_NAME = "PROJECT_NAME"
URL_LIST = ["https://bscscan.com/search?f=0&q=" + TOKEN_NAME + "%20Token",
            "https://bscscan.com/search?f=0&q=" + TOKEN_NAME,
            "https://bscscan.com/search?f=0&q=Binance-Peg%20" + TOKEN_NAME + "%20Token",
            "https://bscscan.com/search?f=0&q=Binance-Peg%20" + TOKEN_NAME,
            "https://bscscan.com/search?f=0&q=" + TOKEN_NAME + "%20Token"
           ]

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

contract = []
def CheckAddress():
    
    for url in URL_LIST:
        page = requests.get(url,headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        main_div = soup.find("div",class_="d-flex clipboard-hover")

        try:
            address = main_div.find_all("a", class_="text-truncate d-block mr-2")
            contract.extend(address)
        
            contract_string = ' '.join(map(str, contract))
            x = contract_string.split(">")
            y = x[1].split("<")
            
            link = "https://bscscan.com/token/" + y[0]
            
            chatIds = ["CHAT_IDS"]
            api = f'https://api.telegram.org/botTOKEN/sendMessage'
            
            for id in chatIds:
                data = {'chat_id': id, 'text': y[0]}
                requests.post(api, data).json()
                data = {'chat_id': id, 'text': link}
                requests.post(api, data).json()
                
        except:
            continue
        
CheckAddress()
