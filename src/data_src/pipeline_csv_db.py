from custom_class.FileExtractor import FileExtractor
from custom_class.SqlCustom import SqlCustom
from sqlalchemy import create_engine

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../../.env"))

DB_USER = os.getenv('POSTGRES_USER')
DB_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_HOST = os.getenv('POSTGRES_HOST')
DB_PORT = os.getenv('POSTGRES_PORT')
DB_NAME = os.getenv('POSTGRES_DB')

# Percorso dei dati synthetic_ecom
path = r"/Users/raffaeleciccarone/Desktop/DataMasters/projectwork/prog_2026/eventi_ecomm/data/synthetic_ecom"

def main():
    '''
    Pipeline che gestisce il caricamento dei dati dai file csv al database.
    '''
    file = FileExtractor(path)
    dfs = file.csv_to_df()
    for nome_df, df in dfs.items():
        logging.info(f"{'_'*10}{nome_df}{'_'*10}".center(10))

    logging.info('creazione db in corso...')

    engine = create_engine(
        f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}'
        f'@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    )

    db = SqlCustom(engine)
    db.crea_tabelle(dfs)


if __name__ == "__main__":
    main()