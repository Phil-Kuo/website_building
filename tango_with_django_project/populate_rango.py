import os
os.environ.setdefault('DJANGO_SETTING_MODULE','tango_with_django_project.settings')

import django
django.setup()

from rango.models import  Category, Page

def populate():
    python_cat = add_cat('Python')
    
    add_page(cat = python_cat,
    title = "Official Python Tutorial",
    url = "http://docs.python,org/2/tutorial/")
    
    django_cat = add_cat("Django")
    
    add_page = (cat = django_cat,
    title = "Official Django Tutorial",
    url = "https://docs,djangoproject.com/en/1.5/intro/tutorial01")
    
    frame_cat = add_cat("Other Frameworks")
    
    for c in Category.objects.all():
        for p in Page.objects.all():
            print "-{0}-{1}".format(str(c),str(p))
            
def add_page(cat, title, url, views = 0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p
    
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c
    
if __name__ == '__main__':
    print "Starting Rango population scripts..."
    populate()
    
    
    
