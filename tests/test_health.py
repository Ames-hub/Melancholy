import sqlite3

# imports health, mingenhealth and maxhealth from the DB
con = sqlite3.connect('game.db')
cur = con.cursor()
cur.execute("SELECT health FROM stats")
health = cur.fetchone()[0]
cur.execute("SELECT mingenhealth FROM stats")
mingenhealth = cur.fetchone()[0]
cur.execute("SELECT maxhealth FROM stats")
maxhealth = cur.fetchone()[0]

def test_health():
    # Tests if health is less than or equal to min health
    assert health < mingenhealth or health == mingenhealth, "Health is less than minimum health"
    # Tests if health is less than or equal to max health
    assert health < maxhealth or health == maxhealth, "Health is greater than maximum health"