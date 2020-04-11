
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' ,'collegeblog.settings')


import django
django.setup()

import random

from blog.models import Posts,Category,UserInfo
from faker import Faker
from django.contrib.auth.models import User
from django.utils import timezone
# from collegeblog import settings


# def UserInfor():
#     u = UserInfo.objects.get_or_create(user=User.objects.get(id=user_id))[0]
#     return u

def create_post(N):
    fake = Faker()

    for _ in range(N):
        user_id = random.randint(1,4)
        cat_id = random.randint(1,3)
        title = fake.name()
        status = random.choice(['Published','Draft'])
        desc = fake.text()
        # category = Category.objects.get(id=cat_id)
        Posts.objects.create(title=title+"'s post!!" , 
        desc = desc , category=Category.objects.get(id=cat_id),
        author= UserInfo.objects.get_or_create(user=User.objects.get(id=user_id))[0],
        status = status,
        slug = "-".join(title.lower().split()),
        uploaded_date = timezone.now(),
        updated_date = timezone.now()
        )



create_post(10)       