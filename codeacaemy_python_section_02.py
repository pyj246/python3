# 2.1--------------------------------------------------------------------------#
# 세 번째 줄에 변수 variable의 값으로 44.50을 지정하세요!

meal = 44.50

# 2.2--------------------------------------------------------------------------#
meal = 44.50
tax = 6.75 / 100

# 2.3--------------------------------------------------------------------------#
# 거의 다 됐습니다! 다섯 번째 줄에 변수 tip을 생성하세요.

meal = 44.50
tax = 0.0675
tip = 0.15

# 2.4--------------------------------------------------------------------------#
# Reassign meal on line 7!

meal = 44.50
tax = 0.0675
tip = 0.15
meal = meal + (meal * tax)

# 2.5--------------------------------------------------------------------------#
# 여덟 번째 줄에 변수 total을 생성하세요!

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)