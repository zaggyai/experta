# Experta

_Forked from `nilp0inter/experta` link broken so we can go off on our own as that 
project appears to abandoned._

Experta is a Python library for building expert systems strongly
inspired by [CLIPS](http://clipsrules.sourceforge.net).

``` python
from random import choice
from experta import *


class Light(Fact):
    """Info about the traffic light."""
    pass


class RobotCrossStreet(KnowledgeEngine):
    @Rule(Light(color='green'))
    def green_light(self):
        print("Walk")

    @Rule(Light(color='red'))
    def red_light(self):
        print("Don't walk")

    @Rule(AS.light << Light(color=L('yellow') | L('blinking-yellow')))
    def cautious(self, light):
        print("Be cautious because light is", light["color"])
```

``` python
>>> engine = RobotCrossStreet()
>>> engine.reset()
>>> engine.declare(Light(color=choice(['green', 'yellow', 'blinking-yellow', 'red'])))
>>> engine.run()
Be cautious because light is blinking-yellow
```

## Examples


You can find some more examples on
[GitHub](https://github.com/nilp0inter/experta/tree/develop/docs).

More yet in the [documentation](https://experta.readthedocs.io/en/latest/).
