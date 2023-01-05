# CODE USED TO GEN STAMINA
# stamina = random.randint(50, 500)

import sqlite3

con = sqlite3.connect('game.db')
cur = con.cursor()

# Imports stamina, maxstamina and min stamina from the DB
cur.execute("SELECT stamina FROM stats")
stamina = cur.fetchone()[0]
cur.execute("SELECT maxstamina FROM stats")
maxstamina = cur.fetchone()[0]
cur.execute("SELECT minstamina FROM stats")
minstamina = cur.fetchone()[0]

def test_stamina(stamina):
    # Returns True IF stamina is below maxstamina
    assert stamina < maxstamina or stamina == maxstamina, "Stamina is greater than maximum stamina"
    # Returns True IF stamina is above minstamina
    assert stamina < minstamina or stamina == minstamina, "Stamina is less than minimum stamina"