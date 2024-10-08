# Generated by Django 5.1.1 on 2024-10-08 21:22

from django.db import migrations


def create_groups(apps, schema_migration):
    # retrieve models
    User = apps.get_model('authentication', 'User')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    # retrieve permissions
    add_photo = Permission.objects.get(codename='add_photo')
    change_photo = Permission.objects.get(codename='change_photo')
    delete_photo = Permission.objects.get(codename='delete_photo')
    view_photo = Permission.objects.get(codename='view_photo')

    # define creators permissions
    creator_permissions = [
        add_photo,
        change_photo,
        delete_photo,
        view_photo,
    ]

    # create creators group
    creators = Group(name='creators')
    creators.save()

    # add creators permissions to creators group
    creators.permissions.set(creator_permissions)

    # create subscriber group
    subscribers = Group(name='subscribers')
    subscribers.save()

    # add only view_photo to subscribers group
    subscribers.permissions.add(view_photo)

    # update user permissions accordingly to they role

    for user in User.objects.all():
        if user.role == 'CREATOR':
            creators.user_set.add(user)
        elif user.role == 'SUBSCRIBER':
            subscribers.user_set.add(user)
        else:
            pass


class Migration(migrations.Migration):
    dependencies = [
        ('authentication', '0003_alter_user_profile_photo'),
    ]

    operations = [
        migrations.RunPython(create_groups),
    ]