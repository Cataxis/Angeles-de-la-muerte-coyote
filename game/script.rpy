define a = Character("Amanda", color="#A51C30")

label start:

    init python:
        def mouse_moviendo():
            pos_actual = renpy.get_mouse_pos()
            pos_objetivo = [960, 500]

            if pos_actual[0] != pos_objetivo[0] or pos_actual[1] != pos_objetivo[1]:
                renpy.set_mouse_pos(pos_objetivo[0], pos_objetivo[1], abs(1.16 * pos_actual[0] - pos_objetivo[0]) * 0.0022)

    screen mouse: 
        timer 0.1 repeat True action Function(mouse_moviendo)

    python:
        import os
        global user 
        user = os.environ.get('USERNAME') or os.environ.get('USER')  
    
    scene bg room with fade

    show tranquila with dissolve

    play music "intro.ogg"
 
    a "Hola. Soy yo, tu ángel de la muerte. Por favor, no temas, puedes evadir tu hora de muerte si decides escucharme."

    hide tranquila with dissolve

    menu uno:
        "Está bien...":
            call respuestaUno from _call_respuestaUno

    label respuestaUno:
        play sound "click.ogg" fadeout 1
        show neutral with dissolve

        a "'Te prometo, hijo, que te compraré muchos juguetes cuando lleguemos, tendrás ropita limpia y nueva y seremos felices tú y yo, te lo juro...'"

        hide neutral
        show seria 

        a "Fue lo último que dijo el hombre al niño que tenía en brazos, pero el pequeño nunca respondió."

        hide seria with dissolve

    menu dos:
        "¿Por qué?":
            call respuestaDos from _call_respuestaDos

    label respuestaDos:
        play sound "lloro.ogg"
        show triste with dissolve

        a "Porque el niño ya se había muerto por insolación…"

        a "El hombre no pudo enterrarlo porque unos oficiales de migración lo detuvieron y lo regresaron a su país, donde el hombre terminó por quitarse la vida."

        $ renpy.pause(.5) 

        hide triste
        show neutral

        a "¿Quieres que te cuente otra historia?"
        hide neutral with dissolve

    menu tres:
        "Sí":
            call respuestaTres from _call_respuestaTres

    label respuestaTres:
        play sound "click.ogg" fadeout 1
        show seria with dissolve

        a "Martina corría con desesperación, su vientre de 7 meses la hacía sentir el peso de su situación, pero aún así continuaba, pujando y con oraciones en su mente. "

        a "Estaba determinada a alcanzar el otro lado de la frontera, convencida de que lo lograría a pesar de las dificultades."
        
        hide seria
        show triste 

        play sound "lloro.ogg"

        a "Sin embargo, su esperanza se vio frustrada cuando unos secuestradores interrumpieron su desgarradora travesía,deteniéndola en seco."
       
        a "Ahora ella es vendida como prostituta."

        hide triste with dissolve

    menu cuatro:
        "¿Y su bebé?":
            call respuestaCuatro from _call_respuestaCuatro
    
    label respuestaCuatro:
    play sound "impacto.mp3" fadeout 1
    show grito with vpunch

    a "¡Obviamente perdió al bebé!"

    $ renpy.pause(1)  

    hide grito 
    show triste 

    play sound "lloro.ogg"

    a "¿Cómo no después de la paliza que le metieron?"

    hide triste 
    show meh 

    a "La estúpida pensaba que en los Estados Unidos podría darle una vida mejor a su hijo porque en el sur del continente, en su país, su esposo solo la golpeaba, nadie en su familia la apoyaba por embarazarse a los 15 años y andar con un hombre de 20."

    hide meh 
    show amenaza 

    a "¿Qué se sentirá haber logrado sobrevivir a un tren bestia, al hambre, a la sed, y que cuando estás a punto de conseguirlo, todo se derrumba?"
    
    a "¿Lo sabes?"

    hide amenaza with dissolve

    menu cinco:
        "No":
            call respuestaCinco from _call_respuestaCinco
    
    label respuestaCinco:
    play sound "impacto.mp3"
    show grito with vpunch
    a "¡Obvio que no!"

    hide grito 
    show meh
    a "Pero si sabías que esos secuestradores operaban en el lugar, después de todo hay mucha demanda de “latinas”."

    $ renpy.pause(1)  

    hide meh 
    show amenaza 

    a "¿Debería matarte o quieres escuchar otra historia?"
    hide amenaza with dissolve

    menu seis:
        "Otra historia...":
            call respuestaSeis from _call_respuestaSeis 
    
    label respuestaSeis:
    stop music fadeout 1.5
    play sound "click.ogg" fadeout 1
    show seria with dissolve 
    a "Un agente de migración encontró un cuaderno, y en el había un poema, y decía:"  

    hide seria
    show recitando

    play music "poema.mp3"

    a "En el rincón humilde de mi corazón,
    late un amor profundo, pura pasión,
    un joven soñador que sin fortuna,
    sus sentimientos al viento desentuna."
 
    hide recitando  
    show sonrojada 

    a "En tus ojos, estrellas del firmamento,
    hallé un brillo eterno, un fuego lento,
    mas en la sombra de mi pobreza,
    temo no ser digno de tu nobleza."

    a "Eres la rosa más hermosa del jardín,
    tu esencia embriaga como vino sin fin,
    pero mi bolsillo es apenas un suspiro,
    una triste melodía en el desvío."

    a "Mis manos, descalzas, buscan tu piel,
    acariciar el alma de mi querer,
    pero la distancia, un muro sin cesar,
    nos separa, sin poderme acercar."
    
    hide sonrojada 
    show sad 

    play sound "lloro.ogg"

    a "¡Ay, cruel destino, qué implacable eres!,
    un corazón apasionado que no merece,
    la dulce mirada de quien tanto anhelo,
    la caricia suave, el amor sincero."

    a "¿Sabes quien lo escribió?"

    stop music fadeout 1.5

    hide sad with dissolve

    menu siete:
        "No...":
            call respuestaSiete from _call_respuestaSiete
    
    label respuestaSiete:
    play sound "click.ogg" fadeout 1
    show seria with dissolve 
    play music "intro.ogg"
    a "Ricardo Valle, un joven guatemalteco, parque escribió para expresar sus sentimientos hacia una chica de su país, quien lamentablemente lo rechazó con una desalentadora respuesta:"

    hide seria 
    show amenaza 

    a "'Si fueras rico, sería tu novia.'"

    hide amenaza 
    show recitando 

    a "Ricardo provenía de una familia de escasos recursos y ante la adversidad, optó por buscar oportunidades en un país lleno de sueños, pero desafortunadamente, solo encontró pesadillas."

    hide recitando 
    show triste

    play sound "lloro.ogg"

    a "Trágicamente, su vida llegó a un abrupto final debido a una mordedura de víbora de cascabel."

    $ renpy.pause(1) 

    hide triste
    show neutral

    a "¿Aún quieres vivir?"

    hide neutral 

    menu ocho:
        "Sí...":
            call respuestaOcho from _call_respuestaOcho
    
    label respuestaOcho:
    play sound "click.ogg" fadeout 1
    show amenaza with dissolve 
    a "Permíteme contarte la historia de Gerardo: Mientras cruzaba el Río Bravo, sostenía en sus brazos a su hija de 10 años. "

    a "Desafortunadamente, su grupo lo había abandonado, ya que no querían retrasarse por ellos, creyendo que cada persona debe velar por sí misma."

    a "¿Te gustaría saber qué sucedió después?"
    hide amenaza with dissolve

    menu nueve:
        "¿Sí?":
            call respuestaNueve from _call_respuestaNueve
    
    label respuestaNueve:
    stop music fadeout 2 
    show sad with dissolve 
    play sound "lloro.ogg"

    a "Encontraron el cadáver de aquel hombre tendido en la orilla del río, junto a él yacía el cuerpo de su hija totalmente desnuda."

    a "Las pruebas forenses revelaron que la niña presentaba muestras de ADN distintas en su “interior”..."
    
    $ renpy.pause(1) 

    hide sad
    show amenaza 
    stop music fadeout 1
    play music "intro.ogg"

    a "Basura humana, ¿todavía quieres vivir?"

    hide amenaza with dissolve

    menu diez:
        "Sí...":
            call respuestaDiez from _call_respuestaDiez
    
    label respuestaDiez:
    play sound "click.ogg" fadeout 1
    show triste with dissolve 
    a "Si eso deseas…"
    hide triste 
    show seria 
    a "Ernesto era un joven talentoso, con un trabajo estable que le permitía costear su vida y ayudar en casa a su hermano pequeño y su madre. Sin embargo, un día la salud de su madre empeoró debido a la diabetes y necesitaba medicamentos costosos. "

    hide seria
    show recitando 
    a "A pesar de las dificultades, Ernesto logró conseguir otro trabajo, aunque apenas le alcanzaba para sobrevivir. Desafortunadamente, la vida le tenía preparada otra desgracia:"

    a "Su hermano enfermó gravemente de cáncer y necesitaba quimioterapias y medicamentos costosos."

    a "Ernesto se vio desesperado al no poder costear los tratamientos y se enfrentó a una difícil decisión:"

    hide recitando
    show triste

    a "Ir a la frontera y cruzar para intentar ahorrar algo y poder ayudar a su familia. Aunque no fue fácil, decidió intentarlo."

    a "Mientras intentaba cruzar la frontera, la caravana en la que viajaba fue atacada y les robaron todo."

    hide triste
    show neutral
    a "A pesar de este revés, Ernesto siguió luchando con todas sus fuerzas."

    hide neutral
    show triste

    a "Lamentablemente, sufrió un accidente y se rompió el pie."

    hide triste 
    play sound "lloro.ogg"
    show sad 

    a "Nadie pudo atenderlo y quedó abandonado, sin recibir ayuda, lo que finalmente resultó en su trágico fallecimiento."

    hide sad
    show seria

    $ renpy.pause(1) 

    a "Y eso fue todo, supongo que ahora debo matarte…"


    hide seria with dissolve
    
    menu once:
        "¡Cuéntame otra historia!":
            call respuestaOnce from _call_respuestaOnce
    
    label respuestaOnce:
    play sound "click.ogg" fadeout 1
    show amenaza with dissolve 
    a "Está bien, parece que si tienes muchas ganas de vivir, una más…"

    hide amenaza
    show recitando
    stop music fadeout 1 
    a "Una caravana de inmigrantes iba en un camión, a punto de cruzar la frontera, cuando de repente una mujer en un ataque de pánico empezó a gritar porque no aguantaba más."
  
    play sound "grito.mp3" 

    a "Ese grito llamó la atención de los oficiales de frontera, quienes abrieron el vehículo y descubrieron a los inmigrantes ocultos dentro."

    play music "intro.ogg"

    a "La caravana estaba compuesta por personas de diversas nacionalidades, cada una de ellas escapando de tiroteos y condiciones precarias en sus países de origen."

    a "Era evidente que nadie quería dejar atrás a sus seres queridos ni abandonar su hogar, pero las circunstancias los forzaban a emprender un peligroso viaje hacia Estados Unidos."

    hide recitando
    show triste
    a "Las historias de cada uno eran trágicas y desgarradoras; hombres, mujeres y niños que arriesgaban sus vidas en busca de un futuro mejor."

    a "No se iban porque quisieran, sino porque no les quedaba otra opción."

    hide triste
    show amenaza
    a "¿Qué tan aterradora y miserable debía ser su vida para llegar a tal extremo?"

    hide amenaza
    show seria 
    a "Se encontraban frente a un destino incierto, pero para ellos, era preferible enfrentar los peligros del viaje que continuar en un lugar donde la violencia y la pobreza eran moneda corriente."

    a "Atravesar la frontera no significaba que todos lograrían quedarse en Estados Unidos, pero aun así, estaban dispuestos a enfrentar el desafío."

    hide seria
    show amenaza 
    a "Había destinos más inciertos y desesperanzadores que la muerte misma, y lo sabían muy bien."
    
    hide amenaza
    show neutral
    a "A pesar del miedo y las dificultades, compartían una determinación inquebrantable de buscar una vida digna y segura para ellos y sus seres queridos."

    hide neutral
    show seria
    a "Pero no lo lograron."

    $ renpy.pause(1) 

    hide seria
    show amenaza 
    a "Te lo preguntaré una última vez, escoria"
    
    $ renpy.pause(1) 

    a "¿Quieres vivir o morir?"

    stop music fadeout 1 

    hide amenaza
    show neutral 

    show screen mouse

    play sound "risas.mp3"

    menu doce:
        "¡Quiero vivir...":
            hide screen mouse
            call respuestaDoce from _call_respuestaDoce

        "¡Quiero vivir...":
            hide screen mouse
            call respuestaDoce from _call_respuestaDoce_1

        "¡Quiero morir!":
            hide screen mouse
            call respuestaDoce from _call_respuestaDoce_2
    
    label respuestaDoce:
    play music "scream.ogg" 
    show loca with dissolve 
    play sound "revelacion.ogg"
    $ sentence = "Oye, {}".format(user)
    
    a "[sentence], Si nunca te di la oportunidad de elegir en todo el juego, ¿por qué crees que puedes hacerlo ahora?"
    
    scene fondo with fade
    play sound "pixel.ogg"
    show terror1 with pixellate
    a "Todas estas historias tienen algo en común:"

    a "Las personas de las que te hablé te pagaron, porque tú fuiste su coyote."

    hide terror1
    play sound "pixel.ogg"
    show terror2 with pixellate
    a "Jugaste con la vida de docenas de personas a cambio de dinero, amasaste una fortuna traficando con seres humanos, vendiendo mujeres y niñas, y traficando órganos de hombres."

    hide loca 
    hide terror2
    play sound "pixel.ogg"
    show terror3 with pixellate
    a "Violaste a jóvenes y dejaste que murieran, sin importarte nada más que tus ganancias. Actuaste como si fueras un dios, manipulando y destruyendo sus vidas, pero no lo eres."



    a "Puede que hoy no te mate, tal vez tampoco lo haga mañana, pero... "

  
    hide terror3
    play sound "pixel.ogg"
    show terror4 with pixellate
    a "Te aseguro que tarde o temprano  vas a morir y no puedes hacer nada para cambiarlo."
    play sound "revelacion.ogg"
    $ renpy.pause(3)
    
    $ renpy.quit()
    return