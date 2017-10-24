# Python README
## by Peter Fuchs
### V20172310

---

### [Threading](threading/)

 * #### Conditions
    * **language**: German/Deutsch<br>
    [Beispiel](threading/condition_variable_de.py)<br>
    Threading mit Condition-Variablen heißt, dass ein Lock mithilfe einer Condition ausgelöst wird.<br />
    Hierfür gibt es folgende Funktionen:<br />
    * notify(n=1)
    *Weckt maximal n Threads auf. Standardmäßig ist n auf 1 gesetzt, heißt, es wird ohne Angabe von Parametern ein Thread aufgeweckt.<br>
    Die Ausführung dieses Threads findet dann statt, wenn der die Methode ausführende Thread seine Ressourcen wieder freigibt.*
    * wait():
    *Legt einen Thread schlafen. Der Thread wartet dann darauf, dass mit er mit der Methode notify wieder aufgeweckt wird.*
    
    * **language**: English<br>
    [Example](threading/condition_variable.py)<br>
    Threading with condition variables means that you
        
    **See also**
    [Python API](https://docs.python.org/2/library/threading.html#condition-objects)
   
