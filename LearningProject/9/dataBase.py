from run_clock import run_clock
import pymysql
import random
import time

MYSQL_CONF = {
    "host": "127.0.0.1",
    "port":3306,
    "user": "root",
    "password": "123456",
    "db": "world"
}


mysql_con=pymysql.connect(**MYSQL_CONF)

mysql_cursor=mysql_con.cursor()#"select * from actor"

@run_clock
def insert_one():
    for i in range(10**3):
        timeStamp = time.strftime("%Y-%m-%d %H-%M-%S")
        lastName=format(random.uniform(1,100) , ".2f")
        SQL = f"""INSERT INTO person (name, age, birthday) 
            VALUES ('People_{random.randint(1,1000)}', '{lastName}', '{timeStamp}');"""
        mysql_cursor.execute(SQL)
        #显式执行commit
        mysql_con.commit()

@run_clock
def insert_many():
    values = []
    for i in range(10 ** 6):
        timeStamp = time.strftime("%Y-%m-%d %H-%M-%S")
        lastName = format(random.uniform(1, 100), ".2f")
        values.append(("person" + str(random.randint(1, 1000)), lastName, timeStamp))

    SQL = f"""INSERT INTO person (name, age, birthday) 
               VALUES (%s,%s,%s);"""
    mysql_cursor.executemany(SQL, values)
    # 显式执行commit
    mysql_con.commit()

@run_clock
def select():
    SQL="""select * from person"""
    result=mysql_cursor.execute(SQL)
    result_set=mysql_cursor.fetchall()

    for i in result_set[0:100]:
        print(f"{i}")
    print(type(result_set))

def transaction():
    try:
        SQL="delete from person where id=2"
        SQL_2 = "delete from person where id="
        mysql_cursor.execute(SQL)
        mysql_cursor.execute(SQL_2)
    except Exception as e:
        print(e)
        mysql_con.rollback()
    finally:
        mysql_con.commit()



if __name__=="__main__":
    #insert_one()
    #insert_many()
    #select()
    transaction()