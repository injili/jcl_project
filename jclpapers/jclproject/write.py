import inspect
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jclproject.settings")
import django
django.setup()
from datetime import date
from jclapp.models import Product


def write_products():
    paper_gsm_80 = Product(name='80gsm A4 Multipurpose Quality Paper', brand='JCL', size='A4', weight='80gsm', color='White', grade='All-purpose Premium Printing paper', sheets_in_ream=500, thickness='110um', quality='Premium', price=450.00, quantity=100, image='ream2.png')
    paper_gsm_80.save()

    paper_gsm_70 = Product(name='70gsm A4 Multipurpose Quality Paper', brand='JCL', size='A4', weight='70gsm', color='White', grade='All-purpose Premium Printing paper', sheets_in_ream=500, thickness='100um', quality='Premium', price=400.00, quantity=100, image='ream2.png')
    paper_gsm_70.save()

    paper_gsm_65 = Product(name='65gsm A4 Multipurpose Quality Paper', brand='JCL', size='A4', weight='65gsm', color='White', grade='All-purpose Premium Printing paper', sheets_in_ream=500, thickness='95um', quality='Premium', price=350.00, quantity=100, image='ream2.png')
    paper_gsm_65.save()

    print('Products written to database')

def clean_data():
    Product.objects.all().delete()
    print('Products deleted from database')

clean_data()
write_products()