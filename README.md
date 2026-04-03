#### CONSEGNA:

E-commerce Clustering Pipeline Development
struttura un piano di azione per svolgere al meglio questa consegna e potermi guidare passo passo per il suo svolgimento:
Dettagli
Contesto

Lavorerai su un dataset di eventi e-commerce in cui ogni riga rappresenta un’azione utente su un prodotto a un certo timestamp. Le colonne includono identificativi di utente, prodotto e categoria, prezzo e tipo di azione (view, add_to_cart, purchase).
Il progetto richiede di progettare e implementare un sistema che costruisca cluster di utenti e prodotti a partire da questi eventi e che sia in grado di stimare l’assegnazione futura ai cluster su orizzonti temporali definiti.

 

Obiettivo del progetto

L’obiettivo principale è costruire una pipeline completa e corretta dal punto di vista metodologico per il clustering di utenti e prodotti, partendo da dati temporali. Il focus è sulla struttura del sistema, sulla riproducibilità e sulla correttezza degli split temporali.
In secondo piano, ma obbligatorio, dovrai implementare un modello supervisionato che predica l’appartenenza futura ai cluster, rispettando rigorosamente il vincolo temporale.

 

Attività richieste

Dovrai progettare una pipeline end-to-end che includa ingestione dei dati, pulizia, costruzione delle feature, training del clustering e assegnazione dei cluster. La pipeline deve essere modulare e facilmente rieseguibile cambiando la data di riferimento o i parametri principali.


La costruzione delle feature è parte integrante del lavoro. Dovrai implementare aggregazioni temporali corrette, assicurandoti che ogni feature utilizzi solo informazioni disponibili fino al tempo di riferimento. Le scelte di finestra temporale e di aggregazione devono essere esplicite.

Per gli utenti dovrai partire dall'analisi RFM ma arricchirlo con indicatori che descrivano propensione alla conversione, varietà di esplorazione, sensibilità al prezzo e differenze tra comportamento recente e storico. Le feature devono raccontare una storia sul comportamento, non limitarsi a contare eventi.


Per il clustering dovrai implementare almeno due approcci, confrontandoli tra di loro mettendo in risalto i punti positivi e negativi di entrambi e identificando quello più adatto allo scenario. L’attenzione è sulla coerenza dei risultati e sulla stabilità operativa, non sull’uso di tecniche complesse fine a sé stesse.


La previsione dell’appartenenza futura ai cluster deve essere trattata come un problema supervisionato. Dovrai definire chiaramente come viene costruita la label futura, implementare split temporali corretti e valutare il modello su periodi realmente futuri. È fondamentale dimostrare che non esiste leakage informativo.


La valutazione del modello di previsione deve includere metriche standard di classificazione multiclasse e una discussione sugli errori più rilevanti dal punto di vista applicativo, ad esempio errori che coinvolgono cluster ad alto valore.

 

Deliverable

Dovrai consegnare un repository o progetto strutturato che contenga codice riutilizzabile per l’intera pipeline, insieme a un notebook in formato .ipynb con all'interno la documentazione con la descrizione dei vari passaggi effettuati ed i commenti alle informazioni principali estratte durante l'analisi. Il codice deve poter essere rieseguito per rigenerare feature, cluster e modelli senza interventi manuali.

 

Criteri di valutazione

La valutazione premierà la correttezza metodologica, la gestione del tempo e degli split, la chiarezza della pipeline e la qualità del codice. Errori concettuali legati all’uso di informazioni future o a una definizione ambigua delle label avranno un impatto significativo sulla valutazione finale.


#### PLAN:
2️⃣ Analisi Esplorativa dei Dati (EDA)
Profilazione completa e controlli di coerenza
Creare un notebook notebooks/01_eda.ipynb che carichi i dati tramite il nuovo loader.
Usare pandas_profiling o sweetviz per report rapidi.
Salvare le statistiche riassuntive come JSON in outputs/eda/.
⏱️ 3 h
3️⃣ Feature Engineering
Variabili temporali, aggregazioni e codifica
Finestre temporali: Definire una funzione build_features(events_df, reference_date, window='30d') che calcoli per utente/prodotto: conteggi, recency, frequency, monetary (RFM).
Join di categorie: Unire attributi di prodotto/categoria.
Codifica: One-hot per variabili categoriali, scaling per quelle numeriche.
Salvare le tabelle generate in data/processed/.
⏱️ 5 h
4️⃣ Clustering
Due algoritmi + valutazione
Algoritmo A: K-Means (con n_init=20, random_state=42).
Algoritmo B: Clustering Gerarchico Agglomerativo oppure DBSCAN (per catturare forme irregolari).
Usare come metriche: Silhouette, Calinski-Harabasz e stabilità nel tempo.
Salvare le assegnazioni dei cluster in data/processed/users_clusters.parquet.
⏱️ 4 h
5️⃣ Predizione Supervisata
Predire il cluster futuro
Definire la label: cluster dell’utente alla reference_date + orizzonte temporale (es. 30 giorni dopo).
Suddividere i dati temporalmente (train su date ≤ cutoff, validazione su date successive).
Provare modelli baseline: Regressione Logistica, Gradient Boosting (xgboost/lightgbm).
Valutare con macro-F1, matrice di confusione e analisi dell’impatto sul business.