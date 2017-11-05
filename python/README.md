# Python README
## by Peter Fuchs
### V20171105

---

### [Threading](threading/)
 * #### What is Threading?
    * **language**: English<br/>
    Threading means running a program on multiple parts on the processor. So the program gets split into different parts that are executed
    parallel. A process has at least 1 thread and 1 thread always belongs to only 1 process
    <small>(which is the same as 1:N in data base management systems)</small>.
    Threads in the same process share the address area so it's easier to synchronize, start and destroy them compared to normal processes.
    The operating system also has no influence on threads, in this case the process controlls everything.

    * **language**: German/Deutsch<br>
    **see also**: [PDFs](threading/sources_de/SEW_4_Threading_Einfuehrung_Python.pdf)<br />
    Threading heißt, dass ein Programm mit mehreren Teilen auf dem Prozessor läuft. Das heißt, dass das Programm in mehrere Teile aufgeteilt
    wird, welche gleichzeitig (parallel) ausgeführt werden. Ein Prozess besteht immer aus mindestens einem Thread, aber ein Thread gehört
    immer nur genau einem Prozess <small>(vergleichbar mit 1:N im DBMS)</small>.
    Threads im selben Prozess teilen sich den Adressraum, somit ist es, verglichen mit einem normalen Prozess, einfacher, sie zu synchronisieren,
    zu starten und auch zu zerstören. Das Betriebssystem hat auch keinen Einfluss auf die Threads, in diesem Fall kontrolliert der Prozess
    <small>(und daher auch der Entwickler)</small> alles.

 * #### Problems
    * **language**: English<br />
    Using multiple threads can cause some problems:
    * **Threads overwriting other threads**<br/>
        This is actually a problem that comes with sharing resources <small>(which actually should be a good thing...)</small>. The Problem here
        is that some threads are taking resources other threads are currently working with - and then the threads aren't synchronized. So if
        you wanted to count a number on multiple threads there could easily be this problem:<br/>
        Let's prevent that Thread 1 took the number and increased it by 1.
        Saying that the number was 0 at the beginning, it now is 1 - in Thread 1 but not yet globally:
        ```python
       Thread 1: number = 1
       Global  : number = 0
       ```
        If now Thread 2 takes the opportunity to increase the number by one, he takes of course what globally is the value of number:
        ```python
       Thread 1: number = 1
       Global  : number = 0
       Thread 2: number = 0  
       ```
        So if now Thread 1 overwrites the global number, Thread 2 already took the old value - and increases it by one:
        ```python
       Thread 1: number = 1
       Global  : number = 1
       Thread 2: number = 1 #Thread 2 already increased number!!
       ```
        And if Thread 2 now overwrites the global number, it stays 1, meaning that even though the number got increased twice, it increased by 1.
        <br/>
        **Solutions: [Locks](#locks), [Conditions](#conditions), [Events](#events), [Queues](#queues), [Atomic Operations](#atomic)**

    * **Deadlocks**<br />
        This occurs when two or more locks need resources from each other:
        ```
        Scenario:
        I am lock1, I currently use the variable number and I want to increase the number by x.
        The problem I have is that I got a dude who currently owns this x and wants my number to
        multiply his x with my number. Since we are both in a lock, we both think our thread is the
        most important part of all time, so we won't just simply give our variable to the other
        person - I'm way more important than him.
       ```
        This scenario ends in a never ending circle of nothing happening. There are some methods that are trying to prevent
        deathlocks from happening:
        **[Deathlock Prevention](#dl_prevention), [Deathlock Avoidance](#dl_avoidance), [Deathlock Detection](#dl_detection)** and the
        **[Ostrich Algorithm](#dl_ostrich).**

    * **language**: German/Deutsch<br/>
    **see also**: [PDFs](threading/sources_de/SEW_4_Probleme_Concurrency.pdf)<br />
    Mehrere Threads zu verwenden kann zu einigen Problemen führen:
    * **Threads überschreiben andere Threads**<br />
        Das ist ein Problem, welches mit dem Teilen von Ressourcen auftritt. Hierbei ist das Problem, dass einige Threads Ressourcen benutzen,
        mit denen andere Threads gerade arbeiten - dadurch werden die Threads asynchronisiert. Wenn man nun zum Beispiel eine Zahl über mehrere
        Threads hinaufzählen will, kann sehr leicht dieses Problem auftreten:<br />
        Angenommen, Thread 1 hat die global Variable genommen und um 1 erhöht. Wenn nun angenommen wird, dass bei 0 begonnen wurde zu zählen,
        heißt das, dass die Zahl jetzt 1 ist - allerdings nur in Thread 1 und noch nicht global:
        ```python
        Thread 1: zahl = 1
        Global  : zahl = 0
       ```
        Wenn nun Thread 2 die Zahl erhöhen will, wird er natürlich wieder auf die globale Variable referenzieren:
        ```python
        Thread 1: zahl = 1
        Global  : zahl = 0
        Thread 2: zahl = 0
       ```
        Jetzt überschreibt Thread 1 die globale Variable und Thread 2 erhöht sie um eins - allerdings noch mit dem alten Wert:
        ```python
        Thread 1: zahl = 1
        Global  : zahl = 1
        Thread 2: zahl = 1 #Thread 2 hat die Zahl bereits um 1 erhöht!!
       ```
        Am Ende überschreibt Thread 2 wieder die globale Zahl. Diese bleibt eins, daher wurde der Wert der Zahl, obwohl zweimal erhöht, insgesamt
        nur um 1 erhöht.<br />
        **Lösungen: [Locks](#locks), [Conditions](#conditions), [Events](#events), [Queues](#queues), [Atomic Operations](#atomic)**

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
    


 * #### <a name="conditions"></a>Conditions
    * **language**: English<br>
    **see also**: [Example](threading/condition_variable.py)<br>
    Threading with condition variables means that a lock runs via conditions.<br>
    Therefore, there are these functions:<br />
    * <a name="notify"></a>notify(n=1)<br/>
    *Awakes a maximum of n threads. n is by default 1, which means that without a special setting of n there will be only one thread woken up.<br>
    The thread gets executed, when the thread that called the method frees its resources.*
    * wait()<br/>
    *Sets a thread to sleep. The thread waits for the notify-method to get awoken again.*
    
    * **Usage**:
    *It is very important that all the constructors that want to use the condition-variable, recieve it.<small>(Which in every case has to be
    the same!)</small> When creating a lock, this variable finds it's usage:<br/>
    The [locked area](threading/condition_variable.py#L38) gets created with it and via the notify-method all the other locks, that got created
    with this variable and shall be awoken with it (see [notify](#notify)), get executed.*

    * **language**: German/Deutsch<br>
    **see also**: [Beispiel](threading/condition_variable_de.py)<br>
    Threading mit Condition-Variablen heißt, dass ein Lock mithilfe einer Condition ausgelöst wird.<br />
    Hierfür gibt es folgende Funktionen:<br />
    * <a name="notify_de"></a>notify(n=1)<br/>
    *Weckt maximal n Threads auf. Standardmäßig ist n auf 1 gesetzt, das heißt, es wird ohne Angabe von Parametern ein Thread aufgeweckt.<br>
    Die Ausführung dieses Threads findet dann statt, wenn der die Methode ausführende Thread seine Ressourcen wieder freigibt.*
    * wait()<br/>
    *Legt einen Thread schlafen. Der Thread wartet dann darauf, dass mit er mit der Methode notify wieder aufgeweckt wird.*
    
    * **Aufbau**:
    *Wichtig ist, dass dem Konstruktor der betroffen Klassen jeweils eine Condition-Variable übergeben wird. <small>(Diese muss in jedem Fall die
    selbe sein!)</small> Beim Erstellen des Locks kommt nun die übergebene Condition-Variable zum Einsatz:<br/>
    Der [Lock-Bereich](threading/condition_variable_de.py#L38) wird mit dieser erstellt und über die notify-Methode werden alle anderen Locks,
    die mit dieser Variable aufgeweckt werden (siehe [notify](#notify_de)), ausgeführt.*

        **See also**<br/>
        [Python API](https://docs.python.org/2/library/threading.html#condition-objects)
   

## Python API Reference
Condition Objects: https://docs.python.org/2/library/threading.html#condition-objects