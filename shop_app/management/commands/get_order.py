from django.core.management.base import BaseCommand
from shop_app.models import Order


class Command(BaseCommand):
    """
    Выбор одного заказа по ID
    """

    help = "Get single order"

    def add_arguments(self, parser):
        """
        Аргумент поиска
        """
        parser.add_argument("pk", type=int, help="Order ID")

    def handle(self, *args, **kwargs):

        pk = kwargs["pk"]
        order = Order.objects.filter(pk=pk).first()
        if order:
            self.stdout.write(f"{order}")
        else:
            self.stdout.write("Not found")
