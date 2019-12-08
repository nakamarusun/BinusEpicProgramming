def convert_to_days():
	h = float(input("Hours: "))
	m = float(input("Minutes: "))
	s = float(input("Seconds: "))
	print(round(get_days(h, m, s), 4))

def get_days(hours, minutes, seconds):
	return (hours / 24 + minutes / 1440 + seconds / 86400)

convert_to_days()
