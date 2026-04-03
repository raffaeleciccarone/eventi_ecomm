import pandas as pd
import os
import logging

class FileExtractor:
    '''
    Classe per l'estrazione e il caricamento di file CSV da una cartella

    esempio di utilizzo:
    path = r'your_dir/with_csvfiles'
    file = FileExtractor(path)
    dfs = file.csv_to_df()

    # utilizzare metodi dei dizionari per accedere 
    # a chiavi(nomi df) e valori(i df)
    dfs.keys()

    ## nota bene:
    # se hai data wrangler installato nell'IDE
    # puoi tranquillamente usarlo così
    # per avere il df direttamente nella cella
    # del notebook
    -> dfs['categories']
    ''' 
    def __init__(self, path):
        self.path = path

    def extraction(self):
        '''
        Metodo che guarda nella cartella di riferimento e procede con l'estrazione dei dati
        funziona solo con csv al momento
        ''' 
        files_csv = [f for f in os.listdir(self.path) if f.endswith('.csv')]
        nomi_file = [f.replace('.csv', '') for f in files_csv]

        logging.info('Ecco la lista dei vari file:'.center(20))

        for f in nomi_file:
            logging.info(f.center(5))

        return files_csv

    def csv_to_df(self):
        '''
        Legge tutti i CSV nella cartella e ritorna un dizionario {nome_file: dataframe}
        '''
        estrazione = self.extraction()
        dfs = {}

        for file in estrazione:
            full_path = os.path.join(self.path, file)
            df = pd.read_csv(full_path)
            dfs[file.replace('.csv','')] = df

        return dfs
