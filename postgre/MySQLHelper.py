import pymysql
from logging import *
import aiomysql

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
basicConfig(level=DEBUG, format=LOG_FORMAT)


class AsyncMySQLHelper:
    def __init__(self):
        self.cursor = None
        self.db = None

    async def init(self, host='localhost', port=3306, user='root', password='Python.init(520)', db=None, autocommit=True):
        try:
            self.db = await aiomysql.connect(host=host, port=port, user=user, password=password, db=db, autocommit=autocommit)
            self.cursor = await self.db.cursor()
            info('Connect Successful')
        except Exception as e:
            error(e)

    async def createDB(self, db):
        try:
            sql = 'CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8_general_ci'.format(db)
            await self.cursor.execute(sql)
            info('Create Successful')
        except Exception as e:
            error(e)

    async def insert(self, table, data):
        if isinstance(data, dict):
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
            update = ','.join([" {key} = %s".format(key=key) for key in data])
            sql += update
            try:
                await self.cursor.execute(sql, tuple(data.values()) * 2)
                info('Insert Or Update Successful')
            except Exception as e:
                error(e)
        elif isinstance(data, list):
            count = 0
            dataLen = len(data)
            for d in data:
                keys = ', '.join(d.keys())
                values = ', '.join(['%s'] * len(d))
                sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
                update = ','.join([" {key} = %s".format(key=key) for key in d])
                sql += update
                try:
                    await self.cursor.execute(sql, tuple(d.values()) * 2)
                    count += 1
                    info('Insert Or Update Successful {}/{}'.format(count, dataLen))
                except Exception as e:
                    error(e)
        else:
            warning('单条数据用字典包装，多条数据用数组表示')

    async def delete(self, table, condition):
        sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
        try:
            await self.cursor.execute(sql)
            info('Delete Successful')
        except Exception as e:
            error(e)

    # 只执行查询不返回，可通过cursor获取结果
    async def find(self, sql):
        try:
            await self.cursor.execute(sql)
            info('Find Successful')
        except Exception as e:
            error(e)

    async def find_one(self, sql):
        try:
            await self.cursor.execute(sql)
            info('FindOne Successful')
            return await self.cursor.fetchone()
        except Exception as e:
            error(e)

    async def find_many(self, sql, size):
        try:
            await self.cursor.execute(sql)
            info('FindMany Successful')
            return await self.cursor.fetchmany(size)
        except Exception as e:
            error(e)

    async def find_all(self, sql):
        try:
            await self.cursor.execute(sql)
            info('FindAll Successful')
            return await self.cursor.fetchall()
        except Exception as e:
            error(e)

    async def execute(self, sql):
        try:
            await self.cursor.execute(sql)
            info('Execute Successful')
        except Exception as e:
            error(e)

    async def close(self):
        await self.cursor.close()
        self.db.close()


class MySQLHelper:
    def __init__(self, host='localhost', port=3306, user='root', password='Python.init(520)', db=None):
        try:
            self.db = pymysql.connect(host=host, user=user, password=password, port=port, db=db)
            self.cursor = self.db.cursor()
            info('Connect Successful')
        except Exception as e:
            error(e)

    def createDB(self, db):
        try:
            sql = 'CREATE DATABASE IF NOT EXISTS {} DEFAULT CHARACTER SET utf8mb4 COLLATE utf8_general_ci'.format(db)
            self.cursor.execute(sql)
            info('Create Successful')
        except Exception as e:
            error(e)

    def insert(self, table, data):
        if isinstance(data, dict):
            keys = ', '.join(data.keys())
            values = ', '.join(['%s'] * len(data))
            sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
            update = ','.join([" {key} = %s".format(key=key) for key in data])
            sql += update
            try:
                self.cursor.execute(sql, tuple(data.values()) * 2)
                info('Insert Or Update Successful')
                self.db.commit()
            except Exception as e:
                error(e)
                self.db.rollback()
        elif isinstance(data, list):
            count = 0
            dataLen = len(data)
            for d in data:
                keys = ', '.join(d.keys())
                values = ', '.join(['%s'] * len(d))
                sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys, values=values)
                update = ','.join([" {key} = %s".format(key=key) for key in d])
                sql += update
                try:
                    self.cursor.execute(sql, tuple(d.values()) * 2)
                    count+=1
                    info('Insert Or Update Successful {}/{}'.format(count, dataLen))
                    self.db.commit()
                except Exception as e:
                    error(e)
                    error('Insert Or Update Error {}/{}'.format(count, dataLen))
                    self.db.rollback()
        else:
            warning('单条数据用字典包装，多条数据用数组表示')

    def delete(self, table, condition):
        sql = 'DELETE FROM {table} WHERE {condition}'.format(table=table, condition=condition)
        try:
            self.cursor.execute(sql)
            info('Delete Successful')
            self.db.commit()
        except Exception as e:
            error(e)
            self.db.rollback()

    # 只执行查询不返回，可通过cursor获取结果
    def find(self, sql):
        try:
            self.cursor.execute(sql)
            info('Find Successful')
        except Exception as e:
            error(e)

    def find_one(self, sql):
        try:
            self.cursor.execute(sql)
            info('FindOne Successful')
            return self.cursor.fetchone()
        except Exception as e:
            error(e)

    def find_many(self, sql, size):
        try:
            self.cursor.execute(sql)
            info('FindMany Successful')
            return self.cursor.fetchmany(size)
        except Exception as e:
            error(e)

    def find_all(self, sql):
        try:
            self.cursor.execute(sql)
            info('FindAll Successful')
            return self.cursor.fetchall()
        except Exception as e:
            error(e)

    def execute(self, sql):
        try:
            self.cursor.execute(sql)
            info('Execute Successful')
            self.db.commit()
        except Exception as e:
            error(e)
            self.db.rollback()

    def close(self):
        self.cursor.close()
        self.db.close()
        info('Connect Close')


if __name__ == '__main__':
    mySQLHelper = MySQLHelper(db='qigushi')
    print(mySQLHelper.find_one('select * from story'))
    #mySQLHelper.insert('story', {'name':'1', 'nameKeyWords':'1', 'content':'1', 'contentKeyWords':'2', 'tips':'', 'tipsKeyWords':''})
    mySQLHelper.close()