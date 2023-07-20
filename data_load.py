
def load_data(file_path):
    # z pliku wyciagam oddzielnie dane punktów x,y
    x_values = []
    y_values = []

    with open(file_path,"r") as f:
        for line in f:
            #rozdzielamy zmienne przy uzyciu ","
            data = line.strip().split(",")
            #potwierdzamy ze dane mają conajmniej dwie wartości x i y
            if len(data)>=2:
                #konwertujemy dane na typ float
                try:
                    x = float(data[0])
                    y = float(data[1])
                    #dodajemy do listy
                    x_values.append(x)
                    y_values.append(y)
                except ValueError:
                    #w przypadku błędu konwersji typów
                    print("Error: Invalid data in line:" , line)
    #teraz zwracamy listy danych
    print("X:" ,x_values,"\nY:",y_values)
    return x_values,y_values

trainX , trainY = load_data("dataset/train.csv")
print("\n")
testX, testY = load_data("dataset/test.csv")
