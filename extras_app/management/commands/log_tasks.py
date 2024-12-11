from datetime import datetime

from django.core.management.base import BaseCommand
from orm_app.models import Task


class Command(BaseCommand):
    help = "Print all tasks"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.NOTICE(f'Komenda rozpoczęta: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        )

        tasks = Task.objects.all()
        for task in tasks:
            print(task.name)


        self.stdout.write(
            self.style.SUCCESS(f'Komenda zakończona: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        )

# python manage.py log_tasks