# Python README
## by Peter Fuchs
### V20171105

---

### [Threading](threading/)
 * #### What is Threading?
    Threading means running a program on multiple parts on the processor. So the program gets split into different parts that are executed
    parallel. A process has at least 1 thread and 1 thread always belongs to only 1 process
    <small>(which is the same as 1:N in data base management systems)</small>.
    Threads in the same process share the address area so it's easier to synchronize, start and destroy them compared to normal processes.
    The operating system also has no influence on threads, in this case the process controlls everything.

 * #### Problems
    Using multiple threads can cause some problems:
    * **Threads overwriting other threads**<br/>
        This is actually a problem that comes with sharing resources <small>(which actually should be a good thing...)</small>. The Problem here
        is that some threads are taking resources other threads are currently working with - and then the threads aren't synchronized. So if
        you wanted to count a number on multiple threads there could easily be this problem:<br/>
        Let's prevent that Thread 1 took the number and increased it by 1.
        Saying that the number was 0 at the beginning, it now is 1 - in Thread 1 but not yet globally:
        ```
       Thread 1: number = 1
       Global  : number = 0
       ```
        If now Thread 2 takes the opportunity to increase the number by one, he takes of course what globally is the value of number:
        ```
       Thread 1: number = 1
       Global  : number = 0
       Thread 2: number = 0  
       ```
        So if now Thread 1 overwrites the global number, Thread 2 already took the old value - and increases it by one:
        ```
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

 * #### <a name="locks"></a>Locks
    



 * #### <a name="conditions"></a>Conditions
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

        **Links**<br/>
        [Python API](https://docs.python.org/3/library/threading.html#condition-objects)
   
 * #### <a name="events"></a>Events




 * #### <a name="queues"></a>Queues




 * #### <a name="atomic"></a>Atomic Operations

   

## Python API Reference
- Python 2   
Condition Objects: https://docs.python.org/2/library/threading.html#condition-objects
- Python 3  
Condition Objects: https://docs.python.org/3/library/threading.html#condition-objects