from django_seed import Seed

from pinterest.users.models import RoleAdmin

# Seeder
seeder = Seed.seeder()
seeder.add_entity(RoleAdmin, 1, {'name': 'admin'})

inserted_pks = seeder.execute()
