import numpy as np

def calculate_loads(thickness_brick, thickness_mortar, density_brick, density_mortar, density_concrete, thickness_concrete, density_ceiling, live_load):
    q_brick = thickness_brick * density_brick
    q_mortar = thickness_mortar * density_mortar
    q_concrete = thickness_concrete * density_concrete
    q_ceiling = density_ceiling

    q_g = q_brick + q_mortar + q_concrete + q_ceiling
    q_q = live_load
    q_total = q_g + q_q

    return q_g, q_q, q_total

def calculate_dimensions(l1, l3, h_base):
    h_single = (1/40 + 1/30) / 2 * l1
    h_cross = (1/14 + 1/8) / 2 * l3
    b_cross = (1/3.5 + 1/1.5) / 2 * h_cross

    return h_single, h_cross, b_cross

def calculate_span(l_n, h, a, beam_width):
    l0_1 = l_n + h / 2
    l0_2 = l_n + a / 2
    l0 = min(l0_1, l0_2)
    l_middle = l0 - beam_width

    return l0, l_middle

def calculate_internal_forces(q_total, l0, l_middle):
    M_max_edge = q_total * l0**2 / 8
    V_max_edge = q_total * l0 / 2
    M_max_middle = q_total * l_middle**2 / 8
    V_max_middle = q_total * l_middle / 2

    return M_max_edge, V_max_edge, M_max_middle, V_max_middle

def generate_calculation_report(thickness_brick, thickness_mortar, density_brick, density_mortar, density_concrete, thickness_concrete, density_ceiling, live_load, l1, l3, l_n, a, beam_width):
    q_g, q_q, q_total = calculate_loads(thickness_brick, thickness_mortar, density_brick, density_mortar, density_concrete, thickness_concrete, density_ceiling, live_load)
    h_single, h_cross, b_cross = calculate_dimensions(l1, l3, thickness_concrete)
    l0, l_middle = calculate_span(l_n, h_cross, a, beam_width)
    M_max_edge, V_max_edge, M_max_middle, V_max_middle = calculate_internal_forces(q_total, l0, l_middle)

    report = f"""
    计算书

    一、楼盖布置
    1. 地面砖厚度: {thickness_brick} mm，密度: {density_brick} kN/m^3
    2. 水泥砂浆找平层厚度: {thickness_mortar} mm，密度: {density_mortar} kN/m^3
    3. 钢筋混凝土结构层厚度: {thickness_concrete} mm，密度: {density_concrete} kN/m^3
    4. 钢龙骨石膏板吊顶荷载: {density_ceiling} kN/m^2
    5. 楼面活荷载: {live_load} kN/m^2

    二、荷载计算
    1. 永久荷载: {q_g:.2f} kN/m^2
    2. 活荷载: {q_q:.2f} kN/m^2
    3. 总荷载: {q_total:.2f} kN/m^2

    三、构件截面尺寸确定
    1. 单向板底板厚度: {h_single:.2f} mm
    2. 截面高度: {h_cross:.2f} mm
    3. 截面宽度: {b_cross:.2f} mm

    四、内力计算
    1. 边跨跨度: {l0:.2f} mm
    2. 中跨跨度: {l_middle:.2f} mm
    3. 边跨最大弯矩: {M_max_edge:.2f} kN·m
    4. 边跨最大剪力: {V_max_edge:.2f} kN
    5. 中跨最大弯矩: {M_max_middle:.2f} kN·m
    6. 中跨最大剪力: {V_max_middle:.2f} kN
    """

    return report

# 输入参数
thickness_brick = 10  # mm
thickness_mortar = 20  # mm
density_brick = 25  # kN/m^3
density_mortar = 20  # kN/m^3
density_concrete = 25  # kN/m^3
thickness_concrete = 120  # mm
density_ceiling = 0.18  # kN/m^2
live_load = 4.0  # kN/m^2
l1 = 5400 / 2  # mm
l3 = 6900  # mm
l_n = 5400  # mm
a = 120  # mm
beam_width = 300  # mm

# 生成计算书
report = generate_calculation_report(thickness_brick, thickness_mortar, density_brick, density_mortar, density_concrete, thickness_concrete, density_ceiling, live_load, l1, l3, l_n, a, beam_width)
print(report)
