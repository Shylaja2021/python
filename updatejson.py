import json

addr='{"city":"bangalore","state":"karnataka","country":"india"}'
pin={"pincode":100119}

fulladr=json.loads(addr)
fulladr.update(pin)

print(fulladr)

