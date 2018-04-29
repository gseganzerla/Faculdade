#!/usr/bin/python3

import MySQLdb
import os


class Mysqli:

    def __init__(self):
        if os.path.exists("dados.txt"):
            pass

        else:
            self.data()

        arq = open("dados.txt", "r")

        var1 = arq.readline()
        var2 = arq.readline()
        var3 = arq.readline()
        var4 = arq.readline()

        var1 = self.restring(var1)
        var2 = self.restring(var2)
        var3 = self.restring(var3)
        var4 = self.restring(var4)

        self.Con = MySQLdb.connect(host=var1, user=var2, passwd=var3, db=var4)
        self.Con.select_db(var4)

    def data(self):

        try:
            open("dados.txt")

        except FileNotFoundError:

            arq = open("dados.txt", "w")

            host = input("Digite o host ")
            user = input("Digite o usuario ")
            passwd = input("Digite a senha ")
            db = input("Digite o bd ")

            arq.write("{}\n".format(host))
            arq.write("{}\n".format(user))
            arq.write("{}\n".format(passwd))
            arq.write("{}\n".format(db))

            arq.close()

    def restring(self, b):
        b = b.replace("\n", "")
        return b

    def query(self, q):
        cursor = self.Con.cursor()
        cursor.execute(q)
        self.Con.commit()
        print(q)
