# def contact():
#     print(("contact details of the school"))
#     print("delhi public school")
#     print("bangluru karnataka")
#     print("8791477988")
#     print("aakashk3741@gmail.com")

# for i in range(5):
#     a = input("name of the student:-")
#     b = int(input("enter the marks of the math:-"))   
#     c = int(input("enter the marks of the science:-"))
#     d = int(input("enter the marks of the social science:-"))
#     e = int(input("enter the marks of drawing:-"))
#     f = int(input("enter the marks of the hindi:-"))
#     g = int(input("enter the marks of the english:-"))
#     print("percent of the student:-",(b+c+d+e+f+g)*100/600)

# contact()

# def electricity_bill():
#     n = int(input("enter the value of n:-"))
#     if (n<=500):
#         print("your bill in rs",n*5)
#     elif(n>=500 and n<=700):
#         print("your bill in rs",n*10)
#     elif(n>=700 and n<=1000):
#         print("your bill in rs",n*15)
#     elif(n>=1000):
#         print("your bill in rs",n*20)

# def instruction():
#     print("your last bill is paying 20 april")
#     print("after 20 april you need to pay 1000rs as a fine")
#     print("electricity office new delhi")

# electricity_bill()
# instruction()


# num = [1,12,456,7,8,9,'aakash kumar','aakash kumar123']
# print(num)
# print(len(num))
# print(type(num))
# print(num[::4])
# num.append("vikash")
# num.insert(4,"guava")
# num.remove("aakash kumar123")
# num.pop(2)
# more_fruits = ("pineapple","mango") 
# num.extend(more_fruits)
# print(num)


# dict = {1:2,34:5,5:56,"num":2,"name":"aakash","village":"madhopur"}
# print(dict["num"])
# print(dict[34])
# print(dict.keys())
# dict["city"]="areilly"
# print(dict)
# dict.pop("num")
# print(dict)
# print(dict) 
# print(len(dict))
# print(type(dict))


# tuple = (1,2,3,4,5,6,7,8,9,10)
# print(tuple[1])
# print(len(tuple))
# print(type(tuple))
# more_values =(13,45,"vikash")
# tuple = tuple+more_values
# print(tuple)


# thisset = set(("alpha","beta","gamma"))
# print(thisset)
# print(type(thisset))


# set = {"aakash","vikas","sagar"}
# print(set)
# print(type(set))
# x = set()
# print(type(x))
# for i in set:
#     print(i)

# print("saloni" in set)
# print("aakash" in set)
# set.add("neeraj")
# set.remove("sagar")
# set.pop()
# set.clear()
# print(set)

# x = {1,23,4,5,5678}
# y = {"aaksh ","vikas","saloni"}
# x.union(y)
# x.update(y)
# print(x)
# print(max(x))
# print(min(x))


# set1 = {1,2,3,4,5,6,7}
# set2 = {2,4,6,23,45,7}
# print(set1.intersection(set2))

# num1 = int(input("enter the value:-"))
# num2 = int(input("enter the value:-"))

# operator = input("enter the any operator:-")
 
  
# match operator:

#   case"+":     
#    add = num1+num2
#    print(add)
 
#   case"-":
#    sub = num1-num2
#    print(sub)

#   case"*":
#    mul = num1*num2
#    print(mul)

#   case"/":
#    divide = num1/num2
#    print(divide)






# import qrcode
# qr = qrcode.make("youtube.com/watch?v=M9rqo776gV8&list=PLxzTa0VPR9ryvGSuCm4RS8aeAvOLXz9XM")
# qr.save("qr_code.jpg")




#    FLAPPY BIRD PROGRAM:-

# import pygame
# import random

# # Initialize Pygame
# pygame.init()

# # Set up the screen
# screen_width = 400
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption("Flappy Bird")

# # Colors
# white = (255, 255, 255)
# black = (0, 0, 0)

# # Game variables
# bird_size = 30
# bird_x = 50
# bird_y = screen_height // 2
# bird_speed = 0
# gravity = 0.25
# jump = -5
# pipe_width = 50
# pipe_gap = 200
# pipe_speed = 3
# pipes = []

# # Fonts
# font = pygame.font.SysFont(None, 40)

# def draw_bird(x, y):
#     pygame.draw.circle(screen, black, (x, y), bird_size)

# def draw_pipe(x, y, height):
#     pygame.draw.rect(screen, black, (x, 0, pipe_width, y))
#     pygame.draw.rect(screen, black, (x, y + pipe_gap, pipe_width, screen_height - y - pipe_gap))

# def collision(bx, by, px, py, pw, ph):
#     if bx + bird_size > px and bx < px + pw:
#         if by < py or by + bird_size > py + ph:
#             return True
#     return False

# running = True
# while running:
#     screen.fill(white)

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = True
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 bird_speed = jump

#     bird_speed += gravity
#     bird_y += bird_speed

#     if bird_y > screen_height or bird_y < 0:
#         running = True

#     if len(pipes) == 0 or pipes[-1][0] < screen_width - 200:
#         pipe_height = random.randint(50, screen_height - pipe_gap - 50)
#         pipes.append((screen_width, pipe_height))

#     for pipe in pipes:
#         pipe_x, pipe_height = pipe
#         draw_pipe(pipe_x, 0, pipe_height)
#         draw_pipe(pipe_x, pipe_height + pipe_gap, screen_height - pipe_height - pipe_gap)
#         pipe_x -= pipe_speed
#         if collision(bird_x, bird_y, pipe_x, 0, pipe_width, pipe_height) or collision(bird_x, bird_y, pipe_x, pipe_height + pipe_gap, pipe_width, screen_height - pipe_height - pipe_gap):
#             running = True
#         if pipe_x < -pipe_width:
#             pipes.remove(pipe)

#     draw_bird(bird_x, int(bird_y))

#     pygame.display.update()
#     pygame.time.Clock().tick(60)

# pygame.quit()





# name = input("enter the name :-")
# city_name = input("enter the city name :-")
# father_name = input ("enter the name of your father :-")
# mother_name = input("enter your mothers name :-")
# adhar_number = int(input("enter your adhar number :-"))
# percentage_of_high_School = float(input("enter the parcentage of the high school :-"))
# percentage_of_twelve = float(input("enter the parcenatge of the twelve class :-"))
# school_name = input("enter the name of the school :-")
# Catagory_name = input("enter your Catagory name :-")
# parmanent_address =input("enter your parmanent address:")


# print(name,city_name,mother_name,adhar_number,percentage_of_high_School,percentage_of_twelve,school_name,Catagory_name,parmanent_address)
 
# num1 = int(input("enter the any number:"))
# num2 = int(input("enter the second number:"))

# print(num1+num2)
# print(num1*num2)
# print(num1-num2)
# print(num1/num2)
# print(num1,num2)


# import turtle
# import colorsys
# t = turtle.Turtle()
# s = turtle.Screen().bgcolor('black')
# t.speed(0)
# n = 70
# h = 0
# for i in range(360):
#     c = colorsys.hsv_to_rgb(h, 1, 0.8)
#     h+= 1/n
#     t.color(c)
#     t.left(1)
#     t.fd(1)
#     for j in range(2):
#         t.left(2)
#         t.circle(100)

 
# from turtle import*
# import colorsys
# speed(90)
# hideturtle()
# bgcolor("black")
# tracer(5)
# width(2)
# h=0.01
# for i in range(55):
# 	color(colorsys.hsv_to_rgb(h,1,1))
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	right(120)
# 	circle(50)
# 	left(240)
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	h+=0.02
# 	color(colorsys.hsv_to_rgb(h,1,1))
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	right(120)
# 	circle(-50)
# 	left(240)
# 	forward(100)
# 	left(60)
# 	forward(100)
# 	left(2)
# 	h+=0.02
# done()


 