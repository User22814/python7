import psycopg2

# CRUD

# # CREATE TABLE
# ############################################################################

# conn = psycopg2.connect("dbname=db_new_hw35 user=postgres password=qwerty228")
# cur = conn.cursor()
#
# query_string = """
# CREATE TABLE public.books
# (
#     id integer,
#     title text,
#     author text,
#     price real,
#     page_counts integer,
#     PRIMARY KEY (id)
# );
#
# ALTER TABLE IF EXISTS public.books
#     OWNER to postgres;
# """
# cur.execute(query_string)
# conn.commit()
# conn.close()

# # CREATE (INSERT)
# ############################################################################
# conn = psycopg2.connect("dbname=db_new_hw35 user=postgres password=qwerty228")
# cur = conn.cursor()
#
#
# new_arr = []
#
# for i in range(1, 10 + 1):
#     tmp_arr = [0, 0, 0, 0, 0]
#     tmp_arr[0] = i
#     tmp_arr[1] = f'Book {i}'
#     tmp_arr[2] = f'Author {i}'
#     tmp_arr[3] = i * 1000
#     tmp_arr[4] = i * 100
#     new_arr.append(tmp_arr)
#
# # create data
# index = 12
# for i in new_arr:
#     query_string = f"""
#     INSERT INTO public.books (id, title, author, price, page_counts)
#     VALUES ({i[0]}, '{i[1]}', '{i[2]}', {i[3]}, {i[4]})
#     """
#
#     cur.execute(query_string)
#     conn.commit()  # применение данных после изменений
#
# conn.close()


# READ (SELECT)
############################################################################
# conn = psycopg2.connect("dbname=db_new_hw35 user=postgres password=qwerty228")
# # localhost (127.0.0.1 / 192.168.1.121)
#
# # Open a cursor to perform database operations
# cur = conn.cursor()
#
# # Execute a query
#
# # read data
# cur.execute("""
# SELECT * FROM public.books
# ORDER BY id ASC
# """)
#
# # Retrieve query results
# records = cur.fetchall()
#
# for i in records:
#     print(i)
#
# conn.close()


# # DELETE (DELETE)
# ############################################################################
# conn = psycopg2.connect("dbname=db_new_hw35 user=postgres password=qwerty228")
# cur = conn.cursor()
#
# query_string = """
#     DELETE FROM public.books
#     WHERE id >= 5 and page_counts <= 800;
#     """
#
# #
#
# cur.execute(query_string)
# conn.commit()
# conn.close()

# UPDATE (UPDATE)
############################################################################

conn = psycopg2.connect("dbname=db_new_hw35 user=postgres password=qwerty228")
cur = conn.cursor()

query_string = """
UPDATE public.books
SET price = 1234
WHERE id = 10;
"""

#

cur.execute(query_string)
conn.commit()
conn.close()
