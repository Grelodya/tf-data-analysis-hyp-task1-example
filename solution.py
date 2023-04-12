import pandas as pd
import numpy as np


chat_id = 382319199 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    def proportions_diff_z_stat_ind(i1, n1, i2, n2):
      p1 = i1 / n1
      p2 = i2 / n2 
      P = float(p1*n1 + p2*n2) / (n1 + n2)
      return (p1 - p2) / np.sqrt(P * (1 - P) * (1. / n1 + 1. / n2))
  
    def proportions_diff_z_test(z_stat, alternative = 'two-sided'):
      if alternative not in ('two-sided', 'less', 'greater'):
          raise ValueError("alternative not recognized\n"
                           "should be 'two-sided', 'less' or 'greater'")
      if alternative == 'two-sided':
          return 2 * (1 - scipy.stats.norm.cdf(np.abs(z_stat)))
      if alternative == 'less':
          return scipy.stats.norm.cdf(z_stat)
      if alternative == 'greater':
          return 1 - scipy.stats.norm.cdf(z_stat)    
  
    if proportions_diff_z_test(proportions_diff_z_stat_ind(x_success, x_cnt, y_success, y_cnt), 'less') < 0.1:
      answer = True
    else:
      answer = False
    return answer
