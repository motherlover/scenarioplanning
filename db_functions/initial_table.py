# Insert initial rows into devel_for_branche table
import sqlite3

conn = sqlite3.connect('../development.sqlite3')
branche_list = [['akkerbouw', 'kalverhouderij', 'melkveehouderij', 'pluimveehouderij', 'sierteelt', 'varkenshouderij', 'visserij', 'voedingstuinbouw'], ['architectenbureaus', 'grond--weg-waterbouw', 'groothandel-hout-bouwmaterialen', 'hout-bouwmaterialenindustrie', 'ingenieursbureaus', 'installatiebedrijven', 'utiliteitsbouw', 'woningbouw'], ['agf-industrie', 'brood-deegwarenindustrie', 'drankenindustrie', 'groothandel-in-voedingsmiddelen', 'visindustrie', 'vleesindustrie', 'zuivelindustrie'], ['basismetaalindustrie', 'chemische-industrie', 'elektro-en-technische-apparatenindustrie', 'machine-industrie', 'metaalproductenindustrie', 'meubelindustrie', 'rubber-kunststofproductenindustrie', 'transportmiddelenindustrie'], ['attractieparken-dierentuinen', 'campings-vakantieparken', 'foodservice', 'hotels', 'kunst-cultuur', 'restaurants', 'travel'], ['toeleveranciers-aan-de-olie-gasindustrie'], ['autoretail', 'bouwmarkten', 'drogisterijen', 'groothandel-non-food', 'kledingwinkels', 'supermarkten', 'winkels-in-consumentenelektronica', 'woonwinkels'], ['drukkerijen', 'ict-hardware', 'it-software-services', 'reclamebureaus', 'telecom', 'televisie-omroepen', 'uitgeverijen'], ['binnenvaart', 'expediteurs', 'goederenvervoer-over-spoor', 'goederenwegvervoer', 'opslag', 'short-sea-shipping'], ['wind-solar'], ['accountantskantoren', 'advocatenkantoren', 'beveiligingsbedrijven', 'gerechtsdeurwaardersincassobureaus', 'notariskantoren', 'schoonmaakbedrijven', 'uitzendbureaus']]

cur = conn.cursor()

query_read = '''SELECT rowid FROM development_table;'''
query_write = '''INSERT INTO devel_for_branche(branche,devel_id) VALUES(?,?);'''

cur.execute(query_read)
row_ids = cur.fetchall()
# for branches in branche_list:	
# 	for branche in branches:		
# 		[cur.execute(query_write,(branche,str(row_id_iter[0]))) for row_id_iter in row_ids]


[[[cur.execute(query_write,(branche,row_id_iter[0])) for row_id_iter in row_ids] for branche in branches] for branches in branche_list]

conn.commit()

conn.close()
