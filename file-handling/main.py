try:
    f = open("message.txt", "r")

    content = f.read(6)
    print(content)

    more_content = f.read(12)
    print(more_content)

finally:
    f.close()