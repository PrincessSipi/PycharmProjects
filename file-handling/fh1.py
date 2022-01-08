with  open("message.txt", "r") as f:

    content = f.read(7)
    print(content)

    more_content = f.read()
    print(more_content)


