import requests
from bs4 import BeautifulSoup
class InquiryNatureCauseWealth:
    def __init__(self):
        self.title = "An Inquiry into the Nature and Causes of the Wealth of Nations"
        self.author = "Adam Smith"
        self.year = 1776
    def get_text(self, url = "https://www.gutenberg.org/files/3300/3300-h/3300-h.htm"):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text
    

class PrinciplePoliticalEconomyTaxation:
    def __init__(self):
        self.title = "On The Principles of Political Economy, and Taxation"
        self.author = "David Ricardo"
        self.year = 1817
    def get_text(self, url = "https://www.gutenberg.org/files/33310/33310-h/33310-h.htm"):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text
    
class ConditionWorkingClassEngland:
    def __init__(self):
        self.title = "The Condition of the Working-Class in England in 1844"
        self.author = "Frederick Engels"
        self.year = 1845
    def get_text(self, url = "https://www.gutenberg.org/files/17306/17306-h/17306-h.htm"):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text
    
class GeneralTheroyEmployment:
    def __init__(self):
        self.title = "The General Theory of Employment, Interest, and Money"
        self.author = "John Maynard Keynes"
        self.year = 1845
    def get_text(self, url = "http://gutenberg.net.au/ebooks03/0300071h/printall.html"):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text
    
class PrinciplesOfEconomics:
    def __init__(self):
        self.title = "Principles of Economics"
        self.author = "Alfred Marshall"
        self.year = 1890
    def get_text(self, url = """
    https://oll.libertyfund.org/titles/marshall-principles-of-economics-8th-ed
    """):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text
    
    
class CritiquePoliticalEconomy:
    def __init__(self):
        self.title = "Capital: A Critique of Political Economy. Volume I: The Process of Capitalist Production"
        self.author = "Karl Marx"
        self.year = 1867
    def get_text(self, url = "https://oll.libertyfund.org/titles/marx-capital-a-critique-of-political-economy-volume-i-the-process-of-capitalist-production"):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text
    
    
class HumanAction:
    def __init__(self):
        self.title = "Human Action: A Treatise on Economics, vol. 1 (LF ed.)"
        self.author = "Ludwig von Mises"
        self.year = 1996
    def get_text(self, url = "https://oll.libertyfund.org/titles/mises-human-action-a-treatise-on-economics-vol-1-lf-ed"):
        get_url = requests.get(url).text
        soup = BeautifulSoup(get_url, "html.parser")
        raw_text = [paragraph.text for paragraph in soup.find_all("p")]
        return raw_text