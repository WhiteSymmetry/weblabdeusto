# -*- coding: utf-8 -*-

import os

romie_sqlite = os.path.join(CURRENT_PATH, "forotech.db")
romie_time = 194.159 # 3 minutes, 14.159 seconds
questions = [
	[ # 0 difficulty
		{
			"question": '¿Qué espectro de ondas electromagnéticas usan las radiografías?',
			"answers": [
				'Rayos gamma',
				'Rayos X',
				'Ondas de radio'
			],
			"correct": 1,
			"points": 70,
			"time": 30
		},
		{
			"question": 'En un programa informático ¿Qué es la barra de herramientas?',
			"answers": [
				'La barra de navegación',
				'Botones empleados para activar funciones de una aplicación',
				'Barra con llaves inglesas para arreglar el PC'
			],
			"correct": 1,
			"points": 70,
			"time": 30
		},
		{
			"question": '¿Cuántos huesos tiene el ser humano?',
			"answers": [
				128,
				204,
				233,
				206
			],
			"correct": 3,
			"points": 80,
			"time": 35
		},
		{
			"question": 'El número pi(π) está presente en',
			"answers": [
				'La naturaleza',
				'Cilindros',
				'Esferas',
				'Todas son correctas'
			],
			"correct": 3,
			"points": 75,
			"time": 30
		},
		{
			"question": '¿Cúantos decimales tiene el número pi(π)?',
			"answers": [
				'4',
				'10',
				'Infinitos',
			],
			"correct": 2,
			"points": 70,
			"time": 30
		},
		{
			"question": 'Si multiplicamos el diametro del pie de un elefante por 2*π ¿Qué obtenemos?',
			"answers": [
				'Su peso',
				'Su altura',
				'La superficie de sus orejas'
			],
			"correct": 1,
			"points": 75,
			"time": 30
		},
		{
			"question": '¿Qué paralelogramo no tiene los lados adyacentes iguales ni los ángulos rectos?',
			"answers": [
				'Círculo',
				'Rectangulo',
				'Romboide'
			],
			"correct": 2,
			"points": 70,
			"time": 30
		},
		{
			"question": '¿Cuántos milímetros son un decámetro?',
			"answers": [
				1000,
				10,
				10000,
				100
			],
			"correct": 2,
			"points": 70,
			"time": 30
		},
		{
			"question": '¿Cómo llamamos a la estrella luminosa centro de nuestro sistema planetario?',
			"answers": [
				'Luna',
				'Sol',
				'Marte',
				'Orión'
			],
			"correct": 1,
			"points": 70,
			"time": 30
		},
		{
			"question": '¿Qué es un mp3?',
			"answers": [
				'Acronimo de "música para tres"',
				'Formato de audio digital comprimido',
				'Un formato de imagen'
			],
			"correct": 1,
			"points": 60,
			"time": 25
		},
		{
			"question": 'El número pi(π) fue encontrado por',
			"answers": [
				'la civilización occidental',
				'varias civilizaciones simultáneamente más o menos (griega, china, india...)',
				'revelación mística: vino del cielo o de un lugar similar'
			],
			"correct": 1,
			"points": 80,
			"time": 30
		}
	],
	[ # 1 difficulty
		{
			"question": '¿Cuántas horas tiene el 29 de febrero de un año bisiesto?',
			"answers": [
				23.5,
				24,
				24.5
			],
			"correct": 1,
			"points": 100,
			"time": 25
		},
		{
			"question": '¿En qué año se descubrió América?',
			"answers": [
				1465,
				1523,
				1492,
				1812
			],
			"correct": 2,
			"points": 100,
			"time": 25
		},
		{
			"question": '¿Qué miembro de una orquesta puede dar la espalda en un concierto?',
			"answers": [
				'El batería',
				'El arpa',
				'El violín',
				'El director'
			],
			"correct": 3,
			"points": 100,
			"time": 25
		},
		{
			"question": '¿Qué mide una pinta?',
			"answers": [
				'El volumen',
				'La masa',
				'La fuerza',
				'No hay ninguna medida llamada pinta'
			],
			"correct": 0,
			"points": 100,
			"time": 24
		},
		{
			"question": 'Brújula de navegación marina',
			"answers": [
				'Escuadra',
				'Compás',
				'Regla',
				'Calibre'
			],
			"correct": 1,
			"points": 110,
			"time": 24
		},
		{
			"question": 'Si en una granja hay 4 perros y 10 gallinas. ¿Cuántas patas hay en la granja?',
			"answers": [
				'56',
				'36',
				'30',
				'46'
			],
			"correct": 1,
			"points": 100,
			"time": 24
		},
		{
			"question": '¿Cuántos grados tiene media circunferencia?',
			"answers": [
				180,
				90,
				270,
				360
			],
			"correct": 0,
			"points": 90,
			"time": 25
		},
		{
			"question": 'El número pi(π) fue...',
			"answers": [
				'Inventado',
				'Descubierto',
				'Calculado',
				'Las tres anteriores',
				'Ninguna de las anteriores'
			],
			"correct": 1,
			"points": 100,
			"time": 25
		},
		{
			"question": '¿Qué es el login?',
			"answers": [
				'Identificación de usuario',
				'Contraseña para validarse en un sitio',
				'Un logo pequeño'
			],
			"correct": 0,
			"points": 90,
			"time": 25
		},
		{
			"question": 'En 1987, en EE.UU., el congresista Edwin J. Goodwin intentó que el congreso norteamericano aprobara un proyecto que implicaba "cuadrar el círculo" y que implicaba para pi(π) un valor de 3,2.',
			"answers": [
				'Verdadero aunque increíble',
				'Falso y no sé por qué',
			],
			"correct": 0,
			"points": 90,
			"time": 25
		}
	],
	[ # 2 difficulty
		{
			"question": '¿Cómo se llaman los naturales de Huesca?',
			"answers": [
				'Huescanos',
				'Oscenses',
				'Huescenses',
				'De Huesca'
			],
			"correct": 1,
			"points": 105,
			"time": 25
		},
		{
			"question": '¿Qué relaciona el número pi (π)?',
			"answers": [
				'La relación entre el diámetro y la superficie de un círculo',
				'La relación entre el radio y el diámetro de un círculo',
				'La relación entre un cuadrado y un círculo',
				'La relación entre el diámetro y la circunferencia de un círculo'
			],
			"correct": 3,
			"points": 115,
			"time": 20
		},
		{
			"question": 'El número pi(π) es un número',
			"answers": [
				'Racional',
				'Irracional',
				'Ninguna de las anteriores',
			],
			"correct": 1,
			"points": 55,
			"time": 20
		},
		{
			"question": '¿Cuántas provincias gallegas limitan con Portugal?',
			"answers": [
				'Ninguna',
				1,
				2,
				3
			],
			"correct": 2,
			"points": 155,
			"time": 20
		},
		{
			"question": 'Sinónimo de grados Celsius',
			"answers": [
				'Grados centígrados',
				'Grados fahrenheit',
				'Grados faraday',
				'Ninguna es correcta'
			],
			"correct": 0,
			"points": 155,
			"time": 20
		},
		{
			"question": ' la altura de la pirámide de Keops dividida por su base da como resultado...',
			"answers": [
				'e',
				10,
				'Pi(π)',
				'Ninguna es correcta'
			],
			"correct": 2,
			"points": 155,
			"time": 20
		},
		{
			"question": 'Qué se puede recordar con este poema?\nSoy y seré a todos definible\nmi nombre tengo que daros\ncociente diametral siempre inmedible\nsoy de los redondos aros',
			"answers": [
				'Las primeras 20 cifras o dígitos del número pi(π)',
				'Lo bonita que es la poesía',
				'El alcance del número pi(π)',
				'Esto no tiene que ver con pi(π)'
			],
			"correct": 0,
			"points": 155,
			"time": 20
		},
		{
			"question": 'En esta frase “Hizo fundir asimismo un mar de diez codos de un lado al otro, perfectamente redondo. Tenía cinco codos de altura y a su alrededor un cordón de treinta codos” ¿Cuánto vale pi según este texto?',
			"answers": [
				'pi(π)',
				3,
				3,141592,
				'No se sabe, es un texto bíblico'
			],
			"correct": 1,
			"points": 155,
			"time": 20
		}
	],
	[ # 3 difficulty
		{
			"question": '¿Cuáles son las siglas en inglés para el término OVNI?',
			"answers": [
				'ET',
				'OVNI',
				'UFO',
				'EIL'
			],
			"correct": 2,
			"points": 135,
			"time": 25
		},
		{
			"question": '¿Qué mide una pinta?',
			"answers": [
				'El volumen',
				'La masa',
				'La fuerza',
				'No hay ninguna medida llamada pinta'
			],
			"correct": 0,
			"points": 140,
			"time": 24
		},
		{
			"question": 'Si un número natural sólo se puede dividir por si mismo y por la unidad se llama número...',
			"answers": [
				'Entero',
				'Primo',
				'Par',
				'Hermano'
			],
			"correct": 1,
			"points": 140,
			"time": 24
		},
		{
			"question": '¿Cuántos números primos hay entre 0 y 10?',
			"answers": [
				3,
				5,
				9,
				0
			],
			"correct": 1,
			"points": 140,
			"time": 24
		},
		{
			"question": 'El número pi es...',
			"answers": [
				'Irracional',
				'Trascendente',
				'Las dos cosas'
			],
			"correct": 2,
			"points": 140,
			"time": 24
		},
		{
			"question": 'Lee esta frase “Hizo fundir asimismo un mar de diez codos de un lado al otro, perfectamente redondo. Tenía cinco codos de altura y a su alrededor un cordón de treinta codos” ¿Crees que vale como cálculo del número pi?',
			"answers": [
				'Sí',
				'No',
				'Sí pero es un cálculo grueso',
				'No tiene nada que ver'
			],
			"correct": 2,
			"points": 140,
			"time": 24
		},
		{
			"question": '¿Cuándo se celebra el día mundial del número pi(π)?',
			"answers": [
				'8 de abril',
				'14 de marzo',
				'5 de mayo',
				'29 de febrero'
			],
			"correct": 1,
			"points": 140,
			"time": 24
		},
		{
			"question": '¿Cuál es el dígito del 0 al 9 que tarda más en salir en el número pi(π)?',
			"answers": [
				0,
				1,
				7,
				3
			],
			"correct": 2,
			"points": 140,
			"time": 24
		}
	],
	[ # 4 difficulty
		{
			"question": '¿Cual es la longitud de una circunferencia?',
			"answers": [
				'4*pi*r',
				'4/3*pi*r',
				'2*pi*r',
				'pi*r'
			],
			"correct": 2,
			"points": 65,
			"time": 25
		},
		{
			"question": '¿Cuáles son las células encargadas de destruir los virus en nuestro organismo?',
			"answers": [
				'Los glóbulos blancos',
				'Los anticuerpos',
				'Las neuronas',
				'Los góbulos rojos'
			],
			"correct": 0,
			"points": 165,
			"time": 25
		},
		{
			"question": '¿Qué matemático realizó la primera estimación del valor de pi(π)?',
			"answers": [
				'Galileo Galilei',
				'René Descartes',
				'Arquímedes de Siracusa',
				'Pitágoras'
			],
			"correct": 2,
			"points": 165,
			"time": 25
		},
		{
			"question": '¿Cuál fue la primera civilización en emplear el número pi(π)?',
			"answers": [
				'Romanos',
				'Egipcios',
				'Griegos',
				'Persas'
			],
			"correct": 1,
			"points": 165,
			"time": 25
		},
		{
			"question": '¿Crees que tu número de teléfono aparece dentro del número pi(π)?',
			"answers": [
				'Sí, probablemente ',
				'No, probablemente',
				'Yo que sé',
				'El número pi no tiene nada que ver con mi teléfono'
			],
			"correct": 0,
			"points": 165,
			"time": 25
		},
		{
			"question": 'La persona que más dígitos sabe de memoria del número pi(π), Lu Chao, es capaz de recitar:',
			"answers": [
				'67.890 decimales',
				'1.000 decimales',
				'100.000.000 decimales'			],
			"correct": 0,
			"points": 165,
			"time": 25
		},
		{
			"question": '¿Cuánto vale el volumen de un cilindro?',
			"answers": [
				'4/3*π*r',
				'π²*h',
				'2*π*h'			],
			"correct": 1,
			"points": 165,
			"time": 25
		}
	],
	[ # 5 difficulty
		{
			"question": '¿En qué año se creó el ordenador personal Apple I?',
			"answers": [
				1834,
				1954,
				1976,
				1994
			],
			"correct": 2,
			"points": 195,
			"time": 24
		},
		{
			"question": '¿En qué año llegaron los seres humanos a la Luna?',
			"answers": [
				'Nunca han llegado seres humanos a la Luna',
				1468,
				1969,
				2005
			],
			"correct": 2,
			"points": 205,
			"time": 25
		},
		{
			"question": '¿Cuantos decimales del número pi(π) se conocen hoy?',
			"answers": [
				'Mil',
				'Tres millones',
				'Diez trillones',
				'Siete billones'
			],
			"correct": 2,
			"points": 205,
			"time": 25
		},
		{
			"question": '¿Cómo se llama el famoso cometa que pasa cada 76 años?',
			"answers": [
				'Humels',
				'Halley',
				'Homer',
				'Marte'
			],
			"correct": 1,
			"points": 200,
			"time": 24
		},
		{
			"question": '¿En qué lugar surgieron las matemáticas?',
			"answers": [
				'Grecia',
				'Egipto',
				'Mesopotamia',
				'Roma'
			],
			"correct": 2,
			"points": 200,
			"time": 24
		},
		{
			"question": 'William Shanks, matemático inglés, dedico 20 años de su vida a la obtención de 707 decimales de pi(π).(En 1945 se descubrió que había cometido un error en el decimal 528 y a partir de este todos los demás eran incorrectos)',
			"answers": [
				'Cierto',
				'Falso',
				'El número pi no tiene tantos decimales'
			],
			"correct": 0,
			"points": 200,
			"time": 24
		}
	],
	[ # 6 difficulty
		{
			"question": '¿En qué año nació Alan Turing, creador del primer ordenador de la historia?',
			"answers": [
				1876,
				1912,
				1945,
				1987
			],
			"correct": 1,
			"points": 225,
			"time": 25
		},
		{
			"question": '¿En qué año se data la primera referencia al número pi(π)?',
			"answers": [
				'1650 adC',
				'0',
				'200 adC',
				'1000 adC'
			],
			"correct": 0,
			"points": 225,
			"time": 25
		},
		{
			"question": '¿Cuál es el volumen de una esfera?',
			"answers": [
				'4*π*r',
				'4/3*π*r',
				'2*π*r',
				'π*r'
			],
			"correct": 1,
			"points": 225,
			"time": 22
		},
		{
			"question": '¿se repiten por igual los dígitos del 0 al 9 dentro del número pi(π)?',
			"answers": [
				'Sí',
				'No',
				'No se sabe por ahora, pero se cree que sí'
			],
			"correct": 2,
			"points": 225,
			"time": 22
		},
		{
			"question": '¿Quién no ha estado directamente relacionado con el cálculo del número pi(π)?',
			"answers": [
				'Euler',
				'Einstein',
				'Leibniz',
				'Newton'
			],
			"correct": 1,
			"points": 225,
			"time": 22
		}
	],
	[ # 7 difficulty
		{
			"question": '¿Cual fue el último y más poderoso lider de los Hunos?',
			"answers": [
				'Anibal',
				'Atila',
				'Julio Cesar',
				'Joffrey Baratheon'
			],
			"correct": 1,
			"points": 250,
			"time": 20
		},
		{
			"question": '¿Cúantos años dura un cíclo solar?',
			"answers": [
				20,
				50,
				11,
				1
			],
			"correct": 2,
			"points": 250,
			"time": 20
		},
		{
			"question": '¿se repiten por igual los dígitos del 00 al 99 dentro del número pi(π)?',
			"answers": [
				'Sí',
				'No',
				'No se sabe por ahora, pero se cree que sí'
			],
			"correct": 2,
			"points": 250,
			"time": 20
		}
	],
	[ # 8 difficulty
		{
			"question": '¿En qué provincia española están las ruinas de Numancia?',
			"answers": [
				'Palencia',
				'Segovia',
				'Ávila',
				'Burgos'
			],
			"correct": 0,
			"points": 255,
			"time": 20
		},
		{
			"question": '¿Quién electrocutó a un elefante para demostrar los peligros de la corriente alterna?',
			"answers": [
				'Edison',
				'Tesla',
				'Chiquito de la Calzada',
				'Faraday'
			],
			"correct": 0,
			"points": 255,
			"time": 24
		},
		{
			"question": '¿El número pi(π) se parece al número…??',
			"answers": [
				'e',
				'Aureo',
				'Gordo',
				'raiz(2)'
			],
			"correct": 1,
			"points": 255,
			"time": 24
		}
	],
	[ # 9 difficulty
		{
			"question": '¿Quién fue el primero en usar la letra griega pi (π) para el número 3,141592653...?',
			"answers": [
				'Leonhard Euler',
				'Alan Turing',
				'William Jones',
				'William Oughtred'
			],
			"correct": 3,
			"points": 314,
			"time": 31
		},
		{
			"question": '¿Quién fue el primer filósofo que relacionó la física con las matemáticas?',
			"answers": [
				'Homero',
				'Aristóteles',
				'Revunidas',
				'Pitágoras'
			],
			"correct": 3,
			"points": 314,
			"time": 31
		},
		{
			"question": '¿Es correcto este número pi(π): 3,14159365358979323846264?',
			"answers": [
				'Sí',
				'No, hay al menos un dígito cambiado',
				'Tal vez'
			],
			"correct": 1,
			"points": 314,
			"time": 31
		},
		{
			"question": '¿La expresión 1-(1/3)+(1/5)-(1/7)+(….. es igual a',
			"answers": [
				'Pi',
				'Pi/2',
				'Pi/4',
				'Ni idea'
			],
			"correct": 2,
			"points": 314,
			"time": 31
		}
	],
	[ # 10 difficulty
		{
			"question": '¿Cuánto dura la incubación de un huevo de emu?',
			"answers": [
				'Aproximadamente 52 días',
				'Aproximadamente 23 días',
				'Aproximadamente 76 días',
				'Aproximadamente 92 días'
			],
			"correct": 0,
			"points": 340,
			"time": 20
		},
		{
			"question": '¿Quién popularizo el número pi(π)?',
			"answers": [
				'William Oughtred',
				'William Jones',
				'Leonhard Euler'
			],
			"correct": 1,
			"points": 340,
			"time": 20
		},
		{
			"question": 'La expresión 1+(1/3)+(1*2)/(3*5)+(1*2*3)/(3*5*7)+(….. es igual a',
			"answers": [
				'π',
				'π/2',
				'π/4',
				'Ni idea'
			],
			"correct": 1,
			"points": 340,
			"time": 20
		},
		{
			"question": 'La expresión (2/1)*(2/3)*(4/3)*(4/5)*(6/5)*(6/7)*….. es igual a',
			"answers": [
				'π',
				'π/2',
				'π/4',
				'Ni idea'
			],
			"correct": 1,
			"points": 340,
			"time": 20
		}
	]
]
