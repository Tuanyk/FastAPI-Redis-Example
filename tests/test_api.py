import pytest
import requests
import hashlib

@pytest.mark.parametrize("word", ["bán hàng online","gửi mình ảnh nude"])
def test_add_item(item_url, word):
    word = word.lower()
    key = hashlib.md5(word.encode()).hexdigest()
    resp = requests.post(item_url, json={'paragraph': word})

    assert resp.status_code == 200, resp.text
    assert key == resp.text.strip("\""), resp.text

@pytest.mark.parametrize("paragraph", ["thử bán hàng online", "hãy gửi mình ảnh nude vào tele"])
def test_api_true(api_url, paragraph):
    resp = requests.post(api_url, json={'paragraph': paragraph})

    assert resp.status_code == 200, resp.text
    assert resp.text == "1", resp.text


@pytest.mark.parametrize("paragraph", ["thử bán hàng offline", "đoạn văn bình thường không có key"])
def test_api_false(api_url, paragraph):
    resp = requests.post(api_url, json={'paragraph': paragraph})

    assert resp.status_code == 200, resp.text
    assert resp.text == "0", resp.text