import pymysql
from util.DB import DB


class dbConnect:
    def createUser(uid, name, email, password, user_icon, user_bio):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password, user_icon, user_bio) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(sql, (uid, name, email, password, user_icon, user_bio))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user
        except Exception as e:
            print(f'エラーが発生しています:{e}')
        finally:
            cur.close()


    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f'エラーが発生しています:{e}')
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
        except Exception as e:
            print(f'エラーが発生しています:{e}')
        finally:
            cur.close()
            return channel


    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id,u.uid, user_name, message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def createMessage(id, uid, cid, message, created_at):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(id, uid, cid, message, created_at) VALUES(%s, %s, %s, %s)"
            cur.execute(sql, (id, uid, cid, message, created_at))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def PostImage(image, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO images(image_data, message_id) VALUES(%s, %s)"
            cur.execute(sql, (image, message))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close() 


    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    # プロフィール編集機能のために追加
    def createProfile(name, icon, bio, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (user_name, user_icon, user_bio, uid) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (name, icon, bio, uid))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def getProfile(uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT user_name, user_icon, user_bio FROM users WHERE uid=%s;"
            cur.execute(sql, (uid))
            profile = cur.fetchone()
            return profile
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()


    def updateProfile(newUserName, newUserIcon, newUserBio, uid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE users SET user_name=%s, user_icon=%s, user_bio=%s WHERE uid=%s;"
            cur.execute(sql, (newUserName, newUserIcon, newUserBio, uid))
            conn.commit()
        except Exception as e:
            print(f'エラーが発生しています：{e}')
        finally:
            cur.close()
