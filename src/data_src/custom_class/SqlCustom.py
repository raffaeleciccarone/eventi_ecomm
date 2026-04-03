import logging

class SqlCustom:
    def __init__(self, engine):
        self.engine = engine

    def crea_tabelle(self, dic_dfs):
        '''
        Metodo che prende in input un dizionario di dataframe
        e crea le tabelle nel database. Occhio perchè pandas si appoggia
        a sqlalchemy per la creazione delle tabelle.
        Usa l' engine di sqlalchemy da passare alla classe SqlCustom.
        '''
        with self.engine.begin() as conn:
            for nome_df, df in dic_dfs.items():
                df.to_sql(
                    name = nome_df,
                    con = self.engine,
                    if_exists = 'replace',
                    index = False
                )
                logging.info(f'Tabella {nome_df} creata con successo.')