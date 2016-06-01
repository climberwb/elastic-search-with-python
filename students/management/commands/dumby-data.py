from django.core.management.base import BaseCommand
from model_mommy import mommy
from .models import University, Course, Students
class Command(BaseCommand):
    help = "My shiny new management command."
    def handle(self, *args, **options):
        print 'lala'
        self.make_universities()
    def make_universities(self):
        university_names = (
            'MIT', 'MGU', 'CalTech', 'KPI', 'DPI', 'PSTU'
        )
        self.universities = []
        for name in university_names:
            uni = mommy.make(University, name=name)
            self.universities.append(uni)