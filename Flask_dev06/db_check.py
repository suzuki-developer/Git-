from app import db, Trip

# テーブルの一覧を取得する
tables = db.engine.table_names()

# テーブルの一覧を表示する
print(tables)


