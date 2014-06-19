import numpy

__author__ = 'sujeet'


class Rate_Table:
	def __init__(self):
		self.rows = []
		self.infinityRate = 0
		self.current = 0

	def add_row(self, start, base):
		self.rows.append({'start': start, 'base': base})
		self._process_rows()

	def add_row_list(self, list, startKey='start', baseKey='base'):
		self.rows.extend([dict(start=k[startKey],base=k[baseKey]) for k in list])
		self._process_rows()

	def set_infinity_rate(self, infinity_rate):
		self.infinityRate = infinity_rate
		self._process_rows()

	def _process_rows(self):
		sorted(self.rows, key=lambda x: x['start'])
		for i in range(0, len(self.rows) - 1):
			self.rows[i]['finish'] = self.rows[i + 1]['start']
			self.rows[i]['rate'] = (self.rows[i + 1]['base'] - self.rows[i]['base']) / ((self.rows[i+1]['start'] - self.rows[i]['start']))
		self.rows[len(self.rows) - 1]['finish'] = 99999999
		self.rows[len(self.rows) - 1]['rate'] = self.infinityRate


def _calculate_lookup_attainment(ach, lookup_table):
	return float(sum(map(
		lambda x: (float(min(x['finish'], ach)) - float(x['start'])) * float(x['rate']) + float(x['base']) if ach > x['start'] and ach < x['finish'] else float(0.0), lookup_table)))


calculate_lookup_attainment = numpy.vectorize(_calculate_lookup_attainment,otypes=[numpy.float])
calculate_lookup_attainment.excluded.add(1)