customer = {
    "name": "Spencer",
    "age": 26,
    "is_verified": True
}
customer["email"] = "spencer@gmail.com"
print(customer['name'])
print(customer.get('email', 'default@gmail.com'))
