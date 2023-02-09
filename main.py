number = [1, 2, 3, 4 ,5 ,6 ]
number.append(10) #Thêm một phần tử vào cuối danh sách
number.insert(1, 15) #Thêm một phần tử vào vị trí chỉ định
tropical = [13,13,31]

number.extend(tropical) # Các phần tử sẽ được thêm vào cuối danh sách
number.remove(13) #Xoá phần tử đã chỉ định

number.pop(3) #Xoá phần tử có chỉ mục đã đc chỉ định , nếu ko ghi chỉ mục thì mặc định xoá phần tử cuối cùng
max_number = max(number)
print(len(number))

print(max_number)
