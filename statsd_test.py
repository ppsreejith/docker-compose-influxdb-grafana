import statsd
from random import random, randint

old_send_stat = statsd.client.base.StatsClientBase._send_stat
def new_send_stat(self, stat, value, rate):
    print("testing", stat, value, rate)
    old_send_stat(self, stat, value, rate)

def distribution(self, stat, delta, rate=1):
        """
        Send new distribution information.
        `delta` can be either a number of milliseconds or a timedelta.
        """
        self._send_stat(stat, '%0.6f|d' % delta, rate)

statsd.client.base.StatsClientBase._send_stat = new_send_stat
statsd.client.base.StatsClientBase.distribution = distribution

c = statsd.StatsClient('localhost', 8125)
for index in range(2000):
    c.timing('testing4.foo', index)
print("Reached")
