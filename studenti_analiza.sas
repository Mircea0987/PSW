/* ============================================================
   ANALIZA DATE STUDENTI
   Acoperire cerinte:
     1. Crearea unui set de date SAS din fisiere externe
     2. Formate definite de utilizator
     3. Procesare iterativa si conditionala
     4. Crearea de subseturi de date
     5. Functii SAS
     6. Combinarea seturilor de date (SET, MERGE, SQL)
     7. Masive (ARRAY)
     8. Proceduri pentru raportare
     9. Proceduri statistice
    10. Generare grafice
   ============================================================ */


/* ============================================================
   1. CREAREA SETULUI DE DATE DIN FISIER EXTERN
   ============================================================ */

FILENAME stud "/home/u64505469/Calugaru.Mircea-Costin/data/student-scores.csv";

DATA WORK.studenti;
    LENGTH 
        first_name $ 30
        last_name $ 30
        email $ 50
        gender $ 10
        part_time_job $ 5
        extracurricular $ 5
        career_aspiration $ 30;

    INFILE stud FIRSTOBS=2 DSD TRUNCOVER;

    INPUT
        id
        first_name $
        last_name $
        email $
        gender $
        part_time_job $
        absence_days
        extracurricular $
        weekly_self_study_hours
        career_aspiration $
        math_score
        history_score
        physics_score
        chemistry_score
        biology_score
        english_score
        geography_score;
RUN;

PROC PRINT DATA=WORK.studenti(OBS=10); 
    TITLE "Student Data Read Successfully"; 
RUN;



/* ============================================================
   2. FORMATE DEFINITE DE UTILIZATOR
   ============================================================ */

PROC FORMAT;
    /* Format pentru gen (character) */
    VALUE $GENDER_FMT
        'male'   = 'Masculin'
        'female' = 'Feminin'
        OTHER    = 'Necunoscut';

    /* Format pentru aspiratia in cariera */
    VALUE $CAREER_FMT
        'Doctor'           = 'Medic'
        'Lawyer'           = 'Avocat'
        'Software Engineer'= 'Inginer Software'
        'Teacher'          = 'Profesor'
        'Artist'           = 'Artist'
        'Government Officer'= 'Functionar Public'
        'Unknown'          = 'Nedefinit';

    /* Format numeric pentru scor mediu -> calificativ */
    VALUE GRADE_FMT
        0  -< 65 = 'Insuficient'
        65   -< 75 = 'Satisfacator'
        75   -< 85 = 'Bine'
        85   -< 92 = 'Foarte Bine'
        92   - HIGH= 'Excelent';

    /* Format pentru absente */
    VALUE ABS_FMT
        0    -  2  = 'Prezenta buna'
        3    -  5  = 'Absente moderate'
        6    - HIGH= 'Absente ridicate';
RUN;

/* Aplicare formate pe setul de date */
DATA WORK.studenti;
    SET WORK.studenti;
    FORMAT gender        $GENDER_FMT.
           career_aspiration $CAREER_FMT.
           absence_days  ABS_FMT.;
RUN;

PROC PRINT DATA=WORK.studenti (OBS=5);
    TITLE "2. Formate definite de utilizator - primele 5 observatii";
RUN;


/* ============================================================
   3. PROCESARE ITERATIVA SI CONDITIONALA
   ============================================================ */


DATA WORK.studenti_procesati;
    SET WORK.studenti;
    
    LENGTH calificativ $ 15;


    avg_score = MEAN(math_score, history_score, physics_score,
                     chemistry_score, biology_score,
                     english_score, geography_score);
              
    avg_score = ROUND(avg_score, 0.01);

    total_score = SUM(math_score, history_score, physics_score,
                      chemistry_score, biology_score,
                      english_score, geography_score);

    /* Procesare CONDITIONALA: calificativ */
    IF avg_score >= 92 THEN calificativ = 'Excelent';
    ELSE IF avg_score >= 85 THEN calificativ = 'Foarte Bine';
    ELSE IF avg_score >= 75 THEN calificativ = 'Bine';
    ELSE IF avg_score >= 65 THEN calificativ = 'Satisfacator';
    ELSE calificativ = 'Insuficient';

    /* Procesare conditionala: statut job */
    IF part_time_job = 'TRUE'  THEN statut_job = 'Angajat part-time';
    ELSE                            statut_job = 'Fara job';

    /* SELECT-WHEN (alternativa la IF-ELSE) */
    SELECT (extracurricular);
        WHEN ('True')  activ_extracurricular = 'Da';
        WHEN ('False') activ_extracurricular = 'Nu';
        OTHERWISE      activ_extracurricular = 'NS/NR';
    END;

    /* Procesare ITERATIVA: adaos bonus scor pentru activitati extra */
    bonus = 0;
    DO i = 1 TO 3;               /* 3 iteratii - simulare acordare puncte */
        IF extracurricular = 'True' THEN bonus + 1;
    END;
    DROP i;

    /* Functii SAS pe siruri */
    nume_complet = STRIP(first_name) || ' ' || STRIP(last_name);
    initiale     = SUBSTR(first_name, 1, 1) || '.' || SUBSTR(last_name, 1, 1) || '.';
    email_upper  = UPCASE(email);
    lung_email   = LENGTH(STRIP(email));

    /* Functii SAS numerice/data */
    data_raport  = TODAY();
    FORMAT data_raport DATE9.;

    /* Studiu intens: > 20 ore/saptamana */
    IF weekly_self_study_hours > 20 THEN studiu_intens = 'Da';
    ELSE studiu_intens = 'Nu';

    FORMAT avg_score 8.2;
RUN;

PROC PRINT DATA=WORK.studenti_procesati (OBS=50);
    VAR id nume_complet avg_score total_score calificativ statut_job
        activ_extracurricular bonus studiu_intens;
    TITLE "3. Procesare iterativa si conditionala";
RUN;


/* ============================================================
   4. CREAREA DE SUBSETURI DE DATE
   ============================================================ */

/* Subset 1: Studenti cu medie >= 85 */
DATA WORK.studenti_top;
    SET WORK.studenti_procesati;
    WHERE avg_score >= 85;
RUN;

/* Subset 2: Studente (gen feminin) */
DATA WORK.studente_feminine;
    SET WORK.studenti_procesati;
    IF gender = 'female';
    KEEP id nume_complet avg_score career_aspiration gender;
RUN;

/* Subset 3: Viitori medici si avocati */
DATA WORK.aspiratii_nobile;
    SET WORK.studenti_procesati;
    WHERE career_aspiration IN ('Doctor', 'Lawyer');
    KEEP id nume_complet career_aspiration avg_score math_score biology_score;
RUN;

/* Subset 4: Fara absente excesive si studiu intens */
DATA WORK.studenti_model;
    SET WORK.studenti_procesati;
    WHERE absence_days <= 3 AND weekly_self_study_hours >= 20;
RUN;

PROC PRINT DATA=WORK.studenti_top (OBS=50);
    TITLE "4a. Subset: studenti cu medie >= 85";
RUN;
PROC PRINT DATA=WORK.studente_feminine (OBS=50);
    TITLE "4b. Subset: studente feminine";
RUN;
PROC PRINT DATA=WORK.aspiratii_nobile (OBS=50);
    TITLE "4c. Subset: viitori medici si avocati";
RUN;
PROC PRINT DATA=WORK.studenti_model (OBS=50);
    TITLE "4d. Subset: studenti model (absente <= 3, studiu >= 20h)";
RUN;


/* ============================================================
   5. FUNCTII SAS (aprofundare)
   ============================================================ */

DATA WORK.functii_demo;
    SET WORK.studenti_procesati;

    /* Functii matematice */
    scor_max    = MAX(math_score, history_score, physics_score,
                      chemistry_score, biology_score,
                      english_score, geography_score);
                      
    scor_min    = MIN(math_score, history_score, physics_score,
                      chemistry_score, biology_score,
                      english_score, geography_score);
                      
    deviatia    = ABS(math_score - avg_score);

    /* Functii sir de caractere */
    prenume_upper  = UPCASE(first_name);
    prenume_proper = PROPCASE(first_name);
    email_domeniu  = SCAN(email, 2, '@');
    lung_prenume   = LENGTHN(first_name);

    /* Functii de conversie */
    id_char     = PUT(id, 2.);              /* numeric -> caracter */
    scor_char   = PUT(avg_score, 6.2);

    /* Functii de data */
    an_curent   = YEAR(TODAY());
    zi_saptamana= WEEKDAY(TODAY());

    KEEP id nume_complet avg_score scor_max scor_min deviatia
         prenume_upper prenume_proper email_domeniu lung_prenume
         id_char scor_char an_curent zi_saptamana;
RUN;

PROC PRINT DATA=WORK.functii_demo (OBS=50);
    TITLE "5. Exemple de functii SAS";
RUN;


/* ============================================================
   6. COMBINAREA SETURILOR DE DATE
   ============================================================ */

/* --- 6A: SET (concatenare verticala -> adauga randuri) --- */
/* Cream doua subseturi pe gen, apoi le reunim */
DATA WORK.masculin;
    SET WORK.studenti_procesati;
    WHERE gender = 'male';
RUN;

DATA WORK.feminin;
    SET WORK.studenti_procesati;
    WHERE gender = 'female';
RUN;

DATA WORK.toti_concatenat;
    SET WORK.masculin WORK.feminin;
RUN;

PROC PRINT DATA=WORK.toti_concatenat (OBS=10);
    VAR id nume_complet gender avg_score;
    TITLE "6A. SET - concatenare verticala (masculin + feminin)";
RUN;

/* --- 6B: MERGE (unire pe cheie -> un join) --- */
/* Cream un set auxiliar cu informatii suplimentare */
DATA WORK.info_suplimentara;
    INPUT id rang $ 10. bursa;
DATALINES;
1 Silver 500
2 Gold 1000
3 Gold 1000
4 Bronze 0
5 . 0
6 Silver 500
7 Gold 1000
8 Gold 1000
9 Bronze 0
10 Silver 500
;
RUN;

/* Sortam ambele seturi dupa cheie inainte de MERGE */
PROC SORT DATA=WORK.studenti_procesati; BY id; RUN;
PROC SORT DATA=WORK.info_suplimentara;  BY id; RUN;

DATA WORK.studenti_complet;
    MERGE WORK.studenti_procesati (IN=a)
          WORK.info_suplimentara  (IN=b);
    BY id;
    IF a AND b;   /* Inner join - doar obs comune */
RUN;

PROC PRINT DATA=WORK.studenti_complet (OBS=10);
    VAR id nume_complet avg_score rang bursa;
    TITLE "6B. MERGE - unire pe cheie (id) cu informatii suplimentare";
RUN;

/* --- 6C: PROC SQL (echivalent JOIN) --- */
PROC SQL;
    CREATE TABLE WORK.studenti_sql AS
    SELECT s.id,
           s.nume_complet,
           s.gender,
           s.avg_score,
           s.career_aspiration,
           i.rang,
           i.bursa,
           CASE
               WHEN s.avg_score >= 92 THEN 'Top student'
               WHEN s.avg_score >= 85 THEN 'Bun student'
               ELSE 'Standard'
           END AS categorie
    FROM WORK.studenti_procesati AS s
    INNER JOIN WORK.info_suplimentara AS i
        ON s.id = i.id
    ORDER BY s.avg_score DESC;
QUIT;

PROC PRINT DATA=WORK.studenti_sql;
    TITLE "6C. PROC SQL - JOIN cu CASE WHEN";
RUN;

/* SQL: agregare grupata */
PROC SQL;
    SELECT gender,
           COUNT(*)        AS nr_studenti,
           ROUND(MEAN(avg_score), 0.01) AS medie_gen,
           MAX(avg_score)  AS max_scor,
           MIN(avg_score)  AS min_scor
    FROM WORK.studenti_procesati
    GROUP BY gender
    ORDER BY medie_gen DESC;
QUIT;
/* Titlu afisat dupa executie */
TITLE "6C. SQL - agregare pe gen";


/* ============================================================
   7. MASIVE (ARRAY)
   ============================================================ */

DATA WORK.masive_demo;
    SET WORK.studenti_procesati;

    /* ARRAY unidimensional: toate scorurile */
    ARRAY scoruri[7] math_score history_score physics_score
                     chemistry_score biology_score
                     english_score geography_score;

    /* Calcule iterative pe masiv */
    scor_max2 = scoruri[1];
    scor_min2 = scoruri[1];
    nr_peste_80 = 0;
    nr_sub_70   = 0;

    DO i = 1 TO DIM(scoruri);
        IF scoruri[i] > scor_max2 THEN scor_max2 = scoruri[i];
        IF scoruri[i] < scor_min2 THEN scor_min2 = scoruri[i];
        IF scoruri[i] > 80 THEN nr_peste_80 + 1;
        IF scoruri[i] < 70 THEN nr_sub_70   + 1;
    END;

    /* ARRAY pentru normalizare scoruri (0-100 -> 0-10) */
    ARRAY scoruri_norm[7]
          math_n hist_n phys_n chem_n bio_n eng_n geo_n;

    DO i = 1 TO DIM(scoruri_norm);
        scoruri_norm[i] = ROUND(scoruri[i] / 10, 0.1);
    END;

    DROP i;

    KEEP id nume_complet math_score history_score physics_score
         chemistry_score biology_score english_score geography_score
         scor_max2 scor_min2 nr_peste_80 nr_sub_70
         math_n hist_n phys_n chem_n bio_n eng_n geo_n avg_score;
RUN;

PROC PRINT DATA=WORK.masive_demo (OBS=50);
    VAR id nume_complet avg_score scor_max2 scor_min2
        nr_peste_80 nr_sub_70;
    TITLE "7. Masive (ARRAY) - statistici per student";
RUN;

PROC PRINT DATA=WORK.masive_demo (OBS=10);
    VAR id nume_complet math_n hist_n phys_n chem_n bio_n eng_n geo_n;
    TITLE "7b. Masive - scoruri normalizate (scala 0-10)";
RUN;


/* ============================================================
   8. PROCEDURI PENTRU RAPORTARE
   ============================================================ */

/* 8A: PROC PRINT cu optiuni */
PROC PRINT DATA=WORK.studenti_procesati (OBS=50) NOOBS;
    VAR id nume_complet gender avg_score calificativ career_aspiration;
    WHERE avg_score >= 80;
    LABEL id='Nr. Crt'
          nume_complet='Nume Student'
          gender='Gen'
          avg_score='Medie'
          calificativ='Calificativ'
          career_aspiration='Aspiratie Cariera';
    TITLE "8A. PROC PRINT - Studenti cu medie >= 80";
    FORMAT avg_score 8.2;
RUN;

/* 8B: PROC REPORT */
PROC REPORT DATA=WORK.studenti_procesati (OBS=50) NOWD;
    COLUMNS id nume_complet gender avg_score total_score
            absence_days calificativ;
    DEFINE id           / DISPLAY 'ID';
    DEFINE nume_complet / DISPLAY 'Nume Complet';
    DEFINE gender       / DISPLAY 'Gen';
    DEFINE avg_score    / DISPLAY 'Medie' FORMAT=8.2;
    DEFINE total_score  / DISPLAY 'Total Scoruri';
    DEFINE absence_days / DISPLAY 'Absente';
    DEFINE calificativ  / DISPLAY 'Calificativ';
    TITLE "8B. PROC REPORT - Raport detaliat studenti";
RUN;

/* 8C: PROC TABULATE */
PROC TABULATE DATA=WORK.studenti_procesati;
    CLASS gender calificativ;
    VAR avg_score absence_days weekly_self_study_hours;
    TABLE gender ALL,
          (avg_score absence_days weekly_self_study_hours)
          * (MEAN*F=8.2 N);
    TITLE "8C. PROC TABULATE - Statistici pe gen";
RUN;

/* 8D: PROC FREQ */
PROC FREQ DATA=WORK.studenti_procesati;
    TABLES gender * calificativ / CHISQ NOCOL NOPERCENT;
    TITLE "8D. PROC FREQ - Distributia calificativelor pe gen (cu Chi-patrat)";
RUN;


/* ============================================================
   9. PROCEDURI STATISTICE
   ============================================================ */

/* 9A: PROC MEANS */
PROC MEANS DATA=WORK.studenti_procesati N MEAN STD MIN MAX MEDIAN;
    VAR math_score history_score physics_score chemistry_score
        biology_score english_score geography_score avg_score;
    TITLE "9A. PROC MEANS - Statistici descriptive scoruri";
RUN;

/* 9B: PROC MEANS pe grupuri */
PROC MEANS DATA=WORK.studenti_procesati N MEAN STD;
    CLASS gender;
    VAR avg_score math_score biology_score;
    TITLE "9B. PROC MEANS - Comparatie medii pe gen";
RUN;

/* 9C: PROC UNIVARIATE */
PROC UNIVARIATE DATA=WORK.studenti_procesati NORMAL PLOT;
    VAR avg_score;
    TITLE "9C. PROC UNIVARIATE - Distributia mediei generale";
RUN;

/* 9D: PROC CORR - corelatii intre discipline */
PROC CORR DATA=WORK.studenti_procesati;
    VAR math_score physics_score chemistry_score biology_score
        history_score english_score geography_score;
    TITLE "9D. PROC CORR - Matricea de corelatii intre discipline";
RUN;

/* 9E: PROC REG - regresie: avg_score ~ absente + ore_studiu */
PROC REG DATA=WORK.studenti_procesati (OBS=100);
    MODEL avg_score = absence_days weekly_self_study_hours / R;
    TITLE "9E. PROC REG - Regresia mediei in functie de absente si ore studiu";
RUN;
QUIT;

/* 9F: PROC TTEST - test t independente (gender) */
PROC TTEST DATA=WORK.studenti_procesati;
    CLASS gender;
    VAR avg_score;
    TITLE "9F. PROC TTEST - Test t: diferenta medie masculin vs feminin";
RUN;


/* ============================================================
  10. GENERARE GRAFICE (PROC SGPLOT, SGPANEL, SGSCATTER)
   ============================================================ */

/* 10A: Histograma distributia mediei generale */
PROC SGPLOT DATA=WORK.studenti_procesati;
    HISTOGRAM avg_score / BINWIDTH=5 FILLATTRS=(COLOR=CX4E79A7);
    DENSITY avg_score / TYPE=KERNEL LINEATTRS=(COLOR=CXE15759 THICKNESS=2);
    XAXIS LABEL="Medie generala";
    YAXIS LABEL="Frecventa";
    TITLE "10A. Distributia mediei generale a studentilor";
RUN;

/* 10B: Bar chart - distributia pe calificative */
PROC SGPLOT DATA=WORK.studenti_procesati;
    VBAR calificativ / FILLATTRS=(COLOR=CX76B7B2) DATALABEL;
    XAXIS LABEL="Calificativ";
    YAXIS LABEL="Nr. Studenti";
    TITLE "10B. Distributia studentilor pe calificative";
RUN;

/* 10C: Scatter plot - ore studiu vs medie generala, colorat pe gen */
PROC SGPLOT DATA=WORK.studenti_procesati;
    SCATTER X=weekly_self_study_hours Y=avg_score /
            GROUP=gender
            MARKERATTRS=(SIZE=10)
            DATALABEL=initiale;
    REG     X=weekly_self_study_hours Y=avg_score /
            GROUP=gender LINEATTRS=(THICKNESS=1.5);
    XAXIS LABEL="Ore studiu individual / sapt.";
    YAXIS LABEL="Medie generala";
    KEYLEGEND / TITLE="Gen";
    TITLE "10C. Relatia ore studiu vs medie, pe gen (cu dreapta de regresie)";
RUN;

/* 10D: Box plot - medii pe aspiratie profesionala */
PROC SGPLOT DATA=WORK.studenti_procesati;
    VBOX avg_score / CATEGORY=career_aspiration
                     FILLATTRS=(COLOR=CXF28E2B)
                     BOXWIDTH=0.4;
    XAXIS LABEL="Aspiratie in cariera" DISCRETEORDER=FORMATTED;
    YAXIS LABEL="Medie generala";
    TITLE "10D. Distributia mediei pe aspiratii in cariera (Box Plot)";
RUN;

/* 10E: Grafic comparativ scoruri pe discipline (bar clustering) */
PROC SGPLOT DATA=WORK.studenti_procesati;
    VBOX math_score /    FILLATTRS=(COLOR=CX4E79A7) LEGENDLABEL='Matematica' NAME='Math';
    VBOX physics_score / FILLATTRS=(COLOR=CXE15759) LEGENDLABEL='Fizica'     NAME='Phys';
    VBOX biology_score / FILLATTRS=(COLOR=CX59A14F) LEGENDLABEL='Biologie'   NAME='Bio';
    
    YAXIS LABEL="Scor";
    KEYLEGEND 'Math' 'Phys' 'Bio' / TITLE="Disciplina";
    TITLE "10E. Distributia scorurilor: Matematica / Fizica / Biologie";
RUN;
