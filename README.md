# 1. Requirements
Python 3.8.2
texlive-core (von Arch-Linux)
internet access

# 2. Setup
1. Install python and texlive
2. 'python3.8 -m venv venv'
3. 'source venv/bin/activate'
4. 'pip install -r requirements.txt'

# 3. Usage
Example:
```
from scrapper import rezept
scrapper1 = rezept('https://www.chefkoch.de/rezepte/1728511281966781/Semmelknoedel-aus-der-Form.html')
# The scrapper1 object holds all info about the created pdf but is essentially
# as the pdf gets created in the init() function of the rezept-object.
```