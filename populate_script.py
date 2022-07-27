def create_post(N):
    fake = Faker()

    for _ in range(N):
        cat_id = random.randint(1, 3)
        title = fake.name()
        status = random.choice(['Published', 'Draft'])
        desc = fake.text()
        Posts.objects.create(title=title+"'s post!!",
                             desc=desc, category=Category.objects.get(
                                 id=cat_id),
                             author=UserInfo.objects.get(
                                 user=User.objects.order_by('?').first()),
                             status=status,
                             slug="-".join(title.lower().split()),
                             uploaded_date=timezone.now(),
                             updated_date=timezone.now()
                             )


if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "collegeblog.settings")
    import django
    django.setup()

    import random
    from django.core.management import call_command
    from blog.models import Posts, Category, UserInfo
    from django.utils import timezone
    from django.contrib.auth.models import User
    from faker import Faker
    create_post(10)
