import random

it_was_raining = bool(round(random.random()))
forgot_canoe = bool(round(random.random()))
lost_money = bool(round(random.random()))
lost_drinks = bool(round(random.random()))

festival_failed = (it_was_raining and forgot_canoe) or (lost_drinks and lost_money)
you_liked_festival = not festival_failed

print(f"Lijo: {it_was_raining} \nNepasiemei baidarkes: {forgot_canoe} \nPametei pinigus: {lost_money} "
      f"\nPametei gerimus: {lost_drinks} \nFestivalis patiko: {you_liked_festival}")