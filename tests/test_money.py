# CMD USED TO GEN MONEY IN starter.py
# money = random.randint(2, 20)

import sqlite3
# imports money, minmoney and maxgenmoney from the DB
con = sqlite3.connect('game.db')
cur = con.cursor()
cur.execute("SELECT money FROM stats")
money = cur.fetchone()[0]
cur.execute("SELECT minmoney FROM stats")
minmoney = cur.fetchone()[0]
cur.execute("SELECT maxgenmoney FROM stats")
maxgenmoney = cur.fetchone()[0]

def test_money():
    # Tests if money is less than or equal to min money
    assert money > minmoney or money == minmoney, "Money is less than minimum money"
    # Tests if money is more than or equal to max money
    assert money > maxgenmoney or money == maxgenmoney, "Money is greater than maximum money"