# mqtt-python

paho-mqttを利用したMQTT実装です。


## Broker起動
```
$ docker-compose up -d
```

## Subscriber起動
```
$ python mqtt.py sub
```

## Publisher起動
キー入力したメッセージをpublishします。  

```
$ python mqtt.py pub
```