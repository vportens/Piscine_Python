import datetime
import time

'# Aeconde depuis 1970:'
dateInSecond = time.time()

currentDate = datetime.datetime.now().date()
'# special format pour avoir les virgules et 4 chiffres decimales '
formatted_time = "{:,.4f}".format(dateInSecond)

print(f"Seconds since January 1, 1970: {formatted_time}"
      "or {dateInSecond:.2e} in scientific notation")
print(currentDate.strftime('%b %d %Y$'))
