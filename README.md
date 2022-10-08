# linespool

## A python print spooler for line printers.


### Integration in Home Assistant:

```
rest_command:
  print_update:
    url: "http://127.0.0.1:5000/msg"
    method: POST
    content_type: "application/x-www-form-urlencoded"
    payload: "message={{printmsg}}"
```
