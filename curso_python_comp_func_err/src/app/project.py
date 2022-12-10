import csv, pdb

def main(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = set(next(reader))
        population_dict = {}
        for row in reader:
            iterable = zip(header, row, strict=True)
            country = { column: row2 for column, row2 in iterable if 'Population' in row}
            pdb.set_trace()
            print(country)
if __name__ == "__main__":
    main('./world_population.csv')
