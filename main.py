# Using the pymssql driver
import pymssql

# Connect to your database.
# Replace server pos, userpos, and password with your credentials
# Code is dependent on AdventureWorks database
conn = pymssql.connect(server='healthsight.database.windows.net', user='username@healthsight.database.windows.net',
                       password='yourpassword', database='HealthSight')
cursor = conn.cursor()

cursor.execute("""
IF OBJECT_ID('azuretest8', 'U') IS NOT NULL
    DROP TABLE azuretest8
CREATE TABLE azuretest8 (
    id INT NOT NULL,
	pos1 VARCHAR(100),
	pos2 VARCHAR(100),
	pos3 VARCHAR(100),
	pos4 VARCHAR(100),
	pos5 VARCHAR(100),
	pos6 VARCHAR(100),
	pos7 VARCHAR(100),
	pos8 VARCHAR(100),
	pos9 VARCHAR(100),
	pos10 VARCHAR(100),
	pos11 VARCHAR(100),
	pos12 VARCHAR(100),
	pos13 VARCHAR(100),
	pos14 VARCHAR(100),
	pos15 VARCHAR(100),
    pos16 VARCHAR(100),
	pos17 VARCHAR(100),
	pos18 VARCHAR(100),
	pos19 VARCHAR(100),
	pos20 VARCHAR(100),
	pos21 VARCHAR(100),
	pos22 VARCHAR(100),
	pos23 VARCHAR(100),
	pos24 VARCHAR(100),
	pos25 VARCHAR(100),
	pos26 VARCHAR(100),
	pos27 VARCHAR(100),
	pos28 VARCHAR(100),
	pos29 VARCHAR(100),
	pos30 VARCHAR(100),
	pos31 VARCHAR(100),
	pos32 VARCHAR(100),
    pos33 VARCHAR(100),
	pos34 VARCHAR(100),
	pos35 VARCHAR(100),
	pos36 VARCHAR(100),
	pos37 VARCHAR(100),
	pos38 VARCHAR(100),
	pos39 VARCHAR(100),
	pos40 VARCHAR(100),
	pos41 VARCHAR(100),
	pos42 VARCHAR(100),
	pos43 VARCHAR(100),
	pos44 VARCHAR(100),
	pos45 VARCHAR(100),
	pos46 VARCHAR(100),
	pos47 VARCHAR(100),
	pos48 VARCHAR(100),
	pos49 VARCHAR(100),
    pos50 VARCHAR(100),
	pos51 VARCHAR(100),
	pos52 VARCHAR(100),
	pos53 VARCHAR(100),
	pos54 VARCHAR(100),
    PRIMARY KEY(id)
)
""")

inpfile = open('data.txt', 'r')

while 1:
    line = inpfile.readline()
    if line == '':
        break
    num, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25, pos26, pos27, pos28, pos29, pos30, pos31, pos32, pos33, pos34, pos35, pos36, pos37, pos38, pos39, pos40, pos41, pos42, pos43, pos44, pos45, pos46, pos47, pos48, pos49, pos50, pos51, pos52, pos53, pos54= line.split()
    stmt = (
        """insert into azuretest8(id, pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, pos10, pos11, pos12, pos13, pos14, pos15, pos16, pos17, pos18, pos19, pos20, pos21, pos22, pos23, pos24, pos25, pos26, pos27, pos28, pos29, pos30, pos31, pos32, pos33, pos34, pos35, pos36, pos37, pos38, pos39, pos40, pos41, pos42, pos43, pos44, pos45, pos46, pos47, pos48, pos49, pos50, pos51, pos52, pos53, pos54) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""" % (
            num, "'" + str(pos1) + "'", "'" + str(pos2) + "'", "'" + str(pos3) + "'", "'" + str(pos4) + "'",
            "'" + str(pos5) + "'", "'" + str(pos6) + "'", "'" + str(pos7) + "'", "'" + str(pos8) + "'",
            "'" + str(pos9) + "'",
            "'" + str(pos10) + "'", "'" + str(pos11) + "'", "'" + str(pos12) + "'", "'" + str(pos13) + "'",
            "'" + str(pos14) + "'", "'" + str(pos15) + "'", "'" + str(pos16) + "'", "'" + str(pos17) + "'",
            "'" + str(pos18) + "'", "'" + str(pos19) + "'", "'" + str(pos20) + "'", "'" + str(pos21) + "'",
            "'" + str(pos22) + "'", "'" + str(pos23) + "'", "'" + str(pos24) + "'", "'" + str(pos25) + "'",
            "'" + str(pos26) + "'", "'" + str(pos27) + "'", "'" + str(pos28) + "'", "'" + str(pos29) + "'",
            "'" + str(pos30) + "'", "'" + str(pos31) + "'", "'" + str(pos32) + "'", "'" + str(pos33) + "'",
            "'" + str(pos34) + "'", "'" + str(pos35) + "'", "'" + str(pos36) + "'", "'" + str(pos37) + "'",
            "'" + str(pos38) + "'", "'" + str(pos39) + "'", "'" + str(pos40) + "'", "'" + str(pos41) + "'",
            "'" + str(pos42) + "'", "'" + str(pos43) + "'", "'" + str(pos44) + "'", "'" + str(pos45) + "'",
            "'" + str(pos46) + "'", "'" + str(pos47) + "'", "'" + str(pos48) + "'", "'" + str(pos49) + "'",
            "'" + str(pos50) + "'", "'" + str(pos51) + "'", "'" + str(pos52) + "'", "'" + str(pos53) + "'",
            "'" + str(pos54) + "'"))

    cursor.execute(stmt)

conn.commit()
conn.close()
