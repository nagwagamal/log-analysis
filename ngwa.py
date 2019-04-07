#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 03:49:17 2018
@author: Nagwa
"""
import psycopg2
na = psycopg2.connect("dbname=news")
gc = na.cursor()


def n1():
    print('******************')
    gc.execute("""SELECT a.title, count(*) as cunt
           FROM articles a
           JOIN log b
           ON b.path = concat('/article/', a.slug)
           GROUP BY title ORDER BY cunt DESC LIMIT 3;""")
    rs = gc.fetchall()
    for (title, view) in rs:
        print("{} - {}views".format(title, view))
    print('******************')


def n2():
    gc.execute('''
        SELECT ag.name, COUNT(*) as cuntnum
        FROM authors as ag
        join articles as gn
        on  ag.id = gn.author
        join log
        ON log.path = concat('/article/', gn.slug)
        GROUP BY ag.name
        ORDER BY cuntnum DESC;''')
    rs = gc.fetchall()
    for (name, view) in rs:
        print("{} - {} views".format(name, view))
    print('******************')


def n3():
    gc.execute('''
        SELECT eview.date, round(100.0*eview.eview / tv.tv,2)
        as errors from tv , eview
        where eview.date=tv.date
        and (eview.eview)>(tv.tv*0.01);''')
    rs = gc.fetchall()
    for (date, percentage) in rs:
        print("{} - {}% eview".format(date, percentage))
    print('******************')
if __name__ == "__main__":
    n1()
    n2()
    n3()
