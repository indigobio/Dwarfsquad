import csv


def read_csv(csv_path):

    rows = []
    with open(csv_path, 'rU') as f:
        dialect = csv.Sniffer().sniff(f.read(16000))
        f.seek(0)
        reader = csv.DictReader(f, dialect=dialect)
        for line in reader:
            rows.append(line)
    return rows