PROGRAM PERFILES;
USES AUX1,DOS,CRT,GRAFICOS,PRINTER;
VAR
U,X,Y,C:ARRAY[0..200]OF REAL;
K,L,J,OP1,OP,N,I:INTEGER;
MOT,MO,CA,M2,CT,CP,A,H:REAL;
OPA,OPA1,OPA2,VEN,DE:STRING;
PROCEDURE DATOS;
BEGIN
     CLRSCR;
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN('     ###  INDUSTRIAS MACA Ltda.  ###  | autor : Rafael Antequera Caballero |');
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     GOTOXY(5,5);
     WRITELN;
     WRITELN('              ####################################################');
     WRITELN('              ####                                            ####');
     WRITELN('              ####      PROPORCIONE LOS SIGUIENTES DATOS :    ####');
     WRITELN('              ####                                            ####');
     WRITELN('              ####                                            ####');
     WRITELN('              ####      ANCHO DE LA PIEZA [metros]  :         ####');
     WRITELN('              ####      ALTO DE LA PIEZA  [metros]  :         ####');
     WRITELN('              ####      NUMERO DE PIEZAS  [unid.]   :         ####');
     WRITELN('              ####                                            ####');
     WRITELN('              ####      IDENTIFICACION DE LA PIEZA  :         ####');
     WRITELN('              ####                                            ####');
     WRITELN('              ####                                            ####');
     WRITELN('              ####################################################');
     GOTOXY(55,11);
     READLN(A);
     GOTOXY(55,12);
     READLN(H);
     GOTOXY(55,13);
     READLN(N);
     GOTOXY(55,15);
     READLN(VEN);
END;
PROCEDURE COSTO;
BEGIN
     Y[0]:=X[0]*7.25;Y[1]:=X[1]*0.46;Y[2]:=X[2]*0.60;Y[3]:=X[3]*0.6;Y[4]:=X[4]*0.6;
     Y[5]:=X[5]*0.6;Y[6]:=X[6]*0.05;Y[7]:=X[7]*0.05;Y[8]:=X[8]*8;Y[9]:=X[9]*0.05;
     Y[10]:=X[10]*0.05;Y[11]:=X[11]*0.05;Y[12]:=X[12]*0.05;Y[13]:=X[13]*0.05;Y[14]:=X[14]*0.05;
     Y[15]:=X[15]*0.05;Y[16]:=X[16]*0.05;Y[17]:=X[17]*0.05;Y[18]:=X[18]*0.25;Y[19]:=X[19]*0.25;
     Y[20]:=X[20]*20;Y[21]:=X[21]*6.3;Y[22]:=X[22]*5.6;Y[23]:=X[23]*0.25;Y[24]:=X[24]*0.05;
     Y[25]:=X[25]*13.9;Y[26]:=X[26]*3.5;Y[27]:=X[27]*0.05;Y[28]:=X[28]*2.3;Y[29]:=X[29]*0.75;
     Y[30]:=X[30]*0.06;Y[31]:=X[31]*0.03;Y[32]:=X[32]*1;Y[33]:=X[33]*2.39;Y[34]:=X[34]*0.8;
     Y[35]:=X[35]*0.07;Y[36]:=X[36]*1.3;Y[37]:=X[37]*0.08;Y[38]:=X[38]*0.03;Y[39]:=X[39]*0.35;
     Y[40]:=X[40]*12.44;Y[41]:=X[41]*2.4;Y[42]:=X[42]*0.8;Y[43]:=X[43]*0.25;Y[44]:=X[44]*0.5;
     Y[45]:=X[45]*11.2;Y[46]:=X[46]*3.2;Y[47]:=X[47]*2.9;Y[48]:=X[48]*3.6;Y[49]:=X[49]*14.2;
     Y[50]:=X[50]*18.5;Y[51]:=X[51]*22.6;Y[52]:=X[52]*26.8;Y[53]:=X[53]*31.1;Y[54]:=X[54]*41;
     Y[55]:=X[55]*12.1;Y[56]:=X[56]*15.5;Y[57]:=X[57]*18.4;Y[58]:=X[58]*21.4;Y[59]:=X[59]*25.3;
     Y[60]:=X[60]*35.4;MO:=X[0]*2;
END;
PROCEDURE INI;
BEGIN
     MOT:=0;
     FOR I:=0 TO 100 DO
         BEGIN
              X[I]:=0;Y[I]:=0;
              U[I]:=0;C[I]:=0;
         END;
END;
PROCEDURE INI1;
BEGIN
     FOR I:=0 TO 100 DO
         BEGIN
              X[I]:=0;Y[I]:=0;
         END;
END;
PROCEDURE SCA;
BEGIN
     CA:=0;
     FOR I:=6 TO 100 DO
         BEGIN
              CA:=Y[I]+CA;
         END;
END;
PROCEDURE S;
BEGIN
     FOR I:=0 TO 100 DO
         BEGIN
              U[I]:=U[I]+X[I];
              C[I]:=C[I]+Y[I];
         END;
END;
PROCEDURE II;
BEGIN
     WRITELN('                  a = ',A:2:2,'  [Mt]      h = ',H:2:2,'   [Mt]');
     WRITELN;
     WRITELN('               PLANILLA DE COTIZACION PIEZA  :  ',VEN);
     WRITELN('         ARTICULO                       CANTIDAD         COSTO');
     WRITELN('    Aluminio                           ',X[0]:5:2,' [Kgr]   ',Y[0]:5:2,' [$us]');
     WRITELN('    Burlete # 385                      ',X[1]:5:2,' [mt]    ',Y[1]:5:2,' [$us]');
     WRITELN('    Burlete # 2007                     ',X[2]:5:2,' [mt]    ',Y[2]:5:2,' [$us]');
     WRITELN('    Felpa  7 x 7                       ',X[3]:5:2,' [mt]    ',Y[3]:5:2,' [$us]');
     WRITELN('    Felpa  7 x 5                       ',X[4]:5:2,' [mt]    ',Y[4]:5:2,' [$us]');
     WRITELN('    Felpa  5 x 5                       ',X[5]:5:2,' [mt]    ',Y[5]:5:2,' [$us]');
     WRITELN('    Mano de obra                                     ',MO:5:2,' [$us]');
     WRITELN('    Accesorios                                       ',CA:5:2,' [$us]');
     CP:=Y[0]+Y[1]+Y[2]+Y[3]+Y[4]+Y[5]+MO+CA;
     WRITELN('    TOTAL POR UNA PIEZA                              ',CP:5:2,' [$us]');
     WRITELN('           Cantidad de piezas           ',N);CT:=CP*N;
     WRITE('    TOTAL POR ',N,' PIEZAS                              ',CT:6:2,' [$us]');
     READLN;
     MOT:=MOT+(MO*N);
     CLRSCR;
END;
PROCEDURE RESUMEN;
     BEGIN
     CA:=0;
     FOR I:=6 TO 100 DO
         BEGIN
              CA:=CA+C[I];
         END;
     CLRSCR;
     WRITELN(LST);
     WRITELN(LST,'                        +++++++++++++++++++++++++++++++    ');
     WRITELN(LST,'                        ###  INDUSTRIAS MACA Ltda.  ###    ');
     WRITELN(LST,'                        +++++++++++++++++++++++++++++++    ');
     WRITELN(LST,'                                   por: R.A.C.');
     WRITELN(LST);
     WRITELN(LST,'                        PLANILLA GENERAL DE MATERIALES ');
     WRITELN(LST);
     WRITELN(LST,'         ARTICULO                       CANTIDAD         COSTO');
     WRITELN(LST);
     WRITELN(LST,'    Aluminio                              ',U[0]:5:2,' [Kgr]   ',C[0]:5:2,' [$us]');
     WRITELN(LST,'    Burlete # 385                         ',U[1]:5:2,' [mt]    ',C[1]:5:2,' [$us]');
     WRITELN(LST,'    Burlete # 2007                        ',U[2]:5:2,' [mt]    ',C[2]:5:2,' [$us]');
     WRITELN(LST,'    Felpa  7 x 7                          ',U[3]:5:2,' [mt]    ',C[3]:5:2,' [$us]');
     WRITELN(LST,'    Felpa  7 x 5                          ',U[4]:5:2,' [mt]    ',C[4]:5:2,' [$us]');
     WRITELN(LST,'    Felpa  5 x 5                          ',U[5]:5:2,' [mt]    ',C[5]:5:2,' [$us]');
     WRITELN(LST,'    Mano de obra                                        ',MOT:5:2,' [$us]');
     WRITELN(LST);
     WRITELN(LST,'         ACCESORIOS');
     WRITELN(LST);
     WRITELN(LST,'    Tornillo de carpinter#a 2" x 10        ',U[6]:4:0,' [Unid]   ',C[6]:5:2,' [$us]');
     WRITELN(LST,'    Taco fisher # 8                        ',U[7]:4:0,' [Unid]   ',C[7]:5:2,' [$us]');
     WRITELN(LST,'    Silicona transparente                  ',U[8]:2:2,' [Unid]   ',C[8]:5:2,' [$us]');
     WRITELN(LST,'    Tornillo de encarne 1(1/4)" x 8        ',U[9]:4:0,' [Unid]   ',C[9]:5:2,' [$us]');
     WRITELN(LST,'    Tornillo de encarne 1(1/2)" x 10       ',U[10]:4:0,' [Unid]   ',C[10]:5:2,' [$us]');
     WRITELN(LST,'    Tornillo de encarne 1" x 14            ',U[11]:4:0,' [Unid]   ',C[11]:5:2,' [$us]');
     WRITELN(LST,'    Tornillo de encarne 1" x 7             ',U[12]:4:0,' [Unid]   ',C[12]:5:2,' [$us]');
     WRITELN(LST,'    Tornillo de encarne (3/8)" x 6         ',U[13]:4:0,' [Unid]   ',C[13]:5:2,' [$us]');
     WRITELN(LST,'    Tornillo de encarne (1/2)" x 8         ',U[14]:4:0,' [Unid]   ',C[14]:5:2,' [$us]');
     WRITELN(LST,'    Remache poop 4 x 10                    ',U[15]:4:0,' [Unid]   ',C[15]:5:2,' [$us]');
     WRITELN(LST,'    Remache poop 3,2 x 5,2                 ',U[16]:4:0,' [Unid]   ',C[16]:5:2,' [$us]');
     WRITELN(LST,'    Remache poop 4 x 8                     ',U[17]:4:0,' [Unid]   ',C[17]:5:2,' [$us]');
     WRITELN(LST,'    Escuadras                              ',U[18]:4:0,' [Unid]   ',C[18]:5:2,' [$us]');
     WRITELN(LST,'    Perfil " U "                           ',U[19]:4:0,' [Unid]   ',C[19]:5:2,' [$us]');
     WRITELN(LST,'    Cerradura " GIACO "                    ',U[20]:4:0,' [Unid]   ',C[20]:5:2,' [$us]');
     WRITELN(LST,'    Picaporte " PLATIL "                   ',U[21]:4:0,' [Unid]   ',C[21]:5:2,' [$us]');
     WRITELN(LST,'    Bisagra normal " FLAMIA "              ',U[22]:4:0,' [Unid]   ',C[22]:5:2,' [$us]');
     WRITELN(LST,'    Perno (5/16) x 1"                      ',U[23]:4:0,' [Unid]   ',C[23]:5:2,' [$us]');
     WRITELN(LST,'    Bolanda de presi#n (5/16)"             ',U[24]:4:0,' [Unid]   ',C[24]:5:2,' [$us]');
     WRITELN(LST,'    Cerradura " AN _ DIF "                 ',U[25]:4:0,' [Unid]   ',C[25]:5:2,' [$us]');
     WRITELN(LST,'    Bisagra liviana " FLAMIA "             ',U[26]:4:0,' [Unid]   ',C[26]:5:2,' [$us]');
     WRITELN(LST,'    Bolanda de presi#n (1/4)"              ',U[27]:4:0,' [Unid]   ',C[27]:5:2,' [$us]');
     WRITELN(LST,'    Aldaba " CHAMICAL "                    ',U[28]:4:0,' [Unid]   ',C[28]:5:2,' [$us]');
     WRITELN(LST,'    Rueda " CHAMICAL "                     ',U[29]:4:0,' [Unid]   ',C[29]:5:2,' [$us]');
     WRITELN(LST,'    Antiruido T-50                         ',U[30]:4:0,' [Unid]   ',C[30]:5:2,' [$us]');
     WRITELN(LST,'    Tapon tope goma B-26                   ',U[31]:4:0,' [Unid]   ',C[31]:5:2,' [$us]');
     WRITELN(LST,'    Jalador de empotrar # 124              ',U[32]:4:0,' [Unid]   ',C[32]:5:2,' [$us]');
     WRITELN(LST,'    Cierre central # 1101                  ',U[33]:4:0,' [Unid]   ',C[33]:5:2,' [$us]');
     WRITELN(LST,'    Rodamiento con ruleman # 1150          ',U[34]:4:0,' [Unid]   ',C[34]:5:2,' [$us]');
     WRITELN(LST,'    Gu#a pl#stica antiruido # 1250         ',U[35]:4:0,' [Unid]   ',C[35]:5:2,' [$us]');
     WRITELN(LST,'    Rodamiento para duchero                ',U[36]:4:0,' [Unid]   ',C[36]:5:2,' [$us]');
     WRITELN(LST,'    Pat#n interior D2                      ',U[37]:4:0,' [Unid]   ',C[37]:5:2,' [$us]');
     WRITELN(LST,'    Pat#n exterior D3                      ',U[38]:4:0,' [Unid]   ',C[38]:5:2,' [$us]');
     WRITELN(LST,'    Porta toallero pl#stico D4             ',U[39]:4:0,' [Unid]   ',C[39]:5:2,' [$us]');
     WRITELN(LST,'    Acrilico                               ',U[40]:2:2,' [mt^2]   ',C[40]:5:2,' [$us]');
     WRITELN(LST,'    Brazo ventilete 30 nat.                ',U[41]:4:0,' [Unid]   ',C[41]:5:2,' [$us]');
     WRITELN(LST,'    Bisagra 2"                             ',U[42]:4:0,' [Unid]   ',C[42]:5:2,' [$us]');
     WRITELN(LST,'    Perno y tuerca (3/16) x (1/2)"         ',U[43]:4:0,' [Unid]   ',C[43]:5:2,' [$us]');
     WRITELN(LST,'    Rueda de aluminio # 3004               ',U[44]:4:0,' [Unid]   ',C[44]:5:2,' [$us]');
     WRITELN(LST,'    Cerradura pico de loro                 ',U[45]:4:0,' [Unid]   ',C[45]:5:2,' [$us]');
     WRITELN(LST,'    Brazo ventilete 30 br.                 ',U[46]:4:0,' [Unid]   ',C[46]:5:2,' [$us]');
     WRITELN(LST,'    Brazo ventilete 40 nat.                ',U[47]:4:0,' [Unid]   ',C[47]:5:2,' [$us]');
     WRITELN(LST,'    Brazo ventilete 40 br.                 ',U[48]:4:0,' [Unid]   ',C[48]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 2 aletas H-320 bronce          ',U[49]:4:0,' [Unid]   ',C[49]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 3 aletas H-460 bronce          ',U[50]:4:0,' [Unid]   ',C[50]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 4 aletas H-600 bronce          ',U[51]:4:0,' [Unid]   ',C[51]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 5 aletas H-740 bronce          ',U[52]:4:0,' [Unid]   ',C[52]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 6 aletas H-880 bronce          ',U[53]:4:0,' [Unid]   ',C[53]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 7 aletas H-1020 bronce         ',U[54]:4:0,' [Unid]   ',C[54]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 2 aletas H-320 natural         ',U[55]:4:0,' [Unid]   ',C[55]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 3 aletas H-460 natural         ',U[56]:4:0,' [Unid]   ',C[56]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 4 aletas H-600 natural         ',U[57]:4:0,' [Unid]   ',C[57]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 5 aletas H-740 natural         ',U[58]:4:0,' [Unid]   ',C[58]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 6 aletas H-880 natural         ',U[59]:4:0,' [Unid]   ',C[59]:5:2,' [$us]');
     WRITELN(LST,'    Celosia 7 aletas H-1020 natural        ',U[60]:4:0,' [Unid]   ',C[60]:5:2,' [$us]');
     WRITELN(LST);
     WRITELN(LST,'    TOTAL COSTO ACCESORIOS                           ',CA:5:2,' [$us]');
     WRITELN(LST);CP:=C[0]+C[1]+C[2]+C[3]+C[4]+C[5]+MOT+CA;
     WRITELN(LST,'    TOTAL COSTO DEL ALUMINIO Y ACCESORIOS            ',CP:5:2,' [$us]');
     READLN;
END;
PROCEDURE S6000;
BEGIN
SUBMENU1;
READLN(OP1);
CLRSCR;
IF OP1<>6 THEN
DATOS;
IF OP1=2 THEN
BEGIN
    INI1;
    X[16]:=2;X[33]:=1;X[34]:=4;X[35]:=8;X[9]:=16;
    X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=((2*A)+(2*H))/20;
    X[0]:=2.088*A+2.661*H;X[2]:=2*A+4*H;X[5]:=4*A+6*H;
    G7;COSTO;SCA;II;
END;
IF OP1=3 THEN
BEGIN
    INI1;
    X[16]:=4;X[33]:=2;X[34]:=6;X[35]:=12;X[9]:=20;
    X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=((2*A)+(2*H))/20;
    X[0]:=2.088*A+3.456*H;X[2]:=2*A+6*H;X[5]:=4*A+8*H;
    G8;COSTO;SCA;II;
END;
IF OP1=4 THEN
BEGIN
    INI1;
    X[16]:=4;X[33]:=2;X[34]:=8;X[35]:=16;X[9]:=24;
    X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=((2*A)+(2*H))/20;
    X[0]:=2.088*A+4.771*H;X[2]:=2*A+8*H;X[5]:=4*A+12*H;
    G9;COSTO;SCA;II;
END;
IF OP1=5 THEN
BEGIN
    INI1;
    CLRSCR;
    GOTOXY(15,15);
    WRITE(' ESTA LINEA NO SOPORTA ESA CANTIDAD DE PA#OS !!!!!!!!');
    READLN;
    {G10;COSTO;SCA;II;}
END;
IF (OP1<>5) AND (OP1<>6) THEN
BEGIN
FOR I:=0 TO 100 DO
BEGIN
     X[I]:=N*X[I];
     Y[I]:=Y[I]*N;
END;
S;
CLRSCR;
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('#########################################################################');
WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
WRITELN('                             VENTANA S/6000');
WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [ventana(s)]');
WRITELN('#########################################################################');
WRITELN;
WRITELN('           DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
WRITELN('                                                         ($us)    ($us)');
WRITELN('   Remache poop 3.2 x 5.5              ',X[16]:3:0,'    piezas      0.05     ',(Y[16]):4:2);
WRITELN('   Cierre central # 1101               ',X[33]:3:0,'    piezas      0.25     ',(Y[33]):4:2);
WRITELN('   Rodamiento con ruleman # 1150       ',X[34]:3:0,'    piezas      0.80     ',(Y[34]):4:2);
WRITELN('   Guia pl#stica antiruido # 1250      ',X[35]:3:0,'    piezas      0.07     ',(Y[35]):4:2);
WRITELN('   Tornillo de encarne 1(1/4) x 8      ',X[9]:3:0,'    piezas      0.05     ',(Y[9]):4:2);
WRITELN('   Tornillo de carpinter#a             ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
WRITELN('   Taco fisher # 8                     ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
WRITELN('   Silicona transparente               ',X[8]:2:2,'    piezas      8.00     ',(Y[8]):4:2);
WRITELN('#########################################################################');
WRITE('   TOTAL                                                           ',(CA*N):4:2);
READLN;
END;
END;
PROCEDURE VCST;
BEGIN
SUBMENU1;
READLN(OP1);
CLRSCR;
IF OP1<>6 THEN
DATOS;
IF OP1=2 THEN
BEGIN
    INI1;
    X[28]:=1;X[29]:=4;X[30]:=8;X[31]:=8;X[15]:=32;X[10]:=8;
    X[32]:=2;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;
    X[4]:=4*A+6*H;X[1]:=2*A+4*H;X[0]:=2.226*A+3.074*H;
    G7;COSTO;SCA;II;
END;
IF OP1=3 THEN
BEGIN
    INI1;
    X[28]:=2;X[29]:=6;X[30]:=12;X[31]:=12;X[15]:=32;X[10]:=12;
    X[32]:=2;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;
    X[4]:=4*A+8*H;X[1]:=2*A+6*H;X[0]:=2.226*A+3.931*H;
    G8;COSTO;SCA;II;
END;
IF OP1=4 THEN
BEGIN
    INI1;
    X[28]:=2;X[29]:=8;X[30]:=16;X[31]:=16;X[15]:=32;X[10]:=16;
    X[32]:=2;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;X[12]:=3;
    X[4]:=4*A+12*H;X[1]:=2*A+8*H;X[0]:=2.226*A+5.162*H;
    G9;COSTO;SCA;II;
END;
IF OP1=5 THEN
BEGIN
    INI1;
    X[28]:=2;X[29]:=10;X[30]:=20;X[31]:=20;X[15]:=32;X[10]:=20;X[14]:=4;
    X[32]:=4;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;X[12]:=6;
    X[4]:=4*A+12*H;X[1]:=2*A+10*H;X[0]:=2.226*A+6.392*H;
    G10;COSTO;SCA;II;
END;
IF OP1<>6 THEN
BEGIN
FOR I:=0 TO 100 DO
BEGIN
     X[I]:=N*X[I];
     Y[I]:=Y[I]*N;
END;
S;
CLRSCR;
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('#########################################################################');
WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
WRITELN('                        VENTANA CORREDIZA LIVIANA');
WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [ventana(s)]');
WRITELN('#########################################################################');
WRITELN;
WRITELN('          DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
WRITELN('                                                         ($us)    ($us)');
WRITELN('    Aldaba chamical                     ',X[28]:3:0,'    piezas      2.30     ',(Y[28]):4:2);
WRITELN('    Rueda chamical                      ',X[29]:3:0,'    piezas      0.75     ',(Y[29]):4:2);
WRITELN('    Antiruido T-50                      ',X[30]:3:0,'    piezas      0.06     ',(Y[30]):4:2);
WRITELN('    Tapon tope goma                     ',X[31]:3:0,'    piezas      0.03     ',(Y[31]):4:2);
WRITELN('    Remache poop  4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
WRITELN('    Tornillo encarne 1(1/2) x 10        ',X[10]:3:0,'    piezas      0.05     ',(Y[10]):4:2);
WRITELN('    Tacos fisher # 8                    ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
WRITELN('    Tornillo de carpinter#a 2 x 10      ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
WRITELN('    Silicona transparente               ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
WRITELN('    Tornillo de encarne 1 x 7           ',X[12]:3:0,'    piezas      0.05     ',(Y[12]):4:2);
WRITELN('    Tornillo de encarne de (1/2) x 6    ',X[14]:3:0,'    piezas      0.05     ',(Y[14]):4:2);
WRITELN('    Jalador de empotrar                 ',X[32]:3:0,'    piezas      1.00     ',(Y[32]):4:2);
WRITELN('#########################################################################');
WRITE('   TOTAL                                                           ',(CA*N):4:2);
READLN;
END;
END;
PROCEDURE VC;
BEGIN
SUBMENU1;
READLN(OP1);
CLRSCR;
IF OP1<>6 THEN
DATOS;
IF OP1=2 THEN
BEGIN
    INI1;
    X[28]:=1;X[29]:=4;X[30]:=8;X[31]:=8;X[15]:=32;X[10]:=8;
    X[32]:=2;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;
    X[4]:=4*A+6*H;X[1]:=2*A+4*H;X[0]:=2.697*A+4.645*H;
    G7;COSTO;SCA;II;
END;
IF OP1=3 THEN
BEGIN
    INI1;
    X[28]:=2;X[29]:=6;X[30]:=12;X[31]:=12;X[15]:=32;X[10]:=12;
    X[32]:=2;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;
    X[4]:=4*A+8*H;X[1]:=2*A+6*H;X[0]:=2.697*A+5.758*H;
    G8;COSTO;SCA;II;
END;
IF OP1=4 THEN
BEGIN
    INI1;
    X[28]:=2;X[29]:=8;X[30]:=16;X[31]:=16;X[15]:=32;X[10]:=16;
    X[32]:=2;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;X[12]:=3;
    X[4]:=4*A+12*H;X[1]:=2*A+8*H;X[0]:=2.697*A+7.285*H;
    G9;COSTO;SCA;II;
END;
IF OP1=5 THEN
BEGIN
    INI1;
    X[28]:=2;X[29]:=10;X[30]:=20;X[31]:=20;X[15]:=32;X[10]:=20;X[14]:=4;
    X[32]:=4;X[6]:=INT((A+H)*4);X[7]:=X[6];X[8]:=(2*A+2*H)/20;X[12]:=6;
    X[4]:=4*A+12*H;X[1]:=2*A+10*H;X[0]:=2.697*A+8.813*H;
    G10;COSTO;SCA;II;
END;
IF OP1<>6 THEN
BEGIN
FOR I:=0 TO 100 DO
BEGIN
     X[I]:=N*X[I];
     Y[I]:=Y[I]*N;
END;
S;
CLRSCR;
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('#########################################################################');
WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
WRITELN('                            VENTANA CORREDIZA');
WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [ventana(s)]');
WRITELN('#########################################################################');
WRITELN;
WRITELN(' CODIGO   DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
WRITELN('                                                         ($us)    ($us)');
WRITELN('    Aldaba chamical                     ',X[28]:3:0,'    piezas      2.30     ',(Y[28]):4:2);
WRITELN('    Rueda chamical                      ',X[29]:3:0,'    piezas      0.75     ',(Y[29]):4:2);
WRITELN('    Antiruido T-50                      ',X[30]:3:0,'    piezas      0.06     ',(Y[30]):4:2);
WRITELN('    Tapon tope goma                     ',X[31]:3:0,'    piezas      0.03     ',(Y[31]):4:2);
WRITELN('    Remache poop  4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
WRITELN('    Tornillo encarne 1(1/2) x 10        ',X[10]:3:0,'    piezas      0.05     ',(Y[10]):4:2);
WRITELN('    Tacos fisher # 8                    ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
WRITELN('    Tornillo de carpinter#a 2 x 10      ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
WRITELN('    Silicona transparente               ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
WRITELN('    Tornillo de encarne 1 x 7           ',X[12]:3:0,'    piezas      0.05     ',(Y[12]):4:2);
WRITELN('    Tornillo de encarne de (1/2) x 6    ',X[14]:3:0,'    piezas      0.05     ',(Y[14]):4:2);
WRITELN('    Jalador de empotrar                 ',X[32]:3:0,'    piezas      1.00     ',(Y[32]):4:2);
WRITELN('#########################################################################');
WRITE('   TOTAL                                                           ',(CA*N):4:2);
READLN;
END;
END;
PROCEDURE MAX;
BEGIN
     X[17]:=65;X[42]:=2;X[43]:=8;X[14]:=2;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[5]:=3*A+4*H;X[1]:=2*A+2*H;X[0]:=2.459*A+3.374*H;
END;
PROCEDURE PAL;
BEGIN
     X[25]:=1;X[21]:=1;X[26]:=3;X[11]:=8;X[15]:=35;
     X[18]:=2;X[27]:=8;X[8]:=(2*A+2*H)/20;X[1]:=4*A+2*H;X[4]:=A+2*H;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[0]:=4.202*A+3.138*H;
END;
PROCEDURE PA;
BEGIN
     X[20]:=1;X[21]:=1;X[22]:=3;X[15]:=16;X[23]:=8;
     X[18]:=2;X[24]:=8;X[6]:=INT((A+H)*4);X[7]:=X[6];
     X[8]:=(2*A+2*H)/20;X[3]:=A+2*H;X[1]:=4*A+2*H;
     X[0]:=5.406*A+4.505*H;
END;
PROCEDURE OPITA;
BEGIN
IF OPA='S' THEN
    BEGIN
	IF OPA1='S' THEN
            BEGIN
            	IF OPA2='A' THEN
                     X[49]:=1;
            	IF OPA2='B' THEN
                     X[50]:=1;
            	IF OPA2='C' THEN
                     X[51]:=1;
            	IF OPA2='D' THEN
                     X[52]:=1;
            	IF OPA2='E' THEN
                     X[53]:=1;
            	IF OPA2='F' THEN
                     X[54]:=1;
            END
            ELSE
            BEGIN
            	IF OPA2='A' THEN
                     X[55]:=1;
            	IF OPA2='B' THEN
                     X[56]:=1;
            	IF OPA2='C' THEN
                     X[57]:=1;
            	IF OPA2='D' THEN
                     X[58]:=1;
            	IF OPA2='E' THEN
                     X[59]:=1;
            	IF OPA2='F' THEN
                     X[60]:=1;
            END;
    END;
END;
PROCEDURE OPITA1;
BEGIN
IF OPA='S' THEN
    BEGIN
	IF OPA1='S' THEN
            BEGIN
            	IF OPA2='A' THEN
                     WRITELN('    Celosia de 2 aletas H-320 BR.      ',X[49]:2:2,'   piezas     14.20     ',(Y[49]):4:2);
            	IF OPA2='B' THEN
                     WRITELN('    Celosia de 3 aletas H-460 BR.      ',X[50]:2:2,'   piezas     18.50     ',(Y[50]):4:2);
            	IF OPA2='C' THEN
                     WRITELN('    Celosia de 4 aletas H-600 BR.      ',X[51]:2:2,'   piezas     22.60     ',(Y[51]):4:2);
            	IF OPA2='D' THEN
                     WRITELN('    Celosia de 5 aletas H-740 BR.      ',X[52]:2:2,'   piezas     26.80     ',(Y[52]):4:2);
            	IF OPA2='E' THEN
                     WRITELN('    Celosia de 6 aletas H-880 BR.      ',X[53]:2:2,'   piezas     31.10     ',(Y[53]):4:2);
            	IF OPA2='F' THEN
                     WRITELN('    Celosia de 7 aletas H-1020 BR.     ',X[54]:2:2,'   piezas     41.00     ',(Y[54]):4:2);
            END
            ELSE
            BEGIN
            	IF OPA2='A' THEN
                     WRITELN('    Celosia de 2 aletas H-320  NAT.    ',X[55]:2:2,'   piezas     12.10     ',(Y[55]):4:2);
            	IF OPA2='B' THEN
                     WRITELN('    Celosia de 3 aletas H-460  NAT.    ',X[56]:2:2,'   piezas     15.50     ',(Y[56]):4:2);
            	IF OPA2='C' THEN
                     WRITELN('    Celosia de 4 aletas H-600  NAT.    ',X[57]:2:2,'   piezas     18.40     ',(Y[57]):4:2);
            	IF OPA2='D' THEN
                     WRITELN('    Celosia de 5 aletas H-740  NAT.    ',X[58]:2:2,'   piezas     21.40     ',(Y[58]):4:2);
            	IF OPA2='E' THEN
                     WRITELN('    Celosia de 6 aletas H-880  NAT.    ',X[59]:2:2,'   piezas     25.30     ',(Y[59]):4:2);
            	IF OPA2='F' THEN
                     WRITELN('    Celosia de 7 aletas H-1020 NAT.    ',X[60]:2:2,'   piezas     35.40     ',(Y[60]):4:2);
            END;
    END;
END;
PROCEDURE MENUSITO;
BEGIN
CLRSCR;
GOTOXY(15,15);
WRITE('EL PA#O FIJO ES CON CELOSIAS ?? [S/N]  :  ');
READLN(OPA);
IF OPA='S' THEN
BEGIN
CLRSCR;
GOTOXY(5,10);
WRITELN;
WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
WRITELN('     ###۲###                                                  ###۲###');
WRITELN('     ###۲### EL COLOR DEL ALUMINIO ES BRONCE ???? [S/N] :     ###۲###');
WRITELN('     ###۲###                                                  ###۲###');
WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
GOTOXY(60,13);
READLN(OPA1);
CLRSCR;
GOTOXY(5,10);
WRITELN;
WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
WRITELN('     ###۲###                                                  ###۲###');
WRITELN('     ###۲###  H-320 = "A"        H-460 = "B"      H-600 = "C" ###۲###');
WRITELN('     ###۲###  H-740 = "D"        H-880 = "E"      H-1020= "F" ###۲###');
WRITELN('     ###۲###                                                  ###۲###');
WRITELN('     ###۲###                   OPCION   :                     ###۲###');
WRITELN('     ###۲###                                                  ###۲###');
WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
GOTOXY(45,16);
READLN(OPA2);
END
ELSE
BEGIN
OPA1:='FLACO';
OPA2:=OPA1;
END;
END;
PROCEDURE PF67;
BEGIN
SUBMENU2;
READLN(OP1);
MENUSITO;
CLRSCR;
IF OP1<>7 THEN
DATOS;
IF OP1=1 THEN
BEGIN
     INI1;
     X[1]:=2*A+2*H;X[18]:=4;X[15]:=32;X[10]:=0;X[19]:=0;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.492*A+1.492*H;
     G1;OPITA;COSTO;SCA;II;
END;
IF OP1=2 THEN
BEGIN
     INI1;
     X[1]:=2*A+4*H;X[18]:=4;X[15]:=36;X[10]:=4;X[19]:=2;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.492*A+2.726*H;
     G2;OPITA;COSTO;SCA;II;
END;
IF OP1=3 THEN
BEGIN
     INI1;
     X[1]:=2*A+6*H;X[18]:=4;X[15]:=40;X[10]:=8;X[19]:=4;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.492*A+3.960*H;
     G3;OPITA;COSTO;SCA;II;
END;
IF OP1=4 THEN
BEGIN
     INI1;
     X[1]:=2*A+8*H;X[18]:=4;X[15]:=44;X[10]:=12;X[19]:=6;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.492*A+5.194*H;
     G4;OPITA;COSTO;SCA;II;
END;
IF OP1=5 THEN
BEGIN
     INI1;
     X[1]:=2*A+10*H;X[18]:=4;X[15]:=48;X[10]:=16;X[19]:=8;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.492*A+6.428*H;
     G5;OPITA;COSTO;SCA;II;
END;
IF OP1=6 THEN
BEGIN
     INI1;
     X[1]:=2*A+12*H;X[18]:=4;X[15]:=52;X[10]:=20;X[19]:=10;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.492*A+7.662*H;
     G6;OPITA;COSTO;SCA;II;
END;
IF OP1<>7 THEN
BEGIN
FOR I:=0 TO 100 DO
BEGIN
     X[I]:=N*X[I];
     Y[I]:=Y[I]*N;
END;
S;
CLRSCR;
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('#########################################################################');
WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
WRITELN('                                PA#O FIJO 67');
WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [pa#o(s)]');
WRITELN('#########################################################################');
WRITELN;
WRITELN('          DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
WRITELN('                                                         ($us)    ($us)');
WRITELN('    Escuadras                          ',X[18]:3:0,'    piezas      0.25     ',(Y[18]):4:2);
WRITELN('    Perfil " U "                       ',X[19]:3:0,'    piezas      0.25     ',(Y[19]):4:2);
WRITELN('    Tornillo de encarne 1(1/2) x 10    ',X[10]:3:0,'    piezas      0.05     ',(Y[10]):4:2);
WRITELN('    Remache poop 4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
WRITELN('    Tacos fisher # 8                   ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
WRITELN('    Tornillo de carpinter#a 2 x 10     ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
WRITELN('    Silicona transparente              ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
OPITA1;
WRITELN('#########################################################################');
WRITE('   TOTAL                                                           ',(CA*N):4:2);
READLN;
END;
END;
PROCEDURE PF75;
BEGIN
SUBMENU2;
READLN(OP1);
MENUSITO;
CLRSCR;
IF OP1<>7 THEN
DATOS;
IF OP1=1 THEN
BEGIN
     INI1;
     X[1]:=2*A+2*H;X[18]:=4;X[15]:=32;X[10]:=0;X[19]:=0;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.594*A+1.594*H;
     G1;OPITA;COSTO;SCA;II;
END;
IF OP1=2 THEN
BEGIN
     INI1;
     X[1]:=2*A+4*H;X[18]:=4;X[15]:=36;X[10]:=4;X[19]:=2;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.594*A+2.979*H;
     G2;OPITA;COSTO;SCA;II;
END;
IF OP1=3 THEN
BEGIN
     INI1;
     X[1]:=2*A+6*H;X[18]:=4;X[15]:=40;X[10]:=8;X[19]:=4;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.594*A+4.359*H;
     G3;OPITA;COSTO;SCA;II;
END;
IF OP1=4 THEN
BEGIN
     INI1;
     X[1]:=2*A+8*H;X[18]:=4;X[15]:=44;X[10]:=12;X[19]:=6;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.594*A+5.745*H;
     G4;OPITA;COSTO;SCA;II;
END;
IF OP1=5 THEN
BEGIN
     INI1;
     X[1]:=2*A+10*H;X[18]:=4;X[15]:=48;X[10]:=16;X[19]:=8;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.594*A+7.123*H;
     G5;OPITA;COSTO;SCA;II;
END;
IF OP1=6 THEN
BEGIN
     INI1;
     X[1]:=2*A+12*H;X[18]:=4;X[15]:=52;X[10]:=20;X[19]:=10;
     X[7]:=INT((A+H)*4);X[6]:=X[7];X[8]:=(2*A+2*H)/20;
     X[0]:=1.594*A+8.505*H;
     G6;OPITA;COSTO;SCA;II;
END;
IF OP1<>7 THEN
BEGIN
FOR I:=0 TO 100 DO
BEGIN
     X[I]:=N*X[I];
     Y[I]:=Y[I]*N;
END;
S;
CLRSCR;
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
WRITELN('                +++++++++++++++++++++++++++++++      -------------');
WRITELN('#########################################################################');
WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
WRITELN('                               PA#O FIJO 75');
WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [pa#o(s)]');
WRITELN('#########################################################################');
WRITELN;
WRITELN(' CODIGO   DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
WRITELN('                                                         ($us)    ($us)');
WRITELN('    Escuadras                          ',X[18]:3:0,'    piezas      0.25     ',(Y[18]):4:2);
WRITELN('    Perfil " U "                       ',X[19]:3:0,'    piezas      0.25     ',(Y[19]):4:2);
WRITELN('    Tornillo de encarne 1(1/2) x 10    ',X[10]:3:0,'    piezas      0.05     ',(Y[10]):4:2);
WRITELN('    Remache poop 4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
WRITELN('    Tacos fisher # 8                   ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
WRITELN('    Tornillo de carpinter#a 2 x 10     ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
WRITELN('    Silicona transparente              ',X[8]:2:2,'    piezas      8.00     ',(Y[8]):4:2);
OPITA1;
WRITELN('#########################################################################');
WRITE('   TOTAL                                                           ',(CA*N):4:2);
READLN;
END;
END;
PROCEDURE PC;
BEGIN
     X[44]:=4;X[28]:=1;X[45]:=1;X[30]:=8;X[31]:=8;X[15]:=32;
     X[32]:=2;X[13]:=4;X[7]:=INT((A+H)*4);X[6]:=X[7];X[18]:=4;
     X[8]:=(2*A+2*H)/20;X[10]:=8;X[1]:=2*A+4*H;X[4]:=4*A+6*H;
     X[0]:=3.488*A+4.711*H;
END;
PROCEDURE PB;
BEGIN
     X[36]:=4;X[37]:=2;X[38]:=2;X[39]:=2;X[40]:=A*H;X[13]:=6;
     X[12]:=2;X[15]:=50;X[18]:=4;X[7]:=INT((A+H)*4);
     X[6]:=X[7];X[8]:=(2*A+2*H)/20;X[0]:=1.929*A+1.929*H;
     X[1]:=2*A+4*H;
END;
PROCEDURE INICIO;
BEGIN
     FOR I:=1 TO 78 DO
         BEGIN
              FOR J:=1 TO 25 DO
                  BEGIN
                       GOTOXY(I,J);
                       WRITE('#');
                       K:=78-I;L:=26-J;
                       GOTOXY(K,L);
                       WRITE('#');
                  END;
         END;
     FOR J:=1 TO 25 DO
         BEGIN
              FOR I:=1 TO 79 DO
                  BEGIN
                       GOTOXY(I,J);
                       WRITE('#');
                  END;
         END;
     GOTOXY(3,3);
     WRITE('Programa para la obtensi#n de cotizaciones y control de egresos');
     GOTOXY(14,4);
     WRITE('de accesorios para aluminio de almac#n');
     GOTOXY(28,10);
     WRITE('RAFAEL ANTEQUERA CABALLERO');
     GOTOXY(32,12);
     WRITE('DERECHOS RESERVADOS');
     GOTOXY(33,14);
     WRITE(' P E R F I L E S ');
     GOTOXY(37,16);WRITE('#########');
     GOTOXY(37,17);WRITE('## RAC ##');
     GOTOXY(37,18);WRITE('#########');
     GOTOXY(26,20);
     WRITE('INGRESE#LA#CLAVE#PARA#CONTINUAR');
     GOTOXY(35,22);
     WRITE('[###########]');
     GOTOXY(36,22);
     READLN(OPA1);
END;
BEGIN (*PROGRAMA PRINCIPAL*)
     CLRSCR;
     INICIO;
     IF OPA1='RAC-555-RAC' THEN
     BEGIN
     INI;CA:=0;MOT:=0;
     REPEAT
     CLRSCR;
     WRITELN;
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN('     ###  INDUSTRIAS MACA Ltda.  ###  | autor : Rafael Antequera Caballero |');
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN;
     WRITELN('              PROGRAMA PARA COTIZACIONES DE TRABAJOS EN ALUMINIO');
     WRITELN('                 Y DE CONTROL INTERNO DE EGRESO DE MERCADERIA');
     WRITELN;
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰######');
     WRITELN('     ####                                                               ####');
     WRITELN('     ####                              MENU                             ####');
     WRITELN('     ####                                                               ####');
     WRITELN('     #### 1.- VENTANA CORREDIZA           7 .- PUERTA CORREDIZA         ####');
     WRITELN('     #### 2.- VENTANA CORREDIZA LIVIANA   8 .- PA#O BA#ERA              ####');
     WRITELN('     #### 3.- MAX - AIR                   9 .- PA#O FIJO " 67 "         ####');
     WRITELN('     #### 4.- CORREDIZA S/6000            10.- PA#O FIJO " 75 "         ####');
     WRITELN('     #### 5.- PUERTA DE ABRIR LIVIANA     11.- RESUMEN                  ####');
     WRITELN('     #### 6.- PUERTA DE ABRIR             12.- SALIR                    ####');
     WRITELN('     ####                                                               ####');
     WRITELN('     ####                                         by R.A.C              ####');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰######');
     WRITELN;
     WRITE('                                 SU OPCION ES :');
     READLN(OP);
     CASE OP OF
     1:VC;
     2:VCST;
     3:BEGIN
            DATOS;
            CLRSCR;
            INI1;
            GOTOXY(5,10);
            WRITELN;
            WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
            WRITELN('     ###۲###                                                  ###۲###');
            WRITELN('     ###۲### EL COLOR DEL ALUMINIO ES BRONCE ???? [S/N] :     ###۲###');
            WRITELN('     ###۲###                                                  ###۲###');
            WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
            GOTOXY(60,13);
            READLN(OPA1);
            CLRSCR;
            GOTOXY(5,10);
            WRITELN;
            WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
            WRITELN('     ###۲###                                                  ###۲###');
            WRITELN('     ###۲### BRAZO DE 30 =  ( A ) ;   BRAZO DE 40 = ( B ) ;   ###۲###');
            WRITELN('     ###۲###                                                  ###۲###');
            WRITELN('     ###۲###                   OPCION   :                     ###۲###');
            WRITELN('     ###۲###                                                  ###۲###');
            WRITELN('     ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۰#');
            GOTOXY(45,15);
            READLN(OPA2);
            IF (OPA1='S') THEN
            IF (OPA2='A') THEN
            X[46]:=1;
            IF (OPA1='S') THEN
            IF (OPA2='B') THEN
            X[48]:=1;
            IF (OPA1='N') THEN
            IF (OPA2='A') THEN
            X[41]:=1;
            IF (OPA1='N') THEN
            IF (OPA2='B') THEN
            X[47]:=1;
            G12;MAX;COSTO;SCA;II;
            FOR I:=0 TO 100 DO
            BEGIN
                 X[I]:=N*X[I];
                 Y[I]:=Y[I]*N;
            END;
            S;
            CLRSCR;
            WRITELN('                +++++++++++++++++++++++++++++++      -------------');
            WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
            WRITELN('                +++++++++++++++++++++++++++++++      -------------');
            WRITELN('#########################################################################');
            WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
            WRITELN('                                MAX AIR');
            WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [ventana(s)]');
            WRITELN('#########################################################################');
            WRITELN;
            WRITELN('          DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
            WRITELN('                                                         ($us)    ($us)');
            WRITELN('   Remache poop 4 x 8                  ',X[17]:3:0,'    piezas      0.05     ',(Y[17]):4:2);
            WRITELN('   Brazo ventilete 30 nat.             ',X[41]:3:0,'    piezas      2.40     ',(Y[41]):4:2);
            WRITELN('   Brazo ventilete 30 br.              ',X[46]:3:0,'    piezas      3.20     ',(Y[46]):4:2);
            WRITELN('   Brazo ventilete 40 nat.             ',X[47]:3:0,'    piezas      2.90     ',(Y[47]):4:2);
            WRITELN('   Brazo ventilete 40 br.              ',X[48]:3:0,'    piezas      3.60     ',(Y[48]):4:2);
            WRITELN('   Bisagra de 2"                       ',X[42]:3:0,'    piezas      0.80     ',(Y[42]):4:2);
            WRITELN('   Perno y tuerca (3/16) x (1/2)       ',X[43]:3:0,'    piezas      0.25     ',(Y[43]):4:2);
            WRITELN('   Tornillo de encarne (1/2) x 8       ',X[14]:3:0,'    piezas      0.05     ',(Y[14]):4:2);
            WRITELN('   Tacos fisher # 8                    ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
            WRITELN('   Tornillo de carpinter#a 2 x 10      ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
            WRITELN('   Silicona transparente               ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
            WRITELN('#########################################################################');
            WRITE('   TOTAL                                                           ',(CA*N):4:2);
            READLN;
       END;
     4:S6000;
     5:BEGIN
            DATOS;
            INI1;
            G13;PAL;COSTO;SCA;II;
            FOR I:=0 TO 100 DO
            BEGIN
                 X[I]:=N*X[I];
                 Y[I]:=Y[I]*N;
            END;
            S;
            CLRSCR;
            WRITELN('                +++++++++++++++++++++++++++++++      -------------');
            WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
            WRITELN('                +++++++++++++++++++++++++++++++      -------------');
            WRITELN('#########################################################################');
            WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
            WRITELN('                          PUERTA DE ABRIR LIVIANA');
            WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [puerta(s)]');
            WRITELN('#########################################################################');
            WRITELN;
            WRITELN('          DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
            WRITELN('                                                         ($us)    ($us)');
            WRITELN('    Cerradura " AN - DIF "             ',X[25]:3:0,'    piezas     13.90     ',(Y[25]):4:2);
            WRITELN('    Picaporte " PLATIL "               ',X[21]:3:0,'    piezas      6.30     ',(Y[21]):4:2);
            WRITELN('    Bisagra liviana " FLAMIA "         ',X[26]:3:0,'    piezas      3.50     ',(Y[26]):4:2);
            WRITELN('    Tornillos de encarne 14 x 1        ',X[11]:3:0,'    piezas      0.05     ',(Y[11]):4:2);
            WRITELN('    Remache poop 4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
            WRITELN('    Escuadras                          ',X[18]:3:0,'    piezas      0.25     ',(Y[18]):4:2);
            WRITELN('    Bolanda de presi#n (1/4)           ',X[27]:3:0,'    piezas      0.05     ',(Y[27]):4:2);
            WRITELN('    Tacos fisher # 8                   ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
            WRITELN('    Tornillos de carpinter#a           ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
            WRITELN('    Silicona transparente              ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
            WRITELN('#########################################################################');
            WRITE('   TOTAL                                                           ',(CA*N):4:2);
            READLN;
       END;
     6:BEGIN
             DATOS;
             INI1;
             G13;PA;COSTO;SCA;II;
             CLRSCR;
             FOR I:=0 TO 100 DO
             BEGIN
                 X[I]:=N*X[I];
                 Y[I]:=Y[I]*N;
             END;
             S;
             CLRSCR;
             WRITELN('                +++++++++++++++++++++++++++++++      -------------');
             WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
             WRITELN('                +++++++++++++++++++++++++++++++      -------------');
             WRITELN('#########################################################################');
             WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
             WRITELN('                             PUERTA DE ABRIR');
             WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [puerta(s)]');
             WRITELN('#########################################################################');
             WRITELN;
             WRITELN(' CODIGO   DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
             WRITELN('                                                         ($us)    ($us)');
             WRITELN('    Cerradura " GIACO "                ',X[20]:3:0,'    piezas     20.00     ',(Y[20]):4:2);
             WRITELN('    Picaporte " PLATIL "               ',X[21]:3:0,'    piezas      6.30     ',(Y[21]):4:2);
             WRITELN('    Bisagra normal  " FLAMIA "         ',X[22]:3:0,'    piezas      5.60     ',(Y[22]):4:2);
             WRITELN('    Remache poop 4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
             WRITELN('    Perno (5/16) x 1                   ',X[23]:3:0,'    piezas      0.25     ',(Y[23]):4:2);
             WRITELN('    Escuadras                          ',X[18]:3:0,'    piezas      0.25     ',(Y[18]):4:2);
             WRITELN('    Bolanda de presi#n (5/16)          ',X[24]:3:0,'    piezas      0.05     ',(Y[24]):4:2);
             WRITELN('    Tacos fisher # 8                   ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
             WRITELN('    Tornillos de carpinter#a           ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
             WRITELN('    Silicona transparente              ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
             WRITELN('#########################################################################');
             WRITE('   TOTAL                                                           ',(CA*N):4:2);
             READLN;
       END;
     7:BEGIN
             DATOS;
             INI1;
             G2;PC;COSTO;SCA;II;
             CLRSCR;
             FOR I:=0 TO 100 DO
             BEGIN
                 X[I]:=N*X[I];
                 Y[I]:=Y[I]*N;
             END;
             S;
             CLRSCR;
             WRITELN('                +++++++++++++++++++++++++++++++      -------------');
             WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
             WRITELN('                +++++++++++++++++++++++++++++++      -------------');
             WRITELN('#########################################################################');
             WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
             WRITELN('                             PUERTA CORREDIZA');
             WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [puerta(s)]');
             WRITELN('#########################################################################');
             WRITELN('          DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
             WRITELN;
             WRITELN('    Rueda de aluminio # 3004           ',X[44]:3:0,'    piezas      0.50     ',(Y[44]):4:2);
             WRITELN('    Aldaba " CHAMICAL "                ',X[28]:3:0,'    piezas      2.30     ',(Y[28]):4:2);
             WRITELN('    Cerradura pico de loro             ',X[45]:3:0,'    piezas     11.20     ',(Y[45]):4:2);
             WRITELN('    Antiruido T-50                     ',X[30]:3:0,'    piezas      0.06     ',(Y[30]):4:2);
             WRITELN('    Tapon tope goma B-26               ',X[31]:3:0,'    piezas      0.03     ',(Y[31]):4:2);
             WRITELN('    Remache poop 4 x 10                ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
             WRITELN('    Jalador de empotrar # 124          ',X[32]:3:0,'    piezas      1.00     ',(Y[32]):4:2);
             WRITELN('    Tornillo de encarne (3/8) x 6      ',X[13]:3:0,'    piezas      0.05     ',(Y[13]):4:2);
             WRITELN('    Tacos fisher # 8                   ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
             WRITELN('    Tornillo de carpinter#a  2 x 10    ',X[6]:3:0,'    piezas      0.05     ',(Y[5]):4:2);
             WRITELN('    Silicona transparente              ',X[8]:2:2,'    piezas      8.00     ',(Y[8]):4:2);
             WRITELN('    Escuadras                          ',X[18]:3:0,'    piezas      0.25     ',(Y[18]):4:2);
             WRITELN('    Tornillo de encarne 1(1/2) x 10    ',X[10]:3:0,'    piezas      0.05     ',(Y[10]):4:2);
             WRITELN('#########################################################################');
             WRITE('   TOTAL                                                           ',(CA*N):4:2);
             READLN;
             END;
     8:BEGIN
             DATOS;
             INI1;
             G14;PB;COSTO;SCA;II;
             FOR I:=0 TO 100 DO
             BEGIN
                 X[I]:=N*X[I];
                 Y[I]:=Y[I]*N;
             END;
             S;
             CLRSCR;
             WRITELN('                +++++++++++++++++++++++++++++++      -------------');
             WRITELN('                ###  INDUSTRIAS MACA Ltda.  ###     | por: R.A.C. |');
             WRITELN('                +++++++++++++++++++++++++++++++      -------------');
             WRITELN('#########################################################################');
             WRITELN('              RESUMEN DE LA CANTIDAD Y EL COSTO DE ACCESORIOS ');
             WRITELN('                               PUERTA BA#ERA');
             WRITELN('     a = ',A:2:2,' [Mt]      h = ',H:2:2,'  [Mt]     N = ',N,'  [puerta(s)]');
             WRITELN('#########################################################################');
             WRITELN;
             WRITELN('          DENOMINACION                 CANT.   UNID.    P.UNIT.   TOTAL');
             WRITELN('                                                         ($us)    ($us)');
             WRITELN('    Rodamiento para duchero  D1        ',X[36]:3:0,'    piezas      1.30     ',(Y[36]):4:2);
             WRITELN('    Patin interior D2                  ',X[37]:3:0,'    piezas      0.08     ',(Y[37]):4:2);
             WRITELN('    Patin exterior D3                  ',X[38]:3:0,'    piezas      0.03     ',(Y[38]):4:2);
             WRITELN('    Porta toallero pl#stico D4         ',X[39]:3:0,'    piezas      0.35     ',(Y[39]):4:2);
             WRITELN('    Acrilico                           ',X[40]:2:2,'   Metros^2   12.44     ',(Y[40]):4:2);
             WRITELN('    Tornillo de encarne (3/8) x 6      ',X[13]:3:0,'    piezas      0.05     ',(Y[13]):4:2);
             WRITELN('    Tornillo de encarne 7 x 1          ',X[12]:3:0,'    piezas      0.05     ',(Y[12]):4:2);
             WRITELN('    Remache poop  4 x 10               ',X[15]:3:0,'    piezas      0.05     ',(Y[15]):4:2);
             WRITELN('    Escuadras                          ',X[18]:3:0,'    piezas      0.25     ',(Y[18]):4:2);
             WRITELN('    Tacos fisher # 8                   ',X[7]:3:0,'    piezas      0.05     ',(Y[7]):4:2);
             WRITELN('    Tornillos de carpinter#a           ',X[6]:3:0,'    piezas      0.05     ',(Y[6]):4:2);
             WRITELN('    Silicona transparente              ',X[8]:2:2,'   piezas      8.00     ',(Y[8]):4:2);
             WRITELN('#########################################################################');
             WRITE('   TOTAL                                                           ',(CA*N):4:2);
             READLN;
             END;
     9:PF67;
     10:PF75;
     11:RESUMEN;
     12:BEGIN
             CLRSCR;
             GOTOXY(5,10);
             WRITELN;
             WRITELN('                  ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲###');
             WRITELN('                  ###۲###                                ###۲###');
             WRITELN('                  ###۲### GRACIAS POR USAR EL PROGRAMA.  ###۲###');
             WRITELN('                  ###۲###                    atte. R.A.C.###۲###');
             WRITELN('                  ###۲##۲##۲##۲##۲##۲##۲##۲##۲##۲##۲###');
             READLN;
        END;
     END;
     UNTIL OP=12;
     END;
END.