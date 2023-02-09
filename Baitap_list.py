#khoi tao danh sach nhung phim da xem
movies_list = ["Cuoc chien giua nguoi va than",
               "Boruto",
               "Naruto",
               "One piece",
               "Chaisawman"]
print("Nhung bo phim da xem:", movies_list)

#3. Su dung ham input de nhap vao mot bo phim khac ko co torg movies list
movies_list_new = input("Bo phim khac moi xem gan day:")
#4.Them bo phim vua nhap vao cuoi danh sach
movies_list.append(movies_list_new)
print(movies_list)
#4.In ra bo phim dau tien cuoi cung va o giua
len_movies_list = len(movies_list)
print("Bo phim dau tien la:", movies_list[0])
print("Bo phim cuoi cung la: ", movies_list[-1])
print("Bo phim cuoi cung la:", movies_list.pop())
print("Bo phim o giua la: ", movies_list[(len_movies_list//2)])
