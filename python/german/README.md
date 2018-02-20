# Python README
## by Peter Fuchs
### V20171105

---

### [Threading](../threading/)
 * #### Was ist Threading?
    **siehe auch**: [PDFs](../threading/sources_de/SEW_4_Threading_Einfuehrung_Python.pdf)<br />
    Threading heißt, dass ein Programm mit mehreren Teilen auf dem Prozessor läuft. Das heißt, dass das Programm in mehrere Teile aufgeteilt
    wird, welche gleichzeitig (parallel) ausgeführt werden. Ein Prozess besteht immer aus mindestens einem Thread, aber ein Thread gehört
    immer nur genau einem Prozess <small>(vergleichbar mit 1:N im DBMS)</small>.
    Threads im selben Prozess teilen sich den Adressraum, somit ist es, verglichen mit einem normalen Prozess, einfacher, sie zu synchronisieren,
    zu starten und auch zu zerstören. Das Betriebssystem hat auch keinen Einfluss auf die Threads, in diesem Fall kontrolliert der Prozess
    <small>(und daher auch der Entwickler)</small> alles.

 * #### Probleme
    **siehe auch**: [PDFs](../threading/sources_de/SEW_4_Probleme_Concurrency.pdf)<br />
    Mehrere Threads zu verwenden kann zu einigen Problemen führen:
    * **Threads überschreiben andere Threads**<br />
        Das ist ein Problem, welches mit dem Teilen von Ressourcen auftritt. Hierbei ist das Problem, dass einige Threads Ressourcen benutzen,
        mit denen andere Threads gerade arbeiten - dadurch werden die Threads asynchronisiert. Wenn man nun zum Beispiel eine Zahl über mehrere
        Threads hinaufzählen will, kann sehr leicht dieses Problem auftreten:<br />
        Angenommen, Thread 1 hat die global Variable genommen und um 1 erhöht. Wenn nun angenommen wird, dass bei 0 begonnen wurde zu zählen,
        heißt das, dass die Zahl jetzt 1 ist - allerdings nur in Thread 1 und noch nicht global:
        ```
        Thread 1: zahl = 1
        Global  : zahl = 0
       ```
        Wenn nun Thread 2 die Zahl erhöhen will, wird er natürlich wieder auf die globale Variable referenzieren:
        ```
        Thread 1: zahl = 1
        Global  : zahl = 0
        Thread 2: zahl = 0
       ```
        Jetzt überschreibt Thread 1 die globale Variable und Thread 2 erhöht sie um eins - allerdings noch mit dem alten Wert:
        ```
        Thread 1: zahl = 1
        Global  : zahl = 1
        Thread 2: zahl = 1 #Thread 2 hat die Zahl bereits um 1 erhöht!!
       ```
        Am Ende überschreibt Thread 2 wieder die globale Zahl. Diese bleibt eins, daher wurde der Wert der Zahl, obwohl zweimal erhöht, insgesamt
        nur um 1 erhöht.<br />
        **Lösungen: [Locks](#locks), [Bedingungen](#conditions), [Events](#events), [Queues](#queues), [Atomare Operationen](#atomic)**

    * **Deadlocks**<br />
        Deadlocks treten auf, wenn zwei oder mehr Locks eine Ressource vom jeweils anderen Lock benötigen:
        ```
        Szenario:
        Ich bin Lock1 und ich benutze momentan die Variable zahl. Diese möchte ich um die Variable x erhöhen.
        Mein Problem ist nun, dass ich den Besitzer von x zwar kenne, der aber meine Variable zahl haben will, um seine Variable
        x mit meiner zahl multiplizieren zu können. Da wir uns beide in einem Lock befinden, denken wir beide, dass wir die
        höchste Priorität ever besitze, daher würden wir niemals unsere Variable an den anderen Lock geben - ich bin wichtiger als er.
       ```
        Dieses Szenario ist ein ewiger Kreislauf, wo einfach nichts passiert. Es gibt allerdings einige Methoden, um diese Deathlocks zu umgehen:
        <br />
        **[Deathlock Verhütung](#dl_verhuetung), [Deathlock Vermeidung](#dl_vermeidung), [Deathlock Erkennung](#dl_erkennung)** und den
        **[_Ostrich_ (Vogelstrauß) Algorithmus](#dl_vogelstrauss).**
   
 * #### <a name="locks"></a>Locks
    


 * #### <a name="conditions"></a>Bedingungen
    **siehe auch**: [Beispiel](../threading/sources_de/condition_variable_de.py)<br>
    Threading mit Bedingungsvariablen heißt, dass ein Lock mithilfe einer Bedingung ausgelöst wird.<br />
    Hierfür gibt es folgende Funktionen:<br />
    * <a name="notify_de"></a>notify(n=1)<br/>
    *Weckt maximal n Threads auf. Standardmäßig ist n auf 1 gesetzt, das heißt, es wird ohne Angabe von Parametern ein Thread aufgeweckt.<br>
    Die Ausführung dieses Threads findet dann statt, wenn der die Methode ausführende Thread seine Ressourcen wieder freigibt.*
    * wait()<br/>
    *Legt einen Thread schlafen. Der Thread wartet dann darauf, dass mit er mit der Methode notify wieder aufgeweckt wird.*
    
    * **Aufbau**:
    *Wichtig ist, dass dem Konstruktor der betroffen Klassen jeweils eine Bedingungsvariable übergeben wird. <small>(Diese muss in jedem Fall die
    selbe sein!)</small> Beim Erstellen des Locks kommt nun die übergebene Bedingungsvariable zum Einsatz:<br/>
    Der [Lock-Bereich](../threading/sources_de/condition_variable_de.py#L38) wird mit dieser erstellt und über die notify-Methode werden alle anderen Locks,
    die mit dieser Variable aufgeweckt werden (siehe [notify](#notify_de)), ausgeführt.*

        **Links:**<br/>
        [Python API](https://docs.python.org/3/library/threading.html#condition-objects)
   
 * #### <a name="events"></a>Events
	



 * #### <a name="queues"></a>Queues
    **siehe auch**: [Beispiel](../threading/sources_de/queue_example_de.py)<br>
	



 * #### <a name="atomic"></a>Atomare Operationen


## Python API Reference
- Python 2   
Condition Objects: https://docs.python.org/2/library/threading.html#condition-objects
- Python 3  
Condition Objects: https://docs.python.org/3/library/threading.html#condition-objects