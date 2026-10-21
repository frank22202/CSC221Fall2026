import math

def cal_rectangle_area(width, height):
    return width * height

def cal_circle_area(radius) -> float:
    return math.pi * math.pow(radius, 2)

def main() -> None:
    radius = float(input("Enter radius: "))
    width = float(input("Enter width: "))
    height = float(input("Enter height: "))
    print(f'{cal_circle_area(radius):.2f}')
    print(f'{cal_rectangle_area(width, height):.2f}')
    return

if __name__ == '__main__':
    main()

