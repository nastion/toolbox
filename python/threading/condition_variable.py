"""

An example for threading with condition varaibles.

@author: Peter Fuchs <pfuchs@student.tgm.ac.at>
@version: 20171023
@language: de
"""
import threading, time

class Producer(threading.Thread):
    """
    This class represents a producer.
    This producer creates numbers and puts them into
    a shared list of numbers.<br>
    Raises from threading.Thread
    """

    def __init__(self, numbers, condition):
        """
        Initializes the base-class Thread.
        :param numbers: Shared list of numbers
        :param condition: Shared condition variable for synchronization
        """
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.condition = condition

    def run(self):
        """
        Produces numbers and puts them into the shared list self.numbers.
        Uses the shared condition variable for synchronization
        :return: None
        """
        number = 0
        while True:
            # Lock condition variable
            with self.condition:
                print("Producer sperrt condition")
                number = number + 1
                print("Producer erzeugt zahl %d" % number)
                # Put number in shared list
                self.numbers.append(number)
                print("Producer gibt condition wieder frei")
                # Wake up (Notify) treads and free shared conditions
                self.condition.notify()
            # The sleep is that the consumer has some time to work on the numbers
            time.sleep(0.01)


class Consumer(threading.Thread):
    """
    Diese Klasse stellt einen Consumer dar.
    """

    def __init__(self, numbers, condition):
        """
        Initialisiert die Basisklasse Thread.
        :param numbers: Geteilte Zahlen-Liste
        :param condition: Geteilte Bedingungsvariable zur Synchronisation
        """
        threading.Thread.__init__(self)
        self.numbers = numbers
        self.condition = condition

    def run(self):
        """
        Gibt alle Zahlen aus, die in der geteilten Liste self.numbers landen.
        Verwendet die Bedingungsvariable self.condition zur Synchronisation.
        :return: None
        """

        while True:
            # Bedingungsvariable sperren
            with self.condition:
                print("Consumer sperrt condition")
                while True:
                    # Prüfen, ob self.integers nicht leer ist
                    # (in einer Schleife, da ja mehrere Zahlen
                    # in der Liste sein können)
                    if self.numbers:
                        print("Consumer empfing Zahl: %d" % self.numbers.pop())
                    else:
                        break
                print("Consumer gibt condition wieder frei")
                # Auf das Signal warten und Bedingungsvariable freigeben
                self.condition.wait()

if __name__ == '__main__':
    numbers = []
    condition = threading.Condition()
    t1 = Producer(numbers, condition)
    t2 = Consumer(numbers, condition)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
