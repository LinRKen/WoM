import MySQLdb


# db = MySQLdb.connect(host='localhost', user='LinRKen', password='Ken1922346338', database='test01', port=3306)

# cursor = db.cursor()

class WORDS:
    def __init__(
        self,
        host='localhost',
        user='LinRKen',
        password='Ken1922346338',
        database='test01',
        port=3306,
        table_name='words',
        ) -> None:
        super().__init__()
        self.db = MySQLdb.connect(host=host, user=user, password=password, database=database, port=port)
        self.cursor = self.db.cursor()
        self.table_name = table_name
        
    ## 创建表
    def create_table(self, table_name):
        sql = """CREATE TABLE %s (
            word  CHAR(20),
            meaning CHAR(20),
            profix  CHAR(20),
            etyma CHAR(20),
            postfix CHAR(20))""" % (table_name)
        self.cursor.execute(sql)
    # words = """CREATE TABLE words (
    #          word  CHAR(20),
    #          meaning CHAR(20),
    #          profix  CHAR(20),
    #          etyma CHAR(20),
    #          postfix CHAR(20),)"""
    # cursor.execute(words)

    # 插入单词
    def insert_word(self, values):
        word, meaning, profix, etyma, postfix = values
        sql = """INSERT INTO %s (word, meaning, profix, etyma, postfix) VALUES ('%s', '%s', '%s', '%s', '%s')""" % (self.table_name, word, meaning, profix, etyma, postfix)
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()


    # 查询单词
    def select_word(self ,word):
        sql = """SELECT * FROM %s WHERE word = '%s'""" % (self.table_name, word)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        for row in results:
            word = row[0]
            meaning = row[1]
            profix = row[2]
            etyma = row[3]
            postfix = row[4]
            print("word=%s,meaning=%s,profix=%s,etyma=%s,postfix=%s" % (word, meaning, profix, etyma, postfix))
        return results
        
    # 更新单词
    def update_word(self, values):
        word, meaning, profix, etyma, postfix = values
        sql = """UPDATE %s SET meaning = '%s', profix = '%s', etyma = '%s', postfix = '%s' WHERE word = '%s'""" % (self.table_name, meaning, profix, etyma, postfix, word)
        self.cursor.execute(sql)
        self.db.commit()
    
    # 打印表
    def get_values(self):
        sql = """SELECT * FROM words"""
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        # for row in results:
        #     word = row[0]
        #     meaning = row[1]
        #     profix = row[2]
        #     etyma = row[3]
        #     postfix = row[4]
        return results
            
    # 打印列名
    def get_columns(self):
        sql = """SHOW COLUMNS FROM words"""
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        columns = []
        for row in results:
            columns.append(row[0])
        return columns

# ws = WORDS()
# # ws.insert_word(('223', '223', '2', '2', '3'))
# # ws.update_word(('123', '123', '1', '2', '3'))
# ws.insert_word(('hello', '你好', '你', '好', 'd'))
# print(list(ws.get_values()))
        