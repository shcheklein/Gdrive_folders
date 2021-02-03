from .models import Test
from django_q.models import Schedule


def create_test():

    Test.objects.create()


# Schedule.objects.create(
#     func=create_test(),
#     schedule_type=Schedule.MINUTES,
#     minutes=1,
# )
