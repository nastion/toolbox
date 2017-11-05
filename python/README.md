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
        you wanted to count a number on multiple threads there could easily be the problem, that one thread takes the global variable and adds one
        to it.<br/>
        Saying that the number was 0 at the beginning, it now is 1 - in Thread 1 but not globally:
        ```python
       Thread 1: number = 1
       Global  : number = 0
       ```
        If now Thread 2 takes the opportunity to increase the number by one, he takes of course what globally is the value of number:
        ```python
       Thread 1: number = 1
       Global  : number = 0
       Thread 2: number = 1  
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

    * #####
   
 * #### <a name="locks"></a>Locks
    


 * #### <a name="conditions"></a>Conditions
    * **language**: German/Deutsch<br>
    [Beispiel](threading/condition_variable_de.py)<br>
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

    * **language**: English<br>
    [Example](threading/condition_variable.py)<br>
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
        
        **See also**<br/>
        [Python API](https://docs.python.org/2/library/threading.html#condition-objects)
   
