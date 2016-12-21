from django.core.management.base import BaseCommand, CommandError
from webapp.models import Customer


class Command(BaseCommand):
    help = 'Save customer data into db'

    def handle(self, *args, **options):
        data = []
        for line in open("webapp/management/commands/customerdata.txt"):
            content = line.rstrip('\n').split(',')
            data.append(content)
        try:
            for i in range(1, len(data)):
                date = data[i][0]
                phone = data[i][1]
                name = data[i][2]
                price = data[i][3]
                cus_obj = Customer.objects.create(name=name, Amount=float(price), phone=phone, date=date)
                cus_obj.save()
            self.stdout.write(self.style.SUCCESS('Successfully saved to database'))
        except:
            self.stdout.write(self.style.SUCCESS('There is some issue with data'))
