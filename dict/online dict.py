statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Carl": "online",
    "Jacob": "deceased"
}

def online_count(statuses):
    online = 0
    for name in statuses:
        if statuses[name] == "online":
            online += 1
    return online

print(online_count(statuses))
