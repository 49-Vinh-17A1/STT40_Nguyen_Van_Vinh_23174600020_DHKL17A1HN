import numpy as np
data = np.genfromtxt('chuong3\\euro2012.csv', delimiter=',', dtype=str, skip_header=1)
teams = data[:, 0]  
yellow_cards = data[:, 1].astype(int) 
red_cards = data[:, 2].astype(int)


print("Danh sách các đội tham gia Euro 2012:")
print(teams)

print("\nSố thẻ vàng của mỗi đội:")
for team, yellow in zip(teams, yellow_cards):
    print(f"{team}: {yellow}")

print("\nSố thẻ đỏ của mỗi đội:")
for team, red in zip(teams, red_cards):
    print(f"{team}: {red}")


sorted_indices_yellow = np.argsort(yellow_cards)  
sorted_teams_yellow = teams[sorted_indices_yellow] 
sorted_yellow_cards = yellow_cards[sorted_indices_yellow] 

print("\nDanh sách các đội sắp xếp theo số thẻ vàng (tăng dần):")
for team, yellow in zip(sorted_teams_yellow, sorted_yellow_cards):
    print(f"{team}: {yellow}")


sorted_indices_red = np.argsort(red_cards)
sorted_teams_red = teams[sorted_indices_red]  
sorted_red_cards = red_cards[sorted_indices_red] 

print("\nDanh sách các đội sắp xếp theo số thẻ đỏ (tăng dần):")
for team, red in zip(sorted_teams_red, sorted_red_cards):
    print(f"{team}: {red}")