# Telegraf Sandbox

Forked from [this repo](https://github.com/jkehres/docker-compose-influxdb-grafana) 

Multi-container Docker app built from the following services:

* [InfluxDB](https://github.com/influxdata/influxdb) - time series database
* [Grafana](https://github.com/grafana/grafana) - visualization UI for InfluxDB

I set this up to quickly test out Telegraf end to end changes

## Quick Start

To start the app:

1. Install [docker-compose](https://docs.docker.com/compose/install/) on the docker host.
2. Clone this repo on the docker host.
3. Optionally, change default credentials or Grafana provisioning.
4. Run the following command from the root of the cloned repo:
```
docker-compose up -d --build
```
5. You'll have to update the database, username, and password settings in the newly created Grafana's (Available on port 3000 by default) datasource settings.

To stop the app:

1. Run the following command from the root of the cloned repo:
```
docker-compose down
```

## Ports

The services in the app run on the following ports:

| Host Port | Service |
| - | - |
| 3000 | Grafana |
| 8086 | InfluxDB |

If docker is running on a remote machine that supports SSH, use the following command to setup an SSH tunnel to securely access Chronograf by forwarding port 8888 on the remote machine to port 8888 on the local machine:

```
ssh [options] <user>@<docker-host> -L 8888:localhost:8888 -N
```

## Volumes

The app creates the following named volumes (one for each service) so data is not lost when the app is stopped:

* influxdb-storage
* grafana-storage

## Users

The app creates two admin users - one for InfluxDB and one for Grafana. By default, the username and password of both accounts is `admin`. To override the default credentials, set the following environment variables before starting the app (Also available in the local .env file):

* `INFLUXDB_USERNAME`
* `INFLUXDB_PASSWORD`
* `GRAFANA_USERNAME`
* `GRAFANA_PASSWORD`

## Database

The app creates a default InfluxDB database called `telegraf`.

## Data Sources

The app creates a Grafana data source called `InfluxDB` that's connected to the default IndfluxDB database (e.g. `telegraf`).

To provision additional data sources, see the Grafana [documentation](http://docs.grafana.org/administration/provisioning/#datasources) and add a config file to `./grafana-provisioning/datasources/` before starting the app.

## Dashboards

By default, the app does not create any Grafana dashboards. An example dashboard that's configured to work with [artillery-plugin-influxdb](https://github.com/Nordstrom/artillery-plugin-influxdb) is located at `./grafana-provisioning/dashboards/artillery.json.example`. To use this dashboard, rename it to `artillery.json`.

To provision additional dashboards, see the Grafana [documentation](http://docs.grafana.org/administration/provisioning/#dashboards) and add a config file to `./grafana-provisioning/dashboards/` before starting the app.
