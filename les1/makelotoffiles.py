import mysql.connector

woord = input("Waar wil je op zoeken? ")

verbinding = mysql.connector.connect(host="ensembldb.ensembl.org",
                                     user="anonymous",
                                     db="homo_sapiens_core_95_38")

cursor = verbinding.cursor()
cursor.execute("select * from gene where description like '%{}%' ".format(woord))
regel = ""
aantal = 0
while regel != None:
    regel = cursor.fetchone()
    try:
        bestand = open (regel[12],"w")
        bestand.write(regel[9])
        bestand.close()
        aantal +=1
        print (aantal)
    except:
        print("Foutje")
cursor.close()
verbinding.close()
