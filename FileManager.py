import pickle

# l = [1, 2, 3, 4]
# with open("data", "wb") as fp:  # Pickling
#
#     pickle.dump(l, fp)

filename = 1
lastImage = 220
cont = 1

path = "data_full/{}"

while filename <= lastImage:
    with open(path.format(filename), "rb") as fp:  # Unpickling

        filename+=1

        b = pickle.load(fp)
        print(f'{filename-1} : {len(b)}')
        print(b)

# while cont <= 420:
#     if (b[0] == b[cont]):
#         print("Encontrou um igual")
#         break
#     cont+=1
