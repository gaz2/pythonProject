import docx


def main():
    try:
        doc = docx.Document('Сопроводительное письмо - вложение!.docx')  # Creating word reader object.
        data = ""
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
            data = '\n'.join(fullText)

        print(data)

    except IOError:
        print('There was an error opening the file!')
        return


if __name__ == '__main__':
    main()