import mysql.connector

class Articulos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost",
                                              user="root", 
                                              passwd="S3tg4rc_7", 
                                              database="amuht")
        return conexion
    
    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="INSERT INTO `obras_publicas` (`id`, `name`, `lastname`, `birthdate`, `path`) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        
    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor = cone.cursor(buffered=True)
        sql="SELECT `name`, `lastname`, `birthdate`, `path` FROM `obras_publicas` WHERE `id`=%s"
        cursor.execute(sql,datos)
        cursor.close()
        respuesta = cursor.fetchone()
        return respuesta
            
    def recuperar_todos(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor = cone.cursor(buffered=True)
        sql="SELECT `id`, `lastname`, `birthdate`, `path` FROM `obras_publicas` WHERE `name`=%s"
        cursor.execute(sql,datos)
        cone.close()
        respuesta = cursor.fetchall()
        return respuesta
