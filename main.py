from scrapper import rezept


if __name__ == '__main__':
    scrapper1 = rezept('https://www.chefkoch.de/rezepte/1728511281966781/Semmelknoedel-aus-der-Form.html')
    scrapper2 = rezept('https://www.chefkoch.de/rezepte/223571092410598/Texas-Jailhouse-Chili.html?portionen=18')
    scrapper3 = rezept('https://www.chefkoch.de/amp/rezepte/1821961295691963/Rindergulasch.html')
    scrapper4 = rezept('https://www.chefkoch.de/rezepte/492841143637894/Deftige-Erbsensuppe-mit-Kassler.html')
    
    #pdfl = PDFLaTeX.from_texfile('tests/try1.tex')
    #pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True)
    test=1