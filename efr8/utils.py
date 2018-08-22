import json

def write_to_file(write_data, file_name):
	prev_data = []
	try:
		with open(file_name, 'r') as f:
			try:
				prev_data = json.load(f)
			except ValueError:
				prev_data = []
	except IOError:
			prev_data = []
	with open(file_name, 'w+') as f:
		data = prev_data + write_data
		json.dump(data, f)


def read_from_file(file_name):
		try:
			with open(file_name, 'r') as f:
				try:
					data = json.load(f)
				except ValueError:
					data = []
		except IOError:
			data = []
		return data
