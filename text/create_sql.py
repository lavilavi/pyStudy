import random, string

pre = 'insert into make (make_id, make_code, make_name, is_active, is_deleted, creator, create_datetime, updater, ' \
      'update_datetime) values ("'
mid = '","TOYOTA-'
post = '","TOYOTA",1,0,"test user","2020-10-10 ' \
       '10:10:10","test user","2020-10-10 10:10:10");'
ids = []
output = 'make_sql'


def get_unique_id():
    id = ''.join(random.choice(string.ascii_lowercase) for x in range(8))
    while id in ids:
        id = ''.join(random.choice(string.ascii_lowercase) for x in range(8))
    ids.append(id)
    return id


def create_update_sql(table, set_column, set_value, where_column, where_value):
    print(
        'update ' + table + ' set ' + set_column + ' = \'' + set_value + '\' where ' + where_column + ' = \'' + where_value + '\';')


def create_sqls():
    from_values = [line.rstrip() for line in open('vehicle_id_prod_values')]
    to_values = [line.rstrip() for line in open('vehicle_id_stg_values')]

    for i in range(0, len(from_values)):
        create_update_sql('vehicle_image', 'vehicle_id', from_values[i], 'vehicle_id', to_values[i])


create_sqls()
