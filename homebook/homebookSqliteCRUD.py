'''
Created on 2021. 7. 26.
가계부 CRUD
@author: pc368
'''
import sqlite3
from astropy.table import row
def createTable():
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS HOMEBOOK
        (NO INTEGER PRIMARY KEY AUTOINCREMENT,
        DAY TEXT,
        SECTION TEXT,
        ACCOUNTTITLE TEXT,
        REMARK TEXT,
        REVENUE INTEGER,
        EXPENSE INTEGER)
    ''')
    conn.commit()
    c.close()
    conn.close()
    pass

def insertData(day,section,accounttitle,remark,revenue,expense):
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO HOMEBOOK(DAY,SECTION,ACCOUNTTITLE,REMARK,REVENUE,EXPENSE)
        VALUES(?,?,?,?,?,?)
    ''',(day,section,accounttitle,remark,revenue,expense) )
    conn.commit()
    c.close()
    conn.close()
    pass

def selectAll():
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    c.execute('SELECT * FROM HOMEBOOK') 
    rows = c.fetchall()
    conn.commit()
    c.close()
    conn.close()
    pass
    return rows

def select(key):
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    c.execute('SELECT * FROM HOMEBOOK WHERE DAY = ?',(key,)) #매개변수 key가 들어와서 물음표를 채워준다, 유의!!! 튜플형태에 맞춰주기
    row = c.fetchone()
    conn.commit()
    c.close()
    conn.close()
    return row
    pass

def update(vo):
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    c.execute('''
        UPDATE HOMEBOOK SET DAY=?, SECTION=?, ACCOUNTTITLE=?, REMARK=?, REVENUE=?, EXPENSE=? WHERE NO=?
    ''',vo)
    
    conn.commit()
    c.close()
    conn.close()
    pass

def delete(key):
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    res = c.execute('''DELETE FROM HOMEBOOK WHERE NO = ?''',(key,))

    conn.commit()
    c.close()
    conn.close()
    return len(list(res)) #삭제된 것이 있다면 리스트에 만들어진 개수만큼 리턴시킴
    pass

def selectDate(key1,key2):
    conn = sqlite3.connect("homebook.db")
    c = conn.cursor()
    c.execute('SELECT * FROM HOMEBOOK WHERE DAY BETWEEN ? AND ?',(key1,key2))
    row = c.fetchall()
    conn.close()
    return row
    pass