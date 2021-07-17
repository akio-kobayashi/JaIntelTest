# original Python code from https://qiita.com/shimajiroxyz/items/a133d990df2bc3affc12

import re

class MoraUtil:
    def __init__(self):
        super(MoraUtil, self).__init__()
        c1 = '[ウクスツヌフムユルグズヅブプヴ][ァィェォ]' #ウ段＋「ァ/ィ/ェ/ォ」
        c2 = '[イキシシニヒミリギジヂビピ][ャュェョ]' #イ段（「イ」を除く）＋「ャ/ュ/ェ/ョ」
        c3 = '[テデ][ィュ]' #「テ/デ」＋「ャ/ィ/ュ/ョ」
        c4 = '[ァ-ヴー]' #カタカナ１文字（長音含む）

        cond = '('+c1+'|'+c2+'|'+c3+'|'+c4+')'
        self.re_mora = re.compile(cond)

    def kana2mora(self, kana_text):
        return self.re_mora.findall(kana_text)
