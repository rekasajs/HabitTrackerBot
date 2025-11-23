def frequency_changer(frequency):
  if frequency == 'daily':
    return 'Ежедневно'
  else:
    return 'Еженедельно'
  
def is_active_changer(is_active):
  if is_active:
    return '🟢 Активна'
  else:
    return '🔴 Неактивна'