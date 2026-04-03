import logging
from sqlalchemy import text

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
            
            # Aggiunta dei vincoli di integrità dopo aver creato tutte le tabelle
            logging.info("Aggiunta dei vincoli di integrità (PK, FK)...")
            vincoli_queries = [
                "ALTER TABLE categories ADD PRIMARY KEY (category_id);",
                "ALTER TABLE users ADD PRIMARY KEY (user_id);",
                "ALTER TABLE products ADD PRIMARY KEY (product_id);",
                "ALTER TABLE promotions_daily ADD PRIMARY KEY (date);",

                "ALTER TABLE products ADD CONSTRAINT fk_products_category FOREIGN KEY (category_id) REFERENCES categories (category_id) ON DELETE CASCADE;",
                "ALTER TABLE events ADD CONSTRAINT fk_events_user FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE;",
                "ALTER TABLE events ADD CONSTRAINT fk_events_product FOREIGN KEY (product_id) REFERENCES products (product_id) ON DELETE CASCADE;",
                "ALTER TABLE events ADD CONSTRAINT fk_events_category FOREIGN KEY (category_id) REFERENCES categories (category_id) ON DELETE CASCADE;",

                "ALTER TABLE events ALTER COLUMN timestamp SET NOT NULL;",
                "ALTER TABLE events ALTER COLUMN action SET NOT NULL;",
                "ALTER TABLE products ALTER COLUMN base_price SET NOT NULL;"
            ]
            
            for query in vincoli_queries:
                try:
                    conn.execute(text(query))
                    logging.info(f"Eseguito con successo: {query}")
                except Exception as e:
                    logging.error(f"Errore durante l'esecuzione di '{query}': {e}")