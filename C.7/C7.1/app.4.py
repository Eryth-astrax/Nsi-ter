def convert(liste):
    x = ""
    for val in liste:
        for j in val:
            if j:
                x = x + "• "
            else:
                x = x + "  "
        x += "\n"
    return x

Li = [[1, 1, 1, 0, 1, 1, 1],
      [1, 0, 1, 0, 0, 0, 1], 
      [1, 0, 1, 1, 1, 0, 1], 
      [1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 1, 1],
      [1, 0, 0, 0, 0, 0, 1],
      [1, 1, 1, 0, 1, 1, 1]]

print(convert(Li))