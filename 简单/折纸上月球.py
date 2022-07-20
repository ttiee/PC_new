
all_height = 1000000
n = 0
paper_height = 0.088
while paper_height < all_height:
    n += 1
    paper_height *= 2
print(f'需要折{n}次，折出的高度为{paper_height}毫米')

