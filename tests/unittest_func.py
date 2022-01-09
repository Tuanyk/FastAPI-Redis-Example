import unittest

from ..func import detect_bad_words

class TestDectections(unittest.TestCase):

    def test_normal_bad_word(self):
        paragraph = "Hiểu đơn giản, bán hàng online là một hình thức bán hàng nhưng không có cửa hàng thật, hoặc có cửa hàng nhưng đẩy mạnh quảng bá sản phẩm qua các kênh online."
        bad_words = ["bán hàng online", "gửi mình ảnh nude"]
        self.assertTrue(detect_bad_words(paragraph, bad_words))


    def test_capitalize_bad_word(self):
        paragraph = "Hiểu đơn giản, bán hàng online là một hình thức bán hàng nhưng không có cửa hàng thật, hoặc có cửa hàng nhưng đẩy mạnh quảng bá sản phẩm qua các kênh online."
        bad_words = ["Bán HàNg online", "gửi mình ảnh nude"]
        self.assertTrue(detect_bad_words(paragraph, bad_words))

if __name__ == '__main':
    unittest.main()