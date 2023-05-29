import datetime

global day_name
day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

# TODO: write a `function` out of this.
# sample code:
def get_weekname(date: str) -> str:
    day = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return day_name[day]

# TODO: is it ok that we are using a global variable inside the local scope of this funcion?