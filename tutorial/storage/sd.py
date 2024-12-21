def angle_to_wind_direction(angle):
    wind_directions = [
        (348.75, 11.25, "北风"),
        (11.25, 33.75, "北东北风"),
        (33.75, 56.25, "东北风"),
        (56.25, 78.75, "东东北风"),
        (78.75, 101.25, "东风"),
        (101.25, 123.75, "东东南风"),
        (123.75, 146.25, "东南风"),
        (146.25, 168.75, "南东南风"),
        (168.75, 191.25, "南风"),
        (191.25, 213.75, "南西南风"),
        (213.75, 236.25, "西南风"),
        (236.25, 258.75, "西西南风"),
        (258.75, 281.25, "西风"),
        (281.25, 303.75, "西西北风"),
        (303.75, 326.25, "西北风"),
        (326.25, 348.75, "北西北风"),
    ]
    for start, end, direction in wind_directions:
        if start <= angle < end or (start > end and (angle >= start or angle < end)):  # 跨0度的情况
            return direction

    return "unknown wind direction! check list!"

# 测试函数
angles = [0, 45, 90, 135, 180, 225, 270, 315, 360]
for angle in angles:
    print(f"角度 {angle}° 对应风向: {angle_to_wind_direction(angle)}")
