import pandas
from argparse import ArgumentParser
from .db import DatabaseManager

class OrestarDataLoader:

    def __init__(self):
        self.table      = 'orestar_combined'
        self.date_col   = 'Tran Date'
        self.filter_col = 'Filer'

    def read_file(self, filename):
        return pandas.read_excel(filename)

    def load_file(self, filename):
        return self.load_df(self.read_file(filename))

    def load_df(self, df):
        filer = df['Filer'].unique()[0]

        try:
            conn = DatabaseManager().connect()

            cursor = conn.cursor()
            cursor.execute("DELETE FROM {table} WHERE Filer='{filer}'".format(table=self.table, filer=filer))

            conn.commit()
        except:
            print("Error Deleting Existing Data (does it exist?)")

        df.to_sql(self.table, DatabaseManager().create_engine(), if_exists='replace')

if __name__ == "__main__":
    ap = ArgumentParser()

    subparser = ap.add_subparsers(dest='cmd')

    load_file_p = subparser.add_parser('load-file')

    load_file_p.add_argument('filename')

    args = ap.parse_args()

    loader = OrestarDataLoader()

    if args.cmd == 'load-file':
        loader.load_file(args.filename)

    print(loader.read_file('data/KitJohnston.xls').head())

