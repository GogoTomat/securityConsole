import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    cards = Passcard.objects.all()
    # print(cards)
    # first = cards[0]
    # print(first.is_active, first.created_at, first.passcode, first.owner_name, sep=' ')
    # activeN = 0
    # for card in cards:
    #     if card.is_active == True:
    #         activeN += 1
    # print("Amount of active pass is ",activeN)
    active_pass = Passcard.objects.filter(is_active=True)
    print(len(active_pass))

