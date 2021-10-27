'''
Created on 2021. 7. 26.

@author: pc368

'''
from homebook import homebookSqliteCRUD
if __name__ == '__main__':
    # #테이블 만들기
    homebookSqliteCRUD.createTable()
    # # 자료 하나 입력
    # homebookSqliteCRUD.insertData('1','20210727','수입','기타수입','훈장',3000000,0)
