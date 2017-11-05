# Python README
## by Peter Fuchs
### V20172310

---

### [Threading](threading/)
 * #### Lock
       


 * #### Conditions
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
    
    * **Aufbau**:
    *It is very important that all the constructors that want to use the condition-variable, recieve it.<small>(Which in every case has to be
    the same!)</small> When creating a lock, this variable finds it's usage:<br/>
    The [locked area](threading/condition_variable.py#L38) gets created with it and via the notify-method all the other locks, that got created
    with this variable and shall be awoken with it (see [notify](#notify)), get executed.*
        
        **See also**<br/>
        [Python API](https://docs.python.org/2/library/threading.html#condition-objects)
   
