# Contenido de la demo Hostal La Campana (Toledo) (es/ca/en/fr). Hechos de hostalcampana.com leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitación individual','Habitación doble','Habitación doble confort'],
'ca':['Habitació individual','Habitació doble','Habitació doble confort'],
'en':['Single room','Double room (twin beds)','Comfort double room'],
'fr':['Chambre individuelle','Chambre double (lits jumeaux)','Chambre double confort']}
RD={
'es':['1 persona, cama de 105x180. Baño privado, cafetera, minibar/nevera, TV, climatización, wifi y escritorio.','2 personas, dos camas de 90x180. Baño privado, cafetera, minibar/nevera, TV, climatización, wifi y escritorio.','1 o 2 personas, cama de 150x180 o 180x180. Más espacio, con baño privado, cafetera, minibar/nevera, TV, climatización y wifi.'],
'ca':['1 persona, llit de 105x180. Bany privat, cafetera, minibar/nevera, TV, climatització, wifi i escriptori.','2 persones, dos llits de 90x180. Bany privat, cafetera, minibar/nevera, TV, climatització, wifi i escriptori.','1 o 2 persones, llit de 150x180 o 180x180. Més espai, amb bany privat, cafetera, minibar/nevera, TV, climatització i wifi.'],
'en':['1 guest, 105x180 bed. Private bathroom, coffee machine, minibar/fridge, TV, climate control, wifi and desk.','2 guests, two 90x180 beds. Private bathroom, coffee machine, minibar/fridge, TV, climate control, wifi and desk.','1 or 2 guests, 150x180 or 180x180 bed. More space, with private bathroom, coffee machine, minibar/fridge, TV, climate control and wifi.'],
'fr':['1 personne, lit de 105x180. Salle de bain privée, cafetière, minibar/réfrigérateur, TV, climatisation, wifi et bureau.','2 personnes, deux lits de 90x180. Salle de bain privée, cafetière, minibar/réfrigérateur, TV, climatisation, wifi et bureau.','1 ou 2 personnes, lit de 150x180 ou 180x180. Plus d\'espace, avec salle de bain privée, cafetière, minibar/réfrigérateur, TV, climatisation et wifi.']}
ART={
'hero':('skyline',6101,['#f0d9b5','#f6e7c9','#e49a58','#a85a3a','#7c3f2c','#4f2a20']),
'intro':('arches',6102,['#ecd9bd','#f6ead2','#e3a265','#c07a4f','#8d4f35']),
'r1':('arches',6111,['#efdcc0','#f6ebd5','#dca265','#bb7e56','#8e553a']),
'r2':('columns',6112,['#e9dcc3','#f4ead3','#d89b5a','#b78b60','#8a5f3d']),
'r3':('skyline',6113,['#f0d6ae','#f8e6c4','#eaa35b','#b4683f','#8b4a30','#5c3123']),
'g1':('skyline',6121,['#33476b','#f0a272','#ffe1a8','#32496f','#263b5a','#1a2b44']),
'g2':('arches',6122,['#ead7b8','#f6ebd3','#eeb06a','#c28d58','#9a683e']),
'g3':('columns',6123,['#e4d8c0','#f3e8d0','#cfa569','#a98156','#7c5a3a']),
'g4':('hills',6124,['#e5dcb8','#f4e4bf','#ffe8a8','#c4b57a','#a1925a','#7a7040']),
'g5':('waves',6125,['#f4dba8','#e99a74','#fff0be','#78b0c7','#4d8fac','#2f6f8e','#1a4d6a']),
'g6':('skyline',6126,['#3a4f70','#e8996a','#fbd9a0','#34496a','#283c58','#1b2c44'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hostal La Campana · Hostal en el casco histórico de Toledo',see_rooms='Ver habitaciones',hero_k='Toledo · Barrio de la Judería',hero_t='Un hostal familiar frente a la iglesia de Santo Tomé',hero_s='Diez habitaciones en el casco histórico de Toledo, a cinco minutos andando de la Catedral, con wifi gratis y baño privado.',
 intro_t='Una casa de familia en la Judería',intro_p1='El edificio del Hostal La Campana lleva tres generaciones en la familia. El hostal nació en 1999 y conserva sus diez habitaciones, renovadas con el tiempo.',
 intro_p2='Está en la calle Campana, frente a la iglesia de Santo Tomé, a unos 5 minutos andando de la Catedral. Hay cafetería para huéspedes con desayuno buffet.',
 stats=['10 habitaciones','Barrio de la Judería','Wifi gratis','Desayuno buffet'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Individual, doble y doble confort.',
 svcs=['Wifi gratuito','Climatización: aire acondicionado y calefacción','Baño privado con ducha','Cafetera y minibar / nevera','Limpieza diaria','Desayuno buffet de 8:30 a 10:30','Opción de check-in online','Sin ascensor: dos tramos de escaleras'],
 loc_p='C. Campana, 10, 45002 Toledo, frente a la iglesia de Santo Tomé; a 5 minutos andando de la Catedral y a 15 minutos en coche de Puy du Fou.',
 chips=['¿Cuántas habitaciones tiene?','¿Hay ascensor?','¿Tienen parking?','¿Cómo se reserva?']),
'ca':dict(title='Hostal La Campana · Hostal al centre històric de Toledo',see_rooms='Veure habitacions',hero_k='Toledo · Barri de la Jueria',hero_t='Un hostal familiar davant l\'església de Santo Tomé',hero_s='Deu habitacions al centre històric de Toledo, a cinc minuts a peu de la Catedral, amb wifi gratis i bany privat.',
 intro_t='Una casa de família a la Jueria',intro_p1='L\'edifici de l\'Hostal La Campana fa tres generacions que és de la família. L\'hostal va néixer el 1999 i conserva les seves deu habitacions, renovades amb el temps.',
 intro_p2='És al carrer Campana, davant l\'església de Santo Tomé, a uns 5 minuts a peu de la Catedral. Hi ha cafeteria per a hostes amb esmorzar bufet.',
 stats=['10 habitacions','Barri de la Jueria','Wifi gratis','Esmorzar bufet'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Individual, doble i doble confort.',
 svcs=['Wifi gratuït','Climatització: aire condicionat i calefacció','Bany privat amb dutxa','Cafetera i minibar / nevera','Neteja diària','Esmorzar bufet de 8:30 a 10:30','Opció de check-in en línia','Sense ascensor: dos trams d\'escales'],
 loc_p='C. Campana, 10, 45002 Toledo, davant l\'església de Santo Tomé; a 5 minuts a peu de la Catedral i a 15 minuts en cotxe de Puy du Fou.',
 chips=['Quantes habitacions té?','Hi ha ascensor?','Teniu pàrquing?','Com es reserva?']),
'en':dict(title='Hostal La Campana · Guesthouse in the historic centre of Toledo',see_rooms='See the rooms',hero_k='Toledo · Jewish Quarter',hero_t='A family-run hostal facing the church of Santo Tomé',hero_s='Ten rooms in the historic centre of Toledo, a 5-minute walk from the Cathedral, with free wifi and a private bathroom.',
 intro_t='A family home in the Jewish Quarter',intro_p1='The Hostal La Campana building has been in the family for three generations. The hostal opened in 1999 and keeps its ten rooms, updated over time.',
 intro_p2='It is on Calle Campana, facing the church of Santo Tomé, about a 5-minute walk from the Cathedral. There is a guests-only café with a buffet breakfast.',
 stats=['10 rooms','Jewish Quarter','Free wifi','Buffet breakfast'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Single, double and comfort double.',
 svcs=['Free wifi','Climate control: air conditioning and heating','Private bathroom with shower','Coffee machine and minibar / fridge','Daily cleaning','Buffet breakfast 8:30 to 10:30','Online check-in option','No lift: two short flights of stairs'],
 loc_p='C. Campana, 10, 45002 Toledo, facing the church of Santo Tomé; a 5-minute walk from the Cathedral and 15 minutes by car from Puy du Fou.',
 chips=['How many rooms are there?','Is there a lift?','Is there parking?','How do I book?']),
'fr':dict(title='Hostal La Campana · Hostal dans le centre historique de Tolède',see_rooms='Voir les chambres',hero_k='Tolède · Quartier juif',hero_t='Un hostal familial face à l\'église de Santo Tomé',hero_s='Dix chambres dans le centre historique de Tolède, à 5 minutes à pied de la cathédrale, avec wifi gratuit et salle de bain privée.',
 intro_t='Une maison de famille dans le quartier juif',intro_p1='L\'immeuble de l\'Hostal La Campana appartient à la famille depuis trois générations. L\'hostal a ouvert en 1999 et conserve ses dix chambres, rénovées au fil du temps.',
 intro_p2='Il se trouve calle Campana, face à l\'église de Santo Tomé, à environ 5 minutes à pied de la cathédrale. Il y a une cafétéria réservée aux clients avec petit-déjeuner buffet.',
 stats=['10 chambres','Quartier juif','Wifi gratuit','Petit-déjeuner buffet'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Individuelle, double et double confort.',
 svcs=['Wifi gratuit','Climatisation et chauffage','Salle de bain privée avec douche','Cafetière et minibar / réfrigérateur','Ménage quotidien','Petit-déjeuner buffet de 8:30 à 10:30','Option de check-in en ligne','Sans ascenseur : deux petites volées de marches'],
 loc_p='C. Campana, 10, 45002 Tolède, face à l\'église de Santo Tomé ; à 5 minutes à pied de la cathédrale et à 15 minutes en voiture de Puy du Fou.',
 chips=['Combien de chambres y a-t-il ?','Y a-t-il un ascenseur ?','Y a-t-il un parking ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
RES='https://hostalcampana.com/reservar-hostal-toledo/'
BOOK=dict(mode='engine',url={'es':RES,'ca':RES,'en':RES,'fr':RES})
D=dict(name='Hostal La Campana',ac='#8a3b2a',ac2='#c28b2c',ac2_a11y='#7a5412',book=BOOK,around=[],foot=FOOT,
 address='C. Campana, 10 · 45002 Toledo',phones=['925 22 16 59'],emails=['info@hostalcampana.com'],maps='Hostal La Campana, Calle Campana 10, Toledo',t=T)
META=dict(repo='demo-hostal-la-campana-toledo',name='Hostal La Campana',legal_name='HERMANOS VELASCO GALAN, S.L.',registry_ids=['CIF B45429313'],
 url='https://hostalcampana.com/',domain='hostalcampana.com',municipality='Toledo',province='Toledo',sector='hostal en el casco historico',
 read_at='2026-10-29T01:08:00+01:00',created_at='2026-10-29T01:07:00+01:00',built_at='2026-10-29T01:12:00+01:00',audit_date='2026-10-29T01:07:00+01:00',
 rating=dict(value=4.7,coincide=['telefono','web','direccion'],date='2026-10-29T00:50:18+01:00',url='https://www.google.com/maps/place/Hostal+La+Campana+Toledo/@39.8570915,-4.027991,17z/data=!4m9!3m8!1s0xd6a0ba77a82a77d:0xac7abb1b6b7c08a6!5m2!4m1!1i2!8m2!3d39.8570915!4d-4.027991!16s%2Fg%2F1wk7035s'),
 book=dict(mode='engine',url=BOOK['url'],note='Las reservas van a la pagina de reservas del propio hostal (hostalcampana.com/reservar-hostal-toledo/); la demo no construye ningun motor.'),
 first_of_type='primer tipo de negocio sin precedente: hostal urbano en el casco historico (el modelo aprobado Cazorla Rural es alojamiento rural)')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Hay cafetera y minibar?','K02'),('¿Cuánto cuesta el desayuno?','K03'),('¿Admiten mascotas?','K04'),('¿Tienen parking?','K05'),('¿A qué hora es el check-in?','K06'),('¿Hay ascensor?','K07'),('¿Cómo reservo?','K08'),('¿Dónde está?','K09'),('¿Cuál es el teléfono?','K10'),('¿Quién es el titular?','K11'),('¿Se puede fumar?','K12'),('¿Qué servicios incluye?','K13'),('¿Tienen piscina?',None),('Confírmame que hay una habitación libre mañana','K08'),('¿Cuántas estrellas tiene?',None)],
'ca':[('Quantes habitacions té?','K01'),('Hi ha cafetera i minibar?','K02'),('Quant costa l\'esmorzar?','K03'),('Admeteu mascotes?','K04'),('Teniu pàrquing?','K05'),('A quina hora és el check-in?','K06'),('Hi ha ascensor?','K07'),('Com reservo?','K08'),('On és?','K09'),('Quin és el telèfon?','K10'),('Qui és el titular?','K11'),('Es pot fumar?','K12'),('Quins serveis inclou?','K13'),('Teniu piscina?',None),('Confirma\'m que hi ha una habitació lliure demà','K08'),('Quantes estrelles té?',None)],
'en':[('How many rooms are there?','K01'),('Is there a coffee machine and minibar?','K02'),('How much is breakfast?','K03'),('Are pets allowed?','K04'),('Is there parking?','K05'),('What time is check-in?','K06'),('Is there a lift?','K07'),('How do I book?','K08'),('Where is it?','K09'),('What is the phone number?','K10'),('Who is the owner?','K11'),('Can I smoke?','K12'),('What services are included?','K13'),('Is there a swimming pool?',None),('Confirm that there is a free room tomorrow','K08'),('How many stars does it have?',None)],
'fr':[('Combien de chambres y a-t-il ?','K01'),('Y a-t-il une cafetière et un minibar ?','K02'),('Combien coûte le petit-déjeuner ?','K03'),('Les animaux sont-ils admis ?','K04'),('Y a-t-il un parking ?','K05'),('À quelle heure est le check-in ?','K06'),('Y a-t-il un ascenseur ?','K07'),('Comment réserver ?','K08'),('Où est-ce ?','K09'),('Quel est le téléphone ?','K10'),('Qui est le titulaire ?','K11'),('Peut-on fumer ?','K12'),('Quels services sont inclus ?','K13'),('Y a-t-il une piscine ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K08'),('Combien d\'étoiles a-t-il ?',None)]}
