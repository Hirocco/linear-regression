from data_load import load_data

#Normalizuje dane za pomocą techniki min_max, chodzi o znormalizowanie danych do przedzialu [0;1] aby modelowi łatwiej sie uczyło
#pamiętajmy że najłatwiej mu będzie gdy bitów będzie jak najmniej
def data_normalization(data):
    Xmin = min(data)
    Xmax = max(data)
    normalized_data = []
    for num in data:
        normalized_var = (num - Xmin) / (Xmax - Xmin)
        normalized_data.append(normalized_var)
    return normalized_data
#stad wzialem wzor
#https://developers.google.com/machine-learning/data-prep/transform/normalization?hl=pl

X,Y = load_data("dataset/train.csv")
normalized_x_data = data_normalization(X)
normalized_y_data = data_normalization(Y)
