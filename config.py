class Config:
    def __init__(self):
        # размер в СИ

        # P_p - значение усилия пружины при открытом клапане
        self.P_p = 400

        # --------------------SPRING--------------------

        # Максимальный подъем клапана по кулачку
        self.h_sp = 10 * 10 ** (-3)

        # k_sp - жесткость пружины
        self.k_sp = 30000

        # G_sp - модуль сдвига
        self.G_sp = 80 * 10 ** 9

        # m_sp - коэффициент, учитывающий влияние перерезывающих сил,зависящий от с,
        # который с достаточной точностью может быть принят равным 0,95–1,00
        self.m_sp = 0.95

        # n_p - частота вращения распредвала
        self.n_p = 7300 / 60

        # ro_sp - плотность материала пружины
        self.ro_sp = 7860

        # gap_sp - зазор между витками пружины при открытом клапане
        self.gap_sp = 0.2 * 10 ** (-3)

        # i_0p - число опорных витков
        self.i_0p_sp = 2

        # t_0_sp - Допускаемое статическое напряжение (тау), Па
        self.t_0_sp = 600 * 10 ** 6

        # t_0_sp - Допускаемое динамическое напряжение (тау минус один), ПА
        self.t_1_sp = 400 * 10 ** 6

        # эффективный коэффициент концентрации напряжений
        self.k_tau_sp = 1.2

        # Это оценивается коэффициентом влияния состояния поверхностного слоя
        self.e_p_tau_sp = 0.99

        # --------------------END_SPRING--------------------
