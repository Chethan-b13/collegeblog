import random
import os
import django
django.setup()

from blog.models import Posts,Category
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone
# from collegeblog import settings




def create_post(N):
    fake = Faker()

    for _ in range(N):
        auth_id = random.randint(1,4)
        cat_id = random.randint(1,4)
        title = fake.name()
        status = random.choice(['Published','Draft'])
        desc = fake.text()
        # category = Category.objects.get(id=cat_id)
        Posts.objects.create(title=title+"'s post!!" , 
        desc = desc , category=Category.objects.get(id=cat_id),
        author= User.objects.get(id=auth_id),
        status = status,
        slug = "-".join(title.lower().split()),
        uploaded_date = timezone.now(),
        updated_date = timezone.now()
        )


if __name__ == '__main__':
    print ("Starting club population script...")
    # settings.configure()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE' ,'collegeblog.settings')
    create_post(10)       