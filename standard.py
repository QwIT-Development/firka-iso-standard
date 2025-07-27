import datetime
from typing import Generator

now = datetime.datetime.now()
year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second

def generate(from_item: int, padding: int = 2) -> Generator[str, None, None]:
	return (character for character in f"{from_item:0{padding}d}")

def construct_generators() -> dict[str, Generator[str, None, None]]:
	return {
		"Y": generate(year, 4),
		"m": generate(month),
		"D": generate(day),
		"H": generate(hour),
		"M": generate(minute),
		"S": generate(second)
	}

def make_time_standard(format: str) -> str:
	output = ""
	generators = construct_generators()
	
	for char in format:
		if char in generators:
			try:
				output += next(generators[char])
			except:
				output += "?"
		else:
			output += char
	return output
			
firka_format = "mY/DY/YmDY HS:MS:HM"
kreta_format = "mD/Ym/DYYY HH:MM:SS"
print("Firka formátum:", make_time_standard(firka_format))
print("Kréta formátum:", make_time_standard(kreta_format))
