import requests
import json
import re
import os
import urllib.request
from pdflatex import PDFLaTeX

from enum import Enum

class RequiredAttributes(Enum):
    name = 1
    image = 2
    recipeYield = 3
    recipeIngredient = 4
    totalTime = 5
    description = 6
    recipeInstructions = 7
    nutrition = 8
    keywords = 9
    recipeCategory = 10


def slugify(value):
    """
    Shamelessly stolen from Stackoverflow
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    value = re.sub('[-\s]+', '-', value)
    return value

def unicode_normalization_bullshit(s):
    re_normalize = re.compile('([^a-zA-Z0-9\.,-_!?\'\"öäüÖÄÜß&\s\n@\\\\])')
    return re_normalize.sub('', s)

class NotAllAttributesPresentException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class rezept:
    def __init__(self, url):
        self.url = url 
        self.info = {}
        self.__scrap()
        self.create_pdf()
    
    def __scrap(self):
        self.html = self.__get_html()
        re_array = re.compile(
            '<script type="application\/ld\+json">\s*\{.*?\}.*?<\/script>',
            flags=re.S
            )
        found = re_array.findall(self.html)

        info = {}
        re_useless = re.compile('<\/?script.*?>')
        re_whitespaces = re.compile('\s\s+')
        for hit in found:
            useful = re.sub(re_whitespaces, ' ', re.sub(re_useless, '', hit))
            maybe_info = json.loads(useful)
            if "@type" in maybe_info and maybe_info["@type"] == "Recipe":  
                info = maybe_info
        
        if not info:
            raise Exception("No Dictionary found")
        
        for attribute in RequiredAttributes:
            if not attribute.name in info:
                raise NotAllAttributesPresentException(
                    "Key in Dict missing: {attribute.name}"
                    )

        self.info = info

    def __get_html(self):
        page = requests.get(self.url)
        return page.text
    
    def create_pdf(self):
        self._prepare_attributes()
        with open('template.tex') as f:
            tex = f.read()
        
        try:
            urllib.request.urlretrieve(self.info['image'], "image.jpg")
        except Exception as e:
            re_image = re.compile('\\includegraphics.*\n')
            tex = re_image.sub('', tex)
        
        for att in RequiredAttributes:
            tex = tex.replace('%'+att.name+'%', self.info[att.name])
        
        filename = slugify(self.info['name']) + ".tex"
        with open(filename, 'w') as f:
            f.write(tex)
        
        pdfl = PDFLaTeX.from_texfile('./'+filename)
        pdfl.pdf_filename = slugify(self.info['name'])
        pdfl.dir = os.path.dirname(os.path.realpath(__file__))
        pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)
        
        os.remove(filename)
        try:
            os.remove('image.jpg')
        except:
            pass

 
    def _prepare_attributes(self):
        re_time = re.compile('P\d*DT')
        time = re_time.sub('', self.info['totalTime'])
        self.info['totalTime'] = time.replace('H', 'h ').replace('M', 'm')

        self.info['nutrition'] = self.info['nutrition'].get(
            'calories', '???'
            )
        ingredients = ["\item " + i for i in self.info['recipeIngredient']]
        self.info['recipeIngredient'] = "\n".join(ingredients)
        self.info['keywords'] = ', '.join(self.info['keywords'])
        self.info['description'] = unicode_normalization_bullshit(self.info['description'])
        for attr in RequiredAttributes:
            self.info[attr.name] = unicode_normalization_bullshit(self.info[attr.name])
