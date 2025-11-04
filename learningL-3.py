movie = [input("first movie name --> "), input("Second --> "), input("Third --> ")]
movie1 = movie.copy()
movie1.reverse()

if(movie == movie1):
    print("its a Palidrom")
else:
    print("not Palidrom")

print(movie.count("a"))
movie.sort()

print(movie)

