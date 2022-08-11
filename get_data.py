from datetime import datetime, time
import pytz

from dateutil.tz import tzlocal, tzutc

from app.models.user import User
from dateutil import tz

user = User.query.filter_by(id=5).first()

print(user.timestamp)
from_zone = tz.tzutc()
to_zone = tz.tzlocal()
utc = user.timestamp.replace(tzinfo=from_zone)
print("utc")
print(utc)
print("local")
central = utc.astimezone(tzlocal())
print(central)

########### error ###########
print('########### error ###########')
utc = datetime.now().replace(tzinfo=from_zone)
print("utc")
print(utc)
print("local")
central = utc.astimezone(tzlocal())
print(central)
