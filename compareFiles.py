file1 = open("C://Users//Rajput-PC//Desktop//AL//Task 01//assets//files//file1.txt","r")
text1_words = (file1.read()).split(" ")

file2 = open("C://Users//Rajput-PC//Desktop//AL//Task 01//assets//files//file2.txt","r")
text2_words = (file2.read()).split(" ")

similar_words = list(set(text1_words). intersection(text2_words))

cal_similarity = len(similar_words)/((len(text1_words) + len(text2_words))/2) * 100

print("Similarity: "+str(cal_similarity.__round__(2))+"%")