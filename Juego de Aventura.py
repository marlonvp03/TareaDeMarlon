print("JUEGO DE HISTORIA\n")
print("ESCAPE DE LA MANSION SOMBRIA\n")
print("Te despiertas en una habitacion fria y oscura de una mansion en ruinas del cual debes salir con vida.\n")

parte1 = input("Estas encadenado a la pared. ¿Intentas FORZAR la cerradura o Gritar por ayuda?. : ").strip().upper()

if parte1 == "FORZAR":
    parte2 = input("\nTe liberas y sales al pasillo. Hay un guardia de espaldas. ¿Decides ATACAR, ESCONDERTE o PASAR de largo?. : ").strip().upper()
    
    if parte2 == "ATACAR":
        parte3 = input("\nEl guardia cae, pero suena una alarma. ¿Corres hacia la VENTANA, buscas el SOTANO o entras a la COCINA?. : ").strip().upper()

        if parte3 == "VENTANA":
            parte4 = input("\nLa ventana esta alta. ¿Prefieres SALTAR, usar una CUERDA de cortina o romper el VIDRIO?. : ").strip().upper()

            if parte4 == "CUERDA":
                parte5 = input("\nBajas al jardin. Varios perros te ven y corren hacia ti. ¿Intentas CORRER, TREPAR un arbol o LANZAR carne?. : ").strip().upper()

                if parte5 == "TREPAR":
                    parte6 = input("\nDesde el arbol ves la salida. ¿Saltas la CERCA, esperas el AMANECER o pides AUXILIO?. : ").strip().upper()

                    if parte6 == "CERCA":
                        print("\n¡LOGRASTE ESCAPAR! Eres libre.")

                    elif parte6 == "AMANECER" or parte6 == "AUXILIO":
                        print("Te encuentran y vuelven a encerrar. FIN.")
                    else:
                        print("Repuesta no valida. Intenta de nuevo.")
                
                elif parte5 == "CORRER":
                    print("\nRapidamente los perros te acorralan y te atacan sin parar. FIN.")
                elif parte5 == "LANZAR":
                    print("\nLos perros corren hacia la carne, pero no te dan el suficiente tiempo para escapar y te persiguen hasta llegar a ti y acabar contigo. FIN. ")
                else:
                    print("\nRepuesta no valida. Intenta de nuevo")
            
            elif parte4 == "SALTAR":
                print("\nLa caida es fatal y mueres. FIN.")
            elif parte4 == "VIDRIO":
                print("\nTe cortas y por el ruido que haces te encuentran y te encierran de nuevo. FIN.")
            else:
                print("\nRepuesta no valida. Intenta de nuevo")
        
        elif parte3 == "SOTANO":
            print("\nTe acorralan en un callejon sin salida. FIN.")
        elif parte3 == "COCINA":
            print("\nTe encuentras sin salida, aunque tratas de defenderte no es suficiente para tus captores. FIN.")
        else:
            print("\nRepuesta no valida. Intenta de nuevo.")

    elif parte2 == "ESCONDERTE":
        parte3_1 = input("\nEl guardia pasa. Ves una puerta secreta detras de un cuadro. ¿Entras a la BIBLIOTECA, sales al BALCON o intentas bajar por la CHIMENEA?. : ").strip().upper()

        if parte3_1 == "BIBLIOTECA":
            parte4_1 = input("\nEncuentras un pasadizo. ¿Usas una ANTORCHA, caminas a OSCURAS?. : ").strip().upper()

            if parte4_1 == "ANTORCHA":
                parte5_1 = input("\nEl pasadizo llega a una alcantarilla. ¿Decides NADAR en agua sucia, caminas por el BORDE o REGRESAR por miedo a perderte?. : ").strip().upper()

                if parte5_1 == "BORDE":
                    parte6_1 = input("\nLlegas a una rejilla. ¿La EMPUJAS, usas una PALANCA o GRITAS pidiendo ayuda?. : ").strip().upper()

                    if parte6_1 == "PALANCA":
                        print("\n¡La rejilla cede y sales al bosque! VICTORIA.")
                    
                    elif parte6_1 == "EMPUJAS":
                        print("\nNo tienes la fuerza suficiente, te encuentran y capturan de nuevo. FIN.")
                    elif parte6_1 == "GRITAS":
                        print("\nA causa de los gritos te escuchan y te capturan de nuevo. FIN.")
                    else:
                        print("\nRepuesta no valida. Intente de nuevo.")
                
                elif parte5_1 == "NADAR":
                    print("\nNo era solo suciedad, el agua estaba saturada por toxinas que paralizaron los pulmones en cuestion de minutos. FIN.")
                elif parte5_1 == "REGRESAR":
                    print("\nAl hacerlo te encuentra el dueño de la mansion y te captura de nuevo. FIN.")
                else:
                    print("\nRepuesta no valida. Intenta de nuevo.")
            
            elif parte4_1 == "OSCURAS":
                print("\nTe tropiezas en la oscuridad y caes en una trampa. FIN.")
            else:
                print("\nRepuesta no valida. Intenta de nuevo.")
        
        elif parte3_1 == "BALCON":
            print("\nLlegas al balcon, no encuentras salida y mientras dudas que hacer el dueño de la mansion te ataca y captura de nuevo. FIN.")
        elif parte3_1 == "CHIMENEA":
            print("\nEl espacio es muy estrecho, intentas escapar de igual forma pero quedas atrapado. FIN.")
        else:
            print("\nRepuesta no valida. Intenta de nuevo.")
    
    elif parte2 == "PASAR":
        print("\nEl guardia te escucha y te neutraliza. FIN.")
    else:
        print("\nRepuesta no valida. Intente de nuevo.")

elif parte1 == "GRITAR":
    print("\nNadie viene a ayudarte, pero el secuestrador te escucha y decide terminar el juego temprano. FIN.")

else:
    print("\nRepuesta no valida. Intente de nuevo.")