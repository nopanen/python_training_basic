phonebook = {}

n = int(raw_input())
for numberofcommands in range(n):
    command = raw_input()
    commandparts = command.split(' ')
    command = commandparts[0]

    if command == 'add':
        number = int(commandparts[1])
        name = commandparts[2]

        if name in phonebook:
            phonebook[name].append(number)
        else:
            phonebook[name] = [number]

    if command == 'del':
        name = commandparts[1]

        if name in phonebook:
            phonebook.pop(name)

    if command == 'find':
        name = commandparts[1]
        numbers = phonebook[name] if name in phonebook else []

        print min(numbers) if numbers else 'not found'
