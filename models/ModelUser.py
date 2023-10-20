from .entities.User import User

class ModelUser():
    @classmethod
    def login(self,db,user):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id, email, password, nombreCompleto FROM usuarios 
                    WHERE email = '{}'""".format(user.email)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password),row[3])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)
    
    @classmethod
    def get_by_id(self,db,id):
        try:
            cursor=db.connection.cursor()
            sql="""SELECT id,email,nombreCompleto,rubro FROM usuarios WHERE id = '{}'""".format(id)
            cursor.execute(sql)
            row=cursor.fetchone()
            if row != None:
               return User(row[0],row[1],None,row[2],row[3]) 
            else:
                return None
        except Exception as ex:
            raise Exception(ex)