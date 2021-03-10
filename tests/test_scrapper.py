# Tests of the scrapper
from scrapper import rezept
import pytest

cases= [
'https://www.chefkoch.de/rezepte/223571092410598/Texas-Jailhouse-Chili.html?portionen=18',
'https://www.chefkoch.de/amp/rezepte/1821961295691963/Rindergulasch.html',
'https://www.chefkoch.de/rezepte/492841143637894/Deftige-Erbsensuppe-mit-Kassler.html'
]

def test_rezept1():
    rez = rezept(cases[0])
    assert rez.url == cases[0]
    assert rez.info['name'] == 'Texas Jailhouse Chili'
    assert rez.info['image'] == 'https://img.chefkoch-cdn.de/rezepte/223571092410598/bilder/503708/crop-960x540/texas-jailhouse-chili.jpg'
    assert rez.info['recipeYield'] == '18 Portionen'
    assert rez.info['recipeIngredient'] == ['2.250 g Rindfleisch , 2 cm Würfel', '750 g Schweinehackfleisch', '750 g Chorizo , in Scheiben', '6 Zwiebel(n) , grob gehackt', '4 ½ Zehe/n Knoblauch , grob gehackt', '9 Chilischote(n) , mehr oder weniger, je nach Sorte', '375 g Tomatenmark', '750 g Tomate(n) , Dose, gewürfelt', '4 ½ TL Kreuzkümmel , gemahlen', '1 ½ TL Estragon , gemahlen', '1 ½ EL Zucker', '1 ½ EL Salz', '1 ½ EL Pfeffer , schwarz, gemahlen', '3 EL Oregano , gerebelt', '4 ½ EL Gewürzmischung (Chili Würzer)', '4 ½ EL Petersilie , gehackt', '1 ½ EL Worcestershiresauce', '1 ½ EL Essig', '225 g Zartbitterschokolade', '4 ½ Dose/n Bier', '6 Dose/n Bohnen , rot oder Pinto', '300 g Räucherspeck']
    assert rez.info['totalTime'] == 'P0DT1H0M'
    assert rez.info['description'] == 'Texas Jailhouse Chili - echtes Chili, ohne Bohnen. Über 675 Bewertungen und für vorzüglich befunden. Mit ► Portionsrechner ► Kochbuch ► Video-Tipps!'
    assert rez.info['recipeInstructions'] == 'Rindfleisch in Schmalz scharf anbraten, aus dem Topf nehmen und zur Seite stellen. Gehacktes vom Schwein und die Zwiebeln im selben Topf anbräunen. Worcestersauce, Knoblauch & Petersilie dazu rühren, mit Bier ablöschen. Alle Zutaten, außer den Bohnen, dazumischen und das Chili ca. 2 Std. köcheln lassen, wenn notwendig, Wasser nachfüllen.\n\nDie Bohnen separat mit gewürfeltem Speck zubereiten und auch separat dazu reichen. \n\nDies ist ein “echtes Chili”, man kocht die Bohnen nicht im selben Topf, sondern man mischt sich genug Bohnen in das Chili, um die Schärfe nach Bedarf zu mildern.\n\nVorsicht: getrocknete Chilischoten sind sofort scharf, während frische Chilis ein wenig länger brauchen um Wirkung zu zeigen. Habaneros sind die schärfsten Chilis die es gibt, dann Serranos, Jalapenos und Anaheim - in dieser Ordnung.\n\nEs schmeckt besser einen Tag vorher gemacht und dann aufgewärmt.\n\nDazu reicht man traditionell dicken Knoblauchtoast.'
    assert rez.info['nutrition'] == {'@type': 'NutritionInformation', 'calories': '716 kcal', 'servingSize': '1'}
    assert rez.info['keywords'] == ['Fleisch', 'Hauptspeise', 'Rind', 'USA oder Kanada', 'Party', 'Schwein', 'Schmoren', 'Eintopf', 'Gluten', 'Lactose', 'Low Carb']
    assert rez.info['recipeCategory'] == 'Eintopf'

# TODO: Testen was passiert, wenn das image ein png oder anderes ist.