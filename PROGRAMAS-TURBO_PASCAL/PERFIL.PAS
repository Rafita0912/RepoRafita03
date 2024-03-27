PROGRAM OPTIMIZAR;
USES CRT,PRINTER;
VAR
AAAA,DESP,ACUM,BA,MED,RACOSO,SUM,RAC4,RAC5,DIF1,DIF2,RAC:REAL;
PASW,QUE,RAC6,RAC1,CH2,TIPO,CH1,CAD:STRING;
CA,KKK,AAA:ARRAY[0..1000]OF REAL;
NBM,CB:ARRAY[0..1000]OF INTEGER;
UY,ACA,CODIGO,OP:INTEGER;
NN,KA,LL,K,A1,I,L,NB,N,RAC2,NUM,RAC7,A,R,C,J,B:LONGINT;
AA,ABC:FILE OF REAL;
BB:FILE OF LONGINT;
POS:FILE OF STRING;
PROCEDURE DATOS;
BEGIN
     CLRSCR;
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN('     ###  INDUSTRIAS MACA Ltda   ###  | autor : Rafael Antequera Caballero |');
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN;
     WRITELN('              ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('              ####                                                    ####');
     WRITELN('              ####            DATOS GENERALES DEL PROBLEMA            ####');
     WRITELN('              ####                                                    ####');
     WRITELN('              ####    IDENTIFICACION O CODIGO DE LA BARRA..:          ####');
     WRITELN('              ####    LONGITUD DE LA BARRA EN METROS.......:          ####');
     WRITELN('              ####    EL DESPERDICIO ACEPTADO EN METROS....:          ####');
     WRITELN('              ####                                                    ####');
     WRITELN('              ####                    by R.A.C                        ####');
     WRITELN('              ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN;
     GOTOXY(62,9);
     READLN(TIPO);
     GOTOXY(62,10);
     READLN(BA);
     GOTOXY(62,11);
     READLN(DESP);
     CLRSCR;
     N:=0;J:=0;
     WRITELN('           A CONTINUACION PROPORCIONAR LOS SIGUIENTES DATOS :');
     WRITELN;
     WRITELN('        ######################################################');
     REPEAT
     J:=J+1;
     WRITE('                  LA MEDIDA [',J,'] EN METROS : ');
     READLN(MED);
     WRITE('                        # DE PIEZAS : ');
     READLN(NN);
     WRITE('                     MAS MEDIDAS ? (S/N) : ');
     READLN(QUE);
     FOR I:=1 TO NN DO
         BEGIN
              N:=N+1;
              AAA[N]:=MED;
         END;
     UNTIL QUE='N';
     NUM:=N;
     ASSIGN(ABC,'C:\PERFIL\RAC\RAC4.RAC');
     REWRITE(ABC);
     CLOSE(ABC);
END;
PROCEDURE ORDENA;
BEGIN
     FOR J:=1 TO (NUM-1) DO
         BEGIN
              I:=1;
              REPEAT
                    IF AAA[I]<AAA[I+1] THEN
                       BEGIN
                            AAAA:=AAA[I+1];
                            AAA[I+1]:=AAA[I];
                            AAA[I]:=AAAA;
                       END;
                    I:=I+1;
              UNTIL I=NUM;
         END;
END;
PROCEDURE CORREGIR;
BEGIN
  ASSIGN(ABC,'C:\PERFIL\RAC\RAC4.RAC');
  RESET(ABC);
  FOR I:=1 TO NUM DO
    BEGIN
         SEEK(ABC,I);
         WRITE(ABC,AAA[I]);
    END;
    RAC:=0;
    SEEK(ABC,NUM+1);
    WRITE(ABC,RAC);
    AAA[NUM+1]:=0;
     REPEAT
     CLRSCR;
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN('     ###  INDUSTRIAS MACA Ltda   ###  | autor : Rafael Antequera Caballero |');
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN;
     WRITELN('                               OPCIONES DE MODIFICACION');
     WRITELN;
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰###                                                ###۰##۰###');
     WRITELN('     ###۰##۰###                      MENU                      ###۰##۰###');
     WRITELN('     ###۰##۰###                                                ###۰##۰###');
     WRITELN('     ###۰##۰###           1 . - BORRAR DATOS                   ###۰##۰###');
     WRITELN('     ###۰##۰###           2 . - COMPROBAR Y MODIFICAR DATOS    ###۰##۰###');
     WRITELN('     ###۰##۰###           3 . - A#ADIR MAS DATOS               ###۰##۰###');
     WRITELN('     ###۰##۰###           4 . - SALIR AL MENU PRINCIPAL        ###۰##۰###');
     WRITELN('     ###۰##۰###                                                ###۰##۰###');
     WRITELN('     ###۰##۰###                                      by R.A.C  ###۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN;
     WRITE('                                 SU OPCION ES :');
     READLN(OP);
     CASE OP OF
     1:BEGIN
       CLRSCR;
       WRITELN;WRITELN;
       GOTOXY(15,5);
       WRITELN('LOS DATOS DE ESTE PROBLEMA SON LOS SIGUIENTES ...  ');
       WRITELN;
       I:=1;
       REPEAT
               SEEK(ABC,I);
               READ(ABC,RAC);
               WRITE('              LA MEDIDA No. ',I,'  ES :  ',RAC:2:3,'   DESEA BORRARLA ? (S/N)  ');
               READLN(QUE);
               I:=I+1;
               IF QUE='S' THEN
                  BEGIN
                       I:=I-1;
                       FOR J:=I TO NUM DO
                           BEGIN
                                SEEK(ABC,J+1);
                                READ(ABC,RAC4);
                                RAC:=RAC4;
                                SEEK(ABC,J);
                                WRITE(ABC,RAC);
                                AAA[J]:=AAA[J+1];
                           END;
                       NUM:=NUM-1;
                  END;
       UNTIL I=NUM+1;
       FOR I:=1 TO NUM DO
           BEGIN
                SEEK(ABC,I);
                READ(ABC,RAC);
                AAA[I]:=RAC;
           END;
       FOR I:=1 TO NUM DO
           BEGIN
                SEEK(ABC,I);
                RAC:=AAA[I];
                WRITE(ABC,RAC);
           END;
       N:=NUM;
       END;
       2:BEGIN
       CLRSCR;
       WRITELN;WRITELN;
       GOTOXY(15,5);
       WRITELN('LOS DATOS DE ESTE PROBLEMA SON LOS SIGUIENTES ...  ');
       WRITELN;
       FOR I:=1 TO NUM DO
           BEGIN
               SEEK(ABC,I);
               READ(ABC,RAC);
               WRITE('              LA MEDIDA No. ',I,'  ES :  ',RAC:2:3,'   DESEA MODIFICARLA ? (S/N)  ');
               READLN(QUE);
               IF QUE='S' THEN
                  BEGIN
                       WRITE('                       CUAL ES EL NUEVO VALOR   :    ');
                       READLN(RAC);
                       SEEK(ABC,I);
                       WRITE(ABC,RAC);
                  END;
           END;
       FOR I:=1 TO NUM DO
           BEGIN
                SEEK(ABC,I);
                READ(ABC,RAC);
                AAA[I]:=RAC;
           END;
       FOR I:=1 TO NUM DO
           BEGIN
                SEEK(ABC,I);
                RAC:=AAA[I];
                WRITE(ABC,RAC);
           END;
       N:=NUM;
       END;
     3:BEGIN
       CLRSCR;
       J:=NUM;
       N:=J;
       REPEAT
       J:=J+1;
       WRITE('                  LA MEDIDA [',J,'] EN METROS : ');
       READLN(MED);
       WRITE('                        # DE PIEZAS : ');
       READLN(NN);
       WRITE('                     MAS MEDIDAS ? (S/N) : ');
       READLN(QUE);
       FOR I:=1 TO NN DO
           BEGIN
                N:=N+1;
                AAA[N]:=MED;
           END;
       UNTIL QUE='N';
       NUM:=N;
       FOR I:=1 TO NUM DO
           BEGIN
                SEEK(ABC,I);
                RAC:=AAA[I];
                WRITE(ABC,RAC);
           END;
       N:=NUM;
       RAC:=0;
       SEEK(ABC,NUM+1);
       WRITE(ABC,RAC);
       AAA[NUM+1]:=0;
     END;
     END;
     UNTIL OP=4
END;
PROCEDURE OPTIMIZA;
BEGIN
     ACA:=0;
     K:=0;
     NB:=0;
     REPEAT
     NB:=NB+1;
     CLRSCR;
     GOTOXY(20,13);
     WRITELN('PROCESANDO INFORMACION');
     ASSIGN(AA,'C:\PERFIL\RAC\RAC1.RAC');
     ASSIGN(BB,'C:\PERFIL\RAC\RAC2.RAC');
     ASSIGN(POS,'C:\PERFIL\RAC\RAC3.RAC');
     REWRITE(AA);
     REWRITE(BB);
     REWRITE(POS);
     FOR I:=1 TO N DO
         BEGIN
              RAC:=ABS(AAA[I]);
              SEEK(AA,I);
              WRITE(AA,RAC);
              RAC2:=I+1;
              SEEK(BB,I);
              WRITE(BB,RAC2);
              STR(I,CAD);
              RAC1:=CONCAT(CAD,',');
              SEEK(POS,I);
              WRITE(POS,RAC1);
         END;
     A:=1;
     B:=N;
     R:=0;
     C:=0;
     REPEAT
     ACUM:=1000;
     FOR I:=A TO B DO
         BEGIN
              SEEK(BB,I);READ(BB,RAC7);
              IF RAC7<=N THEN
              BEGIN
              FOR J:=RAC7 TO N DO
                  BEGIN
                       SEEK(AA,I);READ(AA,RAC);
                       RAC4:=RAC;
                       SEEK(AA,J);READ(AA,RAC);
                       RAC5:=RAC;
                       RAC:=RAC4+RAC5;
                       IF RAC<=BA THEN
                       BEGIN
                         IF (BA-RAC)<ACUM THEN
                            BEGIN
                                 ACUM:=BA-RAC;
                                 R:=R+1;
                                 STR(J,CAD);
                                 SEEK(BB,N+R);
                                 RAC2:=J+1;
                                 WRITE(BB,RAC2);
                                 SEEK(AA,N+R); WRITE(AA,RAC);
                                 SEEK(POS,I);READ(POS,RAC1);
                                 RAC1:=CONCAT(RAC1,CAD,',');
                                 SEEK(POS,N+R);WRITE(POS,RAC1);
                                 WRITELN('                           ####  ',RAC1,'    ');
                            END;
                       END;
                       IF ((BA-RAC)>=0) AND ((BA-RAC)<=DESP) THEN
                          BEGIN
                               J:=N;I:=B;
                          END;
                  END;
              END;
         END;
     A:=B+1;
     B:=N+R;
     C:=C+1;
     IF ((BA-RAC)>=0) AND ((BA-RAC)<=DESP) THEN
        BEGIN
             J:=N;I:=B;
             C:=N-1;
        END;
     UNTIL C=N-1;
     WRITELN;WRITELN;WRITELN;
     WRITELN('        OPTIMIZACION SEMICONCLUIDA PRESIONE [ENTER] PARA CONTINUAR');
     WRITELN;WRITELN;WRITELN;
     READLN;
     CLRSCR;
     SEEK(POS,1);
     READ(POS,RAC1);
     SEEK(AA,1);
     READ(AA,RAC);
     DIF1:=BA-RAC;
     FOR I:=2 TO R+N DO
         BEGIN
              SEEK(POS,I);
              READ(POS,PASW);
              SEEK(AA,I);
              READ(AA,RAC5);
              DIF2:=BA-RAC5;
              IF RAC>RAC5 THEN
                 BEGIN
                      RACOSO:=RAC;
                      CAD:=RAC1;
                 END
              ELSE
                  BEGIN
                      RACOSO:=RAC5;
                      CAD:=PASW;
                      RAC:=RAC5;
                      RAC1:=PASW;
                  END;
         END;
     CLRSCR;
     RACOSO:=BA-RACOSO;
     WRITELN('               #################################');
     GOTOXY(10,5);
     WRITELN('     PERFIL CODIGO  ',TIPO,'  BARRA   #   :   ',NB);
     GOTOXY(10,7);
     WRITELN('              DE LONGITUD  =  ',BA:2:2,' [mt]');
     GOTOXY(10,10);
     WRITELN('EL CORTE DE LA BARRA CON UN DESPERDICIO DE ',RACOSO:1:3,' [mt]');
     GOTOXY(15,11);
     WRITE('       ES DE LAS MEDIDAS SIGUIENTES');
     CLOSE(AA);CLOSE(BB);CLOSE(POS);
     L:=LENGTH(CAD);
     I:=0;
     REPEAT
     CH2:='';
     REPEAT
              CH1:=COPY(CAD,1,1);
              IF (CH1<>',') THEN
                 BEGIN
                 IF (CH1<>'') THEN
                 BEGIN
                 CH2:=CONCAT(CH2,CH1);
                 DELETE(CAD,1,1);
                 END;
                 END
              ELSE
                  BEGIN
                  DELETE(CAD,1,1);
                  END;
     UNTIL (CH1=',') OR (CH1='');
     I:=I+1;
     VAL(CH2,CA[I],CODIGO);
     CB[I]:=TRUNC(CA[I])
     UNTIL CAD='';
     N:=I;
     WRITELN;WRITELN;
     FOR I:=1 TO N DO
         BEGIN
              ACA:=ACA+1;
              NBM[ACA]:=NB;
              K:=K+1;
              WRITELN('                LA MEDIDA A CORTAR ES : ',AAA[CB[I]]:2:3,' [mt]');
              KKK[K]:=AAA[CB[I]];
         END;
     WRITELN;WRITELN;
     WRITELN('                        optimizado por R.A.C.');
     READLN;
     KA:=0;
     FOR I:=1 TO N DO
         BEGIN
              L:=CB[I];
              FOR J:=L-KA TO NUM DO
                  BEGIN
                       AAA[J]:=AAA[J+1];
                  END;
              KA:=KA+1;
              NUM:=NUM-1;
         END;
     N:=NUM;
     SUM:=0;
     FOR I:=1 TO N DO
         SUM:=SUM+AAA[I];
     NUM:=N;
     UNTIL SUM<=BA;
     IF SUM<>0 THEN
     BEGIN
     CLRSCR;
     NB:=NB+1;
     GOTOXY(10,5);
     WRITELN('      PERFIL CODIGO   ',TIPO,'  BARRA   #   :   ',NB);
     GOTOXY(10,7);
     WRITELN('               DE LONGITUD  =  ',BA:2:2,' [mt]');
     GOTOXY(10,10);
     WRITELN('EL CORTE DE LA BARRA CON UN DESPERDICIO DE ',(BA-SUM):1:3,' [mt]');
     GOTOXY(15,11);
     WRITE('      ES DE LAS MEDIDAS SIGUIENTES');
     WRITELN;WRITELN;
     FOR I:=1 TO N DO
         BEGIN
              ACA:=ACA+1;
              NBM[ACA]:=NB;
              K:=K+1;
              WRITELN('                  LA MEDIDA A CORTAR ES : ',AAA[I]:2:3,' [mt]');
              KKK[K]:=AAA[I];
         END;
     WRITELN;WRITELN;
     WRITELN('                        optimizado por R.A.C.');
     READLN;
     CLRSCR;
     WRITELN;WRITELN;
     WRITELN('               EL NUMERO OPTIMO DE BARRAS A CORTAR ES :  ',NB);
     WRITELN;
     WRITELN('                           DEL PERFIL   ',TIPO);
     WRITELN;
     WRITELN('                          DE LONGITUD  =  ',BA:2:2,' [mt]');
     WRITELN;WRITELN;
     WRITELN('              Y EL ORDEN EN EL QUE SE DEBEN CORTAR LAS MEDIDAS,');
     WRITELN('                           ES EL SIGUIENTE:');
     WRITELN;WRITELN;
     FOR I:=1 TO K DO
         WRITELN('           EL CORTE  ',I,'  DE LA BARRA  ',NBM[I],'  DEBE SER  :  ',KKK[I]:2:3);
     WRITELN;WRITELN;
     WRITELN('                         optimizado por R.A.C.');
     END;
     FOR I:=1 TO K DO
     BEGIN
          AAA[I]:=KKK[I];
     END;
     NUM:=I;
     READLN;
END;
PROCEDURE OPTIMIZA2;
BEGIN
     ACA:=0;
     K:=0;
     NB:=0;
     REPEAT
     NB:=NB+1;
     CLRSCR;
     GOTOXY(20,13);
     WRITELN('PROCESANDO INFORMACION');
     ASSIGN(AA,'C:\PERFIL\RAC\RAC1.RAC');
     ASSIGN(BB,'C:\PERFIL\RAC\RAC2.RAC');
     ASSIGN(POS,'C:\PERFIL\RAC\RAC3.RAC');
     REWRITE(AA);
     REWRITE(BB);
     REWRITE(POS);
     FOR I:=1 TO N DO
         BEGIN
              RAC:=ABS(AAA[I]);
              SEEK(AA,I);
              WRITE(AA,RAC);
              RAC2:=I+1;
              SEEK(BB,I);
              WRITE(BB,RAC2);
              STR(I,CAD);
              RAC1:=CONCAT(CAD,',');
              SEEK(POS,I);
              WRITE(POS,RAC1);
         END;
     A:=1;
     B:=N;
     R:=0;
     C:=0;
     REPEAT
     ACUM:=1000;
     FOR I:=A TO B DO
         BEGIN
              SEEK(BB,I);READ(BB,RAC7);
              IF RAC7<=N THEN
              BEGIN
              FOR J:=RAC7 TO N DO
                  BEGIN
                       SEEK(AA,I);READ(AA,RAC);
                       RAC4:=RAC;
                       SEEK(AA,J);READ(AA,RAC);
                       RAC5:=RAC;
                       RAC:=RAC4+RAC5;
                       IF RAC<=BA THEN
                       BEGIN
                         IF (BA-RAC)<ACUM THEN
                            BEGIN
                                 ACUM:=BA-RAC;
                                 R:=R+1;
                                 STR(J,CAD);
                                 SEEK(BB,N+R);
                                 RAC2:=J+1;
                                 WRITE(BB,RAC2);
                                 SEEK(AA,N+R); WRITE(AA,RAC);
                                 SEEK(POS,I);READ(POS,RAC1);
                                 RAC1:=CONCAT(RAC1,CAD,',');
                                 SEEK(POS,N+R);WRITE(POS,RAC1);
                                 WRITELN('                           ####  ',RAC1,'    ');
                            END;
                       END;
                       IF ((BA-RAC)>=0) AND ((BA-RAC)<=DESP) THEN
                          BEGIN
                               J:=N;I:=B;
                          END;
                  END;
              END;
         END;
     A:=B+1;
     B:=N+R;
     C:=C+1;
     IF ((BA-RAC)>=0) AND ((BA-RAC)<=DESP) THEN
        BEGIN
             J:=N;I:=B;
             C:=N-1;
        END;
     UNTIL C=N-1;
     CLRSCR;
     SEEK(POS,1);
     READ(POS,RAC1);
     SEEK(AA,1);
     READ(AA,RAC);
     DIF1:=BA-RAC;
     FOR I:=2 TO R+N DO
         BEGIN
              SEEK(POS,I);
              READ(POS,PASW);
              SEEK(AA,I);
              READ(AA,RAC5);
              DIF2:=BA-RAC5;
              IF RAC>RAC5 THEN
                 BEGIN
                      RACOSO:=RAC;
                      CAD:=RAC1;
                 END
              ELSE
                  BEGIN
                      RACOSO:=RAC5;
                      CAD:=PASW;
                      RAC:=RAC5;
                      RAC1:=PASW;
                  END;
         END;
     CLRSCR;
     RACOSO:=BA-RACOSO;
     CLOSE(AA);CLOSE(BB);CLOSE(POS);
     L:=LENGTH(CAD);
     I:=0;
     REPEAT
     CH2:='';
     REPEAT
              CH1:=COPY(CAD,1,1);
              IF (CH1<>',') THEN
                 BEGIN
                 IF (CH1<>'') THEN
                 BEGIN
                 CH2:=CONCAT(CH2,CH1);
                 DELETE(CAD,1,1);
                 END;
                 END
              ELSE
                  BEGIN
                  DELETE(CAD,1,1);
                  END;
     UNTIL (CH1=',') OR (CH1='');
     I:=I+1;
     VAL(CH2,CA[I],CODIGO);
     CB[I]:=TRUNC(CA[I])
     UNTIL CAD='';
     N:=I;
     WRITELN;WRITELN;
     FOR I:=1 TO N DO
         BEGIN
              ACA:=ACA+1;
              NBM[ACA]:=NB;
              K:=K+1;
              KKK[K]:=AAA[CB[I]];
         END;
     KA:=0;
     FOR I:=1 TO N DO
         BEGIN
              L:=CB[I];
              FOR J:=L-KA TO NUM DO
                  BEGIN
                       AAA[J]:=AAA[J+1];
                  END;
              KA:=KA+1;
              NUM:=NUM-1;
         END;
     N:=NUM;
     SUM:=0;
     FOR I:=1 TO N DO
         SUM:=SUM+AAA[I];
     NUM:=N;
     UNTIL SUM<=BA;
     IF SUM<>0 THEN
     BEGIN
     CLRSCR;
     NB:=NB+1;
     FOR I:=1 TO N DO
         BEGIN
              ACA:=ACA+1;
              NBM[ACA]:=NB;
              K:=K+1;
              KKK[K]:=AAA[I];
         END;
     CLRSCR;
     END;
     FOR I:=1 TO K DO
     BEGIN
          AAA[I]:=KKK[I];
     END;
     NUM:=I;
END;
PROCEDURE IMPRIMIR;
BEGIN
     CLRSCR;
     GOTOXY(15,15);
     WRITELN('EN ESTE MOMENTO SE IMPRIME LA INFORMACION.  ESPERE');
     WRITELN(LST);
     WRITELN(LST,'             EL NUMERO OPTIMO DE BARRAS A CORTAR ES :  ',NB);
     WRITELN(LST);
     WRITELN(LST,'                         DEL PERFIL   ',TIPO);
     WRITELN(LST);
     WRITELN(LST,'                        DE LONGITUD  =  ',BA:2:2,' [mt]');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'            Y EL ORDEN EN EL QUE SE DEBEN CORTAR LAS MEDIDAS,');
     WRITELN(LST,'                           ES EL SIGUIENTE:');
     WRITELN(LST);WRITELN(LST);
     FOR I:=1 TO K DO
     WRITELN(LST,'             EL CORTE  ',I,'  DE LA BARRA   ',NBM[I],'  DEBE SER  :  ',KKK[I]:2:3);
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                         optimizado por R.A.C.');
     READLN;
END;
PROCEDURE OPTIMIZA1;
BEGIN
     ACA:=0;
     K:=0;
     NB:=0;
     REPEAT
     NB:=NB+1;
     CLRSCR;
     GOTOXY(20,13);
     WRITELN('PROCESANDO INFORMACION');
     ASSIGN(AA,'C:\PERFIL\RAC\RAC1.RAC');
     ASSIGN(BB,'C:\PERFIL\RAC\RAC2.RAC');
     ASSIGN(POS,'C:\PERFIL\RAC\RAC3.RAC');
     REWRITE(AA);
     REWRITE(BB);
     REWRITE(POS);
     FOR I:=1 TO N DO
         BEGIN
              RAC:=ABS(AAA[I]);
              SEEK(AA,I);
              WRITE(AA,RAC);
              RAC2:=I+1;
              SEEK(BB,I);
              WRITE(BB,RAC2);
              STR(I,CAD);
              RAC1:=CONCAT(CAD,',');
              SEEK(POS,I);
              WRITE(POS,RAC1);
         END;
     A:=1;
     B:=N;
     R:=0;
     C:=0;
     REPEAT
     ACUM:=1000;
     FOR I:=A TO B DO
         BEGIN
              SEEK(BB,I);READ(BB,RAC7);
              IF RAC7<=N THEN
              BEGIN
              FOR J:=RAC7 TO N DO
                  BEGIN
                       SEEK(AA,I);READ(AA,RAC);
                       RAC4:=RAC;
                       SEEK(AA,J);READ(AA,RAC);
                       RAC5:=RAC;
                       RAC:=RAC4+RAC5;
                       IF RAC<=BA THEN
                       BEGIN
                         IF (BA-RAC)<ACUM THEN
                            BEGIN
                                 ACUM:=BA-RAC;
                                 R:=R+1;
                                 STR(J,CAD);
                                 SEEK(BB,N+R);
                                 RAC2:=J+1;
                                 WRITE(BB,RAC2);
                                 SEEK(AA,N+R); WRITE(AA,RAC);
                                 SEEK(POS,I);READ(POS,RAC1);
                                 RAC1:=CONCAT(RAC1,CAD,',');
                                 SEEK(POS,N+R);WRITE(POS,RAC1);
                                 WRITELN('                           ####  ',RAC1,'    ');
                            END;
                       END;
                       IF ((BA-RAC)>=0) AND ((BA-RAC)<=DESP) THEN
                          BEGIN
                               J:=N;I:=B;
                          END;
                  END;
              END;
         END;
     A:=B+1;
     B:=N+R;
     C:=C+1;
     IF ((BA-RAC)>=0) AND ((BA-RAC)<=DESP) THEN
        BEGIN
             J:=N;I:=B;
             C:=N-1;
        END;
     UNTIL C=N-1;
     CLRSCR;
     SEEK(POS,1);
     READ(POS,RAC1);
     SEEK(AA,1);
     READ(AA,RAC);
     DIF1:=BA-RAC;
     FOR I:=2 TO R+N DO
         BEGIN
              SEEK(POS,I);
              READ(POS,PASW);
              SEEK(AA,I);
              READ(AA,RAC5);
              DIF2:=BA-RAC5;
              IF RAC>RAC5 THEN
                 BEGIN
                      RACOSO:=RAC;
                      CAD:=RAC1;
                 END
              ELSE
                  BEGIN
                      RACOSO:=RAC5;
                      CAD:=PASW;
                      RAC:=RAC5;
                      RAC1:=PASW;
                  END;
         END;
     RACOSO:=BA-RACOSO;
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                    #################################');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                PERFIL CODIGO  ',TIPO,'  BARRA   #   :   ',NB);
     WRITELN(LST);
     WRITELN(LST,'                          DE LONGITUD  =  ',BA:2:2,' [mt]');
     WRITELN(LST);
     WRITELN(LST,'           EL CORTE DE LA BARRA CON UN DESPERDICIO DE ',RACOSO:1:3,' [mt]');
     WRITELN(LST);
     WRITELN(LST,'                      ES DE LAS MEDIDAS SIGUIENTES');
     CLOSE(AA);CLOSE(BB);CLOSE(POS);
     L:=LENGTH(CAD);
     I:=0;
     REPEAT
     CH2:='';
     REPEAT
              CH1:=COPY(CAD,1,1);
              IF (CH1<>',') THEN
                 BEGIN
                 IF (CH1<>'') THEN
                 BEGIN
                 CH2:=CONCAT(CH2,CH1);
                 DELETE(CAD,1,1);
                 END;
                 END
              ELSE
                  BEGIN
                  DELETE(CAD,1,1);
                  END;
     UNTIL (CH1=',') OR (CH1='');
     I:=I+1;
     VAL(CH2,CA[I],CODIGO);
     CB[I]:=TRUNC(CA[I])
     UNTIL CAD='';
     N:=I;
     WRITELN(LST);WRITELN(LST);
     FOR I:=1 TO N DO
         BEGIN
              ACA:=ACA+1;
              NBM[ACA]:=NB;
              K:=K+1;
              WRITELN(LST,'                    LA MEDIDA A CORTAR ES : ',AAA[CB[I]]:2:3,' [mt]');
              KKK[K]:=AAA[CB[I]];
         END;
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                        optimizado por R.A.C.');
     KA:=0;
     FOR I:=1 TO N DO
         BEGIN
              L:=CB[I];
              FOR J:=L-KA TO NUM DO
                  BEGIN
                       AAA[J]:=AAA[J+1];
                  END;
              KA:=KA+1;
              NUM:=NUM-1;
         END;
     N:=NUM;
     SUM:=0;
     FOR I:=1 TO N DO
         SUM:=SUM+AAA[I];
     NUM:=N;
     UNTIL SUM<=BA;
     IF SUM<>0 THEN
     BEGIN
     NB:=NB+1;
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                 #################################');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                 PERFIL CODIGO   ',TIPO,'  BARRA   #   :   ',NB);
     WRITELN(LST);
     WRITELN(LST,'                          DE LONGITUD  =  ',BA:2:2,' [mt]');
     WRITELN(LST);
     WRITELN(LST,'           EL CORTE DE LA BARRA CON UN DESPERDICIO DE ',(BA-SUM):1:3,' [mt]');
     WRITELN(LST);
     WRITELN(LST,'                      ES DE LAS MEDIDAS SIGUIENTES');
     WRITELN(LST);WRITELN(LST);
     FOR I:=1 TO N DO
         BEGIN
              ACA:=ACA+1;
              NBM[ACA]:=NB;
              K:=K+1;
              WRITELN(LST,'                    LA MEDIDA A CORTAR ES : ',AAA[I]:2:3,' [mt]');
              KKK[K]:=AAA[I];
         END;
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                        optimizado por R.A.C.');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                 #################################');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'               EL NUMERO OPTIMO DE BARRAS A CORTAR ES :  ',NB);
     WRITELN(LST);
     WRITELN(LST,'                           DEL PERFIL   ',TIPO);
     WRITELN(LST);
     WRITELN(LST,'                          DE LONGITUD  =  ',BA:2:2,' [mt]');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'              Y EL ORDEN EN EL QUE SE DEBEN CORTAR LAS MEDIDAS,');
     WRITELN(LST,'                           ES EL SIGUIENTE:');
     WRITELN(LST);WRITELN(LST);
     FOR I:=1 TO K DO
     WRITELN(LST,'               EL CORTE  ',I,'  DE LA BARRA   ',NBM[I],'   DEBE SER  :  ',KKK[I]:2:3);
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                         optimizado por R.A.C.');
     WRITELN(LST);WRITELN(LST);
     WRITELN(LST,'                 #################################');
     END;
     FOR I:=1 TO K DO
     BEGIN
          AAA[I]:=KKK[I];
     END;
     NUM:=I;
     READLN;
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
     WRITE('Programa para optimizar cortes de barras');
     GOTOXY(28,10);
     WRITE('RAFAEL ANTEQUERA CABALLERO');
     GOTOXY(32,12);
     WRITE('DERECHOS RESERVADOS');
     GOTOXY(35,14);
     WRITE(' P E R F I L ');
     GOTOXY(37,16);WRITE('#########');
     GOTOXY(37,17);WRITE('## RAC ##');
     GOTOXY(37,18);WRITE('#########');
     GOTOXY(26,20);
     WRITE('INGRESE#LA#CLAVE#PARA#CONTINUAR');
     GOTOXY(35,22);
     WRITE('[###########]');
     GOTOXY(36,22);
     READLN(PASW);
END;
BEGIN
     CLRSCR;
     INICIO;
     IF PASW='RAC-666-RAC' THEN
     BEGIN
     REPEAT
     CLRSCR;
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN('     ###  INDUSTRIAS MACA Ltda   ###  | autor : Rafael Antequera Caballero |');
     WRITELN('     +++++++++++++++++++++++++++++++  --------------------------------------');
     WRITELN;
     WRITELN('            PROGRAMA PARA OPTIMIZACION DE CORTES DE BARRAS O PERFILES');
     WRITELN;
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰###                                                ###۰##۰###');
     WRITELN('     ###۰##۰###                      MENU                      ###۰##۰###');
     WRITELN('     ###۰##۰###                                                ###۰##۰###');
     WRITELN('     ###۰##۰###      1 . - INTRODUCIR DATOS                    ###۰##۰###');
     WRITELN('     ###۰##۰###      2 . - MODIFICAR DATOS                     ###۰##۰###');
     WRITELN('     ###۰##۰###      3 . - PROCESAR PASO A PASO Y NO IMPRIMIR  ###۰##۰###');
     WRITELN('     ###۰##۰###      4 . - PROCESAR E IMPRIMIR TODO            ###۰##۰###');
     WRITELN('     ###۰##۰###      5 . - PROCESAR E IMPRIMIR SOLO EL RESUMEN ###۰##۰###');
     WRITELN('     ###۰##۰###      6 . - IMPRIMIR RESUMEN (solo si ya fu#    ###۰##۰###');
     WRITELN('     ###۰##۰###         procesada la informaci#n anteriormente)###۰##۰###');
     WRITELN('     ###۰##۰###      7 . - SALIR                               ###۰##۰###');
     WRITELN('     ###۰##۰###                                      by R.A.C  ###۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('     ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN;
     WRITE('                                 SU OPCION ES :');
     READLN(OP);
     CASE OP OF
     1:DATOS;
     2:CORREGIR;
     3:BEGIN
       ORDENA;
       OPTIMIZA;
       END;
     4:BEGIN
       ORDENA;
       OPTIMIZA1;
       END;
     5:BEGIN
            ORDENA;
            OPTIMIZA2;
            IMPRIMIR;
       END;
     6:IMPRIMIR;
     7:BEGIN
            CLRSCR;
     WRITELN;WRITELN;WRITELN;WRITELN;WRITELN;
     WRITELN;WRITELN;WRITELN;WRITELN;WRITELN;
     WRITELN('             ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('             ####                                                ####');
     WRITELN('             ####     GRACIAS POR HACER USO DE ESTE PROGRAMA     ####');
     WRITELN('             ####                         atte   R.A.C.          ####');
     WRITELN('             ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN;
       END;
     END;
     UNTIL OP=7
     END
     ELSE
     BEGIN
     CLRSCR;
     WRITELN;WRITELN;WRITELN;WRITELN;WRITELN;
     WRITELN;WRITELN;WRITELN;WRITELN;WRITELN;
     WRITELN('             ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN('             ####                                                ####');
     WRITELN('             #### ESTE PROGRAMA ES PRIVADO, POR FAVOR NO MOLESTE ####');
     WRITELN('             ####                         atte   R.A.C.          ####');
     WRITELN('             ###۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰##۰###');
     WRITELN;
     END;
READLN;
END.
