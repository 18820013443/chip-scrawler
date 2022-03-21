def WriteTextToFile(filePath, strContent):
    with open(filePath, 'w+', encoding='utf-8') as f:
        f.write(strContent)
