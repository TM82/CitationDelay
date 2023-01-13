import numpy as np
import pandas as pd


class CitationDelay:
    """
    Based on Wang, J., Thijs, B., & Glänzel, W. (2015). Interdisciplinarity and impact: Distinct effects of variety, balance, and disparity. PloS one, 10(5), e0127298.
    """
    
    @staticmethod
    def score(c:list[int]) -> float:
        """
        Parameters: 
        ----------
        c : list
            Citation history, c[0] is the citation of publication year.
        Returns:
        ----------
        float:
            Score of Citation Delay
        """
        return 1 - np.sum((np.cumsum(c)/np.sum(c))[:-1])/(len(c)-1)

    
# Suppose a particular paper published in 2016 has got citations as [2,5,8,6,3,2] from 2016 to 2021.
c_history = [2,5,8,6,3,2]

print(f'Citation Delay = {CitationDelay.score(c_history)}')