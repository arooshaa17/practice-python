BASE_URL = 'https://www.flaconi.de/'

# Home page
SELECT_MARKEN = '#main-navigation [title="Marken"]'
SELECT_PARFUM = '#main-navigation [href="/parfum/"]'
SELECT_PFLEGE = '#main-navigation [href="/pflege/"]'
SELECT_MAKEUP = '#main-navigation [href="/make-up/"]'
SELECT_HAARE = '#main-navigation [href="/haarpflege/"]'
SELECT_ACCESSORIES = '#main-navigation [href="/accessoires/"]'
SELECT_PREMIUM = '#main-navigation [href="/premium/"]'
SELECT_NEW = '#main-navigation [href="/neuheiten/"]'
SELECT_SALE = '#main-navigation [href="/sale/"]'
SELECT_GRATIS = '#main-navigation [href="/gratis-zugaben/"]'
PAGE_SELECTORS_LIST = [SELECT_MARKEN, SELECT_PARFUM, SELECT_PFLEGE, SELECT_MAKEUP, SELECT_HAARE, SELECT_ACCESSORIES, SELECT_PREMIUM, SELECT_NEW, SELECT_SALE, SELECT_GRATIS]

# Page Titles
HOME_PAGE_TITLE = 'Online Parfümerie: Parfum & Kosmetik bestellen | FLACONI'
MARKEN_PAGE_TITLE = 'Markenparfum und Pflege online bestellen | Flaconi'
PARFUM_PAGE_TITLE = 'Parfum online kaufen bei FLACONI'
PFLEGE_PAGE_TITLE = 'Pflege-Produkte online bestellen | Hautpflege | FLACONI'
MAKEUP_PAGE_TITLE = 'Make-up online kaufen | Aktuelle Make-up Trends bei FLACONI'
HAARE_PAGE_TITLE = 'Haarpflege günstig bestellen | Styling & Pflege | FLACONI'
ACCESSORIES_PAGE_TITLE = 'Accessoires online bestellen | FLACONI'
PREMIUM_PAGE_TITLE = 'Premium Marken & Produkte online bestellen | FLACONI'
NEU_PAGE_TITLE = 'Neuheiten online bestellen | Flaconi'
SALE_PAGE_TITLE = 'Sale% - Make-up, Parfum & Kosmetik günstig kaufen bei FLACONI'
GRATIS_PAGE_TITLE = 'Exklusive Gratis-Zugaben sichern | FLACONI'
EXPECTED_PAGE_TITLE_LIST = [MARKEN_PAGE_TITLE, PARFUM_PAGE_TITLE, PFLEGE_PAGE_TITLE, MAKEUP_PAGE_TITLE, HAARE_PAGE_TITLE, ACCESSORIES_PAGE_TITLE, PREMIUM_PAGE_TITLE, NEU_PAGE_TITLE, SALE_PAGE_TITLE, GRATIS_PAGE_TITLE]

# Perfumes
SELECT_PARFUM_ITEM = '[href = "/parfum/yves-saint-laurent/libre/yves-saint-laurent-libre-eau-de-parfum.html"]'
SELECT_PARFUM_ITEM2 = '[href="/parfum/acqua-di-parma/signature-of-the-sun/acqua-di-parma-signature-of-the-sun-sandalo-eau-de-parfum.html"]'

# Cart
ADD_TO_CART = 'button[title="In den Warenkorb"]'
MOVE_TO_CART = '[href="https://www.flaconi.de/warenkorb/"]'
EXPECTED_ITEM_VALUE = "https://www.flaconi.de/parfum/yves-saint-laurent/libre/yves-saint-laurent-libre-eau-de-parfum.html"
EXPECTED_ITEM_VALUE2 = "https://www.flaconi.de/parfum/acqua-di-parma/signature-of-the-sun/acqua-di-parma-signature-of-the-sun-sandalo-eau-de-parfum.html"
