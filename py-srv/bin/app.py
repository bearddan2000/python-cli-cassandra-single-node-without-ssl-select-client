import pandas as pd
from cassandra.cluster import Cluster

def connect():
    cluster = Cluster(['db'],port=9042)
    return cluster.connect()

def query(session, query):
    return session.execute(query)

def seed_from_file(session):
    from os import listdir
    from os.path import isfile, join

    mypath = 'cql'
    files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    sorted_files = sorted(files)
    for file in sorted_files:
        with open(join(mypath, file), 'r') as f:
            content = f.read()
        query(session, content)

def main():
    session = connect()
    seed_from_file(session)
    rows = query(session, 'SELECT * FROM citizix.dog')
    df = pd.DataFrame(rows, columns=['id','breedId','colorId'])
    print(df)

if __name__ == "__main__":
    main()