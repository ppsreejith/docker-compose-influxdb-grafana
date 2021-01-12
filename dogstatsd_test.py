from datadog import initialize, statsd
import random
import time

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

namespace = "testing7"
# statsd.distribution('example_metric.distribution', random.randint(0, 20), tags=["environment:dev"])
statsd.timing("%s.timing"%namespace, random.randint(1, 20), tags=["environment:dev"])
statsd.distribution("%s.distribution"%namespace, 50 + random.randint(1, 20), tags=["environment:dev"])
# time.sleep(5)
# statsd.timing("%s.timing"%namespace, random.randint(1, 20), tags=["environment:dev"])
# statsd.distribution("%s.distribution"%namespace, 50 + random.randint(1, 20), tags=["environment:dev"])
